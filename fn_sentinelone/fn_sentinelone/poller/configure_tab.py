# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import logging

from fn_sentinelone.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "SentinelOne"

class SentinelOneTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "f7ea99b0-76e2-45d7-ae35-e95dff66661f"

    CONTAINS = [
        Field("sentinelone_threat_overview_url"),
        Field("sentinelone_agent_id"),
        Field("sentinelone_threat_analyst_verdict"),
        Field("sentinelone_incident_status"),
        Field("sentinelone_classification"),
        Field("sentinelone_confidence_level"),
        Field("sentinelone_mitigation_status"),
        Field("sentinelone_mitigation_status_description"),
        Field("sentinelone_threat_id"),
        Field("sentinelone_threat_name"),
        Datatable("sentinelone_agents_dt")
    ]
    SHOW_IF = [
        Field("sentinelone_threat_id").conditions.has_value()
    ]


# Continue if exception is thrown
def init_sentinelone_tab():
    try:
        create_tab(SentinelOneTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)