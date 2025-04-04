# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging

from fn_vmware_cbc.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Carbon Black Cloud"

class VMwareCBCTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "933422f1-6de1-4ece-88e4-e28a14ec6efb"

    CONTAINS = [
        Field("vmware_cbc_alert_id"),
        Field("vmware_cbc_alert_link"),
        Field("vmware_cbc_alert_type"),
        Field("vmware_cbc_alert_reason_code"),
        Field("vmware_cbc_threat_id"),
        Field("vmware_cbc_workflow_status"),
        Field("vmware_cbc_workflow_closure_reason"),
        Field("vmware_cbc_determination_value"),
        Field("vmware_cbc_tags"),
        Field("vmware_cbc_attack_tactic"),
        Datatable("vmware_cbc_device_dt"),
        Datatable("vmware_cbc_processes_dt"),
        Datatable("vmware_cbc_observations_dt")
    ]
    SHOW_IF = [
        Field("vmware_cbc_alert_id").conditions.has_value()
    ]


# Continue if exception is thrown
def init_vmware_cbc_tab():
    try:
        create_tab(VMwareCBCTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)