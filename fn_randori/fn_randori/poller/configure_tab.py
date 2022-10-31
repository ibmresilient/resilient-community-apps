# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging

from fn_randori.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Randori"

class RandoriTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "f7ea99b0-76e2-45d7-ae35-e95dff66661f"

    CONTAINS = [
        Field("randori_target_id"),
        Field("randori_target_status"),
        Field("randori_target_link"),
        Field("randori_target_temptation"),
        Field("randori_target_authority"),
        Field("randori_target_perspective_name"),
        Field("randori_target_affiliation_state"),
        Field("randori_target_impact_score"),
        Field("randori_target_tech_category"),
        Field("randori_target_tags"),
        Datatable("randori_detections_dt")
    ]
    SHOW_IF = [
        Field("randori_target_id").conditions.has_value()
    ]


# Continue if exception is thrown
def init_randori_tab():
    try:
        create_tab(RandoriTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)