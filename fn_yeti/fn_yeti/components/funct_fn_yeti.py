# -*- coding: utf-8 -*-

"""AppFunction implementation"""
import logging
import traceback

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
import pyeti


PACKAGE_NAME = "fn_yeti"
FN_NAME = "fn_yeti"

LOG = logging.getLogger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_yeti'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: This function makes an API call to Yeti to look for information on the given artifact.
        Inputs:
            -   fn_inputs.yeti_artifact_type
            -   fn_inputs.yeti_artifact_value
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        LOG.info("Querying YETI")

        self.yeti_client = pyeti.YetiApi(self.app_configs.url, (self.app_configs.username,
                                        self.app_configs.password), self.app_configs.apikey)

        artifact_type = fn_inputs.yeti_artifact_type
        artifact_value = fn_inputs.yeti_artifact_value

        validate_fields([
            {"name": "url", "placeholder": "<yeti_instance_url>"},
            {"name": "username"},
            {"name": "apikey", "placeholder" : "<apikey_value>"}],
            self.app_configs)

        LOG.info("Looking up {}: {}".format(artifact_type, artifact_value))

        try:
            # init new indicators object
            indicators = self.yeti_client.observable_search(regex=False,
                                                            value=artifact_value)
            LOG.debug(indicators)
        except ValueError as e:
            LOG.error(traceback.format_exc())
            raise e

        if not indicators or len(indicators) < 1:
            yield FunctionResult({}, success=False, reason="No indicators recieved from Yeti")


        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(indicators)
