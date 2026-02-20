# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, readable_datetime, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, INDICATOR_URL, PACKAGE_NAME

LOOKUP_ARTIFACT_TYPES = {
        "Malware SHA-1 Hash": "FileSha1",
        "FileSha1": "FileSha1",
        "Malware SHA-256 Hash": "FileSha256",
        "FileSha256": "FileSha256",
        "IP Address": "IpAddress",
        "IpAddress": "IpAddress",
        "DNS Name": "DomainName",
        "DomainName": "DomainName",
        "System Name": "DomainName",
        "URL Referer": "Url",
        "URL": "Url",
        "Url": "Url"
    }

FUNCTION = "defender_set_indicator"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_set_indicator''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FUNCTION)
    def _defender_set_indicator_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            yield StatusMessage("Starting 'defender_set_indicator'")
            # Validate required fields
            validate_fields(["defender_title", "defender_description", "defender_indicator_action"], kwargs)

            # Get the function parameters:
            defender_title = kwargs.get("defender_title")  # text
            defender_expiration_time = kwargs.get("defender_expiration_time")  # datetimepicker
            defender_indicator_type = kwargs.get("defender_indicator_type")  # text
            defender_indicator_id = kwargs.get("defender_indicator_id")  # text
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text
            defender_description = kwargs.get("defender_description")  # text
            defender_severity = self.get_select_param(kwargs.get("defender_severity"))  # select, values: "Low", "Medium", "High"
            defender_indicator_action = self.get_select_param(kwargs.get("defender_indicator_action"))  # select, values: "AlertAndBlock", "Alert", "Allowed"

            log.info(f"defender_title: {defender_title}")
            log.info(f"defender_expiration_time: {defender_expiration_time}")
            log.info(f"defender_indicator_type: {defender_indicator_type}")
            log.info(f"defender_indicator_id: {defender_indicator_id}")
            log.info(f"defender_indicator_value: {defender_indicator_value}")
            log.info(f"defender_description: {defender_description}")
            log.info(f"defender_severity: {defender_severity}")
            log.info(f"defender_indicator_action: {defender_indicator_action}")

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Build the payload
            payload = {
                "action": defender_indicator_action,
                "title": defender_title,
                "description": defender_description
            }

            if defender_indicator_type:
                payload["indicatorType"] = lookup_artifact_type(defender_indicator_type)
                payload["indicatorValue"] = defender_indicator_value
            if defender_expiration_time:
                payload["expirationTime"] = readable_datetime(defender_expiration_time)
            if defender_severity:
                payload["severity"] = defender_severity
            log.debug(payload)

            indicator_payload, status, reason = defender_api.call(
                '/'.join([INDICATOR_URL, defender_indicator_id]) if defender_indicator_id else INDICATOR_URL,
                payload=payload,
                oper="PATCH" if defender_indicator_id else "POST")
            # Convert dates to timestamps
            if status:
                indicator_payload['creationTimeDateTimeUtc_ts'] = convert_date(indicator_payload.get('creationTimeDateTimeUtc', None))
                indicator_payload['expirationTime_ts'] = convert_date(indicator_payload.get('expirationTime', None))
                indicator_payload['lastUpdateTime_ts'] = convert_date(indicator_payload.get('lastUpdateTime', None))
            else:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            yield StatusMessage("Finished 'defender_list_indicators'")

            results = rp.done(status, indicator_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))

def lookup_artifact_type(artifact_type):
    """Convert artifact types to defender types

    Args:
        artifact_type ([str]): IP Address, Malware Sha1, etc.

    Raises:
        ValueError: If artifact type not allowed by Defender

    Returns:
        [str]: Defender indicator type
    """
    if not artifact_type:
        return

    if artifact_type not in LOOKUP_ARTIFACT_TYPES:
        raise ValueError(f"Unable to use artifact type: {artifact_type}")

    return LOOKUP_ARTIFACT_TYPES[artifact_type]
