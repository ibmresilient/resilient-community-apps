# -*- coding: utf-8 -*-
"""Action Module circuits component """

import logging
import re
import datetime
import time
import json
import csv
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

        # Get a list of artifact types that are multi-aware (support CSV split of value)
        self.multi_aware_artifacts = [item["name"] for item in self._get_constants()["artifact_types"] if item["multi_aware"]]

        # We cache the types (because they shouldn't change often)
        # and refresh if more than 5 minutes old (so you can test without too much delay)
        self.types_timestamp = 0
        self.interesting_fields = None
        self.artifacts_by_type = {}

    def _get_constants(self):
        """return data from Resilient /const endpoint"""
        client = self.rest_client()
        url = "{}/rest/const".format(client.base_url)
        response = client._execute_request(client.session.get, url, proxies=client.proxies,
                                           cookies=client.cookies, headers=client.headers)
        return response.json()

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
        elif ftype == "number":
            value = str(value)
        elif ftype in ["textarea"]:
            # Value may be {"content":"...", "format":"text"}
            if isinstance(value, dict):
                value = value.get("content", "")
            # Value may include text for embedded hyperlinks, as '<http://xxx>' ... strip them out brute-force
            value = re.sub(r'<http.*>', "", value or "")
        elif isinstance(value, list):
            # If this is a 'multiselect' field, resolve each of the the ids
            value = [self.get_field_label(fieldname, v) for v in value]
            value = u", ".join(value)
        else:
            # If this is a 'select' field, resolve the id
            value = self.get_field_label(fieldname, value)
        return value.strip()

    @handler()
    def _fields_to_artifacts(self, event, *args, **kwargs):
        """Handle any custom action on this message destination"""

        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # Defer processing, this is low priority
        if event.defer(self, delay=3):
            # OK, let's handle it later
            return

        client = self.rest_client()
        incident = event.message["incident"]
        inc_id = incident["id"]

        # Find all the incident fields
        # that have a tooltip in the format:
        #   [Artifact: xxxx]
        # where we'll assume that xxxx is an Artifact Type.
        regex = re.compile(r"\[Artifact:(.*)\]")
        if self.interesting_fields is None or self.types_timestamp < (time.time() - 240):
            fields = client.get("/types/incident/fields")
            self.interesting_fields = [field for field in fields if regex.match(field.get("tooltip", ""))]
            self.types_timestamp = time.time()

        if len(self.interesting_fields) == 0:
            msg = "No fields are configured for mapping to artifacts"
            LOG.warn(msg)
            return msg

        # Fetch the incident again, getting plaintext instead of richtext, and resolved values for handle ids
        incident_url = "/incidents/{0}?handle_format=names&text_content_output_format=always_text".format(inc_id)
        incident = client.get(incident_url)

        # Fetch all the artifacts for this incident
        artifacts_url = "/incidents/{0}/artifacts?handle_format=names".format(inc_id)
        artifacts = client.get(artifacts_url)
        self.artifacts_by_type = {}
        for artifact in artifacts:
            atype = artifact["type"]
            values = self.artifacts_by_type.get(atype, [])
            values.append(artifact["value"])
            self.artifacts_by_type[atype] = values

        # For each of the interesting fields:
        # - Find the field value
        # - Check whether there is an artifact with that value.
        #   If not, create it.
        add_artifact_url = "/incidents/{0}/artifacts".format(inc_id)
        for field in self.interesting_fields:
            match = regex.match(field["tooltip"])
            artifact_type = match.group(1).strip()
            if artifact_type not in self.all_artifact_types:
                # The artifact type is not valid
                LOG.error("Tooltip for field '%s' specifies an invalid artifact type: '%s'",
                          field["name"],
                          artifact_type)
                continue
            value = self._field_value_string(incident, field)
            if value is None or len(value) == 0:
                # nothing to do
                continue

            if artifact_type in self.multi_aware_artifacts:
                reader = csv.reader([value,], delimiter=',', skipinitialspace=True)
                values = [row for row in reader][0]
            else:
                values = [value,]

            for value in values:
                if value not in self.artifacts_by_type.get(artifact_type, []):
                    # We don't have this artifact.  Add it
                    self._create_artifact(add_artifact_url, artifact_type, value, field, event.context)

        LOG.info("Done")

    def _create_artifact(self, url, atype, value, field, co3_context_token):
        """Create artifact"""
        value = value.strip()
        LOG.info("Adding artifact '%s' for field '%s': '%s'",
                 atype,
                 field["name"],
                 value)
        new_artifact = {"type": atype,
                        "value": value,
                        "description": "From incident field '{}'".format(field["text"])}
        try:
            self.rest_client().post(url, new_artifact, co3_context_token=co3_context_token)
            # Add new artifact to our list
            values = self.artifacts_by_type.get(atype, [])
            values.append(value)
            self.artifacts_by_type[atype] = values
        except:
            # Log the error and carry on
            LOG.exception("Error adding artifact '%s' for field '%s' (invalid value?): '%s'",
                          atype,
                          field["name"],
                          value)
