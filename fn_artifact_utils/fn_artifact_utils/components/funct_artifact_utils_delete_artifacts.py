# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.2.4321

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_artifact_utils"
FN_NAME = "artifact_utils_delete_artifacts"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'artifact_utils_delete_artifacts'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function used to delete Artifacts from an Incident and clean up the Global table if needed.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.artifact_id_list
            -   fn_inputs.artifact_remove_globally
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)
        validate_fields(["incident_id", "artifact_id_list", "artifact_remove_globally"], fn_inputs)

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
        Deleting Artifact
        """
        for artifact_id in fn_inputs.artifact_id_list.split(','):
            global_artifact = res_client.get('/incidents/{}/artifacts/{}?handle_format=names'.format(fn_inputs.incident_id, artifact_id))['global_artifact'][0]
            self.LOG.debug("Global Artifact Info: %s", global_artifact)
            self.LOG.info("Deleting Incident Artifact: %s", artifact_id)
            incident_artifact_deletion = res_client.delete('/incidents/{}/artifacts/{}'.format(fn_inputs.incident_id, artifact_id))
            self.LOG.debug("Incident Artifact Deleted: %s", incident_artifact_deletion)
            results = {"incident_artifact_deletion": incident_artifact_deletion}
            if global_artifact['related_incident_count'] == 1 and fn_inputs.artifact_remove_globally:
                self.LOG.info("Deleting Global Artifact: %s", global_artifact['id'])
                global_artifact_deletion = res_client.delete('/artifacts/{}'.format(global_artifact['id']))
                self.LOG.debug("Global Artifact Deleted: %s", global_artifact_deletion)
                results['global_artifact_deletion'] = global_artifact_deletion
        ##############################################

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        # results = {"mock_key": "Mock Value!"}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
