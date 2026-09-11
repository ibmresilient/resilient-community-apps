# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_guardium_integration
"""
import logging
import json
from re import findall
from time import time
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.lib.ssh_service import ParamikoSSH
from fn_guardium_integration.lib.check_configs import validate_app_configs
from resilient_lib import validate_fields
from fn_guardium_integration.lib.firewall_auth import firewall_authenticate

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_guardium_integration", {})
    log.debug("Started Resilient-Guardium Package Self-Test.")

    try:
        # Checking App.Config Params
        validate_app_configs(options=options)
        validate_fields(["cli_user", "cli_password"], options)

        # Getting App.config
        guardium_cli_username = options.get("cli_user")
        guardium_cli_password = options.get("cli_password")
        grd_host_ip = options.get('guardium_host')
        proxy_command = options.get('proxy_command')

        # Checking for firewall
        if options.get('enable_firewall_auth').lower() == "true":
            log.debug(u"Process - Authenticating with firewall...")
            firewall_authenticate(bso_ip=options.get('bso_ip'), bso_user=options.get('bso_user'),
                                  bso_password=options.get('bso_password'), log=log)
        # Validating Guardium ssh connection & cli user credentials
        cli_object = ParamikoSSH(grd_host_ip, guardium_cli_username, guardium_cli_password, sock=proxy_command)
        unique_client_id = 'client' + str(int(time()))
        log.debug(u"Generated Guardium Unique ID: %s", unique_client_id)
        response = cli_object.exec_cmd('grdapi register_oauth_client client_id={}'.format(unique_client_id),
                                       print_stdout=False)
        response = json.loads(findall(r"\{.*\}", response)[0])
        client_secret = response['client_secret']
        log.debug(u"Generated Guardium Client secret: %s", client_secret)

        # Validating Rest connection & and trying to generate the access token
        grd_rest_object = GrdRestEndpoint(options, client_secret, unique_client_id, log)
        log.debug(u"Generated Guardium Access token: %s", grd_rest_object.access_token)
        return {"state": "success"}
    except Exception as er:
        log.error(repr(er))
        return {"state": "failure"}
