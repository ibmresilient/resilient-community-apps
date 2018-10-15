# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os.path
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_machine_learning.lib.resilient_utils as resilient_utils
from fn_machine_learning.lib.ml_model_common import MlModelCommon

APP_CONFIG_SECTION = "machine_learning_predict"
MODEL_DIR_KEY = "model_dir"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ml_predict"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_machine_learning", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_machine_learning", {})

    @function("ml_predict")
    def _ml_predict_function(self, event, *args, **kwargs):
        """
        This function takes input of incident id and saved model name. It will
            1. Retrieve the corresponding incident from Resilient server
            2. Read the saved model
            3. Use the model to make a prediction for this incident.
        :param event:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            # Get the function parameters:
            ml_incident_id = kwargs.get("ml_incident_id")  # number
            ml_model_file = kwargs.get("ml_model_file")  # text

            log = logging.getLogger(__name__)
            log.info("ml_incident_id: %s", ml_incident_id)
            log.info("ml_model_file: %s", ml_model_file)

            yield StatusMessage("starting...")
            inc = self.rest_client().get("/incidents/{}".format(str(ml_incident_id)))
            log.debug("Incident {id}: {dic}".format(id=str(ml_incident_id),
                                                    dic=inc))
            #
            # Read model folder from app.config
            #
            model_folder = self.opts[APP_CONFIG_SECTION].get(MODEL_DIR_KEY, None)
            selected_model = os.path.join(model_folder, ml_model_file)

            if selected_model:
                model = MlModelCommon.load_from_file(selected_model)
            else:
                raise ValueError("active_model not defined in app.config")

            mapping = resilient_utils.get_field_def(self.rest_client(),
                                                    model.config.predict_field,
                                                    "incident")
            prediction = ""
            if model:
                prediction = model.predict_map(inc, mapping)
            else:
                raise Exception("Failed to load model file: {}".format(selected_model))

            results = {
                "prediction": prediction
            }
            log.info("Result: {}".format(results))

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()