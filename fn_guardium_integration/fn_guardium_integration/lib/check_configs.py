# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from fn_guardium_integration.lib.custom_exceptions import ResilientAppConfigError


def validate_app_configs(options):
    """
    :param options: App Config params
    :return:
    """
    if not options:
        raise ResilientAppConfigError(u"Guardium-Integration App section not set in configuration file. "
                                      u"You must add section by `resilient-circuits config -u`")
    for key, value in options.items():
        if key == "enable_firewall_auth" and value == "true":
            if not options.get("bso_user") or not options.get("bso_password") or not options.get("bso_ip"):
                raise ResilientAppConfigError(u"Firewall authentication credentials params needs to be configured.")
        elif key not in ["bso_user", "bso_password", "bso_ip", "proxy", "proxy_command", "poll_interval",
                         "utc_offset", "cli_user", "cli_password"]:
            if not value:
                raise ResilientAppConfigError(u"app config param: {} to be configured".format(key))
