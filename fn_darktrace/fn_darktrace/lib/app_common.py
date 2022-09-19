# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import hashlib
import hmac
import logging
from datetime import datetime
from urllib.parse import urljoin

from resilient_lib import (IntegrationError, RequestsCommon, str_to_bool,
                           validate_fields)

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_darktrace"
EVENT_DT_NAME = "darktrace_incident_events_dt"
DEVICE_DT_NAME = "darktrace_associated_devices_dt"
MODEL_BREACHES_DT = "darktrace_associated_model_breaches_dt"

# E N D P O I N T S
SYSTEM_STATUS_URI = "/status"
MODEL_BREACHES_URI = "/modelbreaches"
MODEL_BREACHES_COMMENTS_URI = urljoin(MODEL_BREACHES_URI, "/{pbid}/comments")
AI_ANALYST_INCIDENT_GROUPS = "/aianalyst/groups"
AI_ANALYST_EVENTS_URI = "/aianalyst/incidentevents"
AI_ANALYST_EVENT_COMMENTS_URI = "/aianalyst/incident/comments"
DEVICES_URI = "/devices"


# C O N F I G S
PUBLIC_KEY_CONFIG = "api_key"
PRIVATE_KEY_CONFIG = "api_secret"
URL_CONFIG = "instance_url"
MIN_SCORE_CONFIG = "min_score"
LOCALE_CONFIG = "locale"
EXCLUDE_DEVICE_LIST_CONFIG = "exclude_did"
SAAS_ONLY_CONFIG = "saas_only"
REQUEST_VERIFY_CONFIG = "verify"

# D E F A U L T S
DEFAULT_VERIFY = True
DEFAULT_MIN_SCORE = 0.0
DEFAULT_SAAS_ONLY = "false"
DEFAULT_LOCALE = "en_US"

# O T H E R   C O N S T A N T S
UNSET_GROUP_ID = "UNSET"

class AppCommon():
    def __init__(self, rc: RequestsCommon, app_configs: dict, integrations_configs: dict = {}) -> None:
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        :param integrations_configs: integration-server-wide configs (only used here for gathering ``verify`` values)
        :type integrations_configs: dict
        """

        # ensure that the required fields are present
        validate_fields([PUBLIC_KEY_CONFIG, PRIVATE_KEY_CONFIG, URL_CONFIG], app_configs)

        self.rc = rc

        # required configs
        self.public_key = app_configs.get(PUBLIC_KEY_CONFIG)
        self.private_key = app_configs.get(PRIVATE_KEY_CONFIG)
        self.base_url = app_configs.get(URL_CONFIG)

        # optional configs
        self.verify = _get_verify_ssl(app_configs, integrations_configs)
        self.min_score = float(app_configs.get(MIN_SCORE_CONFIG, DEFAULT_MIN_SCORE))
        self.saas_only = app_configs.get(SAAS_ONLY_CONFIG, DEFAULT_SAAS_ONLY)
        self.locale = app_configs.get(LOCALE_CONFIG, DEFAULT_LOCALE)
        self.exclude_did = app_configs.get(EXCLUDE_DEVICE_LIST_CONFIG, "")

    ##################
    # STATIC METHODS #
    ##################
    @staticmethod
    def _generate_query_from_params(base_request: str, params: dict) -> str:
        """
        Parse given params into url query format.
        This is necessary because the API requires generating
        a signature of the whole request, including the params
        which would not work without knowing the full path
        of the request.

        Example

        .. code-block::python

            base_request = "/modelbreaches"
            params = {"expandenums": "true", "otherparam": "value"}

            full_path_request = _generate_query_from_params(base_request, params)
            # returns: "/modelbreaches?expandenums=true&otherparam=value"

            # `full_path_request` can now be used to build out the url with the base_url

        :param base_request: base path of request (i.e. "/modelbreaches")
        :type base_request: str
        :param params: dictionary of key-value pairs
        :type params: dict
        :return: built full request with query added
        :rtype: str
        """
        query = "&".join(f"{key}={str(params[key])}" if not isinstance(params[key], int) else f"{key}={params[key]}"
                for key in params)
        return base_request + "?" + query if params else base_request

    ######################
    # END STATIC METHODS #
    ######################

    #########################
    # PRIVATE CLASS METHODS #
    #########################
    def _get_headers(self, time: str, signature: str) -> dict:
        """
        Generate the required headers to reach the Darktrace API.

        The value of the public_key and time must match what was used to generate the
        request signature else the API will return an error.

        :param time: time to be used for request. value must match value hashed in signature
        :type time: str
        :param signature: generated signature
        :type signature: str
        :return: required request headers for Darktrace API calls
        :rtype: dict
        """
        return {
            "DTAPI-Token": self.public_key,
            "DTAPI-Date": time,
            "DTAPI-Signature": signature
        }

    def _generate_signature(self, path_request: str, time: str) -> str:
        """
        Darktrace's API requires hashing the request, public key, and date
        into a signature using your private key. The private key is generated
        in the Darktrace UI per user and can only be seen the first time it
        is generated.
        The signature ensures that you have the appropriate private key.

        :param path_request: request to be sent, i.e. '/status?fast=true&includechildren=false'
        :type path_request: str
        :param time: time to set for request. usually it is now
        :type time: str
        :return: hashed signature
        :rtype: str
        """
        signature = hmac.new(self.private_key.encode('ASCII'),
                                (path_request +'\n'+ self.public_key +'\n'+ time).encode('ASCII'),
                                hashlib.sha1).hexdigest()

        return signature

    def _execute_dt_request(self, method: str, path_request: str, params: dict = {}, time: str = None, capture_error=False, **kwargs) -> RequestsCommon.execute:
        """
        Execute a request to Darktrace. Constructs the appropriate "signature" which is the 
        hash of the request path, the public key, and the time of the request, which is required by the DT API.
        This involves parsing any potential query parameters for the request path
        into a query style string i.e. <path_request>?<param1:val1>&<param2:val2>&....

        :param method: HTTP method (i.e. GET, POST, etc...)
        :type method: str
        :param path_request: Path to execute in the request
        :type path_request: str
        :param params: Parameters to use for the request, defaults to {}
        :type params: dict, optional
        :param time: Time to execute the request for, formatted in %Y%m%dT%H%M%S. 
                     If None, sets time to UTC.now; time must be within 30 minute of the execute time
        :type time: str, optional
        :param capture_error: If True, any failing request will be captured and no error will be thrown.
                              The error will be logged at debug level. Useful for frequently failing requests.
        :type capture_error: bool
        :return: Response object
        :rtype: ``requests.Response``
        """

        if not time:
            time = datetime.utcnow().strftime("%Y%m%dT%H%M%S")

        # need to add the query params to the path_request so that the signature is correct
        # NOTE: can't use execute(..., params=params) because that will not generate the
        #       correct signature for the DT request
        path_request = self._generate_query_from_params(path_request, params)
        signature = self._generate_signature(path_request, time)
        url = urljoin(self.base_url, path_request)

        LOG.debug(f"Query endpoint at url={url} with: time={time}, signature={signature}, verify={self.verify}")

        try:
            response = self.rc.execute(method=method, url=url, headers=self._get_headers(time, signature), verify=self.verify, **kwargs)
        except IntegrationError as err:
            if capture_error:
                LOG.error("Darktrace API call failed for request %s %s Captured error: %s", method, path_request, str(err))
                return None
            raise err

        return response.json()
    #############################
    # END PRIVATE CLASS METHODS #
    #############################

    ########################
    # PUBLIC CLASS METHODS #
    ########################
    def query_entities_since_ts(self, timestamp: datetime, *_args, **_kwargs) -> list:
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """
        base_query = {
            # params that are set by the app configs or passed in to this function
            "starttime": timestamp,
            "minscore": self.min_score,
            "locale": self.locale,
            "saasonly": self.saas_only,
            "excludedid": self.exclude_did,

            # required params for the purposes of the poller app
            "includeacknowledged": "true",
            "includeallpinned": "false"
        }

        try:
            # in order to support auto-sync updates, we have first grab the
            # events that match the criteria since the last poll
            # these events will then generate the list of UUIDs to search
            # for in the groups endpoint
            candidate_events = self.get_incident_events(params=base_query)

            # grab the list of all incident groups since the last timestamp.
            # each incident group is comprised of one or more events
            # who's data will be enhanced in the loop below
            group_ids = ",".join(e.get("currentGroup", "") for e in candidate_events if e.get("currentGroup"))

            # if no group ids are found, no entities to process so can return an empty list
            if not group_ids:
                return []

            base_query.update({"includegroupurl": "true", "groupid": group_ids})
            LOG.debug("Querying Darktrace for incident groups with query %s", base_query)
            incident_groups = self.get_incident_groups(base_query)

            # enhance data for each group
            for group in incident_groups:

                # enhance events
                group["enhancedIncidentEvents"] = self.get_incident_events(group_id=group.get("id"), capture_error=True)

                # add comments to each incident event
                for event in group.get("enhancedIncidentEvents"):
                    event.update(self.get_incident_group_comments(incident_id=event.get("id"), capture_error=True))

                    # enhance breach details by adding url to each model breach object
                    for breach in event.get("relatedBreaches"):
                        breach_query = {
                            "includebreachurl": "true",
                            "includeacknowledged": "true",
                            # restrict the returned data for performance
                            "responsedata": "breachUrl,acknowledged",
                            "pbid": breach.get("pbid")
                        }
                        breach.update(self.get_model_breaches(params=breach_query))

                # enhance devices -- NOTE the endpoint allows for comma-separated list of did's
                # but will only return a list if there is at least a comma in there -- thus we
                # need to include the last comma there otherwise if there was only one device
                # we'd get a dict result rather than a list
                query = {"did": ",".join(map(str, group.get("devices", []))) + ","}
                group["enhancedDevices"] = self.get_devices(query, capture_error=True)


        except IntegrationError as err:
            LOG.error("%s incident groups API call failed: %s", PACKAGE_NAME, str(err))
            return []

        return incident_groups

    def get_system_status(self, params: dict = None, capture_error: bool = False) -> dict:
        """
        Check the system status. This is usually used as a fast API call to simply
        to assure that the app is configured properly to communicate with the system.

        See https://customerportal.darktrace.com/product-guides/main/api-status-schema for response schema.

        :param params: set of query params to use, defaults to {"fast":True, "includechildren":False}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool
        :return: returns the system status information
        :rtype: dict
        """
        if not params:
            params = {"fast":True, "includechildren":False}

        return self._execute_dt_request("GET", SYSTEM_STATUS_URI, params=params, capture_error=capture_error)

    def get_model_breaches(self, params: dict = None, capture_error: bool = False) -> list:
        """
        Get list of model breaches that matches the given query parameters.

        See https://customerportal.darktrace.com/product-guides/main/api-modelbreaches-schema for response schema.

        :param params: set of query params, defaults to {"expandenums": "true"}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool
        :return: returns a list of model breaches
        :rtype: list
        """
        if not params:
            params = {"expandenums": "true"}

        return self._execute_dt_request("GET", MODEL_BREACHES_URI, params=params, capture_error=capture_error)

    def get_model_breach_comments(self, breach_id: str, params: dict = None, capture_error: bool = False) -> list:
        """
        Get list of comments for a given model breach.

        https://customerportal.darktrace.com/product-guides/main/api-modelbreaches-comments-schema for response schema.

        :param breach_id: ID of the model breach to get comments for
        :type breach_id: str
        :param params: optional extra query parameters, defaults to {}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool
        :return: returns the list of comments associated with the given breach
        :rtype: list
        """
        if not params:
            params = {}

        return self._execute_dt_request("GET", MODEL_BREACHES_COMMENTS_URI.format(breach_id), params=params, capture_error=capture_error)

    def get_incident_groups(self, params: dict = None, capture_error: bool = False) -> list:
        """
        List incident groups that match the given parameters.

        See https://customerportal.darktrace.com/product-guides/main/api-aianalyst-groups-schema for response schema.

        :param params: query params, defaults to {}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool
        :return: returns the list of incident groups
        :rtype: list
        """
        if not params:
            params = {}

        return self._execute_dt_request("GET", AI_ANALYST_INCIDENT_GROUPS, params=params, capture_error=capture_error)

    def get_incident_events(self, group_id: str = None, params: dict = None, capture_error: bool = False) -> list:
        """
        Get a list of incident events that match the given query parameters.
        Should usually be paired with a incident group ID to only gather the events 
        associated with the incident group.

        See https://customerportal.darktrace.com/product-guides/main/api-aianalyst-incidentevents-schema for response schema.

        :param group_id: group id to look for events in, defaults to None
        :type group_id: str, optional
        :param params: query params to include, defaults to {"includeacknowledged": "true", "includeincidenteventurl": "true"}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool
        :return: returns the list of incident events
        :rtype: list
        """
        if not params:
            params = {"includeacknowledged": "true", "includeincidenteventurl": "true", "locale": self.locale}

        if group_id:
            params.update({"groupid": group_id})
        return self._execute_dt_request("GET", AI_ANALYST_EVENTS_URI, params=params, capture_error=capture_error)

    ########
    # TODO: there is an endpoint that allows you to download an event as a PDF — this should be exposed!
    # EX: GET https://euw2-75824-01.cloud.darktrace.com/aianalyst/incidentevents?filename=test2.pdf&locale=en_US&format=pdf&uuid=c4d450cd-a4a4-4840-bd95-042b73a2ca3f
    ########

    def get_incident_group_comments(self, incident_id: str = None, params: dict = None, capture_error: bool = False) -> dict:
        """
        Get comments from an incident event.

        :param incident_id: id of the incident to get comments of, defaults to None
        :type incident_id: str|int, optional
        :param params: query params to include, defaults to {}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool, optional
        :return: dict with object "comments" which is a list of comments on the incident event
        :rtype: list
        """
        if not params:
            params = {}

        if incident_id:
            params.update({"incident_id": incident_id})
        return self._execute_dt_request("GET", AI_ANALYST_EVENT_COMMENTS_URI, params=params, capture_error=capture_error)

    def add_incident_group_comment(self, incident_id: str, comment: str, params: dict = None, capture_error: bool = False) -> dict:
        """
        Add a comment to an incident group.

        Can be used when the incident group is synced to SOAR to post a comment

        :param incident_id: id of the incident
        :type incident_id: str
        :param comment: content to post to the comment
        :type comment: str
        :param params: other parameters to add, defaults to {}
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored, defaults to False
        :type capture_error: bool, optional
        :return: response from posting the comment
        :rtype: dict
        """
        if not params:
            params = {}

        body = {
            "incident_id": incident_id,
            "message": comment
        }
        return self._execute_dt_request("POST", AI_ANALYST_EVENT_COMMENTS_URI, data=body, params=params, capture_error=capture_error)

    def get_devices(self, params: dict = None, capture_error: bool = False) -> list:
        """
        Get a list of devices.
        To get one devices by ID: ``params={"did": "<device_id>"}`` -> returns {...}
        To get a list of devices by their IDs: ``params={"did": "<device_id_1>,<decive_id_2"}`` -> returns [{...}, {...}, ...]

        NOTE: You can include a trailing comma with just one device to get a list returned.

        See https://customerportal.darktrace.com/product-guides/main/api-devices-schema for response schema.

        :param params: query params to include
        :type params: dict, optional
        :param capture_error: if True, failing requests will be captured, logged, but ignored
        :type capture_error: bool
        :return: returns the list of devices
        :rtype: list
        """
        if not params:
            params = {}

        return self._execute_dt_request("GET", DEVICES_URI, params=params, capture_error=capture_error)
    #############
    # END CLASS #
    #############



##################
# HELPER METHODS #
##################



def _get_verify_ssl(app_configs: dict, integrations_configs: dict = {}) -> bool:
    """
    Get ``verify`` parameter from app config.
    Value can be set in [integrations] or in the [fn_darktrace] section
    Value in [fn_darktrace] takes precedence over [integrations]

    :param opts: All of the app.config file as a dict
    :type opts: dict
    :param app_options: App specific configs
    :type app_options: dict
    :return: Value to set ``requests.request.verify`` to. Either a path or a boolean. Defaults to ``True``
    :rtype: bool|str(path)
    """

    verify = app_configs.get(REQUEST_VERIFY_CONFIG)

    # NOTE: specifically want ``if verify is None`` rather than
    # ``if not verify``, as the value of verify can be set to "False"
    if verify is None:
        verify = integrations_configs.get(REQUEST_VERIFY_CONFIG, DEFAULT_VERIFY)

    # because verify can be either a boolean or a path,
    # we need to check if it is a string with a boolean 
    # value first then, and only then, we convert it to a bool
    # NOTE: that this will then only support "true" or "false"
    # (case-insensitive) rather than the normal "true", "yes", etc...
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    return verify
