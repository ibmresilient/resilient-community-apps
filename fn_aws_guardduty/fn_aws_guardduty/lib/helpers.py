# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Helpers for AWS GuardDuty """
# Map GuardDuty finding fields to Resilient Incident custom fields.
import re
import datetime as dt

CUSTOM_FIELDS_MAP = {
    "Id": "aws_guardduty_finding_id",
    "Arn": "aws_guardduty_finding_arn",
    "Type": "aws_guardduty_finding_type",
    "UpdatedAt": "aws_guardduty_finding_updated_at",
    "Region": "aws_guardduty_region",
    "Resource": {
        "ResourceType": "aws_guardduty_resource_type"
    },
    "Service": {
        "Count": "aws_guardduty_count",
        "DetectorId": "aws_guardduty_detector_id"
    }
}

class IQuery(dict):
    """Class to create a query for existing findings from AWS GuardDuty in Resilient.

    # Default query example:
        {"filters":[{
              "conditions":
                  [{"field_name":"plan_status", "method":"equals", "value":"A"},
                   {"field_name":"properties.aws_guardduty_finding_id", "method":"equals",
                    "value":"b8baffd3f900972453b724a4147cba6f"},
                   {"field_name":"properties.aws_guardduty_region", "method":"equals", "value":"us-west-2"}]}
          ],
          "sorts":[
            {"field_name":"create_date", "type":"desc"}
          ]
        }
    Alternate query example:
        {"filters":[{
            "conditions":
                [{"field_name":"plan_status", "method":"equals", "value":"A"},
                 {"field_name":"properties.aws_guardduty_finding_id", "method":"has_a_value"},
                 {"field_name":"properties.aws_guardduty_region", "method":"has_a_value"}]}
         ]}
        }
    """
    def __init__(self, finding, fields, alt=False):
        # Add default condition.
        self["filters"] = [{
            "conditions": [
                {
                    "field_name": "plan_status",
                    "method": "equals",
                    "value": 'A'
                }
            ]
        }]
        if alt:
            self.add_alt_conditions(finding, fields)
        else:
            self.add_conditions(finding, fields)

    def add_conditions(self, finding, fields):
        """
        Update query for conditions for GuardDuty finding fields.

        :param finding: GuardDuty finding properties
        :param fields: List of GuardDuty finding fields names
        """
        [self["filters"][0]["conditions"].append({
            "field_name": "properties.{}".format(CUSTOM_FIELDS_MAP[f]),
            "method": "equals",
            "value": finding[f]
        }) for f in fields]
        self["sorts"] =  [{
            "field_name": "create_date",
            "type": "desc"
        }]

    def add_alt_conditions(self, finding, fields):
        """
        Update query for alternate conditions for GuardDuty finding fields.

        :param finding: GuardDuty finding properties
        :param fields: List of GuardDuty finding fields names
        """
        [self["filters"][0]["conditions"].append({
            "field_name": "properties.{}".format(CUSTOM_FIELDS_MAP[f]),
            "method": "has_a_value"
        }) for f in fields]

class FCrit(dict):
    """Class to create criteria for querying findings on AWS GuardDuty.

    # Example criterion:

    """
    def __init__(self):
        # Add default empty criterion.
        self["Criterion"] = {}

    def set_severity(self, severity_threshold):
        """
        Set severity criterion for GuardDuty findings.

        :param severity_threshold: GuardDuty severity threshold
        """
        self["Criterion"].update({
            'severity': {'Gte': severity_threshold}
        })

    def set_update(self, update_epoch):
        """
        Set updated criteria for GuardDuty findings.

        :param update_epoch: Epoch value in millisecs
        """
        self["Criterion"].update({
            "updatedAt": {"Gte": int(update_epoch)}
        })

def is_regex(regex_str):
    """"Test if sting is a correctly formed regular expression.

    :param regex_str: Regular expression string.
    :return: Boolean.
    """
    try:
        re.compile(regex_str)
        return True
    except re.error:
        return False

def get_lastrun_unix_epoch(lookback_interval):
    """
    Get Unix epoch in miliseconds sincs last run.

    :param lookback_interval: Interval in minutes(int) or a datetime object.
    :return: Unix epoch in miliseconds.
    """
    now = dt.datetime.now()
    if isinstance(lookback_interval, int):
        past = now - dt.timedelta(minutes=lookback_interval)
    else:
        past = lookback_interval

    return dt.datetime.timestamp(past) * 1000.0