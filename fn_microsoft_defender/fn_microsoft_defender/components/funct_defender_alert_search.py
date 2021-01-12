# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, readable_datetime, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, ALERTS_URL, PACKAGE_NAME

FUNCTION = "defender_alert_search"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_alert_search''"""

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
    def _defender_alert_search_function(self, event, *args, **kwargs):
        """Function: Return Defender alerts based on a set of search criteria"""
        try:
            yield StatusMessage("Starting 'defender_alert_search'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_machine_id"], kwargs)

            # Get the function parameters:
            defender_alert_severity = self.get_select_param(kwargs.get("defender_alert_severity"))  # select, values: "Informational", "Low", "Medium", "High"
            defender_alert_result_max = kwargs.get("defender_alert_result_max")  # number
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            defender_alert_lastupdatetime = kwargs.get("defender_alert_lastupdatetime")  # datetimepicker
            defender_alert_creationdate = kwargs.get("defender_alert_creationdate")  # datetimepicker

            log = logging.getLogger(__name__)
            log.info("defender_alert_severity: %s", defender_alert_severity)
            log.info("defender_alert_result_max: %s", defender_alert_result_max)
            log.info("defender_machine_id: %s", defender_machine_id)
            log.info("defender_alert_lastupdatetime: %s", defender_alert_lastupdatetime)
            log.info("defender_alert_creationdate: %s", defender_alert_creationdate)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            params = {
            }
            filters = []

            if defender_alert_result_max:
                params['$top'] = defender_alert_result_max
            if defender_alert_severity:
                filters.append("severity+eq+'{}'".format(defender_alert_severity))
            if defender_alert_lastupdatetime:
                filters.append("lastUpdateTime+ge+'{}'".format(readable_datetime(defender_alert_lastupdatetime)))
            if defender_alert_creationdate:
                filters.append("alertCreationDate+ge+'{}'".format(readable_datetime(defender_alert_creationdate)))

            if filters:
                params['$filter'] = " and ".join(filters)
            log.debug(params)

            alert_payload, status, reason = defender_api.call(ALERTS_URL, payload=params)

            ## TODO
            xstatus = True
            xalert_payload = {
                "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Alerts",
                "value": [
                    {
                        "id": "da637308392288907382_-880718168",
                        "incidentId": 7587,
                        "investigationId": 723156,
                        "assignedTo": "secop123@contoso.com",
                        "severity": "Low",
                        "status": "New",
                        "classification": "TruePositive",
                        "determination": None,
                        "investigationState": "Queued",
                        "detectionSource": "WindowsDefenderAv",
                        "category": "SuspiciousActivity",
                        "threatFamilyName": "Meterpreter",
                        "title": "Suspicious 'Meterpreter' behavior was detected",
                        "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nA malware is considered active if it is found running on the machine or it already has persistence mechanisms in place. Active malware detections are assigned higher severity ratings.\n\nBecause this malware was active, take precautionary measures and check for residual signs of infection.",
                        "alertCreationTime": "2020-07-20T10:53:48.7657932Z",
                        "firstEventTime": "2020-07-20T10:52:17.6654369Z",
                        "lastEventTime": "2020-07-20T10:52:18.1362905Z",
                        "lastUpdateTime": "2020-07-20T10:53:50.19Z",
                        "resolvedTime": None,
                        "machineId": "12ee6dd8c833c8a052ea231ec1b19adaf497b625",
                        "computerDnsName": "temp123.middleeast.corp.microsoft.com",
                        "rbacGroupName": "MiddleEast",
                        "aadTenantId": "a839b112-1253-6432-9bf6-94542403f21c",
                        "relatedUser": {
                            "userName": "temp123",
                            "domainName": "MIDDLEEAST"
                        },
                        "comments": [
                            {
                                "comment": "test comment for docs",
                                "createdBy": "secop123@contoso.com",
                                "createdTime": "2020-07-21T01:00:37.8404534Z"
                            }
                        ],
                        "evidence": []
                    }
                ]
            }
            ## TODO

            # filter on machine id and convert dates to timestamps
            filtered_alerts = []
            if status:
                for alert in alert_payload['value']:
                    # filter on machine_id
                    if alert['machineId'] == defender_machine_id:
                        filtered_alert = alert.copy()
                        filtered_alert['alertCreationTime_ts'] = convert_date(filtered_alert['alertCreationTime'])
                        filtered_alert['firstEventTime_ts'] = convert_date(filtered_alert['firstEventTime'])
                        filtered_alert['lastEventTime_ts'] = convert_date(filtered_alert['lastEventTime'])
                        filtered_alert['lastUpdateTime_ts'] = convert_date(filtered_alert['lastUpdateTime'])
                        filtered_alert['resolvedTime_ts'] = convert_date(filtered_alert['resolvedTime'])
                        filtered_alerts.append(filtered_alert)
                alert_payload['value'] = filtered_alerts

                yield StatusMessage("Alerts found: {} for machine_id: {}"\
                        .format(len(alert_payload['value']), defender_machine_id))
            else:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_alert_search'")

            results = rp.done(status, alert_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
