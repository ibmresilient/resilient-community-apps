# -*- coding: utf-8 -*-#
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
from resilient_lib.ui import Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser
from logging import getLogger

LOG = getLogger(__name__)

class SNOWTab(Tab):
    SECTION = "fn_service_now"
    NAME = "Service Now"

    UUID = "2209daaa-cfa7-4adc-89bf-d933c9e46094"
    CONTAINS = [
        Field("sn_snow_record_id"),
        Field("sn_snow_record_link"),
        Datatable("sn_records_dt")
    ]

    SHOW_IF = [
        Field("sn_snow_record_id").conditions.has_value()
    ]

# Continues if exception is thrown
try:
    create_tab(SNOWTab, AppArgumentParser().parse_args(), update_existing=True)
except SystemExit as e:
    LOG.warning(f"Failed trying to create_tab.\nERROR: {e}")
