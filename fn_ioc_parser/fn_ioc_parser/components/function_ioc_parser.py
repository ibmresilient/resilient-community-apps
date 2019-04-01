# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_ioc_parser.util.selftest as selftest
from resilient_lib import ResultPayload
from iocparser import IOCParser
from fn_ioc_parser.util.ioc_parser_helper import *
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_ioc_parser"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ioc_parser", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ioc_parser", {})

    @function("function_ioc_parser")
    def _function_ioc_parser_function(self, event, *args, **kwargs):
        """Function: A function to extract IOC's(Indicators of Compromise) from (text-based Data) Artifact and attachments."""
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

            # Resilient Rest call url's
            ARTIFACT_META_DATA_URL = "/incidents/{0}/artifacts/{1}"
            ARTIFACT_DATA_URL = "/incidents/{0}/artifacts/{1}/contents"
            ATTACHMENT_META_DATA_URL = "/incidents/{0}/attachments/{1}"
            ATTACHMENT_DATA_URL = "/incidents/{0}/attachments/{1}/contents"
            TASK_META_DATA_URL = "/tasks/{0}/attachments/{1}"
            TASK_DATA_URL = "/tasks/{0}/attachments/{1}/contents"

            yield StatusMessage("Starting to Parse IOCs from given Artifact/attachment data")

            # Initialising the Result Payload class and variables
            result_obj = ResultPayload(pkgname="fn_ioc_parser",
                                       function_iputs=[ioc_parser_incident_id, ioc_parser_task_id,
                                                       ioc_parser_attachment_id, ioc_parser_artifact_id,
                                                       ioc_parser_artifact_type,
                                                       ioc_parser_artifact_value])
            result_success = False              # Function result status
            reason = None                       # Function execution status message if any
            function_result = dict()            # Function result data
            ioc_parser_data = None  # Variable to hold data to be parsed
            if ioc_parser_incident_id:
                # Initialising the Resilient Rest client
                resilient_client = self.rest_client()

                if ioc_parser_artifact_id:
                    # A block to parse and download the data from Artifact
                    if ioc_parser_artifact_type.lower().strip() != 'string':
                        metadata_uri = ARTIFACT_META_DATA_URL.format(ioc_parser_incident_id, ioc_parser_artifact_id)
                        data_uri = ARTIFACT_DATA_URL.format(ioc_parser_incident_id, ioc_parser_artifact_id)
                        print("The Artifact Meta URL {}".format(metadata_uri))

                        # Checking if an artifact has any attachments
                        metadata_data = resilient_client.get(metadata_uri)
                        print("meta data : {}".format(metadata_data))
                        # Checking if an artifact has an attached file
                        if metadata_data.get('attachment'):
                            attachement_data = resilient_client.get_content(data_uri)
                            attachement_file_name = metadata_data.get('attachment').get('name')
                            if attachement_file_name.find('.pdf') != -1:
                                log.info("Artifact attachment is .pdf file.")
                                ioc_parser_data = IOCParserHelper.extract_text_from_pdf(attachement_data)
                                print("###################################", ioc_parser_data)
                            elif attachement_file_name.find('.docx') != -1:
                                log.info("Artifact attachment is .docx file.")
                                ioc_parser_data = IOCParserHelper.extract_text_from_docx(attachement_data)
                            else:
                                ioc_parser_data = attachement_data

                        else:
                            ioc_parser_data = metadata_data.get('description')
                    else:
                        ioc_parser_data = ioc_parser_artifact_value

                elif ioc_parser_attachment_id:
                    # A block to parse and download the data from attachment
                    metadata_uri = ATTACHMENT_META_DATA_URL.format(ioc_parser_incident_id, ioc_parser_attachment_id)
                    data_uri = ATTACHMENT_DATA_URL.format(ioc_parser_incident_id, ioc_parser_attachment_id)
                    if ioc_parser_task_id:
                        metadata_uri = TASK_META_DATA_URL.format(ioc_parser_task_id, ioc_parser_attachment_id)
                        data_uri = TASK_DATA_URL.format(ioc_parser_task_id, ioc_parser_attachment_id)
                    metadata_data = resilient_client.get(metadata_uri)
                    attachement_data = resilient_client.get_content(data_uri)
                    attachement_file_name = metadata_data.get('name')
                    print("The attachment Meta data --------->{}".format(metadata_data))
                    if attachement_file_name.find('.pdf') != -1:
                        ioc_parser_data = IOCParserHelper.extract_text_from_pdf(attachement_data)
                    elif attachement_file_name.find('.docx') != -1:
                        ioc_parser_data = IOCParserHelper.extract_text_from_docx(attachement_data)
                    else:
                        ioc_parser_data = attachement_data
                else:
                    raise FunctionError("IOC Parser can be called on artifacts or attachments")

            else:
                raise FunctionError("The Incident id shouldn't be None Type")

           # print("Data to be sent IOC Parser : {} ".format(ioc_parser_data))
            print("--------------------------->DATA CONTENT-----------------------------------\n", ioc_parser_data)
            textobj = IOCParser(str(ioc_parser_data))
            print("################", textobj)
            ioc_results = textobj.parse()
            for ioc_res_obj in ioc_results:
                print("{}------------------->{}".format(ioc_res_obj.kind, ioc_res_obj.value))
                if not function_result.get(ioc_res_obj.kind):
                    function_result[ioc_res_obj.kind] = []
                    function_result[ioc_res_obj.kind].append(ioc_res_obj.value)
                else:
                    function_result[ioc_res_obj.kind].append(ioc_res_obj.value)
            yield StatusMessage("Completed IOC Parsing on artifact/attachment data")
            log.info("Function Result : {0}".format(function_result))
            results = {
                "content": function_result
            }

            fun_result = result_obj.done(result_success, results, reason)
            log.info("Function Final Done Result : {0}".format(fun_result))
            # Produce a FunctionResult with the results
            yield FunctionResult(fun_result)
        except Exception as com_err:
            yield FunctionError(com_err)