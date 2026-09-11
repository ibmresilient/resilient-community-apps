from packaging.version import Version
from resilient.app_config import AppConfigManager
from resilient_circuits import AppFunctionComponent

from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.model_helper import ModelHelper
from fn_watsonx_analyst.util.util import get_soar_version
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
AI_FIELDS_SOAR_VERSION = "51.0.11.0"

log = create_logger(__name__)

class WatsonxAppFunction(AppFunctionComponent):
    @staticmethod
    def ai_fields_present():
        # return True
        return Version(get_soar_version(app_state.get().res_client)) >= Version(AI_FIELDS_SOAR_VERSION)

    def __init__(self, opts):
        if isinstance(opts, AppConfigManager):
            opts = opts.data

        super(WatsonxAppFunction, self).__init__(opts, PACKAGE_NAME)

    def setup(self, fn_inputs: dict, purpose: AiResponsePurpose, fn_name: str):
        generate_request_id()

        app_state.get().reset()
        app_state.get().opts = self.opts

        app_state.get().res_client = self.rest_client()
        app_state.get().purpose = purpose
        app_state.get().set_model(
            getattr(fn_inputs, "fn_watsonx_analyst_model_id", ModelHelper.get_default_model().get("name")))

        return self.status_message(f"Starting App Function: '{fn_name}'")
