# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from logging import getLogger
from resilient_lib import SOARCommon
from fn_microsoft_sentinel.lib.constants import FROM_SOAR_COMMENT_HDR

LOG = getLogger(__name__)

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client
        self.soar_common = SOARCommon(rest_client)

    def filter_resilient_comments(self, incident_id, sentinel_comments):
        """
        Need to avoid creating same comments over and over this logic will read all comments
        from an incident and remove those comments which have already sync.
        :param incident_id [str]: SOAR incident id
        :param sentinel_comments [list]: Comments from the sentinel incident
        :return: new_comments [list]
        """
        soar_comments = self.soar_common.get_case_comments(incident_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # Filter comments with our SOAR header
        new_comments = [comment for comment in sentinel_comments if FROM_SOAR_COMMENT_HDR not in comment['properties']['message']]

        # Filter out the comments already sync'd
        if soar_comment_list:
            new_comments = [comment for comment in new_comments \
                if not any([comment['name'] in already_syncd for already_syncd in soar_comment_list])]

        return new_comments
    
    def get_soar_incident(self, incident_id):
        """
        Get a SOAR incident (Added so that this can be mocked for tests)
        :param incident_id: SOAR incident ID
        """
        return self.rest_client.get(f"/incidents/{incident_id}?handle_format=names")
