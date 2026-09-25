# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from logging import getLogger
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Field, Tab, create_tab

LOG = getLogger(__name__)

class PagerDutyTab(Tab):
    SECTION = "fn_pagerduty"
    NAME = "PagerDuty Incident"
    UUID = "9bd6eb82-84a9-47bd-9619-9ddef7a22b53"

    CONTAINS = [
        Field("pd_incident_id"),
        Field("pd_incident_key"),
        Field("pd_incident_url"),
        Field("pd_incident_status"),
        Field("pd_incident_priority"),
        Field("ps_incident_service_name"),
        Field("pd_incident_service_id"),
        Field("pd_incident_escalation_policy_name"),
        Field("pd_incident_escalation_policy_id")
    ]

    SHOW_IF = [
        Field("pd_incident_id").conditions.has_value()
    ]

# Continue if exception is thrown
def init_PagerDuty_tab():
    try:
        create_tab(PagerDutyTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", PagerDutyTab.NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", PagerDutyTab.NAME, e)
