# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging

from fn_salesforce.lib.app_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Salesforce"

class SalesforceTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "17b826ac-12ef-4d61-a26f-dbcadff7eada"

    CONTAINS = [
        Field("salesforce_case_number"),
        Field("salesforce_case_id"),
        Field("salesforce_status"),
        Field("salesforce_case_type"),
        Field("salesforce_reason"),
        Field("salesforce_case_link"),
        Field("salesforce_account_name"),
        Field("salesforce_case_owner"),
        Field("salesforce_origin"),
        Field("salesforce_contact_name"),
        Field("salesforce_contact_phone"),
        Field("salesforce_contact_email"),
        Field("salesforce_contact_fax"),
        Field("salesforce_supplied_name"),
        Field("salesforce_supplied_email"),
        Field("salesforce_supplied_phone"),
        Field("salesforce_supplied_company"),
        Field("salesforce_account_id"),
        Field("salesforce_owner_id"),
        Field("salesforce_contact_id"),
    ]
    SHOW_IF = [
        Field("salesforce_case_id").conditions.has_value()
    ]


# Continue if exception is thrown
def init_salesforce_tab():
    try:
        create_tab(SalesforceTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)