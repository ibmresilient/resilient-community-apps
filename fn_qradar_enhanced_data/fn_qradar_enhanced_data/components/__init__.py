# -*- coding: utf-8 -*-#
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
from resilient_lib.ui import Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser
import logging

LOG = logging.getLogger(__name__)

class QRadarTab(Tab):
    SECTION = "fn_qradar_integration"
    NAME = "QRadar Offense Details"

    UUID = "d1ca8936-897b-4a83-8225-01c58db0470b"
    CONTAINS = [
        Field("qradar_id"),
        Field("qradar_destination"),
        Field("qr_offense_index_type"),
        Field("qr_offense_index_value"),
        Field("qr_offense_source"),
        Field("qr_source_ip_count"),
        Field("qr_destination_ip_count"),
        Field("qr_event_count"),
        Field("qr_flow_count"),
        Field("qr_assigned"),
        Field("qr_magnitude"),
        Field("qr_credibility"),
        Field("qr_relevance"),
        Field("qr_severity"),
        Datatable("qr_offense_top_events"),
        Datatable("qr_flows"),
        Datatable("qr_triggered_rules"),
        Datatable("qr_top_destination_ips"),
        Datatable("qr_top_source_ips"),
        Datatable("qr_categories"),
        Datatable("qr_assets")
    ]

    SHOW_IF = [
        Field("qradar_id").conditions.has_value()
    ]

# Continues if exception is thrown
try:
    create_tab(QRadarTab, AppArgumentParser().parse_args(), update_existing=True)
except SystemExit as e:
    LOG.warning("Failed trying to create_tab.\nERROR: %s", e)
