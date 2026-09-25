# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from resilient_lib import IntegrationError
from fn_symantec_dlp.lib.constants import FROM_SYMANTEC_DLP_COMMENT_HDR, FROM_SOAR_COMMENT_HDR

TYPES_URI = "/types"

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def get_incident_comments(self, incident_id):
        try:
            uri = f'/incidents/{incident_id}/comments'

            comment_response = self.rest_client.get(uri=uri)
            return comment_response

        except Exception as err:
            raise IntegrationError(err)

    def filter_resilient_comments(self, soar_case_id, sdlp_comments):
        """
            need to avoid creating same comments over and over
              this logic will read all comments from an incident
              and remove those comments which have already sync

        Args:
            soar_case_id ([str]): [ SOAR case id]
            sdlp_comments ([list]): [description]
        Returns:
            new_comments ([list])
        """
        soar_comments = self.get_incident_comments(soar_case_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # filter comments with our SOAR header
        new_comments = [comment for comment in sdlp_comments if FROM_SOAR_COMMENT_HDR not in comment]

        # filter out the comments already sync'd
        if soar_comment_list:
            for comment in new_comments:
                # Get the timestamp in the note and compare to see if it should be added in SOAR.
                sdlp_timestamp = self.get_sdlp_timestamp_from_note(comment)
                for soar_comment in soar_comment_list:
                    soar_timestamp = self.get_sdlp_timestamp_from_note(soar_comment)
                    if sdlp_timestamp and (sdlp_timestamp == soar_timestamp):
                        # Match is found so remove from list of new comments to post.
                        new_comments.remove(comment)
                        break

        return new_comments

    def get_sdlp_timestamp_from_note(self, note_text):
        note_header = f"{FROM_SYMANTEC_DLP_COMMENT_HDR} ("
        if note_header in note_text:
            split_note = note_text.split(note_header)
            timestamp = split_note[1].split(")")
            return timestamp[0]
