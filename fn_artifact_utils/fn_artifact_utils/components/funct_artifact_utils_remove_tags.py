# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.2.4321

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_artifact_utils"
FN_NAME = "artifact_utils_remove_tags"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'artifact_utils_remove_tags'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function used to remove one or more Tags from one or more Artifacts in an incident at the global level.
        Inputs:
            -   fn_inputs.artifact_tag_values
            -   fn_inputs.incident_id
            -   fn_inputs.artifact_id_list
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)
        validate_fields(["artifact_id_list", "incident_id", "artifact_tag_values"], fn_inputs)

        # Example accessing optional attribute in fn_inputs and initializing it to None if it does not exist (this is similar for app_configs)
        # optional_input =  getattr(fn_inputs, "optional_input", None)

        # Example getting access to self.get_fn_msg()
        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        res_client = self.rest_client()
        # function_details = res_client.get(f"/functions/{FN_NAME}?handle_format=names")

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################
        """
        Remove Tag from Artifact
        """
        updated_artifacts = {}        
        for artifact_id in fn_inputs.artifact_id_list.split(','):
            global_artifact = res_client.get('/incidents/{}/artifacts/{}?handle_format=names'.format(fn_inputs.incident_id, artifact_id))['global_artifact'][0]
            self.LOG.debug("Global Artifact Info: %s", global_artifact)
            for tag in fn_inputs.artifact_tag_values.split(','):
                for global_tag in global_artifact['tags']:
                    if global_tag['tag_handle'] == tag:
                        self.LOG.info("Tag Found and Removed: %s", tag)
                        global_artifact['tags'].remove(global_tag)
            self.LOG.debug("Updated Artifact: %s", global_artifact)
            updated_artifact = res_client.put('/artifacts/{}'.format(global_artifact['id']), global_artifact)
            updated_artifacts[global_artifact['id']] = updated_artifact
        ##############################################

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        results = updated_artifacts

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
