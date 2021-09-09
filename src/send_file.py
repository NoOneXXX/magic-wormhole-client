import logging
import traceback
import json
from email.errors import MessageError

from twisted.trial import unittest
import wormhole

from wormhole.cli import public_relay
from wormhole.cli.cmd_receive import RespondError
from wormhole.errors import LonelyError
from twisted.internet import defer, reactor

APPID = "li1567-118.members.linode.com/magic-wormhole-better-hro-gui"


class WormholeDelegate:
    def __init__(self):
        self.welcome = None
        self.code = None
        self.key = None
        self.verifier = None
        self.versions = None
        self.messages = []
        self.closed = None

    def wormhole_got_welcome(self, welcome):
        self.welcome = welcome

    def wormhole_got_code(self, code):
        self.code = code

    def wormhole_got_unverified_key(self, key):
        self.key = key

    def wormhole_got_verifier(self, verifier):
        self.verifier = verifier

    def wormhole_got_versions(self, versions):
        self.versions = versions

    def wormhole_got_message(self, data):
        self.messages.append(data)

    def wormhole_closed(self, result):
        self.closed = result


@defer.inlineCallbacks
def poll_until(predicate):
    # return a Deferred that won't fire until the predicate is True
    while not predicate():
        d = defer.Deferred()
        reactor.callLater(0.001, d.callback, None)
        yield d


class wormhole_proxy(unittest.TestCase):

    @defer.inlineCallbacks
    def test_get_code(self):
        print('test this method for all --->')

