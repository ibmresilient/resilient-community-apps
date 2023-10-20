# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from resilient_lib.ui import Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser


import logging

LOG = logging.getLogger(__name__)

TAB_NAME = "QRadar SIEM"
PACKAGE_NAME =  "fn_qradar_integration"
class QRadarSIEMTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME

    UUID = "781f26c5-1ae2-51c5-1f46-fc27a3fb5466"
    CONTAINS = [
        Field("qradar_id"),
        Datatable("qradar_offense_event"),
        Datatable("qradar_reference_set"),
        Datatable("qradar_reference_table_queried_rows"),
        Datatable("qradar_reference_table")
    ]

    SHOW_IF = [
        Field("qradar_id").conditions.has_value()
    ]

# Continue if exception is thrown
def init_qradar_siem_tab():
    try:
        create_tab(QRadarSIEMTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)
