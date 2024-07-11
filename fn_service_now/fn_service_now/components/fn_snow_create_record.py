# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from json import loads
from logging import getLogger
from time import time

from resilient_circuits import (FunctionResult, ResilientComponent,
                                StatusMessage, function, handler)
from resilient_lib import ResultPayload, validate_fields

from fn_service_now.util.resilient_helper import (CONFIG_DATA_SECTION,
                                                  ResilientHelper)
from fn_service_now.util.sn_records_dt import ServiceNowRecordsDataTable


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.reason = None
        self.inputs = inputs
        self.row_id = None            # The row_id of the row created in Datatable
        self.res_id = None            # RES-<incId>-<taskId>
        self.res_link = None          # Link to res incident/task
        # Local (to its table) unique id of ServiceNow record
        self.sn_ref_id = None
        self.sn_sys_id = None         # Global unique id of ServiceNow record
        self.sn_record_state = None   # Current state of the Record in ServiceNow
        self.sn_record_link = None    # Link to ServiceNow record
        # Timestamp from Resilient Integration server when record was created
        self.sn_time_created = None
        self.sn_table_name = None

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

        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["incident_id"], kwargs)

        # Get the function inputs:
        inputs = {
            # number (required)
            "incident_id": kwargs.get("incident_id"),
            # number (optional)
            "task_id": kwargs.get("task_id"),
            # text (optional)
            "sn_table_name": kwargs.get("sn_table_name"),
            # text (optional)
            "sn_init_work_note": kwargs.get("sn_init_work_note"),
            # text, JSON String (optional)
            "sn_optional_fields": kwargs.get("sn_optional_fields"),
            # text (optional)
            "sn_parent_ref_id": kwargs.get("sn_parent_ref_id")
        }

        # Convert 'sn_optional_fields' JSON string to Dictionary
        try:
            inputs["sn_optional_fields"] = loads(
                inputs["sn_optional_fields"], object_hook=res_helper._byteify)
        except Exception as err:
            raise ValueError("sn_optional_fields JSON String is invalid") from err

        # Create payload dict with inputs
        payload = FunctionPayload(inputs)

        yield StatusMessage("Function Inputs OK")

        # Instantiate new Resilient API object
        res_client = self.rest_client()

        # Instantiate a reference to the ServiceNow Datatable
        datatable = ServiceNowRecordsDataTable(
            res_client, payload.inputs["incident_id"])

        # Generate the res_link
        payload.res_link = res_helper.generate_res_link(
            payload.inputs["incident_id"], self.host, res_client.org_id, payload.inputs["task_id"])

        # Find the table name to send this to either from the inputs or from the app.config setting as a default
        payload.sn_table_name = kwargs.get("sn_table_name") or res_helper.table_name

        # Generate the request_data
        req = res_helper.generate_sn_request_data(
            res_client=res_client,
            res_datatable=datatable,
            incident_id=payload.inputs["incident_id"],
            res_link=payload.res_link,
            sn_table_name=payload.sn_table_name,
            task_id=payload.inputs["task_id"],
            init_note=payload.inputs["sn_init_work_note"],
            sn_optional_fields=payload.inputs["sn_optional_fields"]
        )

        # If we fail to generate the request_data (because the ServiceNow record already exists)
        # raise an Action Status message and set success to False
        if not req.get("success"):
            err_msg = req.get("data")
            yield StatusMessage(err_msg)
            payload.reason = err_msg
            payload.success = False

        else:
            request_data = req.get("data")

            obj_type = "Incident" if request_data.get("type") == "res_incident" else "Task"
            obj_name = request_data.get("incident_name") or request_data.get("task_name")
            yield StatusMessage(f"Creating a new ServiceNow Record for {obj_type}: {obj_name}")

            # Call POST and get response
            create_in_sn_response = res_helper.sn_api_request("POST", "/create", data=request_data)

            if not create_in_sn_response:
                payload.success = False
                raise ValueError("Failed to create record in ServiceNow. The response from ServiceNow was empty")

            # Add values to payload
            payload.res_id = create_in_sn_response["res_id"]
            payload.sn_ref_id = create_in_sn_response["sn_ref_id"]
            payload.sn_sys_id = create_in_sn_response["sn_sys_id"]
            payload.sn_record_state = create_in_sn_response["sn_state"]
            payload.sn_record_link = res_helper.generate_sn_link(
                f"number={payload.sn_ref_id}", payload.sn_table_name)
            # Get current time (*1000 as API does not accept int)
            payload.sn_time_created = int(time() * 1000)

            # get datatable name if short_description was included
            # else set to the incident/task name
            short_desc = payload.inputs.get("sn_optional_fields", {}).get("short_description", None)
            rename_name = short_desc or obj_name

            # adjust the name to reflect the name that will appear in the datatable and on ServiceNow
            if request_data.get("type") == "res_incident":
                res_helper.rename_incident(
                    res_client, request_data.get("incident_id"), rename_name)
            else:
                res_helper.rename_task(
                    res_client, request_data.get("task_id"), rename_name)

            yield StatusMessage(f"New ServiceNow Record created {payload.sn_ref_id}")

            try:
                yield StatusMessage("Adding a new row to the ServiceNow Records Data Table")

                # Add row to the datatable
                add_row_response = datatable.add_row(
                    payload.sn_time_created,
                    rename_name,
                    "Incident" if request_data.get(
                        "type") == "res_incident" else "Task",
                    payload.res_id,
                    payload.sn_ref_id,
                    res_helper.convert_text_to_richtext("Active"),
                    res_helper.convert_text_to_richtext(
                        "Sent to ServiceNow"),
                    payload.sn_table_name,
                    f"""<a href="{payload.res_link}">SOAR</a> &nbsp;&nbsp; <a href="{payload.sn_record_link}">SN</a>""",
                    parent_ref_id=payload.inputs.get("sn_parent_ref_id")
                )

                payload.row_id = add_row_response["id"]

            except Exception as err:
                payload.success = False
                raise ValueError(f"Failed to add row to datatable {err}") from err

        results = payload.as_dict()
        rp_results = rp.done(results.get("success"), results)
        # add in all results for backward-compatibility
        rp_results.update(results)

        log.debug("RESULTS: %s", rp_results)
        log.info("Complete")

        # Produce a FunctionResult with the rp_results
        yield FunctionResult(rp_results)
