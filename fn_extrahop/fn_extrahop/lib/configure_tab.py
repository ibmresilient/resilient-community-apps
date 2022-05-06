# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Helper module  for ExtraHop incident tab setup"""

import logging
from resilient_lib.ui.elements import UIElementBase
from resilient_lib.ui import Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser
from fn_extrahop.lib.app_common import PACKAGE_NAME

LOG = logging.getLogger(__name__)

TAB_NAME = "ExtraHop"

class Header(UIElementBase):
    """ Class to create a Header in an incident tab.
    """
    ELEMENT_TYPE = "header"
    def as_dto(self):
        return {
            "element": self.ELEMENT_TYPE,
            "content": self.api_name
        }

class ExtraHopTab(Tab):
    """ Class to add an ExtraHop incident tab with Headers, properties and data tables.
    """
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME

    UUID = "67eac993-042c-446a-9981-22bf30768a63"
    CONTAINS = [
        Header("ExtraHop Properties"),
        Field("extrahop_detection_id"),
        Field("extrahop_detection_link"),
        Field("extrahop_site_name"),
        Field("extrahop_site_uuid"),
        Field("extrahop_risk_score"),
        Field("extrahop_update_time"),
        Field("extrahop_end_time"),
        Field("extrahop_status"),
        Field("extrahop_ticket_id"),
        Field("extrahop_assignee"),
        Field("extrahop_detection_updated"),
        Header("ExtraHop Details"),
        Datatable("extrahop_detections"),
        Datatable("extrahop_devices"),
        Datatable("extrahop_watchlist"),
        Datatable("extrahop_tags"),
        Datatable("extrahop_activitymaps"),
    ]

    SHOW_IF = [
        Field("extrahop_detection_id").conditions.has_value()
    ]

def init_extrahop_tab():
    """Setup an ExtraHop incident tab"""
    try:
        create_tab(ExtraHopTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as sys_ex:
        # Continue if exception is thrown
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, sys_ex)
