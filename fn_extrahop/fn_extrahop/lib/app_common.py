# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Poller support functionality for interaction with the 3rd party endpoints"""

import logging
from urllib.parse import urljoin
from fn_extrahop.lib.rx_client import RxClient

LOG = logging.getLogger(__name__)

# URL fragment to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "/extrahop/#/detections/detail/{}"

# List of fields to check to determine if an update is required.
UPDATEABLE_FIELDS = [
    "update_time", "end_time", "risk_score",
    "status", "ticket_id", "assignee"
]
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
        self.rx_cli = RxClient(opts, options)

    def get_entities_since_ts(self, timestamp, search_filter):
        """Get changed entities since last poller run

        Args:
            timestamp (datetime): datetime when the last poller ran

        Returns:
            list: changed entity list
        """
        categories = None

        if search_filter:
            search_filter_api = search_filter.copy()
            # Category filters are managed after the api call is made
            if "category" in search_filter:
                categories = search_filter_api .pop("category")

        response = self.rx_cli.search_detections(search_filter=search_filter_api)

        result = response.json()

        if response.status_code not in [200, 201, 204]:
            LOG.error("{{package_name}} API call failed: %s", result)
            return None

        if categories:
            result = self.filter_by_property(result, "categories", categories)

        return result

    def make_linkback_url(self, entity_id, linkback_url=LINKBACK_URL):
        """Create a url to link back to the endpoint alert, case, etc.

        Args:
            template (str): portion of url to join with base url
            entity_id (str/int): id representing the alert, case, etc.

        Returns:
            str: completed url for linkback
        """
        return urljoin(self.endpoint_url, linkback_url.format(entity_id))

    def filter_by_property(self, result, property, filters):
        """Filter result based on a a property list .
           Used for filters not fully supported inb api or don't support a property lists

        Args:
            property (string): Property to filer by.
            filters (list): List of values to filter by.
            result (dict): Result returned from ExtraHop

        Returns:
            filtered_result: Result filtered by risk score threshold
        """
        filtered_result = [r for r in result if any(i in r[property] for i in filters)]
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

        modified_fields = {k: detection[k] for k in UPDATEABLE_FIELDS if k in detection and detection[k] != case["properties"]["extrahop_"+k]}

        if modified_fields:
            LOG.info("Detection ID %s, modified properties: %s. Filtered List: %s", detection["id"], modified_fields)

        return True if modified_fields else False
