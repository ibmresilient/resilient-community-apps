# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging

from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_wiz"
TAB_NAME = "Wiz"

class WizTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "2f9aeb7e-2756-43fa-a1cf-c8f68049d9ae"

    CONTAINS = [
        Field("wiz_issue_id"),
        Field("wiz_issue_type"),
        Field("wiz_issue_status"),
        Field("wiz_description"),
        Datatable("wiz_vulnerabilities_table"),
        Datatable("wiz_projects_table"),
    ]

# Continue if exception is thrown
def init_wiz_tab():
    try:
        create_tab(WizTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)