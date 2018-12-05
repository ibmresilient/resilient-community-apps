# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Class for Resilient circuits Functions supporting REST API client for Cisco AMP for endpoints  """
import logging
import random
import requests
import time
from requests import HTTPError
from requests.auth import HTTPBasicAuth
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin
import json
import re
from datetime import datetime

LOG = logging.getLogger(__name__)
# Define query limit default for the integration.
AMP_LIMIT_DEFAULT = 1000
# Define max query limit REST api will allow as a parameter.
AMP_LIMIT_REST_MAX = 500

class Ampclient(object):
    """
    Client class used to expose Cisco AMP for endpoints Rest API for queries
    """
    def __init__(self, options, rate_limiter):
        """
        Class constructor
        """

        self.base_url = options.get("base_url")
        self.client_id = options.get("client_id")
        self.api_token = options.get("api_token")
        self.api_version = options.get("api_version")
        self.max_retries = int(options.get("max_retries"))
        self.proxies = {}
        if "https_proxy" in options and options["https_proxy"] is not None:
            self.proxies.update({"https": options.get("https_proxy")})
        if "http_proxy" in options and options["http_proxy"] is not None:
            self.proxies.update({"http": options.get("http_proxy")})
        if options.get("query_limit") is not None:
            self.query_limit = int(options.get("query_limit"))
        # Rest request endpoints
        self._endpoints = {
            # Computers
            "computers":                    "/"+self.api_version+"/computers/",
            "computer":                     "/"+self.api_version+"/computers/{}",
            "computer_trajectory":          "/"+self.api_version+"/computers/{}/trajectory/",
            "activity":                     "/"+self.api_version+"/computers/activity",
            # File lists
            "file_lists":                   "/"+self.api_version+"/file_lists/simple_custom_detections",
            "file_lists_files":             "/"+self.api_version+"/file_lists/{}/files",
            "file_lists_files_by_sha256":   "/"+self.api_version+"/file_lists/{}/files/{}",
            # Events
            "events":                       "/"+self.api_version+"/events",
            "event_types":                  "/"+self.api_version+"/event_types/",
            # Groups
            "groups":                       "/"+self.api_version+"/groups/",
            "group_by_guid":                "/"+self.api_version+"/groups/{}"
        }
        self._headers = {"content-type": "application/json", "Accept": "application/json",
                        "Accept-Encoding": "application/gzip", "Authorization": "Basic FILTERED"}
        self._auth = HTTPBasicAuth(self.client_id, self.api_token)
        self._s = requests.Session()

        # Maintain information about the rate-limiter information from the most recent call.
        self.rate_limiter = rate_limiter

    def _save_rate_limit(self, response):
        """Save rate limit info to safelimiter object from the response headers.

        :param response: Response returned from api call.

        """
        limit_headers = {k: v for k, v in response.headers.items() if k.startswith(u"X-RateLimit")}
        self.rate_limiter.save_limits(limit_headers)


    def suggested_delay(self):
        """Return period (in secs) function should wait before making the next api call.

        """
        # Check if this is 1st time rate limiter called (by any function).
        if not self.rate_limiter.get_limit_update_ts():
            # Get here if this is 1st time rate limiter called (by any function) during this
            # resilient circuits run period.
           return 0
        else:
            return self.rate_limiter.get_delay()

    def _req(self, uri, method='GET', params=None, data=None):
        """Method which initiates the REST API call. Default method is the GET method also supports POST, PATCH and
        DELETE. Retries are attempted if a Rate limit exception (429) is  detected.

        :param uri: Used to form url
        :param method: Request method, defaults to "GET"
        :param params: Parameters used by session request to form finished request
        :param data: Data body used in post requests
        :return: Response in json format

        """
        url = urljoin(self.base_url, uri)

        retry_attempts = 0

        if data is None:
            data = {}

        if params is None:
            params = {}

        # See if we need to add rate limit delay.
        rl_delay = self.suggested_delay()
        if rl_delay > 0:
            LOG.debug("Rate limiting! Delay %s seconds for url %s", rl_delay, url)
            time.sleep(rl_delay)

        while retry_attempts <= self.max_retries:
            try:
                # Save timestamp of new request to ratelimiter.
                self.rate_limiter.add_ts(time.time())
                if method == "GET":
                    r = self._s.get(url, params=params, headers=self._headers, auth=self._auth, proxies=self.proxies )
                elif method == "POST":
                    r = self._s.post(url, params=params, data=data, headers=self._headers, auth=self._auth, proxies=self.proxies)
                elif method == "PATCH":
                    r = self._s.patch(url, params=params, data=data, headers=self._headers, auth=self._auth, proxies=self.proxies)
                elif method == "DELETE":
                    r = self._s.delete(url, params=params, headers=self._headers, auth=self._auth, proxies=self.proxies)
                else:
                    raise ValueError("Unsupported request method '{}'.".format(method))
                # Save rate limit data from response.
                self._save_rate_limit(r)

                r.raise_for_status()  # If the request fails throw an error.

            except HTTPError as e:
                if e.response.status_code == 429:
                    LOG.exception("Got Rate Limiting exception type: %s, msg: %s" % (e.__repr__(), getattr(e, 'message', str(e))))
                    # Retry if we get Rate Limiting response.
                    # Set delay to value of r.headers["Retry-After"].
                    retry_delay = int(r.headers.get("Retry-After"))
                    LOG.info("Retrying in %f seconds..." % (retry_delay))
                    time.sleep(retry_delay)
                elif e.response.status_code == 409 and method == "POST":
                    # We are probably trying to redo a successful update operation here.
                    LOG.error("Got '409' error, possible attempt to redo a successfull update operation.")
                    # Allow error to bubble up to the Resilient function.
                    break
                else:
                    raise

            if r.status_code in range(200, 203):
                break
            elif r.status_code != 429:
                LOG.error("Unexpected response '%s' received." % r.status_code)
                raise HTTPError("Unexpected response '{}' received.".format(r.status_code))

            retry_attempts += 1
            if (retry_attempts > self.max_retries):
                LOG.error("Too many retry attempts")
                raise HTTPError("Too many retry attempts")

        return r.json()

    def test_connectivity(self):
        """Connectivity Test which is used by resilient_circuits selftest.

        Calls http 'head' request against 'event_types' url.

        :return: Response
        """
        url = urljoin(self.base_url, self._endpoints["event_types"])
        r = self._s.head(url, auth=self._auth)
        return r

    def get_computers(self, group_guid=None, limit=None, hostname=None, internal_ip=None, external_ip=None):
        """Get a list of computers with agents deployed on them. Use parameters to narrow the search by IP address
        ,hostname or guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param group_guid: Filter by group guid
        :param limit: Limit number of results
        :param hostname: Filter by hostname
        :param internal_ip: Filter by internal ip
        :param external_ip: Filter by external ip
        :return: Response in json format
        """
        uri = self._endpoints["computers"]
        params = {"group_guid": group_guid, "limit": limit, "hostname": hostname,
                  "internal_ip": internal_ip, "external_ip": external_ip }
        r_json = self._req(uri, params=params)
        return r_json

    def get_computer(self, connector_guid):
        """Get information about a specific computer by guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: connector_guid. Computer selection criteria
        :return Result in json format.

        """

        uri = self._endpoints["computer"].format(connector_guid)
        r_json = self._req(uri)
        return r_json

    def get_computer_trajectory(self, connector_guid, q=None, limit=None):
        """Get a list of all activities associated with a particular computer, search by guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: connector_guid. Computer selection criteria
        :param limit: Limit number of results
        :param q: Query string to search for an IP Address, SHA256 or URL.
        :return Result in json format.

        """

        uri = self._endpoints["computer_trajectory"].format(connector_guid)
        params = {"limit": limit, "q": q}
        r_json = self._req(uri, params=params)
        return r_json

    def get_activity(self, q, limit=None, offset=None):
        """Search all computers for any events or activities associated with a file or network operation

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param q: Search query string
        :param limit: Limit number of results
        :param offset: Results from offset
        :return Result in json format.

        """
        uri = self._endpoints["activity"]
        params = {"q": q, "limit": limit, "offset": offset}
        r_json = self._req(uri, params=params)
        return r_json

    def get_file_lists(self, name, limit=None, offset=None):
        """ Returns a list of simple custom detection file lists. List acnwe be filtered by name.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param name: Name search string
        :param limit: Limit number of results
        :param offset: Results from offset
        :return Result in json format.

        """
        uri = self._endpoints["file_lists"]
        params = {"name": name, "limit": limit, "offset": offset}
        r_json = self._req(uri, params=params)
        return r_json

    def get_file_list_files(self, file_list_guid, file_sha256, limit=None, offset=None):
        """ Returns a particular item for a given file_list. A SHA-256 and file_list_guid need to be provided
         to get an item.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param file_list_guid: file_list_guid value.
        :param file_sha256: File sha256 value.
        :param limit: Limit number of results
        :param offset: Results from offset
        :return Result in json format.

        """
        if file_sha256 is None:
            uri = self._endpoints["file_lists_files"].format(file_list_guid)
        else:
            uri = self._endpoints["file_lists_files_by_sha256"].format(file_list_guid, file_sha256)
        params = {"limit": limit, "offset": offset}
        r_json = self._req(uri, params=params)
        return r_json

    def set_file_list_files(self, file_list_guid, file_sha256, description):
        """Add a SHA-256 to a file list using file_list_guid.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param file_list_guid: file_list_guid value.
        :param file_sha256: File sha256 value.
        :return Result in json format.

        """
        uri = self._endpoints["file_lists_files_by_sha256"].format(file_list_guid, file_sha256)
        data = json.dumps({"description": description})
        r_json = self._req(uri, method="POST", data=data)
        return r_json

    def delete_file_list_files(self, file_list_guid, file_sha256):
        """ Delete a file list item with a given SHA-256 and associated to file list with given file_list_guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param file_list_guid: file_list_guid value.
        :param file_sha256: File sha256 value.
        :return Result in json format.

        """
        uri = self._endpoints["file_lists_files_by_sha256"].format(file_list_guid, file_sha256)
        r_json = self._req(uri, method="DELETE")
        return r_json

    def get_events(self, detection_sha256=None, application_sha256=None, connector_guid=None,
                   group_guid=None, start_date=None, event_type=None, limit=None, offset=None):
        """Get a list of events. Filter by criteria set by parameter values. The criteria types
        are logically ORed.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param detection_sha256: Filter by detection sha256
        :param application_sha256: Filter by application sha256
        :param connector_guid: Filter by connector guid
        :param group_guid: Filter by group guid
        :param start_date: Filter by start date
        :param event_type: Filter by event types
        :param limit: Limit number of results
        :param offset: Results from offset
        :return: Response in json format
        """
        uri = self._endpoints["events"]
        # Try and split event_type if not none
        if event_type is not None:
            event_type = re.split('\s+|,', event_type)

        # Convert start_date from Unix timestamp (in secs) to isoformat
        if start_date is not None:
            start_date = datetime.fromtimestamp(int(str(start_date)[0:-3])).isoformat()

        params = {"detection_sha256": detection_sha256, "application_sha256": application_sha256,
                  "connector_guid[]": connector_guid, "group_guid[]": group_guid, "start_date": start_date,
                  "event_type[]": event_type, "limit": limit, "offset": offset }
        r_json = self._req(uri, params=params)
        return r_json

    def get_event_types(self):
        """Get list of human readable names, and short descriptions of each event by ID.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :return Result in json format.

        """
        uri = self._endpoints["event_types"]
        r_json = self._req(uri)
        return r_json

    def get_groups(self, group_guid, name, limit=None):
        """Get information on groups or individual group by group_guid.

         For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: group_guid: Lookup by group_guid
        :param: name: Filter by group name
        :param limit: Limit number of results
        :return Result in json format.

        """
        if group_guid is None:
            uri = self._endpoints["groups"]
        else:
            uri = self._endpoints["group_by_guid"].format(group_guid)
        params = {"name": name , "limit": limit}
        r_json = self._req(uri, params=params)
        return r_json

    def move_computer(self, connector_guid, group_guid):
        """Get information on groups or individual group by group_guid.

         For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: connector_guid: Connector guid of computer to move.
        :param: group_guid: Group guid to move computer to.

        :return Result in json format.

        """
        uri = self._endpoints["computer"].format(connector_guid)
        data = json.dumps({"group_guid": group_guid})
        r_json = self._req(uri, method="PATCH", data=data)
        return r_json

    def get_paginated_total(self, get_method, **params):
        """Get multiple pages of paginated data. Use a limit value to limit returned results.

        The results limit defaults to AMP_LIMIT_DEFAULT unless params["limit"] or the 'query_limit' integration
        configuration property is set with params["limit"] having the highest precedence.

        :param: get_method: Reference to instance get method e.g. self.get_activity, self.get_events etc.
        :param: params: Parameters for get method .

        :return Result in json format.

        """
        results_total = None
        # Set query limit to max 1000 by default.
        limit_max_count = AMP_LIMIT_DEFAULT

        if "limit" in params and params["limit"] is not None:
            # Set to REST call limit parameter.
            limit_max_count = int(params["limit"])
        elif hasattr(self, "query_limit") and self.query_limit is not None:
            # Set limit to global override value.
            limit_max_count = self.query_limit

        if get_method.__name__ == "get_computer_trajectory":
            # Rest call get_computer_trajectory doesn't return a 'results' sub-dict.
            # If method is get_computer_trajectory get total in case limit is lower that total.
            rtn = get_method(**params)
            results_total = len(rtn["data"]["events"])

        if limit_max_count < AMP_LIMIT_REST_MAX or get_method.__name__ == "get_computer_trajectory":
                # Reset limit to query_limit if less than default limit.
                # Limit defined for "get_computer_trajectory" set to default for results calculation.
                params["limit"] = limit_max_count

        if get_method.__name__ != "get_computer_trajectory":
            rtn = get_method(**params)

        if "results" in rtn["metadata"]:
            # The 'get_computer_trajectory' Rest call doesn't return a 'results' sub-dict so assuming it returns all
            # results in that case.
            max_count = rtn["metadata"]["results"]["total"]
            if limit_max_count < max_count:
                max_count = limit_max_count

            offset = items_per_page = rtn["metadata"]["results"]["items_per_page"]
            if "offset" in params and params["offset"] is not None:
                # If offset parameter set add to offset value
                offset += int(params["offset"])
            current_item_count = rtn["metadata"]["results"]["current_item_count"]
            if not current_item_count < items_per_page:
                while max_count > current_item_count:
                    if "offset" in params:
                        # Certain get methods don't have offset in their parameter signature
                        params["offset"] = offset
                    rtn_sub = get_method(**params)
                    rtn["data"].extend(rtn_sub["data"])
                    rtn["metadata"] = rtn_sub["metadata"]
                    current_item_count += rtn["metadata"]["results"]["current_item_count"]
                    offset += items_per_page

        if results_total is not None:
            rtn["total"] = results_total
            # Return slice of rtn["data"]["events"] up to limit for "get_computer_trajectory"
            rtn["data"]["events"] = rtn["data"]["events"][:int(params["limit"])]

        return rtn