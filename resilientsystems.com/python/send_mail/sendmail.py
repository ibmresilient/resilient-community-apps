#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resilient Systems, Inc. ("Resilient") is willing to license software
# or access to software to the company or entity that will be using or
# accessing the software and documentation and that you represent as
# an employee or authorized agent ("you" or "your") only on the condition
# that you accept all of the terms of this license agreement.
#
# The software and documentation within Resilient's Development Kit are
# copyrighted by and contain confidential information of Resilient. By
# accessing and/or using this software and documentation, you agree that
# while you may make derivative works of them, you:
#
# 1)  will not use the software and documentation or any derivative
#     works for anything but your internal business purposes in
#     conjunction your licensed used of Resilient's software, nor
# 2)  provide or disclose the software and documentation or any
#     derivative works to any third party.
#
# THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

"""Action Module circuits component to send a custom email"""

from __future__ import print_function
import logging
import smtplib
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'sendmail'


class SendMailComponent(ResilientComponent):
    """Sends an email manually"""

    # This component sends an email with a user-provided address and message

    def __init__(self, opts):
        super(SendMailComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'filelookup'
        self.channel = "actions." + self.options.get("queue", "outboundmail")

    @handler("send_email")
    def _send_mail(self, event, *args, **kwargs):
        """Function to send an email programmatically using gmail"""

        # Get the incident ID
        properties = event.message['properties']
        email_address = properties[self.options['message_address']]
        email_body = properties[self.options['message_body']]
        email_subject = properties[self.options['message_subject']]

        LOG.info('\nthe email address is ' + email_address + '\n')
        LOG.info('\nthe email message is ' + email_body + '\n')

        LOG.info('Made draft!')
        server = smtplib.SMTP(self.options['gmail_server'])
        LOG.info('1. Made SMTP connection')
        server.ehlo()
        LOG.info('2. Ran ehlo()')
        server.starttls()
        LOG.info('3. Started TLS')
        server.login(self.options['account_address'],
                     self.options['account_password'])
        LOG.info('4. Logged in to server')
        emailmessage = 'Subject:'+email_subject+'\n'+self.options['default_message']+'\n\n'+str(email_body)
        LOG.info(emailmessage)
        server.sendmail(self.options['account_address'],
                        email_address,
                        emailmessage)
        LOG.info('5. Message sent! :D')
        server.quit()
        LOG.info('Quit server')

        yield "Sent mail!"
        # end _send_mail
