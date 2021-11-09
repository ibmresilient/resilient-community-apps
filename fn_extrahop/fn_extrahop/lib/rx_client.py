# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Reveal(x) client class for SOAR app supporting Extrahop integration"""
import json
import logging
import base64
import re

from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)


class RxClient():
    """ Class to support Extrahop Reveal(x) api.

    """
    def __init__(self, opts, fn_opts):
        """ Class constructor.

        :param opts: SOAR options dict.
        :param fn_opts: Function specific options dict.

        """
        if not isinstance(opts, dict) and not opts:
            raise ValueError("The 'opts' parameter is not set correctly.")
        if not isinstance(fn_opts, dict) and not fn_opts:
            raise ValueError("The 'fn_opts' parameter is not set correctly.")
        self.host_url = fn_opts.get("extrahop_rx_host_url")
        self.key_id = fn_opts.get("extrahop_rx_key_id")
        self.key_secret = fn_opts.get("extrahop_rx_key_secret")
        self.api_version = fn_opts.get("extrahop_rx_api_version")
        self.api_base_url = "{}/api/{}".format(self.host_url, self.api_version)
        # Define api endpoints
        self._endpoints = {
            # Devices
            "token":             "/".join([self.host_url, "oauth2/token"]),
            "devices":           "/".join([self.api_base_url, "devices/{}"]),
            "search_devices":    "/".join([self.api_base_url, "devices/search"]),
            "detections":        "/".join([self.api_base_url, "detections/{}"]),
            "search_detections": "/".join([self.api_base_url, "detections/search"]),
            "tags":              "/".join([self.api_base_url, "tags"]),
            "create_tag":        "/".join([self.api_base_url, "tags"]),
            "assign_tag":        "/".join([self.api_base_url, "tags/{}/devices"]),
            "watchlist":         "/".join([self.api_base_url, "watchlist/devices"]),
            "activitymaps":      "/".join([self.api_base_url, "activitymaps/{}"])
        }
        self.rc = RequestsCommon(opts=opts, function_opts=fn_opts)
        self._headers = {"Authorization": "Bearer " + self.get_token()}

    def get_token(self):
        """
        Get an API access token for Reveal(x) 360 authentication.

        :return: API Access token (string)
        """
        uri = self._endpoints["token"]

        auth = base64.b64encode(bytes(self.key_id + ":" + self.key_secret, "utf-8")).decode("utf-8")

        headers = {
            "Authorization": "Basic " + auth,
            "Content-Type": "application/x-www-form-urlencoded",
        }

        r = self.rc.execute_call_v2("post", uri, headers=headers, data="grant_type=client_credentials")

        return r.json()["access_token"]

    def get_devices(self, active_from=None, active_until=None, limit=None, offset=None, device_id=None,
                    search_type=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param search_type: Search type (str)
        :param device_id: device_id (str)
        :param active_from: (Optional) The beginning timestamp (in millisecs) for the request. Default 0 (int)
        :param active_until: (Optional) The ending timestamp (in millisecs) for the request. Default 0 (int)
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :return Result in json format.

        """
        # Set default uri
        uri = self._endpoints["devices"].format('')
        params = {}

        params["active_from"] = active_from if active_from else 0
        params["active_until"] = active_until if active_until else 0
        params["limit"] = int(limit) if limit else 0
        params["offset"] = int(offset) if offset else 0
        params["search_type"] = search_type if offset else "any"

        if device_id:
            uri = self._endpoints["devices"].format(device_id)

        r = self.rc.execute_call_v2("get", uri, headers=self._headers, params=params)

        return r

    def search_devices(self, active_from=None, active_until=None, limit=None, offset=None, search_filter=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param active_from: (Optional) The beginning timestamp (in millisecs) for the request. Default 0 (int)
        :param active_until: (Optional) The ending timestamp (in millisecs) for the request. Default 0 (int)
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :param search_filter: Search filter (json str)
        :return Result in json format.`
        """
        uri = self._endpoints["search_devices"]
        data = {"filter": {}}

        if search_filter:
            try:
                filter_data = json.loads(search_filter)
            except ValueError:
                raise ValueError("The search filter is not valid json content")
        if filter_data.get("filter"):
            data["filter"] = filter_data.get("filter")
        data["active_from"] = active_from if active_from else 0
        data["active_until"] = active_until if active_until else 0
        data["limit"] = int(limit) if limit else 0
        data["offset"] = int(offset) if offset else 0

        r = self.rc.execute_call_v2("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_detections(self, detection_id=None, limit=None):
        """Get information about detections or a specific detection by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param detection_id: Detection id (str)
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :return Result in json format.
        """
        # Set default uri
        uri = self._endpoints["detections"].format('')
        params = {}

        params["limit"] = int(limit) if limit else 0

        if detection_id is not None:
            uri = self._endpoints["detections"].format(detection_id)

        r = self.rc.execute_call_v2("get", uri, headers=self._headers, params=params)

        return r

    def search_detections(self, search_filter=None, active_from=None, active_until=None, limit=None, offset=None,
                          update_time=None, sort=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param search_filter: (Optional) Search filter (json str)
        :param active_from: (Optional)  Get Detections that occurred after the specified timestamp (in millisecs).
        Default 0 (int)
        :param active_until: (Optional) Get detections that ended before the specified timestamp (in millisecs).
        Default 0 (int)
        :param limit: (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :param update_time: (Optional) Get detections that were updated on or after the specified date (int).
        :param sort: (Optional) Sorts returned detections by the specified fields. (int).
        :return Result in json format.`
        """
        uri = self._endpoints["search_detections"]
        data = {"filter": {}}

        if search_filter:
            try:
                filter_data = json.loads(search_filter)
            except ValueError:
                raise ValueError("The search filter is not valid json content")

        if filter_data.get("filter"):
            data["filter"] = filter_data.get("filter")

        if sort:
            try:
                sort_data = json.loads(sort)
            except ValueError:
                raise ValueError("The sort parameter is not valid json content")
            data["sort"] = sort_data
        data["from"] = active_from if active_from else 0
        data["until"] = active_until if active_until else 0
        data["limit"] = int(limit) if limit else 0
        data["offset"] = int(offset) if offset else 0
        data["update_time"] = int(update_time) if update_time else 0

        r = self.rc.execute_call_v2("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def update_detection(self, detection_id=None, incident_id=None, plan_status=None, owner_id=None,
                         resolution_id=None, participants=None):
        """Update a detection with information from a Resilient incident.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param detection_id: Detection id (int)
        :param incident_id: SOAR incident ID (int)
        :param plan_status: SOAR incident status (str)
        :param owner_id: SOAR incident owner ID (str)
        :param resolution_id: SOAR incident resolution (str)
        :return Result in json format.
        """
        uri = self._endpoints["detections"].format(detection_id)
        status_map = {
            "A": 'in_progress',  # active
            "C": 'closed',  # done
        }
        resolution_map = {
            "Unresolved": "no_action_taken",
            "Duplicate": "no_action_taken",
            "Not an Issue": "no_action_taken",
            "Resolved": "action_taken",
        }
        data = {
            "detection_id": detection_id,
            "ticket_id": incident_id,
            "assignee": owner_id
        }
        data["status"] = status_map[plan_status]

        if plan_status == 'C':
            data["resolution"] = resolution_map[resolution_id]

        r = self.rc.execute_call_v2("patch", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_tags(self, tag_id=None):
        """Get information about tags or a specific tag by tag id.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param tag_id: Tag id (int)
        :return Result request response.

        """
        # Set default uri
        uri = self._endpoints["tags"].format('')

        if tag_id is not None:
            uri = self._endpoints["tags"].format(tag_id)

        r = self.rc.execute_call_v2("get", uri, headers=self._headers)

        return r

    def create_tag(self, tag_name=None):
        """Create a tag.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param tag_name: Tag name (str)
        :return Result request response.

        """
        if tag_name is None:
            raise ValueError("Missing 'tag_name' parameter")

        uri = self._endpoints["create_tag"].format(tag_name)

        data = {"name": tag_name}

        r = self.rc.execute_call_v2("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def assign_tag(self, tag_id=None, device_ids=None):
        """Assign a tag to a list of devices.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param tag_id: Tag id (int)
        :param device_ids: Comma or newline separated list of device ids (str)
        :return Result request response.

        """
        if tag_id is None:
            raise ValueError("Missing 'tag_id' parameter")

        if not device_ids:
            raise ValueError("Missing 'device_ids' parameter")

        # Convert keywords in comma or newline seperated string to a list.
        device_ids = list(filter(None, re.split(r"\s+|,|\n", device_ids)))

        uri = self._endpoints["assign_tag"].format(tag_id)

        data = {"assign": device_ids}

        r = self.rc.execute_call_v2("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_watchlist(self):
        """Retrieve all devices that are in the watchlist.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :return Result request response.
        """
        uri = self._endpoints["watchlist"]

        r = self.rc.execute_call_v2("get", uri, headers=self._headers)

        return r

    def update_watchlist(self, assign=None, unassign=None):
        """Retrieve all devices that are in the watchlist.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param assign: Comma or newline separated list of device ids to assign to a watchlist (str)
        :param unassign: Comma or newline separated list of device ids to unassign from a watchlist(str)
        :return Result request response.
        """
        uri = self._endpoints["watchlist"]
        data = {}

        if assign is not None:
            assign_ids = list(filter(None, re.split(r"\s+|,|\n", assign)))
            data = {"assign": assign_ids}

        if unassign is not None:
            unassign_ids = list(filter(None, re.split(r"\s+|,|\n", assign)))
            data = {"assign": unassign_ids}

        r = self.rc.execute_call_v2("get", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_activitymaps(self, activitymap_id=None):
        """Get information about activitymaps or a specific activitymap by id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param activitymap_id: Activitymap id (str)
        :return Result in json format.
        """
        # Set default uri
        uri = self._endpoints["activitymaps"].format('')
        params = {}

        if activitymap_id is not None:
            uri = self._endpoints["activitymaps"].format(activitymap_id)

        r = self.rc.execute_call_v2("get", uri, headers=self._headers)

        return r
