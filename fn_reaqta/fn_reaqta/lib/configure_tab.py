# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from resilient_lib.ui import Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser
from fn_reaqta.lib.app_common import PACKAGE_NAME

import logging

LOG = logging.getLogger(__name__)

TAB_NAME = "ReaQta"

class ReaQtaTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME

    UUID = "ac7d7838-5bf9-ec7f-e23a-b5337e661ee1"
    CONTAINS = [
        Field("reaqta_alert_link"),
        Field("reaqta_trigger_condition"),
        Field("reaqta_groups"),
        Field("reaqta_tags"),
        Field("reaqta_machine_info"),
        Field("reaqta_id"),
        Field("reaqta_endpoint_id"),
        Datatable("reaqta_trigger_events"),
        Datatable("reaqta_process_list")
    ]

    SHOW_IF = [
        Field("reaqta_id").conditions.has_value()
    ]

# Continue if exception is thrown
def init_reaqta_tab():
    try:
        create_tab(ReaQtaTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)
