# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# # Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, build_resilient_url, build_incident_url
from fn_ocm.util.helper import ocm_client, PACKAGE_NAME
from ast import literal_eval

FN_NAME = "on_call_manager_create_event"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'on_call_manager_create_event'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Create client connection
        self.client = ocm_client(self.options.get("ocm_url", None), self.options.get("ocm_api_key_name", None), self.options.get("ocm_api_key_pass", None), self.rc)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create an event
        Inputs:
            -   fn_inputs.ocm_soar_inc_id
            -   fn_inputs.ocm_type_eventtype
            -   fn_inputs.ocm_type_statusorthreshold
            -   fn_inputs.ocm_resource_sourceid
            -   fn_inputs.ocm_resource_displayname
            -   fn_inputs.ocm_resource_location
            -   fn_inputs.ocm_resource_hostname
            -   fn_inputs.ocm_resource_port
            -   fn_inputs.ocm_resource_service
            -   fn_inputs.ocm_resource_application
            -   fn_inputs.ocm_resource_cluster
            -   fn_inputs.ocm_resource_ipaddress
            -   fn_inputs.ocm_resource_name
            -   fn_inputs.ocm_event_severity
            -   fn_inputs.ocm_resource_accessscope
            -   fn_inputs.ocm_resource_component
            -   fn_inputs.ocm_resource_controller
            -   fn_inputs.ocm_resource_correlationkey
            -   fn_inputs.ocm_resource_interface
            -   fn_inputs.ocm_resource_type
            -   fn_inputs.ocm_event_summary
            -   fn_inputs.ocm_deduplicationkey
            -   fn_inputs.ocm_event_priority
            -   fn_inputs.ocm_event_expirytime
            -   fn_inputs.ocm_event_resolution
            -   fn_inputs.ocm_event_details
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        try:
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            # Validate required fields
            validate_fields(["ocm_resource_name", "ocm_event_summary", "ocm_event_severity", "ocm_soar_inc_id"], fn_inputs)
            if not getattr(fn_inputs, "ocm_type_statusorthreshold", None) and not getattr(fn_inputs, "ocm_type_eventtype", None):
                raise ValueError("A value for statusOrThreshold and or eventType is required")
            # Check if the details parameter is given
            details = fn_inputs.ocm_event_details if getattr(fn_inputs, "ocm_event_details", None) else None
            if details and "{" in details and "}" in details: # Check if {} are in the string and then convert it to a dictionary
                details = literal_eval(details)

            results = self.client.create_event(
                soar_inc_link=build_incident_url(build_resilient_url(self.opts.get("host", None), self.opts.get("port", 443)), fn_inputs.ocm_soar_inc_id, self.opts.get("org", None)),
                ocm_resource_name=getattr(fn_inputs, "ocm_resource_name", None),
                summary=getattr(fn_inputs, "ocm_event_summary", None),
                severity=getattr(fn_inputs, "ocm_event_severity", None),
                statusOrThreshold=getattr(fn_inputs, "ocm_type_statusorthreshold", None),
                eventType=getattr(fn_inputs, "ocm_type_eventtype", None),
                resource_accessScope=getattr(fn_inputs, "ocm_resource_accessscope", None),
                resource_application=getattr(fn_inputs, "ocm_resource_application", None),
                resource_cluster=getattr(fn_inputs, "ocm_resource_cluster", None),
                resource_component=getattr(fn_inputs, "ocm_resource_component", None),
                resource_controller=getattr(fn_inputs, "ocm_resource_controller", None),
                resource_correlationKey=getattr(fn_inputs, "ocm_resource_correlationkey", None),
                resource_displayName=getattr(fn_inputs, "ocm_resource_displayname", None),
                resource_hostname=getattr(fn_inputs, "ocm_resource_hostname", None),
                resource_ipaddress=getattr(fn_inputs, "ocm_resource_ipaddress", None),
                resource_interface=getattr(fn_inputs, "ocm_resource_interface", None),
                resource_location=getattr(fn_inputs, "ocm_resource_location", None),
                resource_port=getattr(fn_inputs, "ocm_resource_port", None),
                resource_service=getattr(fn_inputs, "ocm_resource_service", None),
                resource_sourceId=getattr(fn_inputs, "ocm_resource_sourceid", None),
                resource_type=getattr(fn_inputs, "ocm_resource_type", None),
                priority=int(fn_inputs.ocm_event_priority) if getattr(fn_inputs, "ocm_event_priority", None) else None,
                deduplicationkey=getattr(fn_inputs, "ocm_deduplicationkey", None),
                details=details,
                resolution=getattr(fn_inputs, "ocm_event_resolution", False),
                expiryTime=getattr(fn_inputs, "ocm_event_expirytime", None)
            )

            if isinstance(results, dict) and (results.get("level", None) == 'error' or results.get("error", None)):
                yield FunctionResult({}, success=False, reason=str(results))
            else:
                yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err.value)
