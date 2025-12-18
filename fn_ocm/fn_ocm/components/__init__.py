# -*- coding: utf-8 -*-#
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
from resilient_lib.ui import Datatable, Tab, Field, create_tab, HTMLBlock
from resilient_circuits.app import AppArgumentParser
from logging import getLogger

LOG = getLogger(__name__)

class ocmTab(Tab):
    SECTION = "fn_ocm"
    NAME = "On Call Manager"

    UUID = "4b9b68b3-1e28-4b46-8528-80475fcee99b"
    CONTAINS = [
        HTMLBlock("<body>The below fields will be populated by running playbooks 'On Call Manager: Create Event' or 'On Call Manager: Get Incident'</body><br><br>"),
        Field("ocm_incident_summary"),
        Field("ocm_incident_id"),
        Field("ocm_incident_display_id"),
        Field("ocm_incident_description"),
        Field("ocm_incident_last_changed_time"),
        Field("ocm_incident_priority"),
        Field("ocm_incident_state"),
        Field("ocm_incident_assigned_owner"),
        Field("ocm_incident_assigned_team"),
        HTMLBlock("<body>Group and Team are the same thing on OCM. In the API it is called a team, but on the OCM UI it is called a Group.</body><br>"),
        Datatable("on_call_manager_incidents")
    ]

    SHOW_IF = [
        Field("ocm_tab_visible").conditions.equals(True)
    ]

# Continues if exception is thrown
try:
    create_tab(ocmTab, AppArgumentParser().parse_args(), update_existing=True)
except SystemExit as e:
    LOG.warning(f"Failed trying to create_tab On Call Manager.\nERROR: {e}")
