# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from json import loads
from logging import getLogger
from time import time
from resilient_circuits import (FunctionResult, ResilientComponent,
                                StatusMessage, function, handler)
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_service_now.util.resilient_helper import CONFIG_DATA_SECTION, ResilientHelper
from fn_service_now.util.sn_records_dt import ServiceNowRecordsDataTable

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_snow_create_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        # Get host as needed to create link to incident/task
        self.host = opts.get("host")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_snow_create_record")
    def _fn_snow_create_record_function(self, event, *args, **kwargs):
        """Function: Function that uses the '/create' custom endpoint in ServiceNow to create a ServiceNow record from an IBM SOAR Incident or Task"""
        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["incident_id"], kwargs)

        # Get the function inputs:
        payload = {
            "inputs": {
                "incident_id": kwargs.get("incident_id", None), # number (required)
                "task_id": kwargs.get("task_id", None), # number (optional)
                "sn_table_name": kwargs.get("sn_table_name", None) or res_helper.table_name, # text (optional)
                "sn_init_work_note": kwargs.get("sn_init_work_note", None), # text (optional)
                "sn_parent_ref_id": kwargs.get("sn_parent_ref_id", None) # text (optional)
            },
            "sn_table_name": kwargs.get("sn_table_name", None) or res_helper.table_name # text (optional)
        }

        # Convert 'sn_optional_fields' JSON string to Dictionary
        try:
            if kwargs.get("sn_optional_fields", None):
                # text, JSON String (optional)
                payload["inputs"]["sn_optional_fields"] = loads(kwargs.get("sn_optional_fields", None), object_hook=res_helper._byteify)
            else:
                payload["inputs"]["sn_optional_fields"] = None
        except Exception:
            raise ValueError("sn_optional_fields JSON String is invalid")

        yield StatusMessage("Function Inputs OK")

        # Instantiate new SOAR API object
        res_client = self.rest_client()

        # Instantiate a reference to the ServiceNow Datatable
        datatable = ServiceNowRecordsDataTable(res_client, payload.get("inputs", {}).get("incident_id", None))

        # Generate the res_link
        payload["res_link"] = res_helper.generate_res_link(payload.get("inputs", {}).get("incident_id", None), self.host, res_client.org_id, payload.get("inputs", {}).get("task_id", None))

        try:
            # Generate the request_data
            req = res_helper.generate_sn_request_data(
                res_client=res_client,
                res_datatable=datatable,
                incident_id=payload.get("inputs", {}).get("incident_id", None),
                res_link=payload.get("res_link", None),
                sn_table_name=payload.get("inputs", {}).get("sn_table_name", None),
                task_id=payload.get("inputs", {}).get("task_id", None),
                init_note=payload.get("inputs", {}).get("sn_init_work_note", None),
                sn_optional_fields=payload.get("inputs", {}).get("sn_optional_fields", None),
                add_soar_link=kwargs.get("sn_add_soar_link_on_snow", None) # To add a link to the SOAR incident to the SNOW incident note.
            )

            # If we fail to generate the request_data (because the ServiceNow record already exists)
            # raise an Action Status message and set success to False
            if not req.get("success"):
                err_msg = req.get("data")
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            request_data = req.get("data")

            obj_type = "Incident" if request_data.get("type") == "res_incident" else "Task"
            obj_name = request_data.get("incident_name", None) or request_data.get("task_name", None)
            yield StatusMessage(f"Creating a new ServiceNow Record for {obj_type}: {obj_name}")

            # Call POST and get response
            create_in_sn_response = res_helper.sn_api_request("POST", "/create", data=request_data)

            if not create_in_sn_response:
                raise IntegrationError("Failed to create record in ServiceNow. The response from ServiceNow was empty")

            # Add values to payload
            payload["res_id"] = create_in_sn_response.get("res_id", None)
            payload["sn_ref_id"] = create_in_sn_response.get("sn_ref_id", None)
            payload["sn_sys_id"] = create_in_sn_response.get("sn_sys_id", None)
            payload["sn_record_state"] = create_in_sn_response.get("sn_state", None)
            payload["sn_record_link"] = res_helper.generate_sn_link(f"number={payload.get('sn_ref_id', None)}", payload.get("sn_table_name", None))
            # Get current time (*1000 as API does not accept int)
            payload["sn_time_created"] = int(time() * 1000)

            # get datatable name if short_description was included
            # else set to the incident/task names
            rename_name = payload.get("inputs", {}).get("sn_optional_fields", {}).get("short_description", None) or obj_name

            # adjust the name to reflect the name that will appear in the datatable and on ServiceNow
            if request_data.get("type") == "res_incident":
                res_helper.rename_incident(res_client, request_data.get("incident_id", None), rename_name)
            else:
                res_helper.rename_task(res_client, request_data.get("task_id", None), rename_name)

            yield StatusMessage(f"New ServiceNow Record created {payload.get('sn_ref_id', None)}")

            try:
                yield StatusMessage("Adding a new row to the ServiceNow Records Data Table")

                # Add row to the datatable
                add_row_response = datatable.add_row(
                    payload.get("sn_time_created", None),
                    rename_name,
                    "Incident" if request_data.get("type") == "res_incident" else "Task",
                    payload.get("res_id", None),
                    payload.get("sn_ref_id", None),
                    res_helper.convert_text_to_richtext("Active"),
                    res_helper.convert_text_to_richtext("Sent to ServiceNow"),
                    payload.get("sn_table_name", None),
                    f'<a href="{payload.get("res_link", None)}">SOAR</a> &nbsp;&nbsp; <a href="{payload.get("sn_record_link", None)}">SN</a>',
                    parent_ref_id=payload.get("inputs", {}).get("sn_parent_ref_id", None)
                )

                payload["row_id"] = add_row_response.get("id", None)

            except Exception as err:
                raise ValueError(f"Failed to add row to datatable {err}")

            rp_results = rp.done(True, payload)
            # add in all results for backward-compatibility
            rp_results.update(payload)

            log.debug("RESULTS: %s", rp_results)
            log.info("Complete")

            # Produce a FunctionResult with the rp_results
            yield FunctionResult(rp_results)
        except Exception as error:
            yield FunctionResult({}, success=False, reason=error)
