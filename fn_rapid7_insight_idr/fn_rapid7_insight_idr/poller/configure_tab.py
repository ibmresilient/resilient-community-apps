# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging

from fn_rapid7_insight_idr.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Rapid7 InsightIDR"

class Rapid7InsightIDRTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "8e757b59-a53f-439a-9b13-69941bf052d1"

    CONTAINS = [
        Field("rapid7_insight_idr_link"),
        Field("rapid7_insight_idr_rrn"),
        Field("rapid7_insight_idr_status"),
        Field("rapid7_insight_idr_disposition"),
        Field("rapid7_insight_idr_source"),
        Field("rapid7_insight_idr_responsibility"),
        Field("rapid7_insight_idr_assignee"),
        Field("rapid7_insight_idr_assignee_email"),
        Datatable("rapid7_insight_idr_alerts_dt")
    ]
    SHOW_IF = [
        Field("rapid7_insight_idr_rrn").conditions.has_value()
    ]


# Continue if exception is thrown
def init_rapid7_insight_idr_tab():
    try:
        create_tab(Rapid7InsightIDRTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)