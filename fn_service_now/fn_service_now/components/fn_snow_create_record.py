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
        self.reason = None
        self.inputs = inputs
        self.row_id = None            # The row_id of the row created in Datatable
        self.res_id = None            # RES-<incId>-<taskId>
        self.res_link = None          # Link to res incident/task
        self.sn_ref_id = None         # Local (to its table) unique id of ServiceNow record
        self.sn_sys_id = None         # Global unique id of ServiceNow record
        self.sn_record_state = None   # Current state of the Record in ServiceNow
        self.sn_record_link = None    # Link to ServiceNow record
        self.sn_time_created = None   # Timestamp from Resilient Integration server when record was created

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_snow_create_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

        # Get host as needed to create link to incident/task
        self.host = opts.get("host")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("fn_snow_create_record")
    def _fn_snow_create_record_function(self, event, *args, **kwargs):
        """Function: Function that uses the '/create' custom endpoint in ServiceNow to create a ServiceNow record from an IBM Resilient Incident or Task"""

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
                "sn_init_work_note": res_helper.get_function_input(kwargs, "sn_init_work_note", True),  # text (optional)
                "sn_optional_fields": res_helper.get_function_input(kwargs, "sn_optional_fields", True)  # text, JSON String (optional)
            }

            # Convert 'sn_optional_fields' JSON string to Dictionary
            try:
                inputs["sn_optional_fields"] = json.loads(inputs["sn_optional_fields"], object_hook=res_helper._byteify)
            except Exception:
                raise ValueError("sn_optional_fields JSON String is invalid")

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Instansiate a reference to the ServiceNow Datatable
            datatable = ServiceNowRecordsDataTable(res_client, payload.inputs["incident_id"])

            # Generate the res_link
            payload.res_link = res_helper.generate_res_link(payload.inputs["incident_id"], self.host, res_client.org_id, payload.inputs["task_id"])

            # Generate the request_data
            req = res_helper.generate_sn_request_data(
                res_client,
                datatable,
                payload.inputs["incident_id"],
                res_helper.SN_TABLE_NAME,
                payload.res_link,
                payload.inputs["task_id"],
                payload.inputs["sn_init_work_note"],
                payload.inputs["sn_optional_fields"])

            # If we fail to generate the request_data (because the ServiceNow record already exists) 
            # raise an Action Status message and set success to False
            if not req.get("success"):
                err_msg = req.get("data")
                yield StatusMessage(err_msg)
                payload.reason = err_msg
                payload.success = False

            else:
                request_data = req.get("data")

                yield StatusMessage(u"Creating a new ServiceNow Record for the {0}: {1}".format(
                    "Incident" if request_data.get("type") is "res_incident" else "Task", res_helper.str_to_unicode(request_data.get("incident_name")) if request_data.get("incident_name") is not None else res_helper.str_to_unicode(request_data.get("task_name"))))

                # Call POST and get response
                create_in_sn_response = res_helper.sn_api_request(rc, "POST", "/create", data=json.dumps(request_data))

                if create_in_sn_response is not None:

                    # Add values to payload
                    payload.res_id = create_in_sn_response["res_id"]
                    payload.sn_ref_id = create_in_sn_response["sn_ref_id"]
                    payload.sn_sys_id = create_in_sn_response["sn_sys_id"]
                    payload.sn_record_state = create_in_sn_response["sn_state"]
                    payload.sn_record_link = res_helper.generate_sn_link("number={0}".format(payload.sn_ref_id))
                    payload.sn_time_created = int(time.time() * 1000)  # Get current time (*1000 as API does not accept int)


                    # get datatable name if short_description was included
                    # else set to the incident/task name
                    dt_name = payload.inputs["sn_optional_fields"]["short_description"] if payload.inputs.get("sn_optional_fields", {}).get("short_description", None) is not None else request_data.get("incident_name") if request_data.get("incident_name", None) is not None else request_data.get("task_name")

                    # adjust the name to reflect the name that will appear in the datatable and on ServiceNow
                    if request_data.get("type") is "res_incident":
                        res_helper.rename_incident(res_client, request_data.get("incident_id"), dt_name)
                    else:
                        res_helper.rename_task(res_client, request_data.get("task_id"), dt_name)

                    yield StatusMessage("New ServiceNow Record created {0}".format(payload.sn_ref_id))

                    try:
                        yield StatusMessage("Adding a new row to the ServiceNow Records Data Table")

                        # Add row to the datatable
                        add_row_response = datatable.add_row(
                            payload.sn_time_created,
                            dt_name,
                            "Incident" if request_data.get("type") is "res_incident" else "Task",
                            payload.res_id,
                            payload.sn_ref_id,
                            res_helper.convert_text_to_richtext("Active"),
                            res_helper.convert_text_to_richtext("Sent to ServiceNow"),
                            """<a href="{0}">SOAR</a> &nbsp;&nbsp; <a href="{1}">SN</a>""".format(payload.res_link, payload.sn_record_link))

                        payload.row_id = add_row_response["id"]

                    except Exception as err_msg:
                        payload.success = False
                        raise ValueError("Failed to add row to datatable {0}".format(err_msg))

                else:
                    payload.success = False
                    raise ValueError("The response from ServiceNow was empty")

            results = payload.as_dict()
            rp_results = rp.done(results.get("success"), results)
            rp_results.update(results) # add in all results for backward-compatibility

            log.debug("RESULTS: %s", rp_results)
            log.info("Complete")

            # Produce a FunctionResult with the rp_results
            yield FunctionResult(rp_results)
        except Exception:
            yield FunctionError()
