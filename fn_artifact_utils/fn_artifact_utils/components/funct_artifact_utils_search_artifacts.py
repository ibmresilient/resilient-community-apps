# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.2.4321

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_artifact_utils"
FN_NAME = "artifact_utils_search_artifacts"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'artifact_utils_search_artifacts'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Utilities function for Artifacts allowing the searching of incident artifacts based on Type, Value, Description, Tags, and more. This function also allows for advanced filter creation too for more advanced users.
        Inputs:
            -   fn_inputs.artifact_include_incident_count
            -   fn_inputs.artifact_type_method
            -   fn_inputs.artifact_tag_method
            -   fn_inputs.artifact_tag_values
            -   fn_inputs.artifact_value
            -   fn_inputs.artifact_has_attachments
            -   fn_inputs.artifact_type_values
            -   fn_inputs.incident_id
            -   fn_inputs.artifact_description_value
            -   fn_inputs.artifact_value_method
            -   fn_inputs.artifact_has_hits
            -   fn_inputs.artifact_advance_filter
            -   fn_inputs.artifact_description_method
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        
        # Example getting access to self.get_fn_msg()
        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)
        validate_fields(["artifact_include_incident_count", "incident_id"], fn_inputs)

        # Example accessing optional attribute in fn_inputs and initializing it to None if it does not exist (this is similar for app_configs)
        # optional_input =  getattr(fn_inputs, "optional_input", None)
        artifact_type_values =  getattr(fn_inputs, "artifact_type_values", None)
        self.LOG.debug("artifact_type_values: %s", artifact_type_values)
        artifact_type_method =  getattr(fn_inputs, "artifact_type_method", None)
        self.LOG.debug("artifact_type_method: %s", artifact_type_method)
        artifact_value =  getattr(fn_inputs, "artifact_value", None)
        self.LOG.debug("artifact_value: %s", artifact_value)
        artifact_value_method =  getattr(fn_inputs, "artifact_value_method", None)
        self.LOG.debug("artifact_value_method: %s", artifact_value_method)
        artifact_description_value =  getattr(fn_inputs, "artifact_description_value", None)
        self.LOG.debug("artifact_description_value: %s", artifact_description_value)
        artifact_description_method =  getattr(fn_inputs, "artifact_description_method", None)
        self.LOG.debug("artifact_description_method: %s", artifact_description_method)
        artifact_tag_values =  getattr(fn_inputs, "artifact_tag_values", None)
        self.LOG.debug("artifact_tag_values: %s", artifact_tag_values)
        artifact_tag_method =  getattr(fn_inputs, "artifact_tag_method", None)
        self.LOG.debug("artifact_tag_method: %s", artifact_tag_method)
        artifact_has_attachments =  getattr(fn_inputs, "artifact_has_attachments", None)
        self.LOG.debug("artifact_has_attachments: %s", artifact_has_attachments)
        artifact_has_hits =  getattr(fn_inputs, "artifact_has_hits", None)
        self.LOG.debug("artifact_has_hits: %s", artifact_has_hits)
        artifact_advance_filter =  getattr(fn_inputs, "artifact_advance_filter", None)
        self.LOG.debug("artifact_advance_filter: %s", artifact_advance_filter)

        # Example interacting with REST API
        res_client = self.rest_client()
        #function_details = res_client.get(f"/functions/{FN_NAME}?handle_format=names")

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################
        """
        Required Functions
        """
        def verify_entries(uri, item_value, entity_type):
            """Function used to verify that the user provided values exist within the platform providing back their IDs"""
            # Grab available Items from SOAR Instance.
            soar_items = res_client.get(uri)
            
            # Create a list of available Items and a dictionary of their IDs.
            items_available = []
            items_dict = {}
            for item in soar_items['entities']:
                items_available.append(item['name'])
                items_dict[item['name']] = item['id']
                            
            item_type_list = []
            for item in item_value.split(','):
                if item in items_available:
                    item_type_list.append(items_dict[item])
                else:
                    raise IntegrationError("No {} found: {}".format(entity_type, item))
            
            # Return Verified Item List.
            return(item_type_list)
        
        
        """
        Check Artifact and Tag types.
        """
        if artifact_type_values:
            artifact_type_list = verify_entries('/artifact_types?handle_format=names', artifact_type_values, 'artifact')
            self.LOG.info("Artifact Type IDs: %s", artifact_type_list)
        
        if artifact_tag_values:
            artifact_tag_list = verify_entries('/tags/data?handle_format=names&exclude_unused=false', artifact_tag_values, 'Tag')
            self.LOG.info("Artifact Tag IDs: %s", artifact_tag_list)
        
        
        """
        Build the Filter.
        """
        if artifact_advance_filter:
            artifact_filter = artifact_advance_filter
            self.LOG.info("Advanced Filter Option Used: %s", artifact_filter)
        else:
            conditions = []
            
            # Filter for Artifacts with hits.
            if artifact_has_hits == 'has_a_value':
                conditions.append({"field_name": "hits", "method": "has_a_value", "value": [1]})
            elif artifact_has_hits == 'not_has_a_value':
                conditions.append({"field_name": "hits", "method": "not_has_a_value", "value": [0]})
            
            # Filter for Artifacts with attachments.
            if artifact_has_attachments == "has_a_value":
                conditions.append({"field_name": "attachment", "method": "has_a_value", "value": [1]})
            elif artifact_has_attachments == "not_has_a_value":
                conditions.append({"field_name": "attachment", "method": "not_has_a_value", "value": [0]})
            
            # Filter for Artifact Values.
            if artifact_value_method:
                conditions.append({"field_name": "value", "method": artifact_value_method, "value": artifact_value})
           
            # Filter for Artifact Descriptions.
            if artifact_description_method == 'contains' or artifact_description_method == 'not_contains':
                conditions.append({"field_name": "description", "method": artifact_description_method, "value": artifact_description_value})
            elif artifact_description_method == 'not_has_a_value' or artifact_description_method == 'has_a_value':
                conditions.append({"field_name": "description", "method": artifact_description_method})
            
            # Filter for Artifact Types.
            if artifact_type_method:
                conditions.append({"field_name": "type", "method": artifact_type_method, "value": artifact_type_list})
            
            # Filter for Artifact Tags.
            if artifact_tag_method:
                conditions.append({"field_name": "global_info.tags", "method": artifact_tag_method, "value": artifact_tag_list})
            
            # Combine Conditions.
            artifact_filter = { "filters" : [{"conditions" : conditions } ] }
            self.LOG.info("Automated Filter Option Used: %s", artifact_filter)
        
        
        """
        Perform query.
        """
        if fn_inputs.artifact_include_incident_count:
            queried_artifacts = res_client.post('/incidents/{}/artifacts/query_paged?handle_format=names&include_related_incident_count=true'.format(fn_inputs.incident_id), artifact_filter)
        else:
            queried_artifacts = res_client.post('/incidents/{}/artifacts/query_paged?handle_format=names&include_related_incident_count=false'.format(fn_inputs.incident_id), artifact_filter)
        ##############################################

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        results = queried_artifacts

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
