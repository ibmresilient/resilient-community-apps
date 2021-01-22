# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
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
from resilient_lib import validate_fields, ResultPayload
from fn_calendar_invite.lib.calendar_invite_util import get_email_addresses, build_email_message, send_email, get_proxies

CONFIG_DATA_SECTION = 'fn_calendar_invite'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        if self.options == {}:
            raise ValueError("{} section is not set in the config file".format(CONFIG_DATA_SECTION))

        required_fields = ["email_username", "email_password", "email_nickname", "email_host", "email_port"]
        validate_fields(required_fields, self.options)


    @function("fn_calendar_invite")
    def _fn_calendar_invite_function(self, event, *args, **kwargs):
        """Function: A function to invite people to a meeting via a calendar invite"""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

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
            host = self.options.get("email_host")
            port = int(self.options.get("email_port"))
            nickname = self.options.get("email_nickname")
            e_login = self.options.get("email_username")
            e_password = self.options.get("email_password")

            timeout = 60

            now_utc = datetime.datetime.utcnow()
            meeting_time_utc = datetime.datetime.utcfromtimestamp(calendar_invite_datetime / 1000)
            if now_utc > meeting_time_utc:
                log.error("Calendar date and time for meeting is in the past.")
                raise ValueError("Calendar date and time for meeting is in the past.")

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
            proxies = get_proxies(self.opts, self.options)

            send_email(host, port, proxies, timeout, sender, e_login, e_password, attendees,
                       email_message_string)

            yield StatusMessage("Send Mail - Complete")

            # Put query results in the results payload.
            results = rp.done(success=True, content={
                "recipient": attendees,
                "sender": sender,
                "subject": calendar_invite_subject,
                "description": calendar_invite_description
            })

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)
