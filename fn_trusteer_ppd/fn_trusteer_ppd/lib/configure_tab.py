# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import logging

from fn_trusteer_ppd.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Trusteer"

class TrusteerPPDTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "66239367-306f-4a36-a530-1a34dfcebf3e"

    CONTAINS = [
        Field("trusteer_ppd_activity"),
        Field("trusteer_ppd_application_id"),
        Field("trusteer_event_received_at"),
        Field("trusteer_ppd_is_targeted"),
        Field("trusteer_ppd_global_device_id"),
        Field("trusteer_ppd_new_device_indication"),
        Field("trusteer_ppd_puid"),
        Field("trusteer_ppd_reason"),
        Field("trusteer_ppd_reason_id"),
        Field("trusteer_ppd_recommendation"),
        Field("trusteer_ppd_risk_score"),
        Field("trusteer_ppd_session_id"),        
        Field("trusteer_ppd_link_to_alert")
    ]
    SHOW_IF = [
        Field("trusteer_puid").conditions.has_value()
    ]


# Continue if exception is thrown
def init_trusteer_ppd_tab():
    try:
        create_tab(TrusteerPPDTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)