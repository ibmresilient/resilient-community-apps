# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
import re
from data_feeder_plugins.resilientfeed.lib.filters import Filters
from resilient_lib import str_to_bool
from rc_data_feed.lib.feed import FeedDestinationBase
from .resilient_common import Resilient

LOG = logging.getLogger(__name__)

# use for parsing owner or member values to return email addr: First Last (a@example.com)
USER_REGEX = re.compile(r".*\((.*)\)")

# sync properties for an incident
DF_INC_ID = "df_inc_id"
DF_ORG_ID = "df_org_id"

"""
This module contains the ResilientFeedDestination for writing Resilient data
to an instance of Resilient.
"""

class ResilientFeedDestination(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed destination for writing Resilient data to a local directory."""
    def __init__(self, rest_client_helper, options):   # pylint: disable=unused-argument
        super(ResilientFeedDestination, self).__init__()
        self.options = options
        self.resilient_source = Resilient(options, rest_client_helper)
        self.resilient_target = Resilient(options, None)
        # set up the criteria to accept incident synchronizing, if any
        self.filters = Filters(options.get("matching_fields", None), options.get("matching_operator", None))
        # incident fields to filter out
        self.filter_fields = options.get("exclude_incident_fields", "").replace(" ", "").split(",")
        self.sync_references = str_to_bool(options.get("sync_reference_fields", "false"))


    def send_data(self, context, payload):
        """
        synchronize a object between Resilient instances. Steps performed are:
        1) Convert id references to values
        2) Match incident filter criteria
        3) cleanup loads, removing fields identified
        4) Perform syncrhonization, create or update
        :param context:
        :param payload:
        :return:
        """
        type_name = context.type_info.get_pretty_type_name()

        # check for attachments and artifacts with attachments
        if type_name == "attachment" or (type_name == "artifact" and payload.get("attachment", None)):
            # remove org reference
            orig_id, cleaned_payload = self.clean_payload(type_name, payload)

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
            try:
                new_payload = self.convert_values(context, type_name, all_field_names, None, payload,
                                                  self._is_datatable(payload))

                # remove fields unrelated to creating a new type
                orig_id, cleaned_payload = self.clean_payload(type_name, new_payload)

                # perform the creation in the new resilient org
                self.resilient_target.create_update_type(context.inc_id, self.resilient_source.rest_client.org_id,
                                                         type_name, cleaned_payload, orig_id)
            except FilterError as err:
                LOG.info("{} on Incident {}".format(str(err), context.inc_id))

                # create a sync entry so we know we skipped this incident
                self.resilient_target.create_update_type(context.inc_id, self.resilient_source.rest_client.org_id,
                                                         type_name, None, context.inc_id)


    def _is_datatable(self, payload):
        """
        Return boolean regarding object if a datatable
        :param payload:
        :return: True if datatable
        """
        return bool(payload.get("table_name", None))


    def convert_values(self, context, type_name, all_field_names, prefix, payload, datatable_flag):
        """
        recursive function to convert Ids to values for a given object
        :param context:
        :param type_name: type of object converting
        :param all_field_names: type definition for this object
        :param prefix: hierarchical fields have prefixes (incident)
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
                    new_value = {"value": self.convert_selects(field_key, payload[field].get('value', None),
                                                               all_field_names[field])}
                else:
                    new_value = {"value": payload[field].get('value', None)}

            elif isinstance(payload[field], dict):
                # recurse over this dictionary
                new_value = self.convert_values(context, type_name, all_field_names, field, payload[field], datatable_flag)

            else:
                new_value = payload[field]
                if field in all_field_names:
                    if all_field_names[field]['input_type'] in ('select', 'multiselect', 'select_owner', 'multiselect_members') \
                        and all_field_names[field].get('prefix', prefix) == prefix:
                        new_value = self.convert_selects(field_key, payload[field], all_field_names[field])

            if is_incident(type_name) and not self.filters.filter_payload_value(field_key, new_value):
                msg = "Filter fail on {}:{}".format(field_key, new_value)
                raise FilterError(msg)

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

    def clean_payload(self, type_name, payload):
        """
        remove fields which will be problematic if passed on
        :param type_name: type of object
        :param payload:
        :return: cleaned payload
        """
        orig_org_id = payload.get('org_id', None)
        orig_id = payload.pop('id', None)

        # incident
        payload.pop('org', None)
        payload.pop('org_name', None)
        payload.pop('workspace', None)

        # Task
        payload.pop('reng_version', None)
        payload.pop('instr_text', None) # legacy field
        payload.pop('at_id', None)
        if isinstance(payload.get('phase_id', None), dict):
            payload['phase_id'].pop('id', None)
        if isinstance(payload.get('category_id', None), dict):
            payload['category_id'].pop('id', None)

        if is_incident(type_name):
            payload = clean_incident_fields(self.filter_fields, payload)

            if self.sync_references:
                payload['properties'][DF_ORG_ID] = orig_org_id
                payload['properties'][DF_INC_ID] = orig_id

        return orig_id, payload


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

# S T A T I C
def is_incident(type_name):
    return type_name == "incident"

def clean_incident_fields(filter_fields, payload):
    """
    exclude incident fields from an incident
    :param filter_fields - list of fields to exclude
    :param payload:
    :return: updated payload
    """
    new_payload = {}

    for field in payload.keys():
        if field not in filter_fields:
            if isinstance(payload[field], dict):
                new_payload[field] = clean_incident_fields(filter_fields, payload[field])
            else:
                new_payload[field] = payload[field]

    return new_payload


class FilterError(Exception):
    """
    Class used to signal Filter Error. It doesn't add any specific information other than
    identifying the type of error
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)