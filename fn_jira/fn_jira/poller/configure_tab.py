# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from logging import getLogger
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab
from fn_jira.util.helper import PACKAGE_NAME, DEFAULT_JIRA_DT_NAME

LOG = getLogger(__name__)

class IncidentGroupsTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = "Jira Incident"
    UUID = "6f8c7b82-348d-4e3d-8416-a234301347d6"

    CONTAINS = [
        Field("jira_internal_url"),
        Field("jira_issue_id"),
        Field("jira_project_key"),
        Field("jira_server"),
        Field("jira_ticket_url"),
        Field("jira_issue_status"),
        Datatable(DEFAULT_JIRA_DT_NAME)
    ]

    SHOW_IF = [
        Field("jira_issue_id").conditions.has_value()
    ]

# Continue if exception is thrown
def init_incident_groups_tab():
    try:
        create_tab(IncidentGroupsTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", IncidentGroupsTab.NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", IncidentGroupsTab.NAME, e)
