# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Generate payload and data tables data for Resilinet incident from AWS GuardDuty finding"""
import json
import logging
import pprint
import copy
import datetime as dt
from sys import version_info

from fn_aws_guardduty.lib.helpers import search_json, map_property
from fn_aws_guardduty.util import const

LOG = logging.getLogger(__name__)


class ParseFinding():
    """Class that parses an AWS finding and generates a payload and data tables data."""

    def __init__(self, finding, region, refresh=False, existing_artifacts=None):
        """constructor """
        self.timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.finding = self.replace_datetime(finding)
        self.region = region
        self.existing_artifacts = existing_artifacts if existing_artifacts else {}
        self.payload = {}
        self.data_tables = {}
        self.refresh = refresh

        # Add Incident fields to incident payload.
        self.make_incident_fields()

        # Add artifacts from finding to incident payload.
        self.add_artifacts_to_payload()

        # Add finding json as a note to incident payload.

        self.add_note_to_payload()

        # Assemble Data tables for incident
        self.build_data_tables()

        # Remove other unwanted object atributes after finding has been parsed.
        if not self.refresh:
            del self.finding

        del self.existing_artifacts
        del self.refresh

    def to_json(self):
        """
        Return object as a json object to allow it to be returned to Resilient as a result.

        :return: Object as dict.
        """
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def make_incident_fields(self):
        """
        Assemble the Incident DTO Payload / Fields from GuardDuty finding Payload.

        :param finding: Finding payload from GuardDuty.
        :return: Incident DTO payload
        """
        # Create Placeholder with finding properties as values
        self.payload.update({
            "name": self.make_incident_name(),
            "description": self.make_incident_description(),
            "discovered_date": self.finding.get("CreatedAt"),
            "severity_code": self.map_severity(self.finding.get("Severity", "Low")),
            "properties": {},
        })

        # Use mapping to get incident field values from finding payload.
        for gd_prop in const.CUSTOM_FIELDS_MAP.keys():
            (res_prop, path) = map_property(gd_prop)

            # Get GuardDuty property value.
            if path:
                gd_prop_val = self.finding.get(path, {}).get(gd_prop)
            else:
                gd_prop_val = self.finding.get(gd_prop)

            # Convert boolean value to string 'True' or 'False'
            if isinstance(gd_prop_val, bool):
                gd_prop_val = "{}".format(gd_prop_val)

            if isinstance(gd_prop_val, int):
                # Convert number to text equivalent.
                gd_prop_val = str(gd_prop_val)

            self.payload["properties"][res_prop] = gd_prop_val

        if self.finding["Region"] != self.region:
            # In case region in finding payload is different default to value used with API.
            self.payload["properties"][const.CUSTOM_FIELDS_MAP["Region"]] = self.region

        return self.payload

    def make_incident_name(self):
        """
        Create Resilient Incident name from finding.

        :param finding: Finding Payload from Poller
        :return iname: String for Incident Name to be used in Search / Incident Creation
        """
        # Fill event summary when blank
        if not self.finding.get("Title"):
            i_title = "No Title Provided, Create date : {}.".format(self.finding.get("CreatedAt"))
        else:
            i_title = self.finding.get("Title")

        iname = "AWS GuardDuty: {}".format(i_title)
        LOG.debug("Incident Label Assembled: %s", iname)

        return iname

    def make_incident_description(self):
        """
        Make Incident description text from GuardDuty finding description.

        :param finding: Raw GuardDuty Payload
        :return: Return formatted Description for Incident DTO
        """
        i_desc = self.finding.get("Description", "AWS GuardDuty finding --") or "AWS GuardDuty finding --"
        return {"format": "text", "content": i_desc}

    def map_severity(self, finding_severity):
        """
        Map GuardDuty finding severity to Resilient Severity.

        In GuardDuty the value of the severity can fall anywhere within the 1.0 to 8.9 range.
            High 7.0 - 8.9 -> High
            4.0 - 6.9 -> Medium
            1.0 = 3.9 -> Low

        :param finding_severity: GuardDuty finding severity
        :return resilient_severity: Resilient severity string
        """
        resilient_severity = None

        if not isinstance(finding_severity, (int, float)) or not 1.0 <= finding_severity <= 8.9:
            raise ValueError("Incorrect value '{}' set for severity level.".format(finding_severity))
        if 1.0 <= finding_severity <= 3.9:
            resilient_severity = "Low"
        elif 4.0 <= finding_severity <= 6.9:
            resilient_severity = "Medium"
        elif 7.0 <= finding_severity <= 8.9:
            resilient_severity = "High"

        return resilient_severity

    def get_artifact_data(self):
        """
        Add artifact types and values to an artifacts_data payload.

        Example payload entry:
            {'10.0.0.1':
                ('IP Address', 'PrivateIpAddress', '["Resource"]["InstanceDetails"]["NetworkInterfaces"]["0"]')
            }
        :param finding: The finding json content to seach for artifacts.
        :return artifact_data: Dict of artifacts data.
        """
        artifact_data = {}
        for artifact_type, gd_keys in const.ARTIFACT_TYPES_MAP.items():
            base_path = None
            if isinstance(gd_keys, dict):
                # A path to property is defined.
                base_path = gd_keys["path"]
                gd_keys = gd_keys["gd_props"]

            for gd_key in gd_keys:
                result = search_json(self.finding, gd_key, path=base_path)
                if isinstance(result, dict) and result.get("msg"):
                    LOG.debug("%s for finding data %s.", result.get("msg"),
                              result.get("path"))
                    # Artifact match not found in finding skip.
                    continue
                for (artifact_value, path) in result:
                    LOG.debug(u'artifact type %s (%s) ID %s, at path %s', artifact_type, gd_key, artifact_value, path)
                    if isinstance(artifact_value, int):
                        # Convert number to text equivalent.
                        artifact_value = str(artifact_value)
                    if artifact_value in artifact_data:
                        # Artifact value already found skip.
                        continue
                    artifact_data[artifact_value] = (artifact_type, gd_key, path)

        return artifact_data

    def add_artifacts_to_payload(self):
        """Add artifacts to Resilient Incident payload.

        :param artifact_data: Artifact data from finding.
        """

        artifact_data = self.get_artifact_data()
        if not artifact_data:
            return

        self.payload["artifacts"] = []
        # Set up Artifact payload skeleton.
        artifact_payload = {
            'type': {
                'name': 'String',
            },
            'description': {
                'format': 'text',
            }
        }

        # Loop through Artifact data provided with the finding.
        for artifact_val, (artifact_type, gd_key, path) in artifact_data.items():
            # If this is a refresh check it artifact with this value and type already exist.
            if artifact_val not in self.existing_artifacts or self.existing_artifacts[artifact_val] != artifact_type:
                # Populate payload with ID and type and description.
                artifact = copy.deepcopy(artifact_payload)
                desc = "'{}' extracted from GuardDuty from finding property '{}' at path '{}'." \
                    .format(artifact_type, gd_key, path)
                artifact['value'] = artifact_val
                artifact['type']['name'] = const.ARTIFACT_TYPE_API_NAME.get(artifact_type, "String")
                artifact['description']['content'] = desc
                self.payload["artifacts"].append(artifact)

    def add_note_to_payload(self):
        """
        Add a comment/note to the specified Resilient Incident payload.

        :param i_payload: Incident payload.
        :param finding: Raw GuardDuty json to be added as a Resilient incident note.
        """
        self.payload["comments"] = []

        if self.refresh:
            heading = "AWS GuardDuty finding Payload for refresh:\n"
        else:
            heading = "AWS GuardDuty finding Payload:\n"

        if version_info.major == 2:
            finding = self.convert_unicode(self.finding)
        else:
            finding = self.finding

        note = {
            'format': 'text',
            'content': '{}{}'.format(heading, pprint.pformat(finding, indent=4))
        }

        self.payload["comments"].append({'text': note})

    def build_data_tables(self):
        """
        Assemble the Data Table for an incident from a GuardDuty finding json payload

        :return  Returns assembled LIST of DICTs by Resilient data table ID with Data Table column names and values.

        Example Format of returned data including Resilient POST data:

            {
              "gd_action_details":[
                {
                  "cells":{
                    "action_type":{
                      "value":"NETWORK_CONNECTION"
                    },
                    ...
                    ...
                  }
                }
              ],
              "gd_resource_affected":[
                {
                  "cells":{
                    "resource_type":{
                      "value":"Instance"
                    },
                    ...
                    ...
                  }
                }
              ],
              "gd_s3_bucket_details":[
                {
                  "cells":{
                    "s3_bucket_owner":{
                      "value":"Instance"
                    },
                    ...
                    ...
                  }
            }

        """
        for table_id in const.DATA_TABLE_IDS:
            data_table = []
            # Iterate over section for each data table id.
            for dt_section in const.DATA_TABLE_FIELDS_MAP[table_id]:
                path = copy.deepcopy(dt_section.get("path", None))
                if path and isinstance(path[-1], list):
                    # The path to properties in GuardDuty finding points to a list.
                    row_count = 0
                    result = True
                    while result:
                        path[-1] = row_count
                        dt_row = self.setup_data_table_rows(dt_section, path, [])
                        if dt_row:
                            data_table.extend(dt_row)
                            row_count += 1
                        else:
                            result = False
                else:
                    data_table = self.setup_data_table_rows(dt_section, path, data_table)

            LOG.info("Data Table Assembled with %d rows for table id '%s'.", len(data_table), table_id)

            self.data_tables.update({table_id: data_table})

            LOG.debug(pprint.pformat(data_table, indent=4))

    def setup_data_table_rows(self, dt_section, path, table_copy):
        """ Setup data table data row structures for Resilient from finding payload.

        :param dt_section: Section of definitions for a data-table (c.f. DATA_TABLE_FIELDS_MAP in const.py).
        :param path: Path to a data-table property in GuardDuty finding. (c.f. DATA_TABLE_FIELDS_MAP in const.py).
        :param table_copy: Interim list with data table row information for a data-table id.
        :return dt_copy: Return interim data table copy with new rows added.
        """
        table_row = {}
        for key, val in dt_section["fields"].items():
            dt_copy = table_copy[:]
            value = None
            # Search for key at path.
            search_json(self.finding, key, path=path)
            result = search_json(self.finding, key, path=path)
            if result:
                if isinstance(result, dict) and result.get("msg"):
                    LOG.debug("%s for finding data %s.", result.get("msg"),
                              result.get("path"))
                elif isinstance(result, list):
                    # Grab 1st result.
                    (value, _) = result.pop(0)
                    # Convert boolean values to string 'True' or 'False'
                    if isinstance(value, bool):
                        value = "{}".format(value)
                    table_row[val] = {"value": value}
                    if isinstance(value, int):
                        value = str(value)
                    table_row[val] = {"value": value}
            if table_row:
                # Value found for key in search.
                if not dt_copy and "cells" not in table_row:
                    # Setup new data table row.
                    table_row["query_execution_date"] = {"value": self.timestamp}
                    dt_copy.append({"cells": table_row})
                dt_copy[0]["cells"].update(table_row)

        return dt_copy

    def replace_datetime(self, finding):
        """ Convert in-place datetime objects returned in finding payload to strings.

        :param finding: Raw GuardDuty finding json.
        """
        if isinstance(finding, (dict, list)):
            for k, v in finding.items() if isinstance(finding, dict) else enumerate(finding):
                if isinstance(v, dt.datetime):
                    finding[k] = v.strftime("%Y-%m-%d %H:%M:%S")
                self.replace_datetime(v)

        return finding

    def convert_unicode(self, data, level=0):
        """ Convert unicode strings in finding payload e.g. u'string' to allow pretty printing.

        :param data: GuardDuty finding json data.
        :param level: Level of recursion.
        :return conv_finding: Converted finding json.
        """
        if level == 0:
            # Ensure original finding not altered.
            conv_finding = copy.deepcopy(self.finding)
        else:
            conv_finding = data

        if isinstance(conv_finding, (dict, list)):
            for k, v in conv_finding.items() if isinstance(conv_finding, dict) else enumerate(conv_finding):
                if isinstance(k, unicode):
                    del conv_finding[k]
                    conv_finding[k.encode('utf-8')] = v
                if isinstance(v, unicode):
                    conv_finding[k] = v.encode('utf-8')
                self.convert_unicode(v, level=level+1)

        return conv_finding
