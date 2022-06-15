# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging

from bs4 import BeautifulSoup
from fn_service_now.util.resilient_helper import (CONFIG_DATA_SECTION,
                                                  ResilientHelper)
from fn_service_now.util.sn_records_dt import ServiceNowRecordsDataTable
from resilient_circuits import (FunctionError, FunctionResult,
                                ResilientComponent, StatusMessage, function,
                                handler)
from resilient_lib import RequestsCommon, ResultPayload


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.res_id = None
        self.sn_ref_id = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_snow_add_note_to_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("fn_snow_add_note_to_record")
    def _fn_snow_add_note_to_record_function(self, event, *args, **kwargs):
        """Function: Function that adds a Note to a ServiceNow Record. Option to add the note as a 'Work Note' or 'Additional Comment'."""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(CONFIG_DATA_SECTION)

            # Get the function inputs:
            inputs = {
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True),  # number
                "sn_note_text": res_helper.get_function_input(kwargs, "sn_note_text"),  # text (required)
                "sn_note_type": res_helper.get_function_input(kwargs, "sn_note_type")["name"]  # select, text (required)
            }

            # Convert rich text comment to plain text
            soup = BeautifulSoup(inputs["sn_note_text"], 'html.parser')
            soup = soup.get_text()
            inputs["sn_note_text"] = soup.replace(u'\xa0', u' ')

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the datatable
            datatable = ServiceNowRecordsDataTable(res_client, payload.inputs["incident_id"])

            # Generate res_id using incident and task id
            res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Get the sn_ref_id
            sn_ref_id = datatable.get_sn_ref_id(res_id)

            if not sn_ref_id:
                payload.success = False
                err_msg = "Failed to add Note. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

                if payload.inputs["task_id"]:
                    err_msg = err_msg.format("Task", payload.inputs["task_id"])

                else:
                    err_msg = err_msg.format("Incident", payload.inputs["incident_id"])

                raise ValueError(err_msg)

            else:
                # Generate the request_data
                request_data = {
                    "sn_ref_id": sn_ref_id,
                    "sn_table_name": res_helper.get_table_name(sn_ref_id),
                    "type": "comment",
                    "sn_note_text": payload.inputs["sn_note_text"],
                    "sn_note_type": payload.inputs["sn_note_type"]
                }

                yield StatusMessage("Adding Note to ServiceNow Record {0}".format(sn_ref_id))

                # Call POST and get response
                add_in_sn_response = res_helper.sn_api_request(rc, "POST", "/add", data=json.dumps(request_data))
                payload.res_id = res_id
                payload.sn_ref_id = add_in_sn_response["sn_ref_id"]

            results = payload.as_dict()
            rp_results = rp.done(results.get("success"), results)
            rp_results.update(results) # add in all results for backward-compatibility

            log.debug("RESULTS: %s", rp_results)
            log.info("Complete")

            # Produce a FunctionResult with the rp_results
            yield FunctionResult(rp_results)
        except Exception:
            yield FunctionError()
