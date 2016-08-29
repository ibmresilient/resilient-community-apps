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

"""Action Module circuits component """

import logging
import re
import datetime
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'fields_to_artifacts'


class FieldsToArtifactsComponent(ResilientComponent):
    """Assigns users to each task in an incident"""

    def __init__(self, opts):
        super(FieldsToArtifactsComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'fields_to_artifacts'
        self.channel = "actions." + self.options.get("queue", "fields_to_artifacts")

        # Get a list of all the valid artifact types
        # for easier verification later
        artifact_types_url = "/types/artifact/fields/type"
        artifact_types = self.rest_client().get(artifact_types_url)
        self.all_artifact_types = [atype["label"] for atype in artifact_types["values"]]
        LOG.debug("All artifact types: %s", self.all_artifact_types)

    def _field_value_string(self, incident, fielddef):
        """Helper to get the value of a field, as a string"""
        fieldname = fielddef.get("name")
        prefix = fielddef.get("prefix")
        if prefix is None:
            value = incident.get(fieldname)
        else:
            value = incident[prefix].get(fieldname)
        # Format the value
        ftype = fielddef["input_type"]
        if ftype in ["datetimepicker", "datepicker"]:
            # Value is epoch milliseconds
            dtime = datetime.datetime.utcfromtimestamp(int(value) / 1000.0)
            value = dtime.strftime("%Y-%m-%d %H:%M:%S")
        elif ftype in ["textarea"]:
            # Value may be {"content":"...", "format":"text"}
            if isinstance(value, dict):
                value = value.get("content")
        elif isinstance(value, list):
            # If this is a 'multiselect' field, resolve each of the the ids
            value = [self.get_field_label(fieldname, v) for v in value]
            value = ", ".join(value)
        else:
            # If this is a 'select' field, resolve the id
            value = self.get_field_label(fieldname, value)
        return value

    @handler()
    def _fields_to_artifacts(self, event, *args, **kwargs):
        """Handle any custom action on this message destination"""

        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # Find all the incident fields
        # that have a tooltip in the format:
        #   [Artifact: xxxx]
        # where we'll assume that xxxx is an Artifact Type.
        client = self.rest_client()
        fields = client.get("/types/incident/fields")
        regex = re.compile(r"\[Artifact:(.*)\]")
        interesting_fields = [field for field in fields if regex.match(field.get("tooltip", ""))]

        if len(interesting_fields) == 0:
            msg = "No fields are configured for mapping to artifacts"
            LOG.warn(msg)
            return msg

        # Fetch all the artifacts for this incident
        incident = event.message["incident"]
        inc_id = incident["id"]
        artifacts_url = "/incidents/{0}/artifacts?handle_format=names".format(inc_id)
        artifacts = client.get(artifacts_url)
        artifacts_by_type = {}
        for artifact in artifacts:
            atype = artifact["type"]
            values = artifacts_by_type.get(atype, [])
            values.append(artifact["value"])
            artifacts_by_type[atype] = values

        # For each of the interesting fields:
        # - Find the field value
        # - Check whether there is an artifact with that value.
        #   If not, create it.
        add_artifact_url = "/incidents/{0}/artifacts".format(inc_id)
        for field in interesting_fields:
            match = regex.match(field["tooltip"])
            artifact_type = match.group(1).strip()
            value = self._field_value_string(incident, field)
            # Check that the artifact type is valid
            if artifact_type not in self.all_artifact_types:
                LOG.error("Tooltip for field '%s' specifies an invalid artifact type: '%s'",
                          field["name"],
                          artifact_type)
            elif value not in artifacts_by_type.get(artifact_type, []):
                # We don't have this artifact.  Add it
                LOG.info("Adding artifact '%s' for field '%s': '%s'",
                         artifact_type,
                         field["name"],
                         value)
                new_artifact = {"type": artifact_type,
                                "value": value,
                                "description": "From incident field '{}'".format(field["text"])}
                try:
                    client.post(add_artifact_url, new_artifact, co3_context_token=event.context)
                except:
                    # Log the error and carry on
                    LOG.exception("Error adding artifact '%s' for field '%s' (invalid value?): '%s'",
                                  artifact_type,
                                  field["name"],
                                  value)

        LOG.info("Done")
