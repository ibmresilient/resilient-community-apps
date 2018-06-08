#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument, too-many-instance-attributes

"""
Circuits Web component to implement a simple responder for the Resilient custom threat service API.

This responds to the following requests:

*   OPTIONS /<root>
    - returns configuration options.  This includes an indicator whether we support file uploads.

*   POST /<root>
    - handles a request to lookup an artifact.
     This must return as quickly as possible.  So, rather than handling the lookup, it just
     returns HTTP status 303 ("retry") with a new "request ID", and fires a notification to
     any 'searcher components' to lookup the artifact.  Those searchers can independently
     perform their lookups and return values, which will be sent back to Resilient later.

*   GET /<root>/<request_id>
    - returns any available results for the given request_id.
    - if the ID is queued & no results yet => return an HTTP 303 so that the 'retry' info
    - If the ID has results ==> return them.
      Also the results can now be removed from the cache.
    - If we don't have any information about the ID => return null results.
      The cause is probably that we were queried some time ago, but the query expired from the cache,
      or the process died and lost all the cached queries.  Resilient will retry artifact searches
      for open incidents every 48 hours, so we'll likely be asked to lookup again in the future.

The top-level <root> is configurable by 'urlbase' in config, defaults to '/cts'.
All requests below this will also be handled, with each path treated as independent threat services.
Searchers register to a single path, e.g. '/cts/gsb' for the Google Safe Browsing example.

"""

import json
import logging
from collections import namedtuple
from uuid import UUID, uuid4, uuid5
from cachetools import TTLCache
from pkg_resources import Requirement, resource_filename
from rc_webserver.web import exposeWeb
from circuits import Event, BaseComponent
from circuits.web import BaseController
from circuits.core.handlers import handler
from rc_cts import searcher_channel
from requests_toolbelt.multipart import decoder, NonMultipartContentTypeException


LOG = logging.getLogger(__name__)


# Configuration keys
ConfigKey = namedtuple("ConfigKey", "key default")
CONFIG_SECTION = "custom_threat_service"
CONFIG_URLBASE = ConfigKey(key="urlbase", default="/cts")
CONFIG_UPLOAD_FILE = ConfigKey(key="upload_file", default=False)
CONFIG_FIRST_RETRY_SECS = ConfigKey(key="first_retry_secs", default=0)
CONFIG_LATER_RETRY_SECS = ConfigKey(key="later_retry_secs", default=0)
CONFIG_CACHE_SIZE = ConfigKey(key="cache_size", default=10000)
CONFIG_CACHE_TTL = ConfigKey(key="cache_ttl", default=600)
CONFIG_MAX_RETRIES = ConfigKey(key="max_retries", default=60)

HELPER_CHANNEL = "threat_lookup_helper"
LOOKUP_COMPLETE_CHANNEL = "threat_lookup_complete"


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("rc-cts"), "rc_cts/data/app.config.cts")
    with open(section_config_fn, 'r') as section_config_file:
        return section_config_file.read()


class ThreatLookupIncompleteException(Exception):
    """
    A custom threat service searcher can raise this exception if they do not yet have full results
    due to an intermittent condition, and the searcher will be called again later.
    """


class ThreatServiceLookupEvent(Event):
    """
    An event fired to lookup an artifact.
    The event is fired to a channel named (LOOKUP_CHANNEL + ...sub-url...)
    The event name is the artifact type (threat-service artifact type names, 'net.uri', etc).
    """
    complete = True
    complete_channels = (LOOKUP_COMPLETE_CHANNEL,)

    def __init__(self, request_id=None, name="unknown", artifact=None, channel=searcher_channel()):
        super(ThreatServiceLookupEvent, self).__init__(name=name)

        self.channels = (channel,)
        self.request_id = request_id
        self.cts_channel = channel
        self.artifact = artifact
        self.name = name

    def __repr__(self):
        "x.__repr__() <==> repr(x)"

        if len(self.channels) > 1:
            channels = repr(self.channels)
        elif len(self.channels) == 1:
            channels = str(self.channels[0])
        else:
            channels = ""

        return "<%s[%s] (%s)>" % (self.name, channels, self.request_id)


class CustomThreatServiceHelper(BaseComponent):
    """
    A helper component, used to dispatch lookup events 'off-thread'.
    Normally, when an event handler fires an event, the original
    event is notified 'complete' only when all children are done,
    this escapes from that process so that lookup queries
    are queued while the initial request can return immediately.
    """
    channels = (HELPER_CHANNEL,)

    def __init__(self, maincomponent):
        super(CustomThreatServiceHelper, self).__init__()
        self.maincomponent = maincomponent

    @handler(channel=HELPER_CHANNEL)
    def _lookup(self, event, *args, **kwargs):
        """
        A lookup event
        """
        if not isinstance(event, ThreatServiceLookupEvent):
            return
        try:
            LOG.info("helper: %s, %s", event, event.cts_channel)
            self.maincomponent.fire(event, event.cts_channel)
        except:
            LOG.exception("Failed to dispatch event")


def _make_args(opts):
    options = opts.get(CONFIG_SECTION, {})
    channel = options.get(CONFIG_URLBASE.key, CONFIG_URLBASE.default)
    kwargs = {
        "channel": channel
    }
    return kwargs


class CustomThreatService(BaseController):
    """
    Implements a custom threat service for Resilient.
    The root path (/xxx/ below) is configurable.
    The service provides the following URLs:
        OPTIONS /<root_path>/<any_sub_path>
        POST    /<root_path>/<any_sub_path>
        GET     /<root_path>/<any_sub_path>/<id>
    """

    # Arbitrary constant
    namespace = UUID('18222d9c-adf0-409c-aa19-beb27130ba12')

    def __init__(self, opts):
        super(CustomThreatService, self).__init__(**_make_args(opts))

        # Configurable options
        self.options = opts.get(CONFIG_SECTION, {})

        # Do we support "file-content" artifacts?  Default is no.
        # TODO add implementation support to parse the file content
        self.support_upload_file = bool(self.options.get(CONFIG_UPLOAD_FILE.key, CONFIG_UPLOAD_FILE.default))

        # Default time that this service will tell Resilient to retry
        self.first_retry_secs = int(self.options.get(CONFIG_FIRST_RETRY_SECS.key, CONFIG_FIRST_RETRY_SECS.default)) or 5
        self.later_retry_secs = int(self.options.get(CONFIG_LATER_RETRY_SECS.key, CONFIG_LATER_RETRY_SECS.default)) or 60

        # Size of the request cache
        self.cache_size = int(self.options.get(CONFIG_CACHE_SIZE.key, CONFIG_CACHE_SIZE.default))
        # TTL of the request cache (millis before we give up on a request lookup)
        self.cache_ttl = int(self.options.get(CONFIG_CACHE_TTL.key, CONFIG_CACHE_TTL.default))

        # Limit to the number of queries we'll answer for unfinished searchers (count before giving up on them)
        self.max_retries = int(self.options.get(CONFIG_MAX_RETRIES.key, CONFIG_MAX_RETRIES.default))

        # IDs and their results are maintained in a cache so that we can set
        # an upper bound on the number of in-progress and recent lookups.
        self.cache = TTLCache(maxsize=self.cache_size, ttl=self.cache_ttl)

        # Helper component does event dispatch work
        self.async_helper = CustomThreatServiceHelper(self)
        (self.helper_thread, self.bridge) = self.async_helper.start()

        urls = ["{0}/{1}".format(self.channel, e) for e in self.events()]
        LOG.info("Web handler for %s", ", ".join(urls))

    # Web endpoints

    @exposeWeb("OPTIONS")
    def _options_request(self, event, *args, **kwargs):
        """
        Options indicate to Resilient whether file upload is supported.
        """
        LOG.info(event.args[0])
        options = {"upload_file": self.support_upload_file}
        return options

    @exposeWeb("POST")
    def _post_request(self, event, *args, **kwargs):
        LOG.info(event.args[0])
        result = self._handle_post_request(event, *args, **kwargs)
        LOG.info("%s: %s", event.args[1].status, json.dumps(result))
        return result

    def _handle_post_request(self, event, *args, **kwargs):
        """
        Responds to POST /cts/<anything>

        The URL below /cts/ is specific to this threat service. For example,
        /cts/one and /cts/two can be registered as two separate threat sources.
        The string 'one' or 'two' becomes the channel that searcher events are dispatched on.

        Request is a ThreatServiceArtifactDTO containing the artifact to be scanned
        Response is a ResponseDTO containing the response, or 'please retry' (HTTP status 303).
        """
        request = event.args[0]
        response = event.args[1]

        # The channels that searchers are listening for events
        cts_channel = searcher_channel(*args)

        value = request.body.getvalue()

        if not value:
            err = "Empty request"
            LOG.warn(err)
            return {"id": str(uuid4()), "hits": []}

        # Resilient sends artifacts in two formats: multi-part MIME, or plain JSON.
        # server may send either, even for cases where there is no file content,
        # so check content-type and decode appropriately.
        try:
            if request.headers and "form-data" in request.headers.get("Content-Type", ""):
                multipart_data = decoder.MultipartDecoder(value, request.headers["Content-Type"])
                body = json.loads(multipart_data.parts[0].text)
                LOG.debug(body)
            else:
                body = json.loads(value.decode("utf-8"))
                LOG.debug(body)
        except (ValueError, NonMultipartContentTypeException) as e:
            err = "Can't handle request: {}".format(e)
            LOG.warn(err)
            LOG.debug(value)
            return {"id": str(uuid4()), "hits": []}

        if not isinstance(body, dict):
            # Valid JSON but not a valid request.
            err = "Invalid request: {}".format(json.dumps(body))
            LOG.warn(err)
            return {"id": str(uuid4()), "hits": []}
        
        # Generate a request ID, derived from the artifact being requested.
        request_id = str(uuid5(self.namespace, json.dumps(body)))
        artifact_type = body.get("type", "unknown")
        artifact_value = body.get("value")
        response_object = {"id": request_id, "hits": []}
        cache_key = (cts_channel, request_id)

        if artifact_type == "net.name" and artifact_value == "localhost":
            # Hard-coded response to 'net.name' of 'localhost'
            # because this is used in 'resutil threatservicetest'
            # and we want to return an immediate (not async) response
            return response_object

        # If we already have a completed query for this key, return it immmediately
        request_data = self.cache.get(cache_key)
        if request_data and request_data.get("complete"):
            response_object["hits"] = request_data.get("hits", [])
            return response_object

        response.status = 303
        response_object["retry_secs"] = self.first_retry_secs

        # Add the request to the cache, then notify searchers that there's a new request
        self.cache.setdefault(cache_key, {"id": request_id, "artifact": body, "hits": [], "complete": False})
        evt = ThreatServiceLookupEvent(request_id=request_id, name=artifact_type, artifact=body, channel=cts_channel)
        self.async_helper.fire(evt, HELPER_CHANNEL)

        return response_object

    @exposeWeb("GET")
    def _get_request(self, event, *args, **kwargs):
        LOG.info(event.args[0])
        result = self._handle_get_request(event, *args, **kwargs)
        LOG.info("%s: %s", event.args[1].status, json.dumps(result))
        return result

    def _handle_get_request(self, event, *args, **kwargs):
        """
        Responds to GET /cts/<anything>/<request-id>

        The URL below /cts/ is specific to this threat service. For example,
        /cts/one and /cts/two are considered two separate threat sources.

        Response is a ResponseDTO containing the response, or 'please retry'
        """
        LOG.info(event.args[0])
        response = event.args[1]
        request_id = None
        if not args:
            return {"id": request_id, "hits": []}

        # The ID of the lookup request
        request_id = args[-1]
        # The channel that searchers are listening for events
        cts_channel = searcher_channel(*args[:-1])

        response_object = {"id": request_id, "hits": []}

        cache_key = (cts_channel, request_id)
        request_data = self.cache.get(cache_key)
        if not request_data:
            # There's no record of this request in our cache, return empty hits
            response.status = 200
            return response_object

        response_object["hits"] = request_data["hits"]
        if not request_data["complete"]:
            # The searchers haven't finished yet, return partial hits if available
            response.status = 303
            response_object["retry_secs"] = self.later_retry_secs

            # Update the counter, so we can detect "stale" failures
            request_data["count"] = request_data.get("count", 0) + 1
            if request_data["count"] > self.max_retries:
                LOG.info("Exceeded max retries for {}".format(cache_key))
                try:
                    self.cache.pop(cache_key)
                except KeyError:
                    pass
                response.status = 200
                return response_object

            return response_object

        # Remove the result from cache
        # self.cache.pop(cache_key)

        return response_object

    @handler(channel=LOOKUP_COMPLETE_CHANNEL)
    def _lookup_complete(self, event, *args, **kwargs):
        """
        A lookup event was completed
        """
        if not isinstance(event.parent, ThreatServiceLookupEvent):
            return
        results = event.parent.value.getValue()
        artifact = event.parent.artifact
        cts_channel = event.parent.cts_channel
        request_id = event.parent.request_id

        LOG.info("Lookup complete: %s, %s", event.parent, results)

        # Depending on how many components handled this lookup event,
        # the results can be a single value (dict), or an array, or None,
        # or an exception, or a tuple (type, exception, traceback)
        hits = []
        complete = True
        if isinstance(results, list):
            for result in results:
                if result:
                    if isinstance(result, (tuple, ThreatLookupIncompleteException)):
                        LOG.info("Retry later!")
                        complete = False
                    elif isinstance(result, (tuple, Exception)):
                        LOG.error("No hits due to exception")
                    else:
                        hits.append(result)
        elif results:
            if isinstance(results, (tuple, ThreatLookupIncompleteException)):
                LOG.info("Retry later!")
                complete = False
            elif isinstance(results, (tuple, Exception)):
                LOG.error("No hits due to exception")
            else:
                hits.append(results)

        # Store the result and mark as complete (or not)
        cache_key = (cts_channel, request_id)
        self.cache[cache_key] = {"id": request_id, "artifact": artifact, "hits": hits, "complete": complete}
