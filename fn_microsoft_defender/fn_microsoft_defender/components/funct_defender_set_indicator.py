# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, readable_datetime, validate_fields
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
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_title",
                             "defender_description",
                             "defender_indicator_action"], kwargs)

            # Get the function parameters:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            defender_title = kwargs.get("defender_title")  # text
            defender_expiration_time = kwargs.get("defender_expiration_time")  # datetimepicker
            defender_indicator_type = kwargs.get("defender_indicator_type")  # text
            defender_indicator_id = kwargs.get("defender_indicator_id")  # text
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text
            defender_description = kwargs.get("defender_description")  # text
            defender_severity = self.get_select_param(kwargs.get("defender_severity"))  # select, values: "Low", "Medium", "High"
            defender_indicator_action = self.get_select_param(kwargs.get("defender_indicator_action"))  # select, values: "AlertAndBlock", "Alert", "Allowed"

            log = logging.getLogger(__name__)
            log.info("defender_title: %s", defender_title)
            log.info("defender_expiration_time: %s", defender_expiration_time)
            log.info("defender_indicator_type: %s", defender_indicator_type)
            log.info("defender_indicator_id: %s", defender_indicator_id)
            log.info("defender_indicator_value: %s", defender_indicator_value)
            log.info("defender_description: %s", defender_description)
            log.info("defender_severity: %s", defender_severity)
            log.info("defender_indicator_action: %s", defender_indicator_action)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # build the payload
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

            url = '/'.join([INDICATOR_URL, defender_indicator_id]) if defender_indicator_id else INDICATOR_URL
            oper = "PATCH" if defender_indicator_id else "POST"
            indicator_payload, status, reason = defender_api.call(url,
                                                                  payload=payload,
                                                                  oper=oper)
            # convert dates to timestamps
            if status:
                indicator_payload['creationTimeDateTimeUtc_ts'] = convert_date(indicator_payload['creationTimeDateTimeUtc'])
                indicator_payload['expirationTime_ts'] = convert_date(indicator_payload['expirationTime'])
                indicator_payload['lastUpdateTime_ts'] = convert_date(indicator_payload['lastUpdateTime'])
            else:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_list_indicators'")

            results = rp.done(status, indicator_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


def lookup_artifact_type(artifact_type):
    """[convert artifact types to defender types]

    Args:
        artifact_type ([str]): [IP Address, Malware Sha1, etc.]

    Raises:
        ValueError: [if artifact type not allowed by Defender]

    Returns:
        [str]: [defender indicator type]
    """
    if not artifact_type:
        return None

    if artifact_type not in LOOKUP_ARTIFACT_TYPES:
        raise ValueError("Unable to use artifact type: %s", artifact_type)

    return LOOKUP_ARTIFACT_TYPES[artifact_type]
