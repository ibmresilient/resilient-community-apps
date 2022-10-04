# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging

from fn_darktrace.lib.app_common import (DEVICE_DT_NAME, EVENT_DT_NAME,
                                         MODEL_BREACHES_DT, PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

class IncidentGroupsTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = "Darktrace Incident"
    UUID = "6f8c7b82-348d-4e3d-8416-a234301347d6"

    CONTAINS = [
        Field("darktrace_aianalyst_incident_group_id"),
        Field("darktrace_incident_group_link"),
        Field("severity_code"),
        Field("darktrace_incident_group_acknowledged"),
        Field("darktrace_incident_group_start_time"),
        Field("darktrace_incident_last_modified"),
        Field("darktrace_initiating_device_ids"),
        Field("darktrace_associated_device_ids"),
        Field("darktrace_group_category"),
        Field("darktrace_group_score"),
        Field("darktrace_number_of_events_in_group"),
        Datatable(EVENT_DT_NAME),
        Datatable(DEVICE_DT_NAME),
        Datatable(MODEL_BREACHES_DT)
    ]

    SHOW_IF = [
        Field("darktrace_aianalyst_incident_group_id").conditions.has_value()
    ]

class ModelBreachesTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = "Darktrace Model Breaches"
    UUID = "b3f650f8-07da-462f-9ac9-2f036c0d702d"

    CONTAINS = [
        Field("darktrace_pbid"),
    ]

    SHOW_IF = [
        Field("darktrace_pbid").conditions.has_value()
    ]

# Continue if exception is thrown
def init_incident_groups_tab():
    try:
        create_tab(IncidentGroupsTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", IncidentGroupsTab.NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", IncidentGroupsTab.NAME, e)

# extra UUIDs if needed
# UUID('b27793a5-7a40-407f-a8a6-ab0376875813')
# UUID('f986581c-93e7-4c71-a6fb-a0dd01993ff1')
