import logging
import json
import os
import hashlib
from PyQt5.QtCore import QObject
import wormhole
from wormhole.cli import public_relay
from .signal_gui import signal_
from ..errors import (
    MessageError,
    RefusedError,
    RemoteError,
    RespondError,
    SendFileError,
    SendTextError,
)
from .common import source_file
import wormhole.errors
from twisted.internet.defer import inlineCallbacks, returnValue, TimeoutError
from PyQt5.QtWidgets import QMessageBox
from wormhole.cli.cmd_send import APPID
from twisted.python.failure import Failure
from .magic import Wormhole
import humanize
from ..service.common import get_defaul_path
from datetime import datetime


class ConnectionError(Exception):
    """
    Raised when our client cannot establish connection to the rendezvous or the
    transit relay servers.
    """
    verbose_name = 'Connection error'


class HumanError(Exception):
    """
    Raised when one of the humans at either end of the wormhole does something
    that breaks it, e.g. enters the wrong code.
    """
    verbose_name = 'Possible human error'


class SuspiciousOperation(Exception):
    """
    Raised when things do not go according to the protocol, e.g. a message that
    cannot be parsed is received.
    """
    verbose_name = 'Suspicious operation'


class Timeout(Exception):
    """
    Raised when the rendezvous server or the other end of the wormhole take
    longer than expected to respond.
    """
    verbose_name = 'Timeout'


class TransferError(Exception):
    """
    Raised when the file transfer failed, e.g. the connection drops before all
    the bytes have been transferred.
    """
    verbose_name = 'Transfer error'


APPID = "oa.chinahr12333.com/transfer_file"

transit_relay = public_relay.TRANSIT_RELAY
redezvous_relay = public_relay.RENDEZVOUS_RELAY

# transit_relay = u"tcp:10.10.1.215:4001"
# redezvous_relay = u"ws://10.10.1.215:4000/v1"


class ErrorPopup():

    @staticmethod
    def show(error):
        """
        Open a popup with a (hopefully) user-friendly error message.

        The given argument can be either an Exception, or a Twisted Failure, or
        the error message itself as a string.
        """
        if isinstance(error, Failure):
            error = error.value

        message = str(error)

        if hasattr(error, 'verbose_name'):
            title = error.verbose_name
        else:
            title = 'Error'
        # QMessageBox.warning(title, message, QMessageBox.Ok)
        print('title====>', title, '<<<>>>>>>>message===>', message)


class Delegate:
    def __init__(self, signals_, _message):
        self.welcome = None
        self.code = None
        self.key = None
        self.verifier = None
        self.versions = None
        self.messages = []
        self.closed = None
        self._message_handler = _message
        self._signal = signals_

    def wormhole_got_welcome(self, welcome):
        self.welcome = welcome

    def wormhole_got_code(self, code):

        self._signal.set_code_signal.emit(code)
        self.code = code

    def wormhole_got_unverified_key(self, key):
        self.key = key

    def wormhole_got_verifier(self, verifier):
        self.verifier = verifier

    def wormhole_got_versions(self, versions):
        self.versions = versions

    def wormhole_got_message(self, data):
        logging.debug(f"wormhole_got_message: {data}")
        try:
            self._message_handler(data)
        except RespondError as exception:
            print('error info --->', exception)
        except Exception as exception:
            print('print exceptin here ====>', exception)

    def wormhole_closed(self, result):
        self.closed = result


class transfer_file(QObject):
    def __init__(self, reactor_):
        self._wormhole = None
        self._reactor = reactor_
        self._signal = signal_()
        self.offer = None
        self.transit = None
        self.app_id = APPID
        self.rendezvous_relay = redezvous_relay
        self.transit_relay = transit_relay
        self._delegate = Delegate(self._signal, self._handle_message)
        self.file_name = '…'
        self.file_size = '…'
        self.file_size_non_human = 0

        self.bytes_transferred = 0
        self.transferred = '…'
        self.start_time = 0
    def open(self, code):
        logging.debug('invoke open method here')
        if self._wormhole is not None:
            self._wormhole = None

        self._wormhole = wormhole.create(
            appid=self.app_id,
            relay_url=self.rendezvous_relay,
            reactor=self._reactor,
            delegate=self._delegate,
            versions={"v0": {"mode": "connect"}},
        )

        if code is None or code == "":
            self._wormhole.allocate_code(4)
        else:
            self._wormhole.set_code(code)

    @inlineCallbacks
    def open_defer_mode(self, code):
        self._wormhole = Wormhole(_reactor=self._reactor, app_id=self.app_id, rendezvous_relay=self.rendezvous_relay,
                                  transit_relay=self.transit_relay)

        if code is None or code == "":
            codes = yield self._wormhole.generate_code()
            self._signal.set_code_signal.emit(codes)
        else:
            self._wormhole.set_code(code)

    def open_wormhole(self, code):
        """
        Called when the user releases the connect button.
        """
        if self.bytes_transferred > 0:
            self.bytes_transferred = 0
        # init start_time is zore
        self.start_time = 0


        def connect():

            try:
                self._wormhole = Wormhole(_reactor=self._reactor, app_id=self.app_id,
                                          rendezvous_relay=self.rendezvous_relay,
                                          transit_relay=self.transit_relay)
            except Exception as error:
                ErrorPopup.show(error)

            deferred = self._wormhole.connect(code)
            deferred.addCallbacks(exchange_keys, ErrorPopup.show)
            return deferred

        def exchange_keys(code):
            deferred = self._wormhole.exchange_keys()
            deferred.addCallbacks(await_offer, ErrorPopup.show)
            return deferred

        def await_offer(verifier):
            deferred = self._wormhole.await_offer()
            deferred.addCallbacks(show_offer, ErrorPopup.show)
            # return deferred

        def show_offer(offer):
            temp_now = datetime.now()
            self.start_time = datetime.timestamp(temp_now)
            self.file_name = str(offer['filename'])
            self.file_size_non_human = offer['filesize']
            self.file_size = humanize.naturalsize(offer['filesize'])
            self._signal.rec_file_name_and_size.emit(self.file_name + "  (" + self.file_size + ")")
            self._signal.start_receive_file.emit()

        connect()

    def accept_offer(self,path):
        """
        Called when the user releases the accept button.
        """
        default_path = get_defaul_path()
        file_path = os.path.join(path, self.file_name)

        def accept_offer():
            deferred = self._wormhole.accept_offer(file_path, on_chunk)
            deferred.addCallback(show_done)
            return deferred

        def on_chunk(chunk):
            temp_now = datetime.now()
            end_time = datetime.timestamp(temp_now)
            sec = end_time - self.start_time
            minutes, seconds = divmod(sec, 60)
            hours, minutes = divmod(minutes, 60)
            return_date = "%02d:%02d" % (minutes, seconds)
            if hours > 0:
                return_date = "%02d:%02d:%02d" % (hours, minutes, seconds)

            self.bytes_transferred += len(chunk)
            self.transferred = humanize.naturalsize(self.bytes_transferred)
            nums = int(float(self.bytes_transferred) / float(self.file_size_non_human) * 100)
            nums_bytes = str(nums) + "||" + str(self.transferred) + "||" + str(return_date)

            self._signal.render_rec_percent_number.emit(nums_bytes)

        def show_done(hex_digest):
            """close wormhole connection """
            self.close_conn()
            self._signal.close_rec_dialog.emit()

        accept_offer()

    """if wormhole class is not none then close it ,otherwise dismiss and never care about it"""

    def close_conn(self):
        assert self._wormhole is not None
        try:
            self._wormhole.close()
        except AttributeError:
            pass

    def send_file_to_dest(self, path):
        if self.bytes_transferred > 0:
            self.bytes_transferred = 0
        sourecs = source_file(path)
        sourecs.open()
        self._signal.send_file_name_and_size.emit(
            sourecs.name + "  (" + humanize.naturalsize(sourecs.transfer_bytes) + ")")



        def exchange_keys():
            deferred = self._wormhole.exchange_keys(timeout=600)
            deferred.addCallbacks(send_file, None)
            return deferred

        def send_file(verifier):
            temp_now = datetime.now()
            self.start_time = datetime.timestamp(temp_now)
            deferred = self._wormhole.send_file(sourecs.full_path, on_chunk)
            deferred.addCallback(show_done)
            return deferred

        def on_chunk(chunk):
            temp_now = datetime.now()
            end_time = datetime.timestamp(temp_now)
            sec = end_time - self.start_time
            minutes, seconds = divmod(sec, 60)
            hours, minutes = divmod(minutes, 60)
            return_date = "%02d:%02d" % (minutes, seconds)
            if hours > 0:
                return_date = "%02d:%02d:%02d" % (hours, minutes, seconds)


            self.bytes_transferred += len(chunk)
            self.transferred = humanize.naturalsize(sourecs.transfer_bytes)
            nums = int(float(self.bytes_transferred) / float(sourecs.transfer_bytes) * 100)
            nums_bytes = str(nums) + "||" + humanize.naturalsize(self.bytes_transferred) + "||" + str(return_date)

            self._signal.render_send_percent_number.emit(nums_bytes)

        def show_done(hex_digest):
            """close receive wormhole connection"""
            self.close_conn()
            self._signal.close_send_dialog.emit()

        exchange_keys()

    """handle for delegate model"""

    def _handle_message(self, data_bytes):
        try:
            data_string = data_bytes.decode("utf-8")
            data = json.loads(data_string)
        except json.JSONDecodeError:
            raise MessageError(f"Invalid message received: {data_string}")

        if "error" in data:
            raise RemoteError(data["error"])

        for key, contents in data.items():
            if key == "offer":
                self._handle_offer(contents)

            elif key == "transit":
                self._transit.handle_transit(contents)

            elif key == "command" and contents == "shutdown":
                self._signals.wormhole_shutdown_received.emit()
                self.close()

            elif key == "answer" and "message_ack" in contents:
                result = contents["message_ack"]
                is_ok = result == "ok"
                self._signals.message_sent.emit(is_ok)
                if not is_ok:
                    raise SendTextError(result)
                if not self._peer_supports_connect_mode():
                    self.close()

            elif key == "answer" and "file_ack" in contents:
                result = contents["file_ack"]
                if result == "ok":
                    self._transit.handle_file_ack()
                else:
                    raise SendFileError(result)
            else:
                logging.warning(f"Unexpected data received: {key}: {contents}")
