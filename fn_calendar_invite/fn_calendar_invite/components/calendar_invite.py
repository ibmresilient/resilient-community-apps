# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os
import datetime
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

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

            CRLF = "\r\n"
            
            host = self.email_host
            port = int(self.email_port)
            nickname = self.email_nickname
            e_login = self.email_username
            e_password = self.email_password

            def get_user_id(uid):
                uids = []
                try:
                    groups_response = self.rest_client().get('/groups/{}'.format(uid))
                    log.info("{} is a group".format(uid))
                    for member in groups_response['members']:
                        log.info("Adding uid {}".format(member))
                        uids.append(member)
                    return uids
                except Exception:
                    log.info("{} is not a group".format(uid))
                    users_response = self.rest_client().get('/users/{}'.format(uid))
                    log.info("{} is a user".format(uid))
                    uids.append(users_response['id'])
                    return uids


            def get_email(uid):
                user_json = self.rest_client().get('/users/{}'.format(uid))
                log.info("Got {} from uid {}".format(user_json['email'], uid))
                return user_json['email']

            email_addrs = []

            # Get the member ids from the incident then lookup their email
            inc_members_json = self.rest_client().get('/incidents/{}/members'.format(incident_id))
            for member in inc_members_json['members']:
                users_ids = get_user_id(member)
                for user_id in users_ids:
                    email_addrs.append(get_email(user_id))

            # Get the owner id then their email
            inc_owners_json = self.rest_client().get('/incidents/{}'.format(incident_id))
            inc_owner_id = inc_owners_json['owner_id']
            owner_ids = get_user_id(inc_owner_id)
            for owner_id in owner_ids:
                email_addrs.append(get_email(owner_id))

            attendees = email_addrs

            yield StatusMessage("Sending Emails to {}".format(attendees))

            organizer = "ORGANIZER;CN={}:mailto:first{}{}".format(nickname, CRLF, e_login)
            fro = "{} <{}>".format(nickname, e_login)

            ddtstart = datetime.datetime.now()
            dtoff = datetime.timedelta(days = 1)
            dur = datetime.timedelta(hours = 1)
            ddtstart = ddtstart +dtoff
            dtend = ddtstart + dur
            dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
            dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
            dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

            description = "DESCRIPTION: {}{}".format(calendar_invite_description,CRLF)
            attendee = ""
            for att in attendees:
                attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF
            ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
            ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
            ical+= "UID:FIXMEUID"+dtstamp+CRLF
            ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
            ical+= "SUMMARY: [ResilientIncident] {} {}".format(calendar_invite_subject, CRLF)+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF

            eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"
            eml_body_bin = "This is the email body in binary - two steps"
            msg = MIMEMultipart('mixed')
            msg['Reply-To']=fro
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = "[ResilientIncident] {}".format(calendar_invite_subject)
            msg['From'] = fro
            msg['To'] = ",".join(attendees)

            part_email = MIMEText(eml_body,"html")
            part_cal = MIMEText(ical,'calendar;method=REQUEST')

            msgAlternative = MIMEMultipart('alternative')
            msg.attach(msgAlternative)

            ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
            ical_atch.set_payload(ical)
            Encoders.encode_base64(ical_atch)
            ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

            eml_atch = MIMEBase('text/plain','')
            Encoders.encode_base64(eml_atch)
            eml_atch.add_header('Content-Transfer-Encoding', "")

            msgAlternative.attach(part_email)
            msgAlternative.attach(part_cal)
            
            yield StatusMessage("Connecting to Mail Server")

            mailServer = smtplib.SMTP(host, port)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.login(e_login, e_password)
            mailServer.sendmail(fro, attendees, msg.as_string())
            mailServer.close()

            yield StatusMessage("Send Mail - Complete")

            results = {}
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
