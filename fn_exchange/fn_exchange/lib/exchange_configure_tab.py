# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging

from fn_exchange.lib.exchange_helper import PACKAGE_NAME
from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Tab, create_tab

LOG = logging.getLogger(__name__)

TAB_NAME = "Exchange On-Premise"

class ExchangeTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "f9d3a35b-93b2-4fac-a881-b2fe4bbe1785"

    CONTAINS = [
        Datatable("exchange_email_information_dt"),
        Datatable("exchange_dt_meeting_information")
    ]


# Continue if exception is thrown
def init_exchange_tab():
    try:
        create_tab(ExchangeTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)
