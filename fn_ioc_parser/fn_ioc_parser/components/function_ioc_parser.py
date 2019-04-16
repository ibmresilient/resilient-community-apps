# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from iocparser import IOCParser
from fn_ioc_parser.util.ioc_parser_helper import *


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_ioc_parser"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ioc_parser", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ioc_parser", {})

    @function("function_ioc_parser")
    def _function_ioc_parser_function(self, event, *args, **kwargs):
        """A function to extract IOC's(Indicators of Compromise) from (text-based Data) Artifacts & attachments."""
        try:
            # Get the function parameters:
            ioc_parser_incident_id = kwargs.get("ioc_parser_incident_id")  # number
            ioc_parser_task_id = kwargs.get("ioc_parser_task_id")  # number
            ioc_parser_attachment_id = kwargs.get("ioc_parser_attachment_id")  # number
            ioc_parser_artifact_id = kwargs.get("ioc_parser_artifact_id")  # number
            ioc_parser_artifact_type = kwargs.get("ioc_parser_artifact_type")  # text
            ioc_parser_artifact_value = kwargs.get("ioc_parser_artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("ioc_parser_incident_id: %s", ioc_parser_incident_id)
            log.info("ioc_parser_task_id: %s", ioc_parser_task_id)
            log.info("ioc_parser_attachment_id: %s", ioc_parser_attachment_id)
            log.info("ioc_parser_artifact_id: %s", ioc_parser_artifact_id)
            log.info("ioc_parser_artifact_type: %s", ioc_parser_artifact_type)
            log.info("ioc_parser_artifact_value: %s", ioc_parser_artifact_value)

            yield StatusMessage("Extracting IOCs from given Artifact/attachment data")

            # Initialising the Resilient Rest client for making api calls to Resilient system
            resilient_client = self.rest_client()

            # Initialising the IOC Parser Helper class
            IOCHelp_obj = IOCParserHelper()

            if ioc_parser_artifact_id:
                # A block to parse and download the data from Artifacts
                if ioc_parser_artifact_type.lower().strip() in ['string', 'email subject', 'email body']:
                    ioc_parser_data = ioc_parser_artifact_value
                else:
                    metadata_uri = IOCHelp_obj.ARTIFACT_META_DATA_URL.format(ioc_parser_incident_id, ioc_parser_artifact_id)
                    data_uri = IOCHelp_obj.ARTIFACT_DATA_URL.format(ioc_parser_incident_id, ioc_parser_artifact_id)

                    # Getting the Meta data from the Resilient for an artifact
                    metadata_data = resilient_client.get(metadata_uri)
                    if metadata_data.get('attachment'):
                        # Getting the file content from Resilient system
                        attachment_data = resilient_client.get_content(data_uri)

                        attachment_file_name = metadata_data.get('attachment').get('name')
                        ioc_parser_data = IOCParserHelper.extract_text_from_bytes_data(attachment_file_name, attachment_data)
                    else:
                        ioc_parser_data = ioc_parser_artifact_value
            else:
                # A block to parse and download the data from attachments
                metadata_uri = IOCHelp_obj.ATTACHMENT_META_DATA_URL.format(ioc_parser_incident_id, ioc_parser_attachment_id)
                data_uri = IOCHelp_obj.ATTACHMENT_DATA_URL.format(ioc_parser_incident_id, ioc_parser_attachment_id)
                if ioc_parser_task_id:
                    metadata_uri = IOCHelp_obj.TASK_META_DATA_URL.format(ioc_parser_task_id, ioc_parser_attachment_id)
                    data_uri = IOCHelp_obj.TASK_DATA_URL.format(ioc_parser_task_id, ioc_parser_attachment_id)

                # Getting the Meta data from the Resilient for an artifact
                metadata_data = resilient_client.get(metadata_uri)

                # Getting the file content from Resilient system
                attachment_data = resilient_client.get_content(data_uri)

                attachment_file_name = metadata_data.get('name')
                ioc_parser_data = IOCParserHelper.extract_text_from_bytes_data(attachment_file_name, attachment_data)

            ioc_text_obj = IOCParser(ioc_parser_data)
            ioc_results = ioc_text_obj.parse()
            function_result = IOCHelp_obj.correct_iocs_format(ioc_results)

            yield StatusMessage("Completed IOC Parsing on artifact/attachment data")
            results = {
                "value": function_result
            }
            log.debug("Function Result : %s", results)
            yield FunctionResult(results)
        except Exception as com_err:
            yield FunctionError(com_err)