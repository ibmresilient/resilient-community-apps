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

"""Action Module example framework""" # CHANGE inside """. No impact on functionality.

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = "framework_section" # CHANGE inside ". Must match config [framework_section].


class FrameworkComponent(ResilientComponent): # CHANGE FrameworkComponent. No impact on functionality.
    """Example Circuits framework to increase prototyping speed""" # CHANGE inside """. No impact on functionality.

    def __init__(self, opts):
        super(FrameworkComponent, self).__init__(opts) # CHANGE FrameworkComponent. Must match class FrameworkComponent.
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'framework_default_queue'
        self.channel = "actions." + self.options.get("queue", "framework_default_queue") # CHANGE framework_default_queue

    #---- ok to remove these comments for your application ----
    """
    This component subscribes for messages on the queue named in 'this.channel'.
    Those events are processed by a 'message handler function' in the component.
    A single component can include many handler functions, each for different
    action messages sent to the destination.
    Also note, multiple components can subscribe to the same message destination
    - but they should handle distinct action messages.

    There are two ways to declare a handler function:

    1) a handler that will be called for any action message, like this:
        ```
            @handler()
            def _workfunction(self, event, *args, **kwargs):
                if not isinstance(event, ActionMessage):
                    # Some event we are not interested in
                    return
                # the rest of your processing here
        ```
       This is convenient if your action processor should respond to more than
       one different custom action.  For example, you might design a search
       action to be triggered by any number of custom actions, and perform
       variations of the same processing for each.
       But, the generic handler receives lots of "housekeeping" messages too,
       so you need to check each message to be sure you want to handle it.

    2) a handler for one or more specific actions, by name.
        ```
            @handler("action_name", "another_action_name")
            def _workfunction(self, event, source=None, headers=None, message=None):
                # the rest of your processing here
        ```
       The name of the custom action is downcased, and non-word characters are
       converted to spaces, to name the event.  So a handler name "action_name"
       corresponds to a custom action named "Action Name".  (The name of the
       *function* is not important, as long as it's unique in the class).

       You can declare the parameters as "self, event, *args, **kwargs" if you
       prefer, and then find the action data from 'kwargs' but naming the
       parameters is easier since Action messages have only these three:
       - the message source (the Circuits component that fired the event)
       - the message headers (the message destination, timestamp, etc)
       - the action message (data of the incident, artifact, etc, and any
         action fields).

    """
    #----

    @handler("framework_action_title") # CHANGE inside ". Must match "Framework Action Title" as defined in the README.
    def _framework_function(self, event, source=None, headers=None, message=None):
        """FRAMEWORK FUNCTION DOCSTRING""" # CHANGE inside """
        # CHANGE everything after the following line
        # ====================================================================
        # Note: the code isn't meant to be functional.
        # It's just to give an example.
        incident = event.message["incident"]
        inc_id = incident["id"]

        # Example showing how to update an incident with get_put and a callback function
        def framework_change_function(inc):
            """function to pass to the get_put method"""
            inc[self.options.get("framework_field")] = self.options.get("framework_field2")
            return inc

        self.rest_client().get_put("/incidents/"+str(inc_id), framework_change_function)

        # Status string returned here will be displayed in "Action Status" in the Resilient UI
        # Note: use 'yield', not 'return'; this is a generator method.
        status = "Finished executing framework code!"
        yield status
