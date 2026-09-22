# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import readable_datetime
from fn_ocm.util.helper import ocm_client, PACKAGE_NAME

FN_NAME = "on_call_manager_query_incidents"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'on_call_manager_query_incidents'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Create client connection
        self.client = ocm_client(self.options.get("ocm_url", None), self.options.get("ocm_api_key_name", None), self.options.get("ocm_api_key_pass", None), self.rc)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Query incidents for a given period of time based on properties of the incident or properties of the events correlated to the incidents. By default, incidents created in the last 7 days will be retrieved and filtered. A start time and end time can be provided to define the time range, but the range is limited to a 30 day period. The query also has a limit of 500 incidents being returned for any query.
        Incidents can be requested by incident properties, like incident priority and incident state. You can also set 1 or more event filters that set conditions on events that must be correlated to an incident for it to be included in the query results. You can filter only on incident properties, only on properties of the correlated events, or a combination of the two.
        Inputs:
            -   fn_inputs.ocm_starttime
            -   fn_inputs.ocm_event_filter_4
            -   fn_inputs.ocm_event_filter_5
            -   fn_inputs.ocm_event_combiner
            -   fn_inputs.ocm_event_filter_3
            -   fn_inputs.ocm_event_filter_2
            -   fn_inputs.ocm_endtime
            -   fn_inputs.ocm_incident_filter
            -   fn_inputs.ocm_event_filter_1
        """
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            # Make API call to Query incidents
            results = self.client.query_incidents(
                starttime=readable_datetime(fn_inputs.ocm_starttime, "%Y-%m-%dT%H:%M:%S.%fZ") if getattr(fn_inputs, "ocm_starttime", None) else None,
                endtime=readable_datetime(fn_inputs.ocm_endtime, "%Y-%m-%dT%H:%M:%S.%fZ") if getattr(fn_inputs, "ocm_endtime", None) else None,
                incident_filter=fn_inputs.ocm_incident_filter if getattr(fn_inputs, "ocm_incident_filter", None) else None,
                event_combiner=fn_inputs.ocm_event_combiner if getattr(fn_inputs, "ocm_event_combiner", None) else None,
                event_filter_1=fn_inputs.ocm_event_filter_1 if getattr(fn_inputs, "ocm_event_filter_1", None) else None,
                event_filter_2=fn_inputs.ocm_event_filter_2 if getattr(fn_inputs, "ocm_event_filter_2", None) else None,
                event_filter_3=fn_inputs.ocm_event_filter_3 if getattr(fn_inputs, "ocm_event_filter_3", None) else None,
                event_filter_4=fn_inputs.ocm_event_filter_4 if getattr(fn_inputs, "ocm_event_filter_4", None) else None,
                event_filter_5=fn_inputs.ocm_event_filter_5 if getattr(fn_inputs, "ocm_event_filter_5", None) else None
            )
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            if isinstance(results, dict) and (results.get("level", None) == 'error' or results.get("error", None)):
                yield FunctionResult({}, success=False, reason=str(results))
            else:
                yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err.value)
