# -*- coding: utf-8 -*-#
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
from resilient_lib.ui import Datatable, Tab, create_tab, Field
from resilient_circuits.app import AppArgumentParser
from logging import getLogger

LOG = getLogger(__name__)

TAB_NAME = "Azure Automation"

class AzureAutomationTab(Tab):
    SECTION = "fn_azure_automation_utilities"
    NAME = TAB_NAME
    UUID = "f7ea99b0-76e2-45d7-ae35-e95dff66661f"

    CONTAINS = [
        Datatable("azure_automation_accounts"),
        Datatable("azure_automation_runbooks"),
        Datatable("azure_automation_credentials"),
        Datatable("azure_automation_schedules"),
        Datatable("azure_automation_statistics")
    ]
    SHOW_IF = [
        Field("azure_automation_create_ui_tab").conditions.equals(True)
    ]

# Continues if exception is thrown
def init_azureautomation_tab():
    try:
        create_tab(AzureAutomationTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info(f"Tab created: {TAB_NAME}")
    except SystemExit as e:
        LOG.warning(f"Failed to create tab: {TAB_NAME}.\nERROR: {e}")
