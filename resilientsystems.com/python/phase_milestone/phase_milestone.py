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

"""Circuits component for Resilient Action Module message handling"""

import logging
import json
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage

LOG = logging.getLogger(__name__)

# For better tracking of incident progress,
# this automatic action creates a new milestone
# for every phase-change in the incident.
#
# The milestone just says that the phase change occurred.
#
# Trigger from an automatic action named 'autophase'
# with condition: when phase changes.


class PhaseMilestone(ResilientComponent):
    """Add a milestone when the phase changes."""

    def __init__(self, opts):
        super(PhaseMilestone, self).__init__(opts)
        self.options = opts.get("phase_milestone", {})
        LOG.debug(self.options)

        # Channel name beginning "actions." is a Resilient queue or topic
        # The queue name can be specified in the config file, or default to 'phase_milestone'
        self.channel = "actions." + self.options.get("queue", "phase_milestone")

        # Build a map of the phase names, for later
        self.phase_names = {}
        phase_id_field = self.get_incident_field("phase_id")
        for value in phase_id_field["values"]:
            self.phase_names[value["value"]] = value["label"]

    @handler("phase_milestone")
    def _workfunction(self, event, source=None, headers=None, message=None):
        """Do the work"""
        assert isinstance(event, ActionMessage)

        client = self.rest_client()
        incident = message["incident"]
        inc_id = incident["id"]
        LOG.info("AutoPhase: incident %s: '%s'", inc_id, incident["name"])

        timestamp = int(headers.get("timestamp"))
        phase_id = int(incident["phase_id"])
        phase_name = self.phase_names.get(phase_id, str(phase_id))
        title = "Phase changed to '{}'".format(phase_name)

        # Find the previous phase by looking at the newsfeed.
        # Note: this may not be totally reliable, since the newsfeed update lags the causing event.
        prev_phase = None
        news_url = "/incidents/{}/newsfeed?object_type=INCIDENT&entry_type=PHASE_CHANGE&limit=1".format(inc_id)
        news = client.get(news_url, co3_context_token=event.context)
        LOG.debug(json.dumps(news, indent=2))
        if len(news) > 0:
            if news[0].get("after", "") == phase_name:
                prev_phase = news[0].get("before")
                title = "Phase changed from '{}' to '{}'".format(prev_phase, phase_name)
            else:
                # This most recent phase change hasn't hit the newsfeed yet
                prev_phase = news[0].get("after")
                title = "Phase changed from '{}' to '{}'".format(prev_phase, phase_name)
        LOG.info("timestamp {}, {}".format(timestamp, title))

        # Add a milestone
        milestone_entry = {"description": "",
                           "title": title,
                           "date": timestamp}

        post_url = "/incidents/{}/milestones".format(inc_id)
        try:
            m = client.post(post_url, milestone_entry, co3_context_token=event.context)
        except Exception as exc:
            LOG.exception(json.dumps(milestone_entry, indent=2))
            raise

        LOG.debug(json.dumps(m, indent=2))
        yield ""
