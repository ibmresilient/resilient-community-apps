# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""This module contains code for processing Resilient types and fields."""
import abc
import json
import logging
import pytz
from cachetools import cached, TTLCache
from datetime import datetime

LOG = logging.getLogger(__name__)


class TypeInfo(object):
    """
    Base TypeInfo class.  There are two situations where type info is made
    available from the Resilient server.  The first situation is an action
    module message.  The message will contain a condensed amount of data...for
    example it will only contain field value ID/name mapping for values that
    are actually included in the message.

    The second situation where type information is provided by a Resilient server
    is via it's 'types' endpoint.  In that case, we get the data in a different
    format.

    We provide subclasses for both situations.  This base class contains some
    common code.
    """
    fields_cache = {}

    builtin_types = {
        0: "incident",
        1: "task",
        2: "note",
        3: "milestone",
        4: "artifact",
        5: "attachment",
        13: "__emailmessage"
    }

    types_cache = {}

    # preserve the org_name
    org_name_cache = None

    DATATABLE_TYPE_ID = 8

    SELECT_INPUT_TYPES = ["select_owner", "select_user", "select"]
    MULTISELECT_INPUT_TYPES = ["multiselect", "multiselect_members"]
    ALL_SELECT_INPUT_TYPES = SELECT_INPUT_TYPES + MULTISELECT_INPUT_TYPES

    # fields not defined in the schema for an Incident but should be recorded in the datastore
    INCIDENT_INCLUDE_FIELDS = [
        (None, "org_id", "number"),
        (None, "org_name", "text"),
        ("hipaa", "hipaa_acquired_comment", "text"),
        ("hipaa", "hipaa_additional_misuse_comment", "text"),
        ("hipaa", "hipaa_additional_misuse", "boolean"),
        ("hipaa", "hipaa_adverse_comment", "text"),
        ("hipaa", "hipaa_breach_comment", "text"),
        ("hipaa", "hipaa_breach", "boolean"),
        ("hipaa", "hipaa_adverse", "boolean"),
        ("hipaa", "hipaa_acquired", "boolean"),
        ("hipaa", "hipaa_misused_comment", "text"),
        ("hipaa", "hipaa_misused", "boolean")
    ]

    # fields not defined in the schemas for a Note and Attachment but should be recorded in the datastore
    NOTE_ATTACHMENT_INCLUDE_FIELDS = [
        (None, "task_id", "number")
    ]
    # adding content field for attachments
    CONTENT_ATTACHMENT_INCLUDE_FIELDS = [
        (None, "content", "blob")
    ]


    def __init__(self, type_id, rest_client_helper):
        self.type_id = type_id
        self.rest_client_helper = rest_client_helper

    @abc.abstractmethod
    def get_field_names(self):
        """
        Gets the field names applicable for this context.

        :returns A list of field names.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_select_value(self, raw_value, field):
        """
        Gets the select field value for the specified raw_value.

        :param raw_value: The ID value for the selected item.
        :param field: The FieldDefDTO for the select field.

        :returns The string/label value that corresponds to the specified raw_value.
        """
        raise NotImplementedError

    def get_pretty_type_name(self):
        """
        Gets the 'pretty' type name.  Basically, the type name without any
        preceding underscore characters.
        """
        return self.get_type_name(self.type_id, pretty=True)

    def get_all_fields(self, refresh):
        """
        Gets the FieldDTO objects for the current context.  Note that this
        relies on self.type_id to know what the type is.  Only fields for that type
        are returned.

        :param refresh True to force all the fields to be reloaded from the server;
            False to just use the cached value (if there is a cached value).
        """
        if not refresh and self.type_id in TypeInfo.fields_cache:
            return TypeInfo.fields_cache[self.type_id]

        fields = self.rest_client_helper.get("/types/{}/fields".format(self.type_id))

        # some fields for an incident are not part of the /types/0/fields api call, so add them
        if self.type_id == 0:
            fields = self.add_schema_fields(fields, TypeInfo.INCIDENT_INCLUDE_FIELDS)
        if self.type_id in (2, 5):  # notes and attachments can be part of a task
            fields = self.add_schema_fields(fields, TypeInfo.NOTE_ATTACHMENT_INCLUDE_FIELDS)
        if self.type_id in (4, 5): # artifact and attachment
            fields = self.add_schema_fields(fields, TypeInfo.CONTENT_ATTACHMENT_INCLUDE_FIELDS)

        TypeInfo.fields_cache[self.type_id] = fields

        return fields


    def add_schema_fields(self, fields, new_fields):
        """
        add fields which are not included in the types schema
        :param fields:
        :return: new fields array
        """
        all_field_names = [field["name"] for field in fields]

        field_id = 10000     # our start of Ids
        for prefix, field_name, field_type in new_fields:
            # don't repeat fields if already included
            if field_name not in all_field_names:
                field_id += 1
                fields.append(self.make_field(0, field_id, prefix, field_name, field_type))

        return fields


    def make_field(self, type_id, field_id, prefix, field_name, field_type):
        """
        Make a field object with key fields for adding to datastore
        :param type_id:
        :param field_id:
        :param prefix
        :param field_name:
        :param field_type:
        :return: field object
        """
        field = {
            "type_id": type_id,
            "id": field_id,
            "name": field_name,
            "text": field_name,
            "prefix": prefix,
            "input_type": field_type,
            "internal": True
        }

        return field

    def is_data_table(self):
        """Determines if self.type_id is a datatable."""
        type_dto = self.get_type(self.type_id)

        return type_dto['type_id'] == TypeInfo.DATATABLE_TYPE_ID

    def flatten(self, payload, translate_func=None):
        """
        Gets a simplified version of the payload.  Any select/multiselect field
        values will have their ID values replaced with the string labels.  There will
        be only one level in the returned dict.

        :param payload: The object from the Resilient API.  We assume that select values
        are ID values.
        :param translate_func: A function/lambda to do additional conversion.

        :returns A dict that contains each of the fields on a single level of the
        dict.  The key is the field name (without prefix).  The value is the
        translated value.
        """

        # Make sure we have fields for everything referenced in the message.  First,
        # get all of the fields from the types endpoint.  Note that this is cached
        # and we don't specify for it to be refreshed.
        #
        all_fields = self.get_all_fields(refresh=False)

        # We need just the names for a comparison.
        #
        all_field_names = [field['name'] for field in all_fields]

        # Get all the fields that are included in the message.
        #
        message_field_names = self.get_field_names()

        # Make sure that we have all of the fields.  If we don't then something must have
        # been added and we'll refresh our list of fields.
        #
        if not set(message_field_names).issubset(set(all_field_names)):
            all_fields = self.get_all_fields(refresh=True)

        try:
            values = self._get_field_values(payload, all_fields, translate_func, bypass_error=False)
        except ValueError:
            # this will trigger when a field ID is not found
            all_fields = self.get_all_fields(refresh=True)
            values = self._get_field_values(payload, all_fields, translate_func, bypass_error=True)

        return values

    def _get_field_values(self, payload, all_fields, translate_func, bypass_error=False):
        """[convert object values based on a supplied conversion method]

        Args:
            payload ([dict]): [data to convert]
            all_fields ([dict]): [schema of object]
            translate_func ([object]): [method to convert the data based on it's type (int, text, date, etc.)]
            bypass_error (bool, optional): [bypass conversion errors]. Defaults to False.

        Returns:
            [dict]: [converted fields]
        """
        values = {}

        if self.is_data_table():
            # Data table metadata doesn't include an "id" field, but we're going to
            # need it...so pass it on to the caller in a magic 'id' field.
            #
            values['id'] = payload['id']

        for field in all_fields:
            try:
                raw_value = self._get_raw_value_for_field(payload, field)

                if translate_func:
                    value = translate_func(self, field, raw_value)
                else:
                    value = raw_value

                values[field["name"]] = value
            except ValueError:
                if bypass_error:
                    continue # this field will be skipped

                raise

        return values

    @staticmethod
    def pretify_type_name(type_name):
        """
        Makes a pretty version of the type.  Basically, just strips out any
        underscore prefix characters.

        :returns The pretty type name.
        """
        if type_name.startswith('__'):
            return type_name.lstrip('_')
        return type_name

    def get_type(self, type_id):
        """Gets the TypeDTO for the specified type_id.

        :param type_id: The type ID of interest.
        :returns The TypeDTO for the specified type_id."""

        # Need to get the type.
        if type_id in TypeInfo.types_cache:
            type_dto = TypeInfo.types_cache[type_id]
        else:
            type_dto = self.rest_client_helper.get("/types/{}".format(type_id))
            TypeInfo.types_cache[type_id] = type_dto

        return type_dto

    def get_org_name(self, org_id):
        """
        get the org_name from the org_id for the incident. Value will be cached
        :param org_id:
        :return: org_name
        """
        if not self.org_name_cache:
            org_info = self.rest_client_helper.get("")
            self.org_name_cache = org_info["org_info"]["name"]

        return self.org_name_cache

    def get_incident_workspace(self, inc_id):
        """[get an incident workspace label]

        Args:
            inc_id ([int]):

        Returns:
            [str]: [workspace label]
        """
        incident = get_incident(self.rest_client_helper, inc_id)
        if incident:
            return self.get_workspace_from_id(incident['workspace'])

        return None

    def get_workspace_from_id(self, workspace_id):
        """ get an incident workspace label from the workspace id """

        incident_type = self.get_type(0) # incident
        for workspace_value in incident_type['fields']['workspace']['values']:
            if workspace_value['default']:
                default_workspace = workspace_value['label']
            if workspace_id == workspace_value['value']:
                return workspace_value['label']

        return default_workspace

    def get_type_name(self, type_id, pretty=True):
        """
        Gets the type name for the specified type_id value.

        :param type_id: The type ID of interest.  This can actually be either an int
        (the internal type ID value) or a str (the name of the type).
        :param pretty: True if you want the pretty name; False otherwise.

        :returns A str containing the type name.
        """
        type_str = None

        if isinstance(type_id, int):
            if type_id in TypeInfo.builtin_types:
                type_str = TypeInfo.builtin_types[type_id]
            else:
                # Need to get the type from the server so we can get the name.
                type_dto = self.get_type(type_id)

                type_str = type_dto['type_name']

        elif isinstance(type_id, str):
            # type is specified by name.  some of the internal ones have __ as a
            # prefix and we don't want that.
            type_str = type_id

        if type_str is None:
            msg = "Unable to find type name from object type of {} ({})".format(type_id,
                                                                               type(type_id))
            raise LookupError(msg)

        if pretty:
            type_str = TypeInfo.pretify_type_name(type_str)

        return type_str

    def _get_raw_value_for_field(self, payload, field):
        """
        this function will raise ValueError if a schema field is not found in the payload. This is used to trap changes in the
        schema not reflected in the cached schema
        :param payload:
        :param field:
        :return: payload object found
        """
        obj = None
        if self.is_data_table():
            field_id = str(field['id'])

            if payload['cells'].get(field_id):
                obj = payload['cells'][field_id].get('value', None) # 'value' is not always present for datatables
            else:
                LOG.warning("field_id no longer exists: %s", field_id)
                LOG.debug(payload)
                raise ValueError()

        else:
            prefix = field.get('prefix')

            type_name = self.get_type_name(field['type_id'], pretty=False)

            if prefix is None and type_name == 'incident' and not field['internal']:
                # This is lame and required only because the server isn't setting the
                # prefix for custom fields.
                #
                prefix = "properties"

            obj = payload

            if prefix is not None:
                obj = payload.get(prefix)

            if obj is not None and isinstance(obj, dict):
                obj = obj.get(field['name'])

        return obj

    @staticmethod
    def translate_value_select(type_info, field, value):
        return type_info.get_select_value(value, field)

    @staticmethod
    def translate_value_multiselect(type_info, field, value):
        return [type_info.get_select_value(v, field) for v in value]

    @staticmethod
    def translate_value_datetimepicker(type_info, field, value):
        # Server returns date as milliseconds since epoch (1/1/1970), but Python
        # wants it as seconds.  Then, convert to an ISO formatted string
        # representation.
        #
        d = datetime.utcfromtimestamp(value/1000)
        if field['input_type'] == 'datetimepicker':
            d = pytz.timezone('UTC').localize(d)

        return d.isoformat()

    @staticmethod
    def translate_value_list(type_info, field, value):
        # For now, squash lists into a joined string.  May need to actually
        # return the list if the callers are going to need to do something
        # else with it (like write data to a join table).
        #
        try:
            value = u', '.join(value)
        except:
            value = json.dumps(value)

        return value

    @staticmethod
    def translate_value_textarea(type_info, field, value):
        if isinstance(value, dict):
            return value['content']

        return value

    @staticmethod
    def translate_value_number(type_info, field, value):
        if isinstance(value, dict):
            return value['id']

        return value

    @staticmethod
    def translate_value_blob(type_info, field, value):
        return value

    @staticmethod
    def translate_nested_collection(type_info, field, value):
        if isinstance(value, dict):
            return value.get("name", None)

        return value

    @staticmethod
    def no_translate(type_info, field, value):
        return value

    @staticmethod
    def get_default_mapping():
        return {
            "select_owner": TypeInfo.translate_value_select,
            "select_user": TypeInfo.translate_value_select,
            "select": TypeInfo.translate_value_select,
            "multiselect": TypeInfo.translate_value_multiselect,
            "multiselect_members": TypeInfo.translate_value_multiselect,
            "multiselect_tagref": TypeInfo.translate_value_list,
            "nested_collection": TypeInfo.translate_nested_collection,
            "datepicker": TypeInfo.translate_value_datetimepicker,
            "datetimepicker": TypeInfo.translate_value_datetimepicker,
            "textarea": TypeInfo.translate_value_textarea,
            "number": TypeInfo.translate_value_number,
            "blob": TypeInfo.translate_value_blob,
            "list": TypeInfo.translate_value_list,
            "text": TypeInfo.no_translate,
            "boolean": TypeInfo.no_translate
        }

    @staticmethod
    def translate_value(type_info, field, value):
        mapping = TypeInfo.get_default_mapping()

        if value is not None:
            input_type = field['input_type']
            if input_type in mapping:
                rule_function = mapping[input_type]
                value = rule_function(type_info, field, value)

            if isinstance(value, list):
                value = mapping["list"](type_info, field, value)

        return value


class ActionMessageTypeInfo(TypeInfo):
    """
    A TypeInfo implementation for cases where we're going to read the type information from
    an action module (queue) message.
    """
    def __init__(self, type_id, type_info_map, rest_client_helper):
        """
        Creates a new object.

        :param type_id: The ID of the type that we're going to be maintaining type info for.
        :param type_info_map: The type information from the action module message (note that
        this is indexed by type name).
        """
        super(ActionMessageTypeInfo, self).__init__(type_id, rest_client_helper)

        self.type_info_map = type_info_map

    def get_select_value(self, raw_value, field):
        if isinstance(raw_value, dict):
            # Handle case where the select item is an object (we want to index into the field def
            # values by field value ID).
            raw_value = raw_value['id']

        type_name = self.get_type_name(self.type_id, pretty=False)

        if type_name not in self.type_info_map:
            LOG.warning(u"%s not found in %s. Returning raw_value: %s", type_name, self.type_info_map, raw_value)
            return raw_value

        field_name = field['name']

        fields = self.type_info_map[type_name]['fields']

        values_map = fields[field_name]['values']

        return self._find_select_value(raw_value, values_map)

    def get_field_names(self):
        type_name = self.get_type_name(self.type_id, pretty=False)

        return list(self.type_info_map[type_name]['fields'].keys())

    @staticmethod
    def _find_select_value(raw_value, values_map):
        """
        Finds the value in the values map (that came from the action module message's
        type data).
        """
        if not isinstance(raw_value, str):
            # Map keys must be strings for JSON data.
            raw_value = str(raw_value)

        if raw_value not in values_map:
            # Must be a NUMBER field.
            LOG.warning(u"%s not found in %s. Returning raw_value", raw_value, values_map)
            return raw_value

        # if the entry isn't in the values dict then we're really confused (and this
        # will and should raise an exception)
        #
        value_obj = values_map[raw_value]

        return value_obj['label']


class FullTypeInfo(TypeInfo):
    """
    A TypeInfo object for situations where we need to load the type information
    from the REST API's GET /rest/orgs/:orgId/types endpoint.
    """
    def __init__(self, type_id, rest_client_helper, refresh, all_fields=None):
        """
        Constructs a new FullTypeInfo object.

        :param type_id: The type ID of interest.
        :param rest_client_helper: The Resilient SimpleClient object wrapper.
        :param refresh: True to force the field data to be refreshed; False
        to allow any cached field data to be retrieved.
        :param all_fields: If you already have the field data loaded, you can pass
        it in here.  This is expected to be a list of FieldDefDTO objects/dicts.
        """
        super(FullTypeInfo, self).__init__(type_id, rest_client_helper)

        if not all_fields:
            all_fields = self.get_all_fields(refresh)

        self.fields_map = {}

        for field in all_fields:
            field_name = field['name']

            self.fields_map[field_name] = field

    def get_field_names(self):
        # Just return all of the field names here.
        return list(self.fields_map.keys())

    def get_select_value(self, raw_value, field):
        if isinstance(raw_value, dict):
            raw_value = raw_value['id']

        field_name = field['name']

        value_dtos = self.fields_map[field_name]['values']

        try:
            value_dto = next(value for value in value_dtos if value['value'] == raw_value)
            return value_dto['label']
        except StopIteration:
            return None

# cache of incidents based on incident_id
@cached(cache=TTLCache(maxsize=1000, ttl=60), key=lambda rest_client_helper, inc_id: str(inc_id))
def get_incident(rest_client_helper, inc_id):
    """ get an incident based on it's id. Results are cached """
    return rest_client_helper.get("/incidents/{}".format(inc_id))
