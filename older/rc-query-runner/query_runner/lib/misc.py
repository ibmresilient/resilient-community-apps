"""Stuff"""

import collections
import unicodedata
from signal import SIGINT, SIGTERM
import logging
from circuits import Event, Worker
from circuits.core.handlers import handler

LOG = logging.getLogger(__name__)

BASESTRING = str
try:
    BASESTRING = basestring
except NameError:
    # py3
    pass


NONE_VALUES = ["None", "null", "", None]


class InterruptibleWorker(Worker):
    @handler("signal", channel="*")
    def _on_signal(self, signo, stack):
        """Add a signal handler to the worker processes otherwise they swallow SIGINT, SIGTERM
           (see FallBackSignalHandler in circuits/core/helpers.py)
        """
        if signo in [SIGINT, SIGTERM]:
            LOG.info("Worker interrupted")
            raise SystemExit(0)

class NiceEvent(Event):

    """A Circuits event that doesn't dump its load when repr"""

    def _repr(self):
        return ""

    def __repr__(self):
        "x.__repr__() <==> repr(x)"

        if len(self.channels) > 1:
            channels = repr(self.channels)
        elif len(self.channels) == 1:
            channels = str(self.channels[0])
        else:
            channels = ""

        data = self._repr()

        return "<%s[%s] (%s)>" % (self.name, channels, data)


# Exception Definitions
class SearchFailure(Exception):
    """ Search failed to execute """
    def __init__(self, search_id, search_status):
        fail_msg = "Query [%s] failed with status [%s]" % (search_id, search_status)
        Exception.__init__(self, fail_msg)
        self.search_status = search_status


class SearchTimeout(Exception):
    """ Query failed to complete in time specified """
    def __init__(self, search_id, search_status):
        fail_msg = "Query [%s] timed out. Final Status was [%s]" % (search_id, search_status)
        Exception.__init__(self, fail_msg)
        self.search_status = search_status


class abstractstatic(staticmethod):
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True


def ensure_unicode(input):
    """ if input is type str, convert to unicode with utf-8 encoding """

    if input is None:
        return input
    if not isinstance(input, BASESTRING):
        return input
    if isinstance(input, str):
        input_unicode = input.decode('utf-8')
    else:
        input_unicode = input

    input_unicode = unicodedata.normalize('NFKC', input_unicode)
    return input_unicode


def update_with_result(message, result):
    """Update the dict 'message', applying the values in 'result'
        recursively (unlike dict.update() which is shallow).

        >>> update_with_result({"a": 1, "b": "B"}, {"b": 2})
        {'a': 1, 'b': 2}

        >>> update_with_result({"properties": {"a": 1}}, {"properties": {"b": 2}})
        {'properties': {'a': 1, 'b': 2}}

        >>> update_with_result({'values': None}, {'properties': {'b': 2}})
        {'values': None, 'properties': {'b': 2}}

        >>> update_with_result({"properties": "string"}, {"properties": {"b": 2}})
        {'properties': {'b': 2}}

    """
    # LOG.info("Message: %s", message)
    # LOG.info("Result: %s", result)
    for k, v in result.items():
        if isinstance(message, collections.Mapping):
            if isinstance(v, collections.Mapping):
                r = update_with_result(message.get(k, {}), v)
                message[k] = r
            else:
                message[k] = result[k]
        else:
            message = {k: result[k]}
    return message
