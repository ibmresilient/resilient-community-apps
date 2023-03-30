# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Reveal(x) client class for SOAR app supporting Extrahop integration"""
import json
import logging
import base64
import re
import requests
from retry import retry

from resilient_lib import RequestsCommon
from resilient_lib import validate_fields

LOG = logging.getLogger(__name__)


class AuthenticationError(Exception):
    """Trap authentication errors for reauthenticating"""
    pass

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
        validate_settings(fn_opts)
        self.host_url = fn_opts.get("extrahop_rx_host_url")
        self.cloud_console = fn_opts.get("extrahop_rx_cloud_console")
        self.api_version = fn_opts.get("extrahop_rx_api_version")
        self.key_id = fn_opts.get("extrahop_rx_key_id")
        self.key_secret = fn_opts.get("extrahop_rx_key_secret")
        self.api_key = fn_opts.get("extrahop_rx_api_key")
        # Allow explicit setting "do not verify certificates"
        self.verify = fn_opts.get("extrahop_cafile")
        if str(self.verify).lower() == "false":
            LOG.warning("Unverified HTTPS requests to ExtraHop server (cafile=false).")
            requests.packages.urllib3.disable_warnings()  # otherwise things get very noisy
            self.verify = False
        self.api_base_url = "{}/api/{}".format(self.host_url, self.api_version)
        # Define api endpoints
        self._endpoints = {
            # Devices
            "token":             "/".join([self.host_url, "oauth2/token"]),
            "devices":           "/".join([self.api_base_url, "devices/{}"]),
            "search_devices":    "/".join([self.api_base_url, "devices/search"]),
            "detections":        "/".join([self.api_base_url, "detections"]),
            "search_detections": "/".join([self.api_base_url, "detections/search"]),
            "detection_note":    "/".join([self.api_base_url, "detections/{}/notes"]),
            "tags":              "/".join([self.api_base_url, "tags/{}"]),
            "create_tag":        "/".join([self.api_base_url, "tags"]),
            "assign_tag":        "/".join([self.api_base_url, "tags/{}/devices"]),
            "watchlist":         "/".join([self.api_base_url, "watchlist/devices"]),
            "activitymaps":      "/".join([self.api_base_url, "activitymaps/{}"]),
            "search_packets":    "/".join([self.api_base_url, "packets/search"]),
            "networks":          "/".join([self.api_base_url, "networks"])
        }
        self.rc = RequestsCommon(opts=opts, function_opts=fn_opts)
        self.refresh_header = True
        if fn_opts.get("extrahop_rx_key_id"):
            # Connection to Cloud-based service.
            self._headers = {"Authorization": "Bearer " + self.get_token()}
        else:
            # Connection to standalone sensor.
            self._headers = {"Authorization": "ExtraHop apikey=" + self.api_key}

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

        self.refresh_header = False

        r = self.api_call("post", uri, headers=headers, data="grant_type=client_credentials")

        return r.json()["access_token"]

    def get_devices(self, active_from=None, active_until=None, limit=None, offset=None, device_id=None,
                    search_type=None, value=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param search_type: Search type (str)
        :param value: Search value (str)
        :param device_id: device_id (str)
        :param active_from: (Optional) The beginning timestamp (in millisecs) for the request.
        :param active_until: (Optional) The ending timestamp (in millisecs) for the request.
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :return Result in json format.

        """
        # Set default uri
        uri = self._endpoints["devices"].format('')
        params = {}

        if device_id:
            uri = self._endpoints["devices"].format(device_id)
        else:
            params["active_from"] = active_from
            params["active_until"] = active_until
            params["limit"] = int(limit) if limit else None
            params["offset"] = int(offset) if offset else None
            params["search_type"] = search_type if offset else "any"
            params["value"] = value

        r = self.api_call("get", uri, headers=self._headers, params=params)

        return r

    def search_devices(self, active_from=None, active_until=None, limit=None, offset=None, search_filter=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param active_from: (Optional) The beginning timestamp (in millisecs) for the request (int).
        :param active_until: (Optional) The ending timestamp (in millisecs) for the request (int).
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :param search_filter: Search filter (json str)
        :return Result in json format.`
        """
        uri = self._endpoints["search_devices"]
        data = {}

        if search_filter:
            try:
                filter_data = json.loads(search_filter)
            except ValueError:
                raise ValueError("The search filter is not valid json content: '{}'".format(search_filter))
            if filter_data.get("filter"):
                data["filter"] = filter_data.get("filter")

        data["active_from"] = active_from
        data["active_until"] = active_until
        data["limit"] = int(limit) if limit else None
        data["offset"] = int(offset) if offset else None

        r = self.api_call("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_detections(self, detection_id=None, limit=None):
        """Get information about detections or a specific detection by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param detection_id: Detection id (str)
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :return Result in json format.
        """
        # Set default uri
        uri = self._endpoints["detections"]
        params = {}
        if limit:
            params["limit"] = int(limit)

        if detection_id is not None:
            uri = uri + "/{}".format(detection_id)

        r = self.api_call("get", uri, headers=self._headers, params=params)

        return r

    def search_detections(self, search_filter=None, active_from=None, active_until=None, limit=None, offset=None,
                          update_time=None, sort=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param search_filter: (Optional) Search filter (dict or json str)
        :param active_from: (Optional)  Get Detections that occurred after the specified timestamp (in millisecs).
        Default 0 (int)
        :param active_until: (Optional) Get detections that ended before the specified timestamp (in millisecs).
        Default 0 (int)
        :param limit: (Optional) Limit the number of detections returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of detections (int).
        :param update_time: (Optional) Get detections that were updated on or after the specified date (int).
        :param sort: (Optional) Sorts returned detections by the specified fields. (int).
        :return Result in json format.`
        """
        uri = self._endpoints["search_detections"]
        data = {}
        filter_data = {}

        if search_filter:
            if isinstance(search_filter, dict):
                filter_data = search_filter
            else:
                try:
                    filter_data = json.loads(search_filter)
                except ValueError:
                    raise ValueError("The search filter is not valid json content: '{}'".format(search_filter))

            if filter_data:
                if filter_data.get("filter"):
                    data["filter"] = filter_data.get("filter")
                else:
                    data["filter"] = filter_data

        if sort:
            try:
                sort_data = json.loads(sort)
            except ValueError:
                raise ValueError("The sort parameter is not valid json content: '{}'".format(sort))
            data["sort"] = sort_data
        if active_from:
            data["from"] = active_from
        if active_until:
            data["until"] = active_until
        if limit:
            data["limit"] = int(limit)
        if offset:
            data["offset"] = int(offset)
        if update_time:
            data["update_time"] = int(update_time)

        r = self.api_call("post", uri, headers=self._headers, data=json.dumps(data))

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
        :param participants: (Optional) Participants (json str)
        :return Result in json format.
        """
        uri = self._endpoints["detections"] + "/{}".format(detection_id)
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
        }
        if incident_id is not None:
            data["ticket_id"] = str(incident_id)

        if owner_id:
            data["assignee"] = owner_id

        if plan_status:
            data["status"] = status_map[plan_status]

            if plan_status == 'C':
                data["resolution"] = resolution_map[resolution_id]

        if participants:
            try:
                p_data = json.loads(participants)
            except ValueError:
                raise ValueError("The participants parameter is not valid json content: '{}'".format(participants))
            if p_data.get("participants"):
                data["participants"] = p_data.get("participants")

        r = self.api_call("patch", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_detection_note(self, detection_id=None):
        """Get the note from a detection.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param detection_id: Detection id (str)
        """
        uri = self._endpoints["detection_note"].format(detection_id)

        r = self.api_call("get", uri, headers=self._headers)

        return r

    def add_detection_note(self, detection_id=None, note=None, update_time=None):
        """Add a note to a detection.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param detection_id: Detection id (str)
        :param author: The user who updates the note (str)
        :param note: Text to add to note (str).
        :param update_time: (Optional) Time when note was added (in millisecs). Default 0 (int)
        """
        uri = self._endpoints["detection_note"].format(detection_id)
        data = {}

        data["note"] = note
        data["update_time"] = int(update_time) if update_time else 0

        r = self.api_call("put", uri, headers=self._headers, data=json.dumps(data))

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

        r = self.api_call("get", uri, headers=self._headers)

        return r

    def create_tag(self, tag_name=None):
        """Create a tag.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param tag_name: Tag name (str)
        :return Result request response.

        """
        if tag_name is None:
            raise ValueError("Missing 'tag_name' parameter")

        uri = self._endpoints["create_tag"]

        data = {"name": tag_name}

        r = self.api_call("post", uri, headers=self._headers, data=json.dumps(data))

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
        device_ids = [int(v) for v in list(filter(None, re.split(r"\s+|,|\n", device_ids)))]

        uri = self._endpoints["assign_tag"].format(tag_id)

        data = {"assign": device_ids}

        r = self.api_call("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_watchlist(self):
        """Retrieve all devices that are in the watchlist.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :return Result request response.
        """
        uri = self._endpoints["watchlist"]

        r = self.api_call("get", uri, headers=self._headers)

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
            assign_ids = [int(v) for v in list(filter(None, re.split(r"\s+|,|\n", assign)))]
            data = {"assign": assign_ids}

        if unassign is not None:
            unassign_ids = [int(v) for v in list(filter(None, re.split(r"\s+|,|\n", unassign)))]
            data = {"unassign": unassign_ids}

        r = self.api_call("post", uri, headers=self._headers, data=json.dumps(data))

        return r

    def get_activitymaps(self, activitymap_id=None):
        """Get information about activitymaps or a specific activitymap by id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param activitymap_id: Activitymap id (str)
        :return Result in json format.
        """
        # Set default uri
        uri = self._endpoints["activitymaps"].format('')

        if activitymap_id is not None:
            uri = self._endpoints["activitymaps"].format(activitymap_id)

        r = self.api_call("get", uri, headers=self._headers)

        return r

    def search_packets(self, output=None, always_return_body=False, active_from=None, active_until=None, limit_bytes=None,
                       limit_search_duration=None, bpf=None, ip1=None, port1=None, ip2=None, port2=None):
        """Search for and download packets stored on the ExtraHop system

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param output: (Optional) The output format. The following values are valid pcap, keylog_txt, zip(str)
        :param always_return_body: (Optional) If search does not match any packets, returns an empty packet capture
                                              file and an HTTP status of 200.(boolean)
        :param active_from: (Optional)  Get packets that occurred after the specified timestamp (in millisecs).
        Default 0 (int)
        :param active_until: (Optional) Get packets that ended before the specified timestamp (in millisecs).
        Default 0 (int)
        :param limit_bytes: (Optional) The maximum number of bytes to return. (str).
        :param limit_search_duration: (Optional) The maximum amount of time to run the packet search. (int).
        :param bpf:  (Optional) The Berkeley Packet Filter (BPF) syntax for the packet search. (str)
        :param ip1: (Optional) Returns packets sent to or received by the specified IP address. (str)
        :param port1: (Optional) Returns packets sent from or received on the specified port. (str)
        :param ip2: (Optional) Returns packets sent to or received by the specified IP address.
        :param port2: (Optional) Returns packets sent from or received on the specified port.
        :return Result in json format.`
        """
        uri = self._endpoints["search_packets"]
        params = {}

        params["from"] = active_from if active_from else 0
        params["until"] = active_until if active_until else 0
        params["limit_search_duration"] = int(limit_search_duration) if limit_search_duration else 0
        params["always_return_body"] = "{}".format(always_return_body).lower()
        if output:
            params["output"] = output
        if limit_bytes:
            params["limit_bytes"] = int(limit_bytes)
        if bpf:
            params["bpf"] = bpf
        if ip1:
            params["ip1"] = ip1
        if port1:
            params["port1"] = port1
        if ip2:
            params["ip2"] = ip2
        if port2:
            params["port2"] = port2

        r = self.api_call("get", uri, headers=self._headers, params=params)

        return r

    def get_networks(self):
        """Get network information from the ExtraHop environment.

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :return Result request response.

        """
        # Set default uri
        uri = self._endpoints["networks"]

        r = self.api_call("get", uri, headers=self._headers)

        return r.json()

    def callback(self, response):
        """ Callback needed for certain REST API call errors.

        :param response:
        :return: response or raise error for selected error codes
        """
        if response.status_code in [400, 401]:
            self.refresh_header = True
            if response.status_code == 400:
                if "invalid\n" in response.text.lower():
                    # Invalid response can occur because of authentication error
                    r_text = response.text
                elif response.url.endswith("devices/search"):
                    return response
                else:
                    response.raise_for_status()
            else:
                r_text = response.json()
            # Return status dict for selected codes.
            return {
                "error_code": response.status_code,
                "text": r_text
            }

        if response.status_code in [409, 422, 500]:
            return response

        response.raise_for_status()

        return response

    @retry(AuthenticationError, tries=2, delay=2)
    def api_call(self, method, uri, **kwargs):
        """Handle requests to ExtraHop endpoints .

        :param method: Request method such as "get","post", "put"
        :param uri: The uri of the request.
        :param kwargs: Can include request parameter dicts such as headers, data etc.
        :return res: Response
        """
        res = None

        if self.refresh_header and self.rc.function_opts.get("extrahop_rx_key_id"):
            if not uri.endswith("token"):
                # If not a token request refresh token in header for Cloud-based access.
                self._headers = {"Authorization": "Bearer " + self.get_token()}
                kwargs.update({"headers": self._headers})

        res = self.rc.execute_call_v2(method, uri, verify=self.verify, callback=self.callback, **kwargs)

        if isinstance(res, dict):
            error_code = res.get("error_code", None)
            if error_code:
                if error_code in [400, 401]:
                    # If a 400 or 401 error throw authentication error.
                    raise AuthenticationError(res)
        return res

def validate_settings(fn_opts):
    """Validate app config settings.

    :param fn_opts: App settings dict.
    """
    validate_fields([
        {"name": "extrahop_rx_host_url", "placeholder": "<EXTRAHOP_RX_HOST_URL>"},
        {"name": "polling_interval", "placeholder": "<POLLING_INTERVAL>"},
        {"name": "extrahop_rx_api_version"}],
        fn_opts)

    if fn_opts.get("extrahop_rx_key_id"):
        validate_fields([
            {"name": "extrahop_rx_cloud_console", "placeholder": "<EXTRAHOP_RX_CLOUD_CONSOLE>"},
            {"name": "extrahop_rx_key_id", "placeholder": "<EXTRAHOP_RX_API_KEY_ID>"},
            {"name": "extrahop_rx_key_secret", "placeholder": "<EXTRAHOP_RX_API_KEY_SECRET>"}],
            fn_opts)
    else:
        validate_fields([
            {"name": "extrahop_rx_api_key", "placeholder": "<EXTRAHOP_RX_API_KEY>"}],
            fn_opts)

    if fn_opts.get("extrahop_cafile") is not None:
        validate_fields([
            {"name": "extrahop_cafile", "placeholder": "<path to cert file>|false"}],
            fn_opts)
