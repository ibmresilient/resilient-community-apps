# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""AppFunction implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult, app_function)
from resilient_lib import validate_fields, RequestsCommonWithoutSession
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from fn_qradar_enhanced_data.util.function_utils import (clear_table, get_qradar_client, get_search_timeout, get_server_settings)
from fn_qradar_enhanced_data.util.qradar_constants import (GLOBAL_SETTINGS, PACKAGE_NAME)
from fn_qradar_enhanced_data.util.qradar_utils import AuthInfo

FN_NAME = "qradar_get_offense_mitre_reference"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'qradar_get_offense_mitre_reference'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.rc = RequestsCommonWithoutSession(opts, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the MITRE Tactics and Techniques in relation to the rules that were fired to cause the offense in QRadar.
        Inputs:
            -   fn_inputs.qradar_label
            -   fn_inputs.qradar_offense_id
            -   fn_inputs.soar_table_name
            -   fn_inputs.soar_incident_id
        """
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # Validate required parameters
            validate_fields(["qradar_offense_id"], fn_inputs)

            # Log inputs
            self.LOG.info(str(fn_inputs))

            # Get global settings from the app.config
            global_settings = self.opts.get(GLOBAL_SETTINGS, {})
            # Get configuration for QRadar server specified
            options = get_server_settings(self.opts, getattr(fn_inputs, "qradar_label", None))
            # Create connection to QRadar server
            qradar_client = get_qradar_client(self.opts, options)
            # Get authorization info for connected QRadar server
            auth_info = AuthInfo.get_authInfo()
            # API url
            api_url = auth_info.api_url
            # Get search_timeout from app.config or set it to default 600 seconds
            timeout = get_search_timeout(global_settings, options)
            # Get api call header
            header = auth_info.headers.copy()

            # Get rules associated with given QRadar offense
            rules_list = qradar_client.graphql_query({"id": fn_inputs.qradar_offense_id}, qradar_graphql_queries.GRAPHQL_RULESQUERY)["content"]["rules"]
            # Make list of rule IDs into a string
            ids_list_str = ', '.join([rule.get("id") for rule in rules_list])
            # Perform GET request to QRadar server to get the UUID for the rule ID's from the ids_list_str
            # Create a dictionary that contains the rules ID and UUID
            rule_uuid = auth_info.make_call("GET",
                f"{api_url}analytics/rules?fields=id, identifier&filter=id in ({ids_list_str})",
                headers=header, timeout=timeout).json()

            # Get the mappings for all of the rules associated with the QRadar case
            for rule in rules_list:

                # Add identifier/uuid to its corresponding rule
                for uuid in rule_uuid:
                    if str(uuid.get("id")) == rule.get("id"):
                        rules_list[rules_list.index(rule)]["identifier"] = uuid.get("identifier")
                        rule_uuid.remove(uuid) # Removes the uuid from the rule_uuid list after its added to rules_list
                        break # Exits the loop after a match is found

                try:
                    # Perform api call to the Use Case Manager app on the QRadar server to get the MITRE mappings
                    # for the current rule using the rules UUID
                    mitre_results = self.rc.execute("get", f"{api_url[0:len(api_url)-4]}console/plugins/app_proxy:UseCaseManager_Service/api/mappings/by_name?rule_id={rule.get('identifier')}",
                        verify=auth_info.cafile,
                        headers=header,
                        timeout=timeout).json()

                    # Check if mappings are returned and not an empty dictionary
                    if mitre_results:
                        # Add the mapping to its corresponding rule
                        rules_list[rules_list.index(rule)]["mapping"] = mitre_results[rule['name']]['mapping']
                except Exception as er:
                    # If the api call to Use Case Manager errors than Log error and continue
                    self.LOG.error(str(er))

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            if rules_list:
                # Clear specified data table in SOAR based on app.config settings
                clear_table(self.rest_client(), getattr(fn_inputs, "soar_table_name", None), getattr(fn_inputs, "soar_incident_id", None), global_settings)

            yield FunctionResult({'rules': rules_list})
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
