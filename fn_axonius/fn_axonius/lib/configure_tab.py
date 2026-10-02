# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging

from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_axonius"
TAB_NAME = "Axonius"

class AxoniusTab(Tab):
    SECTION = PACKAGE_NAME
    NAME = TAB_NAME
    UUID = "dc45fd78-17c9-45ff-8580-97300ab0a602"

    CONTAINS = [
        Datatable("axonius_devices_dt")
    ]

# Continue if exception is thrown
def init_axonius_tab():
    try:
        create_tab(AxoniusTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab created: %s", TAB_NAME)
    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", TAB_NAME, e)