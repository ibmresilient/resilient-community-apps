# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from iocparser import IOCParser
from fn_ioc_parser_v2.util.helper import *


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'func_ioc_parser_v2"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ioc_parser_v2", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ioc_parser_v2", {})

    @function("func_ioc_parser_v2")
    def _func_ioc_parser_v2_function(self, event, *args, **kwargs):
        """Function: Extract IOCs from Incident/Task Attachments, Text-Based Artifacts and Artifact files."""
        try:

            # Initializing the IOC Parser Helper class
            IOCHelp_obj = IOCParserHelper()

            # Get the function parameters:
            ioc_parser_incident_id = IOCHelp_obj.get_function_input(kwargs, "ioc_parser_v2_incident_id")
            ioc_parser_task_id = IOCHelp_obj.get_function_input(kwargs, "ioc_parser_v2_task_id", optional=True)
            ioc_parser_attachment_id = IOCHelp_obj.get_function_input(kwargs, "ioc_parser_v2_attachment_id", optional=True)
            ioc_parser_artifact_id = IOCHelp_obj.get_function_input(kwargs, "ioc_parser_v2_artifact_id", optional=True)
            ioc_parser_artifact_value = IOCHelp_obj.get_function_input(kwargs, "ioc_parser_v2_artifact_value", optional=True)

            resilient_client = self.rest_client()

            ioc_parser_data = attachment_file_name = None

            yield StatusMessage("Extracting IOCs from given Artifact/attachment data")

            if ioc_parser_artifact_id:

                artifact_metadata_uri = IOCHelp_obj.ARTIFACT_META_DATA_URL.format(ioc_parser_incident_id, ioc_parser_artifact_id)
                artifact_file_data_uri = IOCHelp_obj.ARTIFACT_DATA_URL.format(ioc_parser_incident_id, ioc_parser_artifact_id)
                artifact_metadata = resilient_client.get(artifact_metadata_uri)

                if artifact_metadata.get('attachment'):
                    artifact_file_data = resilient_client.get_content(artifact_file_data_uri)
                    attachment_file_name = artifact_metadata.get('attachment', {}).get('name')
                    ioc_parser_data = IOCParserHelper.extract_text_from_bytes_data(attachment_file_name, artifact_file_data)

                elif ioc_parser_artifact_value:
                    ioc_parser_data = ioc_parser_artifact_value

                else:
                    raise ValueError("Failed to get Artifact Value for Artifact: {0}".format(ioc_parser_artifact_id))

            elif ioc_parser_attachment_id:

                attachment_metadata_uri = attachment_data_uri = None

                if ioc_parser_task_id:
                    attachment_metadata_uri = IOCHelp_obj.TASK_META_DATA_URL.format(ioc_parser_task_id, ioc_parser_attachment_id)
                    attachment_data_uri = IOCHelp_obj.TASK_DATA_URL.format(ioc_parser_task_id, ioc_parser_attachment_id)

                else:
                    attachment_metadata_uri = IOCHelp_obj.ATTACHMENT_META_DATA_URL.format(ioc_parser_incident_id, ioc_parser_attachment_id)
                    attachment_data_uri = IOCHelp_obj.ATTACHMENT_DATA_URL.format(ioc_parser_incident_id, ioc_parser_attachment_id)

                attachment_metadata = resilient_client.get(attachment_metadata_uri)
                attachment_data = resilient_client.get_content(attachment_data_uri)

                attachment_file_name = attachment_metadata.get('name')
                ioc_parser_data = IOCParserHelper.extract_text_from_bytes_data(attachment_file_name, attachment_data)

            ioc_text_obj = IOCParser(ioc_parser_data)
            ioc_results = ioc_text_obj.parse()
            function_result = IOCHelp_obj.format_iocs(ioc_results)

            yield StatusMessage("Completed IOC Parsing on artifact/attachment data")

            results = {
                "attachment_file_name": attachment_file_name,
                "iocs": function_result
            }

            yield FunctionResult(results)

        except Exception as com_err:
            yield FunctionError(com_err)
