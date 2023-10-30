# -*- coding: utf-8 -*-#
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
from resilient_lib.ui import Datatable, Tab, create_tab
from resilient_circuits.app import AppArgumentParser
from logging import getLogger

LOG = getLogger(__name__)

class AzureAutomationTab(Tab):
    SECTION = "fn_azure_automation_utilities"
    NAME = "Azure Automation"

    UUID = "d1ca8936-m5jg-sur9-8225-01c58db0470b"
    CONTAINS = [
        Datatable("azure_automation_accounts"),
        Datatable("azure_automation_runbooks"),
        Datatable("azure_automation_credentials"),
        Datatable("azure_automation_schedules"),
        Datatable("azure_automation_statistics")
    ]

# Continues if exception is thrown
try:
    create_tab(AzureAutomationTab, AppArgumentParser().parse_args(), update_existing=True)
except SystemExit as e:
    LOG.warning(f"Failed trying to create_tab.\nERROR: {e}")