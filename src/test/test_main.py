import logging
import traceback
import json
from email.errors import MessageError

from twisted.internet.defer import inlineCallbacks
from twisted.trial import unittest
import wormhole

from wormhole.cli import public_relay
from wormhole.errors import LonelyError
from twisted.internet import defer, reactor
from ..service.wormhole_transfer import transfer_file
from wormhole.test.common import poll_until
from ..service.wormhole_transfer import Delegate
from ..service.magic import Wormhole

APPID = "li1567-118.members.linode.com/magic-wormhole-better-hro-gui"
TRANSIT_RELAY = u"tcp:transit.magic-wormhole.io:4001"


class wormhole_proxy(unittest.TestCase):

    @inlineCallbacks
    def test_get_code(self):
        dg = Delegate()
        _wormhole_proxy = transfer_file(reactor)
        _wormhole_proxy.open(None)
        yield poll_until(lambda: dg.code is not None)
        print('another test is --->', dg.code)
        cs = _wormhole_proxy._delegate.code
        print('print this code', cs)

    # @inlineCallbacks
    def test_get_code_imd(self):
        dg = Delegate()
        _wormhole_proxy = transfer_file(reactor)
        _wormhole_proxy.open(None)
        codes = _wormhole_proxy.get_code_()

        print('print this code', codes)

    @inlineCallbacks
    def test_go(self):
        w = wormhole.create(APPID, public_relay.RENDEZVOUS_RELAY, reactor)
        w.allocate_code()
        codes = yield w.get_code()
        print(codes, '<<<<<<<<<<<<<<<<<')
        w.closed()

    @inlineCallbacks
    def test_magic_class_generator_code(self):
        w = Wormhole(APPID, public_relay.RENDEZVOUS_RELAY, TRANSIT_RELAY)
        deferred = yield w.generate_code()
        print(deferred,'<<<<<get code here')
        w.close()

    def error_occure(self):
        print('print error here ')

    @inlineCallbacks
    def test_find_code(self):
        w = Wormhole()
        codes = yield w.generate_code()
        print(codes,'<<<<<<<<<<<<<<<<<<<')


if __name__ == "__main__":
    print(int(12/243))
