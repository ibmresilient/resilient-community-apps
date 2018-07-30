# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""
This module contains utility routines used by the fn_calensdar_invite functions
"""
import smtplib
import datetime
import sys

if sys.version_info[0] == 2:
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email.MIMEText import MIMEText
    from email.Utils import COMMASPACE, formatdate
    from email import Encoders
else:
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.utils import COMMASPACE, formatdate
    from email.encoders import encode_base64


def get_user_id(client, log, uid):
    uids = []
    try:
        groups_response = client.get('/groups/{}'.format(uid))
        log.info("{} is a group".format(uid))
        for member in groups_response['members']:
            log.info("Adding uid {}".format(member))
            uids.append(member)
        return uids
    except Exception:
        log.info("{} is not a group".format(uid))
        users_response = client.get('/users/{}'.format(uid))
        log.info("{} is a user".format(uid))
        uids.append(users_response['id'])
        return uids

# Get email address of the user ID.
def get_email_addr(client, log, uid):
    user_json = client.get('/users/{}'.format(uid))
    log.info("Got {} from uid {}".format(user_json['email'], uid))
    return user_json['email']

# Get the member and owner emails associated with an incident.
def get_incident_members_email_addrs(client, log, incident_id):
    email_addrs = []

    # Get the member ids from the incident then lookup their email
    inc_members_json = client.get('/incidents/{}/members'.format(incident_id))
    for member in inc_members_json['members']:
        users_ids = get_user_id(client, log, member)
        for user_id in users_ids:
            email_addrs.append(get_email_addr(client, log, user_id))

    # Get the owner id then their email
    inc_owners_json = client.get('/incidents/{}'.format(incident_id))
    inc_owner_id = inc_owners_json['owner_id']
    owner_ids = get_user_id(client, log, inc_owner_id)
    for owner_id in owner_ids:
        email_addrs.append(get_email_addr(client, log, owner_id))

    return email_addrs


def build_email_message(calendar_invite_datetime, calendar_invite_subject, calendar_invite_description, nickname, e_login, from_string, attendees):
    CRLF = "\r\n"

    organizer = "ORGANIZER;CN={}:mailto:first{}{}".format(nickname, CRLF, e_login)

    ddtstart = datetime.datetime.now()
    dtoff = datetime.timedelta(days=1)
    dur = datetime.timedelta(hours=1)
    ddtstart = ddtstart + dtoff
    dtend = ddtstart + dur
    dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
    dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

    description = "DESCRIPTION: {}{}".format(calendar_invite_description, CRLF)
    attendee = ""
    for att in attendees:
        attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + att + ";X-NUM-GUESTS=0:" + CRLF + " mailto:" + att + CRLF
    ical = "BEGIN:VCALENDAR" + CRLF + "PRODID:pyICSParser" + CRLF + "VERSION:2.0" + CRLF + "CALSCALE:GREGORIAN" + CRLF
    ical += "METHOD:REQUEST" + CRLF + "BEGIN:VEVENT" + CRLF + "DTSTART:" + dtstart + CRLF + "DTEND:" + dtend + CRLF + "DTSTAMP:" + dtstamp + CRLF + organizer + CRLF
    ical += "UID:FIXMEUID" + dtstamp + CRLF
    ical += attendee + "CREATED:" + dtstamp + CRLF + description + "LAST-MODIFIED:" + dtstamp + CRLF + "LOCATION:" + CRLF + "SEQUENCE:0" + CRLF + "STATUS:CONFIRMED" + CRLF
    ical += "SUMMARY: [ResilientIncident] {} {}".format(calendar_invite_subject,
                                                    CRLF) + "TRANSP:OPAQUE" + CRLF + "END:VEVENT" + CRLF + "END:VCALENDAR" + CRLF

    eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"
    msg = MIMEMultipart('mixed')
    msg['Reply-To'] = from_string
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "[ResilientIncident] {}".format(calendar_invite_subject)
    msg['From'] = from_string
    msg['To'] = ",".join(attendees)

    part_email = MIMEText(eml_body, "html")
    part_cal = MIMEText(ical, 'calendar;method=REQUEST')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    ical_atch = MIMEBase('application/ics', ' ;name="%s"' % ("invite.ics"))
    ical_atch.set_payload(ical)
    if sys.version_info[0] == 2:
        Encoders.encode_base64(ical_atch)
    else:
        encode_base64(ical_atch)
    ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"' % ("invite.ics"))

    msgAlternative.attach(part_email)
    msgAlternative.attach(part_cal)

    return msg.as_string()

# Open the SMTP host port and send the email
def send_email(host, port, from_email, e_login, e_password, attendees_email_addr, msg_string):
    mailServer = smtplib.SMTP(host, port)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(e_login, e_password)
    mailServer.sendmail(from_email, attendees_email_addr, msg_string)
    mailServer.quit()
