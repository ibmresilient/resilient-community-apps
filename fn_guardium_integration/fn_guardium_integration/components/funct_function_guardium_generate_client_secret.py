# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
import json
from time import time
from re import findall
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_guardium_integration.lib.check_configs import validate_app_configs
from fn_guardium_integration.lib.firewall_auth import firewall_authenticate
from fn_guardium_integration.lib.ssh_service import ParamikoSSH
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.util.static_data import INCIDENT_TYPES, SECRET_STORE_FIELD


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_generate_client_secret"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_integration", {})
        self.opts_data = opts

        # Validate Resilient App.configs
        validate_app_configs(options=self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @function("function_guardium_generate_client_secret")
    def _function_guardium_generate_client_secret_function(self, event, *args, **kwargs):
        """Function: A function to Generate the Guardium  Client Secret if not available with the system."""
        try:

            # Get the function parameters:
            guardium_username = kwargs.get("guardium_username")  # text
            guardium_password = kwargs.get("guardium_password")  # text

            # Get the app.config parameters:
            grd_host_ip = self.options.get("guardium_host")
            proxy_command = self.options.get("proxy_command")

            yield StatusMessage(u"Creating Resilient Incident Types.")

            # Initialize the resilient service and logger
            log = logging.getLogger(__name__)
            rest_service_object = ResilientRestService(self.opts_data, self.options, log)
            for type_name in INCIDENT_TYPES:
                rest_service_object.create_incident_type(type_name)
            # Checking for firewall
            if self.options.get("enable_firewall_auth").lower() == "true":
                yield StatusMessage(u"Process - Authenticating with firewall...")
                firewall_authenticate(bso_ip=self.options.get("bso_ip"), bso_user=self.options.get("bso_user"),
                                      bso_password=self.options.get("bso_password"), log=log)
                yield StatusMessage(u"Process - Firewall Authentication successful.")

            log.info(u"Establish connection to Guardium server: %s via SSH for client secret.", grd_host_ip)

            cli_object = ParamikoSSH(grd_host_ip, guardium_username, guardium_password, sock=proxy_command)

            # Get the client secret from Guardium
            unique_client_id = "client" + str(int(time()))
            response = cli_object.exec_cmd("grdapi register_oauth_client client_id={}".format(unique_client_id))

            if response and len(response) > 1:
                response = json.loads(findall(r"\{.*\}", response)[0])
                client_secret = response.get("client_secret")
            else:
                raise ValueError(u"No response from grdapi register_oauth_client command")

            # Get the Guardium Unit type
            response = cli_object.exec_cmd("show unit type")
            if response.find("Standalone") != -1:
                unit_type = "standalone"
            else:
                unit_type = "central_manager"

            # Updating Resilient rule action field `Remote data source`.
            log.info(u"Updating Managed Unit data to Search report Action")
            grd_rest_object = GrdRestEndpoint(self.options, client_secret, unique_client_id, log)
            res = grd_rest_object.create_online_report("Managed Units", 1000)
            managed_units = []
            for unit_data in res:
                managed_host = unit_data.get("Host Name")
                if managed_host:
                    managed_units.append(managed_host)

            rest_service_object.update_rule_action_filed_values(managed_units)

            # Guardium `client secret` generation completed.
            secret_data = {"secret": client_secret, "unique_id": unique_client_id, "unit_type": unit_type}
            # Creating/Updating client secret to action filed
            res_action = rest_service_object.create_rule_action_select_field(field_name="guardium_system_reference",
                                                                             field_value=[secret_data])
            if res_action:
                msg = u"Creating secret data field in resilient completed."
            else:
                rest_service_object.update_rule_action_filed_values([secret_data], resilient_field=SECRET_STORE_FIELD)
                msg = u"Updating secret data field in resilient completed."
            yield StatusMessage(msg)
            yield StatusMessage(u"generating Guardium `client secret` completed.")

            results = {
                "content": msg
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as er_msg:
            yield FunctionError(er_msg)
