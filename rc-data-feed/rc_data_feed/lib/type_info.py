"""This module contains code for processing Resilient types and fields."""
import abc
import json
import logging
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

    DATATABLE_TYPE_ID = 8

    SELECT_INPUT_TYPES = ["select_owner", "select_user", "select"]
    MULTISELECT_INPUT_TYPES = ["multiselect", "multiselect_members"]
    ALL_SELECT_INPUT_TYPES = SELECT_INPUT_TYPES + MULTISELECT_INPUT_TYPES

    def __init__(self, type_id, rest_client):
        self.type_id = type_id
        self.rest_client = rest_client

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

        fields = self.rest_client.get("/types/{}/fields".format(self.type_id))

        TypeInfo.fields_cache[self.type_id] = fields

        return fields

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

        values = {}

        if self.is_data_table():
            # Data table metadata doesn't include an "id" field, but we're going to
            # need it...so pass it on to the caller in a magic 'id' field.
            #
            values['id'] = payload['id']

        for field in all_fields:
            raw_value = self._get_raw_value_for_field(payload, field)

            if translate_func:
                value = translate_func(self, field, raw_value)
            else:
                value = raw_value

            values[field["name"]] = value

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
            type_dto = self.rest_client.get("/types/{}".format(type_id))
            TypeInfo.types_cache[type_id] = type_dto

        return type_dto

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
        if self.is_data_table():
            field_id = field['id']

            obj = payload['cells'][str(field_id)].get('value', None) # 'value' is not always present for datatables
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

            if obj is not None:
                obj = obj.get(field['name'])

        return obj

    @staticmethod
    def translate_value(type_info, field, value):
        """Translates the value that we want in the 'flattened' output."""
        if value is not None:
            input_type = field['input_type']

            if input_type in TypeInfo.SELECT_INPUT_TYPES:
                value = type_info.get_select_value(value, field)
            elif input_type in TypeInfo.MULTISELECT_INPUT_TYPES:
                value = [type_info.get_select_value(v, field) for v in value]
            elif input_type in ['datetimepicker', 'datepicker']:
                # Server returns date as milliseconds since epoch (1/1/1970), but Python
                # wants it as seconds.  Then, convert to an ISO formatted string
                # representation.
                #
                value = datetime.utcfromtimestamp(value/1000).isoformat()

            if isinstance(value, list):
                # For now, squash lists into a joined string.  May need to actually
                # return the list if the callers are going to need to do something
                # else with it (like write data to a join table).
                #
                try:
                    value = ', '.join(value)
                except:
                    value = json.dumps(value)

            if input_type == 'textarea' and isinstance(value, dict):
                value = value['content']

            if input_type == 'number' and isinstance(value, dict):
                # TODO This is working around a server issue where the server specifies
                #  a 'number' type for a field that is really a select list.
                #
                value = value['id']

        return value


class ActionMessageTypeInfo(TypeInfo):
    """
    A TypeInfo implementation for cases where we're going to read the type information from
    an action module (queue) message.
    """
    def __init__(self, type_id, type_info_map, rest_client):
        """
        Creates a new object.

        :param type_id: The ID of the type that we're going to be maintaining type info for.
        :param type_info_map: The type information from the action module message (note that
        this is indexed by type name).
        """
        super(ActionMessageTypeInfo, self).__init__(type_id, rest_client)

        self.type_info_map = type_info_map

    def get_select_value(self, raw_value, field):
        if isinstance(raw_value, dict):
            # Handle case where the select item is an object (we want to index into the field def
            # values by field value ID).
            raw_value = raw_value['id']

        type_name = self.get_type_name(self.type_id, pretty=False)

        if type_name not in self.type_info_map:
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
    def __init__(self, type_id, rest_client, refresh, all_fields=None):
        """
        Constructs a new FullTypeInfo ojbect.

        :param type_id: The type ID of interest.
        :param rest_client: The Resilient SimpleClient object.
        :param refresh: True to force the field data to be refreshed; False
        to allow any cached field data to be retrieved.
        :param all_fields: If you already have the field data loaded, you can pass
        it in here.  This is expected to be a list of FieldDefDTO objects/dicts.
        """
        super(FullTypeInfo, self).__init__(type_id, rest_client)

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

        value_dto = next(value for value in value_dtos if value['value'] == raw_value)

        return value_dto['label']
