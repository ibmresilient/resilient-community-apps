# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from fn_calendar_invite.lib.calendar_invite_util import get_incident_members_email_addrs, build_email_message, send_email

CONFIG_DATA_SECTION = 'fn_calendar_invite'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self.email_username = self.options.get("email_username")
        self.email_password = self.options.get("email_password")
        self.email_nickname = self.options.get("email_nickname")
        self.email_host = self.options.get("email_host")
        self.email_port = self.options.get("email_port")

    @function("calendar_invite")
    def _calendar_invite_function(self, event, *args, **kwargs):
        """Function: A function to invite people to a meeting via a calendar invite"""
        try:
            calendar_invite_datetime = kwargs.get("calendar_invite_datetime")  # datetimepicker
            calendar_invite_subject = kwargs.get("calendar_invite_subject")  # text
            calendar_invite_description = kwargs.get("calendar_invite_description")  # text
            incident_id = kwargs.get("calendar_incident_id")

            log = logging.getLogger(__name__)
            log.info("calendar_invite_datetime: %s", calendar_invite_datetime)
            log.info("calendar_invite_subject: %s", calendar_invite_subject)
            log.info("calendar_invite_description: %s", calendar_invite_description)
            
            host = self.email_host
            port = int(self.email_port)
            nickname = self.email_nickname
            e_login = self.email_username
            e_password = self.email_password

            client = self.rest_client()
            attendees = get_incident_members_email_addrs(client, log, incident_id)

            yield StatusMessage("Sending Emails to {}".format(attendees))
            from_string = "{} <{}>".format(nickname, e_login)
            email_message_string = build_email_message(calendar_invite_datetime,
                                                       calendar_invite_subject,
                                                       calendar_invite_description,
                                                       nickname,
                                                       e_login,
                                                       from_string,
                                                       attendees)

            yield StatusMessage("Connecting to Mail Server")

            send_email(host, port, from_string, e_login, e_password, attendees, email_message_string)

            yield StatusMessage("Send Mail - Complete")

            results = {}
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
