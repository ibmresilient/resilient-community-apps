# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate a default configuration-file section for fn_sumo_logic"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_sumo_logic when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_sumo_logic]
# Sumo Logic access ID
access_id = xxx
# Sumo Logic access key
access_key = xxx
# Sumo Logic API endpoint URL
api_endpoint_url=https://api.sumologic.com/api
# Sumo Logic console 
console_url=https://service.sumologic.com
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval = 600
# Number of minutes to lookback for queries the first time the poller runs.
polling_lookback = 120
#
# OPTIONAL: Flag indicating whether or not poller adds SOAR case URL in comment in theSumo Logic Insight.
polling_add_case_url_comment_in_sumo_logic = True
# 
# OPTIONAL: polling filters can be applied when querying Sumo Logic for new insights.
#   The search query string uses sumo logic custom DSL that is used to filter the results.
#   Each filter is in the format field:operator:value. Multiple filters are separated by a space.
#   Operators:
#   - `exampleField:"bar"`: The value of the field is equal to "bar".
#   - `exampleField:in("bar", "baz", "qux")`: The value of the field is equal to either "bar", "baz", or "qux".
#   - `exampleTextField:contains("foo bar")`: The value of the field contains the phrase "foo bar".
#   - `exampleNumField:>5`: The value of the field is greater than 5. There are similar `<`, `<=`, and `>=` operators.
#   - `exampleNumField:5..10`: The value of the field is between 5 and 10 (inclusive).
#   - `exampleDateField:>2019-02-01T05:00:00+00:00`: The value of the date field is after 5 a.m. UTC time on February 2,
#       2019.
#   - `exampleDateField:2019-02-01T05:00:00+00:00..2019-02-01T08:00:00+00:00`: The value of the date field is between 5 a.m.
#       and 8 a.m. UTC time on February 2, 2019.
#
#   Fields: readableId, status, statusId, name, insightId, serialId, description, created, timestamp, closed, assignee
#           entity.id, entity.ip, entity.hostname, entity.username, entity.sensorZone, entity.type, entity.value,
#           involvedEntities.id, involvedEntities.type, involvedEntities.value, enrichment, sensorZone, tag, severity
#           resolution, subResolution, ruleId, records, confidence
#
#   In this example, the query will return all insights: 
#       a confidence greater than or equal to .85 AND
#       a severity greater than or equal to "HIGH" (which would be have values "HIGH" or "CRITICAL")
#       polling_filters = confidence:>=.85 severity:>="HIGH"
#
# The default polling filter is to return all insights with confidence greater than or equal to .70, and severity greater 
# than or equal to "MEDIUM".  Note: Insight status "closed" is included so that insights closed in Sumo Logic are 
# synchronized to corresponding case in SOAR.
#
polling_filters = status:in("inprogress","new","closed") confidence:>=.70 severity:>="MEDIUM"
#
# OPTIONAL: Override value for templates used for creating/updating/closing SOAR cases
# soar_create_case_template=
# soar_close_case_template=
# soar_update_case_template=
# """
    return config_data
