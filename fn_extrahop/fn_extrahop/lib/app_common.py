# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Poller support functionality for interaction with the 3rd party endpoints"""

import logging
from urllib.parse import urljoin
from fn_extrahop.lib.rx_client import RxClient

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_extrahop"

DEFAULT_CLOUD_CONSOLE = "https://ibm-partner.cloud.extrahop.com"
# URL fragment to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "/extrahop/#/detections/detail/{}"
# List of fields to check to determine if an update is required.
UPDATEABLE_FIELDS = [
    "update_time", "end_time", "risk_score",
    "status", "ticket_id", "assignee"
]
# Default prefix for function parameters
F_PREFIX = "extrahop_"


class AppCommon():
    """ Class to support interaction with the 3rd party endpoints for poller.
    """
    def __init__(self, opts, options):
        """initialize the parameters needed to communicate to the endpoint solution

        Args:
            opts (dict): app.config settings for the integration
            options (dict): app.config settings for the app
        """
        self.endpoint_url = options['extrahop_rx_host_url']
        # Flag to indicate if we are connecting to the cloud instance.
        self._cloud_svc = True if options.get("extrahop_rx_key_id") else False
        self.rx_cli = RxClient(opts, options)
        self.entity_count = 0

    def get_entities_since_ts(self, timestamp, search_filter, limit=None, offset=None):
        """Get changed entities since last poller run

        Args:
            timestamp (datetime): datetime when the last poller ran
            search_filter (dict): Filter to use in api call
            offset (int): Start search at offset
            limit (int): Limit number of entries in result

        Returns:
            list: changed entity list
        """
        categories = None
        search_filter_api = {}

        if search_filter:
            search_filter_api = search_filter.copy()
            # Category filters are managed after the api call is made
            if "category" in search_filter:
                categories = search_filter_api.pop("category")

        response = self.rx_cli.search_detections(search_filter=search_filter_api, limit=limit, offset=offset)

        result = response.json()

        if response.status_code not in [200, 201, 204]:
            LOG.error("{{package_name}} API call failed: %s", result)
            return None

        self.entity_count = len(result)

        if categories:
            result = self.filter_by_property(result, "categories", categories)

        return result

    def make_linkback_url(self, entity_id, linkback_url=LINKBACK_URL):
        """Create a url to link back to the endpoint alert, case, etc.

        Args:
            entity_id (str/int): id representing the detection etc.
            linkback_url (str): Over-ride for the default linkback url

        Returns:
            str: completed url for linkback
        """
        if self._cloud_svc:
            return urljoin(DEFAULT_CLOUD_CONSOLE, linkback_url.format(entity_id))
        else:
            return urljoin(self.endpoint_url, linkback_url.format(entity_id))

    def filter_by_property(self, result, prop, filters):
        """Filter result based on a a property list .
           Used for filters not fully supported inb api or don't support a property lists

        Args:
            prop (string): Property to filer by.
            filters (list): List of values to filter by.
            result (dict): Result returned from ExtraHop

        Returns:
            filtered_result: Result filtered by risk score threshold
        """
        filtered_result = [r for r in result if any(i in r[prop] for i in filters)]
        LOG.info("Original List: %s. Filtered List: %s", len(result), len(filtered_result))

        return filtered_result

    def is_detection_modified(self, case, detection):
        """[Make an ExtraHop API call to determine if the detection was modified. Only a small number of
            ExtraHop detection fields will trigger this check]

        Args:
            case ([dict]): [Case object]
            detection ([dict]): [Detection object]

        Returns:
            [bool]: [True if the incident fields modified]
        """
        det_copy = detection.copy()
        # Convert None values to string 'None' for the detection to allow
        # comparison of None values
        for k in det_copy:
            if k in UPDATEABLE_FIELDS and det_copy[k] is None:
                det_copy[k] = str(det_copy[k])

        modified_fields = {k: det_copy[k] for k in UPDATEABLE_FIELDS if k in det_copy and det_copy[k] != case["properties"]["extrahop_"+k]}

        if modified_fields:
            LOG.info("Detection ID %s, modified properties: %s.", detection["id"], modified_fields)

        return bool(modified_fields)

def set_params(fn_inputs, params=None, f_prefix=None, split_index=None):
    """[Setup params dict form fn_input named tuple].
    Make any necessary transformation for api call.

    Args:
        fn_inputs [namedtuple]: Function inputs
        params [dict]: Function parameters dict for 3rd party api
        f_prefix [string]: Function parameter prefix
        split_index [integer]: Index to split prefix

    Returns:
        [dict]: 3rd party api parameters dict.
    """
    params = params if params else {}
    index = split_index if split_index else 1
    f_prefix = f_prefix if f_prefix else F_PREFIX

    # Convert f_inputs named tuple to a dict and filter for prefix value
    f_inputs_as_dict = {k: v for k, v in fn_inputs._asdict().items() if k.startswith(f_prefix)}

    for k, v in f_inputs_as_dict.items():
        # Strip off prefix from input parameter value before adding to params.
        params.update({k.split('_', index)[index]: v})

    return params
