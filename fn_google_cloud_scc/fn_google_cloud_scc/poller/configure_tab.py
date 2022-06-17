# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from resilient_lib.ui import Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser
from fn_google_cloud_scc.util.scc_common import PACKAGE_NAME

import logging

LOG = logging.getLogger(__name__)

TAB_NAME = "Google SCC"
UUID_VAL = "b383ff73-1e09-4f81-a035-df1ccb3b0d04"

class GoogleSCCTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME

    UUID = UUID_VAL
    CONTAINS = [
        Field("google_scc_id"),
        Field("google_scc_name"),
        Field("google_scc_type"),
        Field("google_scc_resource_display_name"),
        Field("google_scc_project_display_name"),
        Field("google_scc_recommendation"),
        Field("google_scc_url"),
        Field("google_scc_remediation_link"),
        Field("google_scc_class"),
        Field("google_scc_category"),
        Field("google_scc_security_marks"),
        Field("google_scc_compliance_standards"),
        Field("google_scc_vulnerability"),
        Field("description"),
        Field("severity_code"),
        Field("google_scc_state")
    ]

    SHOW_IF = [
        Field("google_scc_id").conditions.has_value()
    ]

# Continue if exception is thrown
def init_scc_tab():
    try:
        create_tab(GoogleSCCTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)
