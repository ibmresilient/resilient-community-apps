# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
import re
from rc_data_feed.lib.feed import FeedDestinationBase
from .resilient_common import Resilient

LOG = logging.getLogger(__name__)

# use for parsing owner or member values: First Last (a@example.com)
USER_REGEX = re.compile(r".*\((.*)\)")

"""
This module contains the ResilientFeedDestination for writing Resilient data
to an instance of Resilient.
"""

class ResilientFeedDestination(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed destination for writing Resilient data to a local directory."""
    def __init__(self, rest_client_helper, options):   # pylint: disable=unused-argument
        super(ResilientFeedDestination, self).__init__()
        self.resilient_source = Resilient(options, rest_client_helper)
        self.resilient_target = Resilient(options, None)

    def send_data(self, context, payload):
        """
        TBD
        """
        type_name = context.type_info.get_pretty_type_name()

        # check for attachments and artifacts with attachments
        if type_name == "attachment" or (type_name == "artifact" and payload.get("attachment", None)):
            # remove org reference
            orig_id, cleaned_payload = clean_payload(payload)

            LOG.info('adding %s(%s): %s', type_name, orig_id, cleaned_payload)

            self.resilient_target.upload_attachment(self.resilient_source.rest_client, context.inc_id,
                                                    self.resilient_source.rest_client.org_id, type_name,
                                                    cleaned_payload, orig_id)
        else:
            # get all the field definitions
            all_fields = context.type_info.get_all_fields(refresh=False)

            # invert the list into a dictionary for faster review
            # data tables use the cell id for the column name. So we need to create the index list differently
            if self._is_datatable(payload):
                all_field_names = {str(field['id']):field for field in all_fields}
            else:
                all_field_names = {field['name']:field for field in all_fields}

            # convert selection lists and multi-selection lists to values, not id's
            new_payload = self.convert_values(context, all_field_names, None, payload, self._is_datatable(payload))

            # remove org reference
            orig_id, cleaned_payload = clean_payload(new_payload)

            self.resilient_target.create_update_type(context.inc_id, self.resilient_source.rest_client.org_id,
                                                     type_name, cleaned_payload, orig_id)

    def _is_datatable(self, payload):
        """
        Return boolean regarding object if a datatable
        :param payload:
        :return: True if datatable
        """
        return bool(payload.get("table_name", None))

    def convert_values(self, context, all_field_names, prefix, payload, datatable_flag):
        """
        recursive function to convert Ids to values for a given object
        :param context:
        :param all_field_names: type definition for this object
        :param prefix: heirarchical fields have prefixes (incident)
        :param payload:
        :param datatable_flag:
        :return: converted payload
        """
        new_payload = {}

        # walk the payload, converting any list or ID based field with the appropriate value(s)
        for field in payload:
            field_key = field

            # datatable column names need to be looked up differently based on cell Id
            if datatable_flag and all_field_names.get(field, {}).get('name', None):
                field_key = all_field_names[field]['name']
                if all_field_names[field]['input_type'] in ('select', 'multiselect'):
                    new_value = {"value": self.convert_selects(field_key, payload[field]['value'], all_field_names[field])}
                else:
                    new_value = {"value": payload[field].get('value', None)}

            elif isinstance(payload[field], dict):
                # recurse over this dictionary
                new_value = self.convert_values(context, all_field_names, field, payload[field], datatable_flag)

            else:
                new_value = payload[field]
                if field in all_field_names:
                    #LOG.debug("%s %s %s:%s", field, all_field_names[field]['input_type'], prefix, all_field_names[field]['prefix'])

                    if all_field_names[field]['input_type'] in ('select', 'multiselect', 'select_owner', 'multiselect_members') \
                        and all_field_names[field].get('prefix', prefix) == prefix:
                        new_value = self.convert_selects(field_key, payload[field], all_field_names[field])

            #LOG.debug("{}: {}".format(field_key, new_value))
            new_payload[field_key] = new_value

        return new_payload

    def convert_selects(self, field_key, orig_values, type_info):
        """
        convert select and mutliselects IDs into values
        :param field_key: name of field
        :param orig_values: list or value
        :param type_info: schema for field with all values possible
        :return: converted list or value
        """
        # plan_status is special as the value "C|A" should not be converted
        if field_key == "plan_status":
            return orig_values

        if isinstance(orig_values, list):
            new_value = []
            for item in orig_values:
                found = False
                for value in type_info['values']:
                    if value['value'] == item:
                        replacement_value = self._clean_assignee_value(type_info['input_type'], value['label'])
                        new_value.append(replacement_value)
                        found = True
                        break

                if not found and item:
                    LOG.warning(u"Substitute value: {} not found for field: {}, omitting".format(item, field_key))
        else:
            found = False
            new_value = orig_values
            for value in type_info['values']:
                #LOG.debug("{}:{}".format(value['value'], new_value))
                if value['value'] == orig_values:
                    new_value = self._clean_assignee_value(type_info['input_type'], value['label'])
                    found = True
                    break

            if not found and new_value:
                LOG.warning(u"Substitute value: {} not found for field: {}, omitting".format(new_value, field_key))
                new_value = None

        return new_value

    def _clean_assignee_value(self, input_type, value):
        """
        parse out the string "First Last (a@example.com)" to return only email portion.
        This applies only to select_owner and multiselect_members
        :param input_type:
        :param value:
        :return: value if not input type match or email address
        """
        if input_type not in ('select_owner', 'multiselect_members'):
            return value

        # select_owner or multiselect_members
        match = USER_REGEX.match(value)
        if match:
            return match.group(1)       # just email address

        return value

    def filter_nulls(self, payload):
        """
        instance method
        remove key values pairs where value is null, resilient cannot index these
        :param payload:
        :return: new_payload
        """
        new_payload = dict((key, value) for key, value in payload.items() if value)
        return new_payload

    """
    def get_custom_fields(self, type_name):
        custom_fields = [
            {
                "name": "data_feeder_original_incident_id",
                "text": "original incident_id",
                "prefix": "properties",
                "type_id": 0,
                "tooltip": "data feeder reference",
                "placeholder": "",
                "input_type": "number"
            },
            {
                "name": "data_feeder_original_org_id",
                "text": "original org_id",
                "prefix": "properties",
                "type_id": 0,
                "tooltip": "data feeder reference",
                "placeholder": "",
                "input_type": "number"
            }
        ]

        return custom_fields + self.resilient_source.get_custom_fields(type_name)
    """

# S T A T I C
def clean_payload(payload):
    """
    remove fields which will be problematic if passed on
    :param payload:
    :return: cleaned payload
    """
    orig_id = payload.pop('id', None)

    # incident
    payload.pop('org', None)
    payload.pop('org_name', None)
    payload.pop('workspace', None)

    # Task
    payload.pop('reng_version', None)
    payload.pop('instr_text', None) # legacy field
    payload.pop('at_id', None)

    return orig_id, payload
