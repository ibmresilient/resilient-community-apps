# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import logging

from fn_trusteer_ppd.lib.trusteer_ppd_client import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

class TrusteerPPDTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = "Trusteer"
    UUID = "66239367-306f-4a36-a530-1a34dfcebf3e"

    CONTAINS = [
        Field("trusteer_ppd_puid"),
        Field("trusteer_ppd_link_to_puid"),
        Field("trusteer_ppd_application_id"),
        Datatable("trusteer_ppd_dt_trusteer_alerts")
    ]
    SHOW_IF = [
        Field("trusteer_ppd_puid").conditions.has_value()
    ]


# Continue if exception is thrown
def init_trusteer_ppd_tab():
    try:
        create_tab(TrusteerPPDTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TrusteerPPDTab.NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TrusteerPPDTab.NAME, e)