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
        riskscore_threshold = None

        if search_filter:
            # Risk score thresholds are managed after the api call is made
            if "riskscore_threshold" in search_filter:
                riskscore_threshold = search_filter.pop('riskscore_threshold')

        response = self.rx_cli.search_detections(update_time=timestamp, search_filter=search_filter)

        result = response.json()

        if response.status_code not in [200, 201, 204]:
            LOG.error("{{package_name}} API call failed: %s", result)
            return None

        if riskscore_threshold:
            result = self.filter_by_riskscore(result, riskscore_threshold)

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

    def filter_by_riskscore(self, result, riskscore_threshold):
        """Create a url to link back to the endpoint alert, case, etc.

        Args:
            result (dict): Result returned from ExtraHop

        Returns:
            filtered_result: Result filtered by risk score threshold
        """
        for i in result:
            rs = i["risk_score"]
        filtered_result = [i for i in result if i["risk_score"] >= riskscore_threshold]

        return filtered_result
