"""Our decorator for web service methods"""

import json
import logging
from inspect import getargspec
from functools import update_wrapper
try:
    from json import JSONDecodeError
except ImportError:
    # Python 2
    JSONDecodeError = ValueError

from circuits.core import handler
from circuits.web.wrappers import Response
from circuits.web.exceptions import HTTPException
from circuits.web.errors import httperror
import circuits.six as six


LOG = logging.getLogger(__name__)


def exposeWeb(*channels, **config):
    def decorate(f):
        @handler(*channels, **config)
        def wrapper(self, event, *args, **kwargs):
            try:
                if not hasattr(self, "request"):
                    (self.request, self.response), args = args[:2], args[2:]
                    self.request.args = args
                    self.request.kwargs = kwargs
                    self.cookie = self.request.cookie
                    if hasattr(self.request, "session"):
                        self.session = self.request.session

                if hasattr(self, "_auth"):
                    self._auth()

                if not getattr(f, "event", False):
                    result = f(self, *args, **kwargs)
                else:
                    result = f(self, event, *args, **kwargs)
                if (isinstance(result, httperror)
                    or isinstance(result, Response)
                    or isinstance(result, six.string_types)):
                    return result
                elif result is None:
                    self.response.status = 204
                    return ""
                else:
                    try:
                        self.response.headers["Content-Type"] = "application/json; charset=utf-8"
                        return json.dumps(result)
                    except (JSONDecodeError, TypeError) as e:
                        return httperror(self.request, self.response, code=500,
                                         description="JSON decode failed for object of type '%s'" % type(result))
            except HTTPException as e:
                LOG.exception(e)
                return httperror(self.request, self.response, code=e.code, description=e.description)
            except Exception as e:
                LOG.exception(e)
                return httperror(self.request, self.response, code=500, description=e.message)
            finally:
                if hasattr(self, "request"):
                    del self.request
                    del self.response
                    del self.cookie
                if hasattr(self, "session"):
                    del self.session

        wrapper.args, wrapper.varargs, wrapper.varkw, wrapper.defaults = \
            getargspec(f)
        if wrapper.args and wrapper.args[0] == "self":
            del wrapper.args[0]

        if wrapper.args and wrapper.args[0] == "event":
            f.event = True
            del wrapper.args[0]
        wrapper.event = True

        return update_wrapper(wrapper, f)

    return decorate
