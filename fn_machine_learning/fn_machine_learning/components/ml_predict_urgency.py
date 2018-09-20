# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_machine_learning.lib.resilient_utils as resilient_utils
from fn_machine_learning.lib.ml_model_common import MlModelCommon


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ml_predict_urgency"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_machine_learning", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_machine_learning", {})

    @function("ml_predict_urgency")
    def _ml_predict_urgency_function(self, event, *args, **kwargs):
        """
        This function takes an input of incident id. It will
            1. Retrieve the corresponding incident from Resilient server
            2. Read the active machine model
            3. Use the model to make a prediction for this incident.
        :param event:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            # Get the function parameters:
            ml_incident_id = kwargs.get("ml_incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("ml_incident_id: %s", ml_incident_id)


            yield StatusMessage("starting...")
            inc = self.rest_client().get("/incidents/{}".format(str(ml_incident_id)))
            log.debug("Incident {id}: {dic}".format(id=str(ml_incident_id),
                                                    dic=inc))

            active_model = self.opts["machine_learning_predict"].get("active_model", None)
            if active_model:
                model = MlModelCommon.load_from_file(active_model)
            else:
                raise ValueError("active_model not defined in app.config")

            mapping = resilient_utils.get_field_def(self.rest_client(),
                                                    model.prediction,
                                                    "incident")
            prediction = ""
            if model:
                prediction = model.predict_map(inc, mapping)
            else:
                raise Exception("Failed to load model file: {}".format(active_model))

            yield StatusMessage("done...")

            results = {
                "prediction": prediction
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()