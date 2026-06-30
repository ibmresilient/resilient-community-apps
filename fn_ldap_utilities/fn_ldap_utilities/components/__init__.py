# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from logging import getLogger
from fn_ldap_utilities.util.helper import PACKAGE_NAME
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = getLogger(__name__)

class IncidentGroupsTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = "LDAP Results"
    UUID = '16ec9aa7-599f-44cc-97a2-cfe259d22bfd'

    CONTAINS = [
        Field("ldap_base_dn"),
        Field("ldap_domain_name"),
        Datatable("ldap_query_results")
    ]

    SHOW_IF = [
        Field("ldap_domain_name").conditions.has_value()
    ]

# Continue if exception is thrown
def init_incident_groups_tab():
    try:
        create_tab(IncidentGroupsTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", IncidentGroupsTab.NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", IncidentGroupsTab.NAME, e)
