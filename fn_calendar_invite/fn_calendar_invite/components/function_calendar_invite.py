# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#  -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""fn_calendar_invite sends a calendar invitation via email to all the
 members and owner of an incident for incident management meetings etc.
 It directly connects to an SMTP server to send the email message.
 The meeting information is placed in an Outlook calendar.
 """

import logging
import datetime
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from fn_calendar_invite.lib.calendar_invite_util import get_email_addresses, build_email_message, send_email

CONFIG_DATA_SECTION = 'fn_calendar_invite'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        # Get app.config parameters.
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        if self.options == {}:
            log.error("There is no [fn_calendar_invite] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise ValueError("[fn_calendar_invite] section is not set in the config file")

        self.email_username = self.options.get("email_username")
        self.email_password = self.options.get("email_password")
        self.email_nickname = self.options.get("email_nickname")
        self.email_host = self.options.get("email_host")
        self.email_port = self.options.get("email_port")

        # Check that config parameters are defined.
        if self.email_username is None:
            log.error("email_username is not set. You must set this value to run fn_calendar_invite")
            raise ValueError("email_username is not set. You must set this value to run fn_calendar_invite")
        if self.email_password is None:
            log.error("email_password is not defined. You must set this value to run fn_calendar_invite")
            raise ValueError("email_password is not defined. You must set this value to run fn_calendar_invite")
        if self.email_host is None:
            log.error("email_host is not set. You must set this value to run fn_calendar_invite")
            raise ValueError("email_host is not set. You must set this value to run fn_calendar_invite")
        if self.email_port is None:
            log.error("email_port is not set. You must set this value to run fn_calendar_invite")
            raise ValueError("email_port is not set. You must set this value to run fn_calendar_invite")


    @function("fn_calendar_invite")
    def _fn_calendar_invite_function(self, event, *args, **kwargs):
        """Function: A function to invite people to a meeting via a calendar invite"""
        try:
            # Get the calendar meeting information input
            calendar_invite_datetime = kwargs.get("calendar_invite_datetime")        # datetime picker
            calendar_invite_subject = kwargs.get("calendar_invite_subject")          # text
            calendar_invite_description = kwargs.get("calendar_invite_description")  # text area
            calendar_invite_extra_email_addr = kwargs.get("calendar_invite_extra_email_addr") # text area
            incident_id = kwargs.get("calendar_invite_incident_id")                  # number

            log = logging.getLogger(__name__)
            log.info(u"calendar_invite_datetime: %s", calendar_invite_datetime)
            log.info(u"calendar_invite_subject: %s", calendar_invite_subject)
            log.info(u"calendar_invite_description: %s", calendar_invite_description)
            log.info(u"calendar_invite_extra_email_addr %s", calendar_invite_extra_email_addr)

            # Email sender information
            host = self.email_host
            port = int(self.email_port)
            nickname = self.email_nickname
            e_login = self.email_username
            e_password = self.email_password

            now_utc = datetime.datetime.utcnow()
            meeting_time_utc = datetime.datetime.utcfromtimestamp(calendar_invite_datetime / 1000)
            if now_utc > meeting_time_utc:
                log.error("Calendar date and time for meeting is not valid.")
                yield FunctionError("Calendar date and time for meeting is not valid")

            # Get email addresses of the members and owner of the incident.
            client = self.rest_client()
            attendees = get_email_addresses(client, log, incident_id, calendar_invite_extra_email_addr)

            yield StatusMessage("Sending Emails to {}".format(attendees))

            # Build the email message string to be sent.
            sender = u"{} <{}>".format(nickname, e_login)
            email_message_string = build_email_message(calendar_invite_datetime,
                                                       calendar_invite_subject,
                                                       calendar_invite_description,
                                                       nickname,
                                                       e_login,
                                                       sender,
                                                       attendees)

            yield StatusMessage("Connecting to Mail Server")

            # Connect to SMTP server and send the message.
            send_email(host, port, sender, e_login, e_password, attendees, email_message_string)

            yield StatusMessage("Send Mail - Complete")

            results = {
                "recipient": attendees,
                "sender": sender,
                "subject": calendar_invite_subject,
                "body": email_message_string
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(e.message)
            yield FunctionError(e.message)
