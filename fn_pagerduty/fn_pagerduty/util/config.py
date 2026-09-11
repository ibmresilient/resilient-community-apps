# -*- coding: utf-8 -*-
"""Generate a default configuration-file section for fn_pagerduty"""

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """[pagerduty]
api_token=<api_token>
from_email=<from_email_address>
# bypass https certificate validation (only set to False for testing purposes)
verifyFlag=False
resilient_client=IBM SOAR
# True to sync notes from PagerDuty incidents to their linked SOAR incidents. False to disable.
# The poller has to be running in order to sync notes.
pd_sync_notes=False
# Interval to poll PagerDuty (in seconds)
# When polling_interval equals 0 the poller is off
polling_interval=0
# Amount of time in minutes to look back
polling_lookback=60
# Comma separated filters for PagerDuty incidents to pull from PagerDuty by the poller.
# Only incidents that pass all the filters will be returned. For filters that are lists only one of
#  the values in the filter list have to pass for the incident to be returned.
# Below are the allowed filters:
# "statuses": (list) This filters value is a list and the following values are allowed, "triggered", "acknowledged", and "resolved". Example: "statuses": ["triggered", "acknowledged"]
# "service_ids": (list) This filters value is a list of PagerDuty service IDs. Example: "service_ids": ["PJKQMJA", "PHP6ZDU"]
# "urgencies": (string) This filter can either equal high or low. Example: "urgencies": "high"
# "user_ids": (list) This filters value is a list of PagerDuty user IDs. Example: "user_ids": ["PWTW9U3", "PJ3RV6P"]
# "team_ids": (list) This filters value is a list of PagerDuty team IDs. Example: "team_ids": ["PE8YY7O", "PAZNXUL"]
pd_poller_filters = "statuses": ["triggered", "acknowledged"]
"""
