# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging

from fn_sumo_logic.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Sumo Logic"

class SumoLogicTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "b8eeefdc-f66d-4028-b56d-48f8f3703e34"

    CONTAINS = [
        Field("sumo_logic_insight_id"),
        Field("sumo_logic_insight_readable_id"),
        Field("sumo_logic_insight_link"),
        Field("sumo_logic_insight_global_confidence"),
        Field("sumo_logic_insight_status"),
        Field("sumo_logic_insight_source"),
        Field("sumo_logic_insight_tags"),
        Field("sumo_logic_insight_resolution"),
        Field("sumo_logic_insight_sub_resolution"),
        Field("sumo_logic_insight_assignee"),
        Datatable("sumo_logic_insight_signals_dt")
    ]
    SHOW_IF = [
        Field("sumo_logic_insight_id").conditions.has_value()
    ]


# Continue if exception is thrown
def init_sumo_logic_tab():
    try:
        create_tab(SumoLogicTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)