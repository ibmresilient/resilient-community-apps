# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging

from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Tab, create_tab

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_teams"
TAB_NAME = "MS Teams Approval"

class MSTeamsTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "c8a84bcb-fd24-4788-8d8c-3c81f474cb95"

    CONTAINS = [
        Datatable("msteams_approval_process")
    ]

# Continue if exception is thrown
def init_msteams_tab():
    try:
        create_tab(MSTeamsTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)
