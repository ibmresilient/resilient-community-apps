# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging

from fn_pagerduty.components.pd_common import (PACKAGE_NAME)
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Pagerduty"


class PagerDuty(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "17b826ac-12ef-4d61-a26f-dbcadff7eada"

    CONTAINS = [
        Field("pd_incident_id"),
        Field("pd_incident_url"),
    ]
    SHOW_IF = [
        Field("pd_incident_id").conditions.has_value()
    ]


# Continue if exception is thrown
def init_pagerduty_tab():
    try:
        create_tab(SalesforceTab, AppArgumentParser(
        ).parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)
