# -*- coding: utf-8 -*-#
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
from resilient_lib.ui import Datatable, Tab, create_tab
from resilient_circuits.app import AppArgumentParser
from logging import getLogger

LOG = getLogger(__name__)

TAB_NAME = "Azure Automation"

class AzureAutomationTab(Tab):
    SECTION = "fn_azure_automation_utilities"
    NAME = TAB_NAME
    UUID = "6hca8936-m5jg-sur9-8225-01c58n60470b"

    CONTAINS = [
        Datatable("azure_automation_accounts"),
        Datatable("azure_automation_runbooks"),
        Datatable("azure_automation_credentials"),
        Datatable("azure_automation_schedules"),
        Datatable("azure_automation_statistics")
    ]

# Continues if exception is thrown
def init_azureautomation_tab():
    try:
        create_tab(AzureAutomationTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning(f"Failed trying to create_tab.\nERROR: {e}")