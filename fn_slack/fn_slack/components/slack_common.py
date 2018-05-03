# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import simplejson as json
from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import clean_html, build_incident_url, build_resilient_url, build_timestamp
from slackclient import SlackClient
from six import string_types


def slack_post_message(log, resoptions, slack_details, slack_channel, slack_as_user, slack_user_id, slack_reply_broadcast,
                       slack_parse, slack_link_names, slack_markdown, slack_thread_id, api_token, def_username):
    """
    Process the slack post
    :param log:
    :param resoptions: app.config resilient section
    :param slack_details: json structure for how to structure the payload to slack
    See slack API for the use of these variables
    :param slack_channel:
    :param slack_as_user:
    :param slack_user_id:
    :param slack_reply_broadcast:
    :param slack_parse:
    :param slack_link_names:
    :param slack_markdown:
    :param slack_thread_id:
    :param api_token
    :param def_username - name to use for who posted the message
    :return: JSON result
    """

    sl = SlackClient(api_token)

    data = json.loads(slack_details.replace("\\n", ""), strict=False)  # cleanup for json.loads
    payload = build_payload(data, resoptions)
    log and log.debug(payload)

    # start processing
    results = sl.api_call(
        "chat.postMessage",
        channel=slack_channel,
        text=payload,
        as_user=slack_as_user,
        username=slack_user_id if slack_user_id else def_username,
        reply_broadcast=slack_reply_broadcast,
        parse=slack_parse,
        link_names=slack_link_names,
        mrkdown=slack_markdown,
        thread_ts=slack_thread_id
    )
    log and log.debug(results)

    return results


def build_payload(dataDict, resoptions):
    """
    build the payload string based on the different types of data created
    :param dataDict:
    :return: payload string
    """
    payload = ""

    for key, valDict in dataDict.items():
        if len(payload) > 0:
            payload += "\n"

        if valDict['type'] == 'string' and valDict['data']:
            payload += '{}: {}'.format(key, valDict['data'])

        elif valDict['type'] == 'incident' and valDict['data']:
            payload += '{}: {}'.format(key, build_incident_url(build_resilient_url(resoptions['host'], resoptions['port']), valDict['data']))

        elif valDict['type'] == 'richtext' and valDict['data']:
            cleaned_data = clean_html(valDict['data'])
            if len(cleaned_data) > 0:
                payload += '{}: {}'.format(key, cleaned_data)

        elif valDict['type'] == 'datetime' and valDict['data'] and valDict['data'] != 0:
            payload += '{}: {}'.format(key, build_timestamp(valDict['data']))

        elif valDict['type'] == 'boolean' and valDict['data']:
            payload += '{}: {}'.format(key, _buildBoolean(valDict['data'], true_value='Yes', false_value='No'))

        elif valDict['data']:
            raise IntegrationError("Invalid type: "+ valDict['type'])

    return payload

# Builders for slack presentation
def _buildBoolean(value, true_value="True", false_value="False"):
    """
     convert internal boolean to displayable format
    :param value: boolean
    :param true_value: value to use when boolean=True
    :param false_value: value to use when boolean=False
    :return: payload string
    """
    if isinstance(value, string_types):
        return true_value if value.lower() in ('1', 'yes', 'true') else false_value
    if isinstance(value, int):
        return true_value if value == 1 else false_value

    return false_value