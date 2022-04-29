# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging
import time

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
        self.sn_ref_id = None         # Local (to its table) unique id of ServiceNow record
        self.sn_time_updated = None   # Timestamp from Resilient Integration server when record was updated

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_snow_update_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("fn_snow_update_record")
    def _fn_snow_update_record_function(self, event, *args, **kwargs):
        """Function: Function that uses the '/update' custom endpoint in ServiceNow to update a ServiceNow Record with a given dictionary of field name/value pairs."""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(CONFIG_DATA_SECTION)

            # Get the function inputs:
            inputs = {
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True),  # number (optional)
                "sn_res_id": res_helper.get_function_input(kwargs, "sn_res_id", True),  # text (optional)
                "sn_update_fields": res_helper.get_function_input(kwargs, "sn_update_fields")  # text, JSON String (required)
            }

            # Convert 'sn_update_fields' JSON string to Dictionary
            try:
                inputs["sn_update_fields"] = json.loads(inputs.get("sn_update_fields"), object_hook=res_helper._byteify)
            except Exception:
                raise ValueError("sn_update_fields JSON String is invalid: {0}".format(inputs.get("sn_update_fields")))

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            sn_ref_id = payload.inputs.get("sn_ref_id")

            if sn_ref_id is None:

                # Generate res_id using incident and task id
                res_id = res_helper.generate_res_id(payload.inputs.get("incident_id"), payload.inputs.get("task_id"))

                # Instansiate a reference to the ServiceNow Datatable
                datatable = ServiceNowRecordsDataTable(res_client, payload.inputs.get("incident_id"))

                # Get the sn_ref_id
                sn_ref_id = datatable.get_sn_ref_id(res_id)

                if sn_ref_id is None:
                    payload.success = False
                    err_msg = "Failed to update a ServiceNow Record. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

                    if payload.inputs["task_id"]:
                        err_msg = err_msg.format("Task", payload.inputs.get("task_id"))

                    else:
                        err_msg = err_msg.format("Incident", payload.inputs.get("incident_id"))

                    raise ValueError(err_msg)

            yield StatusMessage("Updating ServiceNow Record {0}".format(sn_ref_id))

            # Get sn_update_fields
            sn_update_fields = payload.inputs.get("sn_update_fields")

            # Initialize list for request_data
            fields = []

            # Loop fields and format for request
            for field_name in sn_update_fields:
                field_value = sn_update_fields[field_name]
                fields.append({"name": field_name, "value": sn_update_fields[field_name]})
                yield StatusMessage("Updating {0} to {1}".format(field_name, field_value))

            request_data = {
                "sn_ref_id": sn_ref_id,
                "sn_table_name": res_helper.get_table_name(sn_ref_id),
                "sn_update_fields": fields
            }

            # Call PATCH and get response
            update_response = res_helper.sn_api_request(rc, "PATCH", "/update", data=json.dumps(request_data))
            payload.sn_ref_id = update_response.get("sn_ref_id")
            payload.sn_time_updated = int(time.time() * 1000)  # Get current time (*1000 as API does not accept int)

            results = payload.as_dict()
            rp_results = rp.done(results.get("success"), results)
            rp_results.update(results) # add in all results for backward-compatibility

            log.debug("RESULTS: %s", rp_results)
            log.info("Complete")

            # Produce a FunctionResult with the rp_results
            yield FunctionResult(rp_results)
        except Exception:
            yield FunctionError()
