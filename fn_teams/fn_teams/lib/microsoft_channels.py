# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

''' Helper function for funct_ms_teams_create_teams'''

import json, logging

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_commons import ResponseHandler


class ChannelInterface:
    def __init__(self, required_parameters):
        self.rc = required_parameters.get("rc")
        self.log = logging.getLogger(__file__)
        self.headers = required_parameters.get("header")
        self.response_handler = ResponseHandler()


    def create_channel(self, options):

        group_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        group_details = group_finder.find_group(options)

        if len(group_details) > 1:
            raise IntegrationError(constants.ERROR_FOUND_MANY_GROUP)

        group_id = group_details[0].get("id")

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_CHANNEL.format(group_id))

        body = {
            "displayName": options.get("displayName"),
            "description": options.get("description"),
            "membershipType": constants.CHANNEL_MEMBERSHIP_TYPE}

        body = json.dumps(body, indent=2)
        self.log.debug("Request body for Channel creation")
        self.log.debug(body)

        response = self.rc.execute(
            method="post",
            url=url,
            data=body,
            headers=self.headers,
            callback=self.response_handler.check_response)

        if response.get("status_code") == 201:
            response["message"] = constants.INFO_SUCCESSFULLY_CREATED_CHANNEL.format(
                options.get("displayName"))
            return response
        else:
            raise IntegrationError(constants.ERROR_COULDNOT_CREATE_CHANNEL)


    def delete_channel(self, options):

        channel_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        channel = channel_finder.find_channel(options)

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LOCATE_CHANNEL.format(
                channel.get("group_id"),
                channel.get("id")))

        response = self.rc.execute(
            method="delete",
            url=url,
            headers=self.headers,
            callback=self.response_handler.check_response)

        if response.get("status_code") == 204:
            response["message"] = (constants
                .INFO_SUCCESSFULLY_DELETED_CHANNEL
                .format(channel.get("displayName")))
            print(json.dumps(response, indent=2))
            return response
        else:
            raise IntegrationError(constants.ERROR_COULDNOT_DELETE_CHANNEL)
