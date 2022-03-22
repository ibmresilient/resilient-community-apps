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

        response = self.rx_cli.search_detections(active_from=timestamp, search_filter=search_filter)

        result = response.json()

        if response.status_code not in [200, 201, 204]:
            LOG.error("{{package_name}} API call failed: %s", result)
            return None

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
