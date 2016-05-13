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

"""Action Module example framework""" # CHANGE inside """

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'framework_section' # CHANGE inside '


class FrameworkComponent(ResilientComponent): # CHANGE FrameworkComponent
    """Example Circuits framework to increase prototyping speed""" # CHANGE inside """

    def __init__(self, opts):
        super(FrameworkComponent, self).__init__(opts) # CHANGE FrameworkComponent
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'framework_default_queue'
        self.channel = "actions." + self.options.get("queue", "framework_default_queue") # CHANGE framework_default_queue

    @handler("framework_action_title") # CHANGE inside "
    def _framework_function(self, event, *args, **kwargs): # CHANGE _framework_function
        """FRAMEWORK FUNCTION DOCSTRING""" # CHANGE inside """
        # CHANGE everything after the following line
        # ====================================================================
        # Note: the code isn't meant to be functional.
        # It's just to give an example.
        incident = event.message['incident']
        inc_id = incident['id']

        def framework_change_function(inc):
            """function to pass to the get_put method"""
            inc[self.options.get['framework_field']] = self.options.get("framework_field2")
            return inc

        # Update the incident owner
        self.rest_client().get_put("/incidents/"+str(inc_id), framework_change_function)

        status = "Finished executing framework code!" # CHANGE inside "
        yield status


