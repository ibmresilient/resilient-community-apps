# -*- coding: utf-8 -*-#
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
from fn_outbound_email.lib.smtp_mailer import CONFIG_DATA_SECTION
from resilient_lib.ui import View, Datatable, Tab, Field, create_tab
from resilient_circuits.app import AppArgumentParser
import logging

LOG = logging.getLogger(__name__)

TAB_NAME = "Email"

class EmailTab(Tab):

    NAME = "email"
    SECTION = CONFIG_DATA_SECTION
    UUID = "c9e6ef5a-4dd1-4fa3-a7a9-19e2c5ccda36"
    CONTAINS = [
        Datatable("email_conversations"),
        Field("email_message_id"),
        View("email:inbox:incident")
    ]

def init_email_tab():
    """Setup an ExtraHop incident tab"""
    try:
        create_tab(EmailTab, AppArgumentParser().parse_args(), update_existing=True)
        LOG.info("Tab updated: %s", TAB_NAME)
    except SystemExit as sys_ex:
        # Continue if exception is thrown
        LOG.warning("Failed to update tab: %s.\nERROR: %s", TAB_NAME, sys_ex)
