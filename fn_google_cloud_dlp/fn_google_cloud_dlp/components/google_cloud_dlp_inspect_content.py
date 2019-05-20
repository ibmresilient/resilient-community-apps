# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_google_cloud_dlp.util.gcp_helper import GCPHelper

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'google_cloud_dlp_inspect_content"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_google_cloud_dlp", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_google_cloud_dlp", {})

    @function("google_cloud_dlp_inspect_content")
    def _google_cloud_dlp_inspect_content_function(self, event, *args, **kwargs):
        """Function: DLP Inspect Content
        Used to take in an input of an attachment or artifact,
        parses the text and sends it to Google Cloud DLP for inspection
        Findings are returned as a dictionary."""
        try:
            # Get the function parameters:
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            gcp_artifact_input = kwargs.get("gcp_artifact_input")  # text
            gcp_dlp_info_types = self.get_select_param(kwargs.get("gcp_dlp_info_types"))  # multiselect, values: "AMERICAN_BANKERS_CUSIP_ID", "AUSTRALIA_MEDICARE_NUMBER", "AUSTRALIA_TAX_FILE_NUMBER", "BRAZIL_CPF_NUMBER", "CANADA_BC_PHN", "CANADA_DRIVERS_LICENSE_NUMBER", "CANADA_OHIP", "CANADA_PASSPORT", "CANADA_QUEBEC_HIN", "CANADA_SOCIAL_INSURANCE_NUMBER", "CHINA_PASSPORT", "CREDIT_CARD_NUMBER", "EMAIL_ADDRESS", "ETHNIC_GROUP", "FEMALE_NAME", "FIRST_NAME", "FRANCE_CNI", "FRANCE_NIR", "FRANCE_PASSPORT", "GCP_CREDENTIALS", "GERMANY_PASSPORT", "IBAN_CODE", "IMEI_HARDWARE_ID", "INDIA_PAN_INDIVIDUAL", "IP_ADDRESS", "JAPAN_INDIVIDUAL_NUMBER", "JAPAN_PASSPORT", "KOREA_PASSPORT", "KOREA_RRN", "LAST_NAME", "MAC_ADDRESS_LOCAL", "MAC_ADDRESS", "MALE_NAME", "MEXICO_CURP_NUMBER", "MEXICO_PASSPORT", "NETHERLANDS_BSN_NUMBER", "NORWAY_NI_NUMBER", "PHONE_NUMBER", "SPAIN_NIE_NUMBER", "SPAIN_NIF_NUMBER", "SPAIN_PASSPORT", "SWIFT_CODE", "UK_DRIVERS_LICENSE_NUMBER", "UK_NATIONAL_HEALTH_SERVICE_NUMBER", "UK_NATIONAL_INSURANCE_NUMBER", "UK_PASSPORT", "UK_TAXPAYER_REFERENCE", "US_ADOPTION_TAXPAYER_IDENTIFICATION_NUMBER", "US_BANK_ROUTING_MICR", "US_DEA_NUMBER", "US_DRIVERS_LICENSE_NUMBER", "US_HEALTHCARE_NPI", "US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER", "US_PASSPORT", "US_PREPARER_TAXPAYER_IDENTIFICATION_NUMBER", "US_SOCIAL_SECURITY_NUMBER", "US_TOLLFREE_PHONE_NUMBER", "US_VEHICLE_IDENTIFICATION_NUMBER", "US_STATE", "FDA_CODE", "ICD9_CODE", "ICD10_CODE", "US_EMPLOYER_IDENTIFICATION_NUMBER", "LOCATION", "DATE", "DATE_OF_BIRTH", "TIME", "PERSON_NAME", "AGE", "GENDER", "ARGENTINA_DNI_NUMBER", "CHILE_CDI_NUMBER", "COLOMBIA_CDC_NUMBER", "NETHERLANDS_PASSPORT", "PARAGUAY_CIC_NUMBER", "PERU_DNI_NUMBER", "PORTUGAL_CDC_NUMBER", "URUGUAY_CDI_NUMBER", "VENEZUELA_CDI_NUMBER", "DOMAIN_NAME", "CHINA_RESIDENT_ID_NUMBER", "POLAND_PESEL_NUMBER", "POLAND_NATIONAL_ID_NUMBER", "POLAND_PASSPORT", "SWEDEN_PASSPORT", "SWEDEN_NATIONAL_ID_NUMBER", "FINLAND_NATIONAL_ID_NUMBER", "JAPAN_BANK_ACCOUNT", "JAPAN_DRIVERS_LICENSE_NUMBER", "SPAIN_DRIVERS_LICENSE_NUMBER", "URL", "DENMARK_CPR_NUMBER"

            payload = ResultPayload("fn_google_cloud_dlp", **kwargs)
            helper = GCPHelper(self.options, res_client=self.rest_client())
            log = logging.getLogger(__name__)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("gcp_artifact_input: %s", gcp_artifact_input)
            log.info("gcp_dlp_info_types: %s", gcp_dlp_info_types)

            # Check if we are dealing with an artifact or attachment and gather the attachment if so.
            attachment_input, attachment_name = helper.download_attachment_if_available(artifact_id,
                                                                                        attachment_id,
                                                                                        gcp_artifact_input,
                                                                                        incident_id,
                                                                                        task_id)

            yield StatusMessage("Sending Data to Google Cloud DLP")
            # Attempt to send the attachment data to Google Cloud
            try:
                findings = helper.inspect_string(
                    content_string=gcp_artifact_input or attachment_input, info_types=gcp_dlp_info_types)
            except Exception as general_exception:
                log.debug("Encountered exception with Google API : %s", general_exception)
                raise FunctionError(u"""Encountered an unexpected exception.
                            Exception Message: {}""".format(general_exception))
            else:
                yield StatusMessage("Data Sent to Google Cloud DLP successfully and response received")

            results = payload.done(
                success=True,
                content={
                    "findings": findings,
                    "attachment_name": attachment_name
                }
            )
            log.info("Complete")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
