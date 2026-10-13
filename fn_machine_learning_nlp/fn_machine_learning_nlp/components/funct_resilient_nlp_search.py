# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-u
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_machine_learning_nlp.lib import util_functions
from fn_machine_learning_nlp.lib.res_utils import ResUtils
from fn_machine_learning_nlp.lib.file_manage import FileManage
import os
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'resilient_nlp_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_machine_learning_nlp", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_machine_learning_nlp", {})

    @function("resilient_nlp_search")
    def _resilient_nlp_search_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            search_incident_id = kwargs.get("search_incident_id")  # number
            nlp_search_string = kwargs.get("nlp_search_string")  # text
            number_incidents = kwargs.get("number_incidents")  # number

            log = logging.getLogger(__name__)
            log.info("search_incident_id: %s", search_incident_id)
            log.info("nlp_search_string: %s", nlp_search_string)
            log.info("number_incidents: %s", number_incidents)

            # Figure out where the saved model is
            model_path = self.options.get("model_path", None)
            if model_path is None:
                log.error("No model_path specified in app.config")
                raise Exception("Need model_path in app.config")

            # Check that the requested number of incidents is less than or equal to the number of incidents in the model
            vec_file = ""
            model_files = os.listdir(model_path)

            for file in model_files:
                # the vec file will always end with -vec.json even if the user inputs a custom name for the model
                if "-vec.json" in file:
                    vec_file = file
                    break

            # Check if sentence vector file exists
            if not vec_file:
                log.error("Model vector JSON file is not found")
                raise Exception("Model vector JSON file is not found. Need to have a built model")

            vec_path = os.path.join(model_path, vec_file)
            data = json.load(open(vec_path, 'r'))

            # Check that the number of top similar incidents being requested does not exceed the number of incidents
            # in the model
            if number_incidents > len(data):
                log.error("The number of similar incidents requested exceeds the number of incidents in the model. There are only {} incidents in the model.".format(
                                len(data)))
                raise Exception("There are only {} incidents in the model. Number of similar incidents to be found should be fewer".format(len(data)))

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            res_client = self.rest_client()
            res_utils = ResUtils(resclient=res_client,
                                 in_log=log)
            nlp_str = nlp_search_string
            if nlp_str is None or len(nlp_str) == 0:
                nlp_str = res_utils.get_inc_art_des(search_incident_id)

            inc_hrefs = util_functions.get_incident_href(nlp_str=nlp_str,
                                                         res_client=res_client,
                                                         num_return=number_incidents,
                                                         model_path=model_path,
                                                         inc_id=search_incident_id)

            cur_time = util_functions.get_cur_time()

            yield StatusMessage("done...")

            results = {
                "incidents": inc_hrefs,
                "time": cur_time
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(e)
            log.error("Failed to find similar incidents, function exception.")
            yield FunctionError()