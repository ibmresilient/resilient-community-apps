# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from logging import getLogger
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME

LOG = getLogger(__name__)

class IncidentGroupsTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = "Microsoft Sentinel Incident"
    UUID = "6f8c7b82-348d-4e3d-8416-a234304347d6"

    CONTAINS = [
        Field("sentinel_incident_assigned_to"),
        Field("sentinel_incident_classification"),
        Field("sentinel_incident_classification_comment"),
        Field("sentinel_incident_classification_reason"),
        Field("sentinel_incident_id"),
        Field("sentinel_incident_labels"),
        Field("sentinel_incident_number"),
        Field("sentinel_incident_status"),
        Field("sentinel_incident_tactics"),
        Field("sentinel_incident_url"),
        Field("sentinel_profile"),
        Datatable("sentinel_incident_alerts"),
        Datatable("sentinel_incident_entities")
    ]

    SHOW_IF = [
        Field("sentinel_incident_number").conditions.has_value()
    ]

# Continue if exception is thrown
def init_incident_groups_tab():
    try:
        create_tab(IncidentGroupsTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", IncidentGroupsTab.NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", IncidentGroupsTab.NAME, e)
