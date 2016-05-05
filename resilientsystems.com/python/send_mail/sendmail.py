#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action Module circuits component to send a custom email"""

from __future__ import print_function
from circuits import Component, Debugger
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
from twitter import *
import smtplib
import os
import csv
import logging
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'sendmail'

class SendMailComponent(ResilientComponent):
    """Sends an email manually"""

    # This component sends an email with a user-provided address and message

    def __init__(self, opts):
        super(SendMailComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file, or default to 'filelookup'
        self.channel = "actions." + self.options.get("queue", "sendmail")


    @handler()
    def _time_delta(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Actions module.
        """

        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return
        
        # Get the incident ID
        incident = event.message["incident"]
        inc_id = incident["id"]
        properties = event.message['properties']
        email_address = properties[self.options['message_address']]
        email_body = properties[self.options['message_body']]
	email_subject = properties[self.options['message_subject']]

        LOG.info('\nthe email address is ' + email_address + '\n')
	LOG.info('\nthe email message is ' + email_body + '\n')
        
        LOG.info('Made draft!')
        server = smtplib.SMTP(self.options['gmail_server'])
        LOG.info('1')
        server.ehlo()
        LOG.info('2')
        server.starttls()
        LOG.info('3')
        server.login(self.options['account_address'],
                     self.options['account_password'])
        LOG.info('4')
        emailmessage = 'Subject:'+email_subject+'\n'+self.options['default_message']+'\n\n'+str(email_body)
	LOG.info(emailmessage)
        server.sendmail(self.options['account_address'],
                        email_address,
                        emailmessage)
        LOG.info('5')
        server.quit()
        LOG.info('Message sent!')	


        yield "Sent mail!"
    #end _lookup_action
