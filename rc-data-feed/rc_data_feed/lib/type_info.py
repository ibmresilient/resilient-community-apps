
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class TypeInfo(object):
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

    SELECT_INPUT_TYPES = ["select_owner", "select"]
    MULTISELECT_INPUT_TYPES = ["multiselect", "multiselect_members"]
    ALL_SELECT_INPUT_TYPES = SELECT_INPUT_TYPES + MULTISELECT_INPUT_TYPES

    def __init__(self, type_id, rest_client):
        self.type_id = type_id
        self.rest_client = rest_client

    def get_message_field_names(self):
        return []

    def get_select_value(self, raw_value, field):
        return None

    def get_pretty_type_name(self):
        return self.get_type_name(self.type_id, for_dto=True)

    def get_all_fields(self, refresh):
        if not refresh and self.type_id in TypeInfo.fields_cache:
            return TypeInfo.fields_cache[self.type_id]

        fields = self.rest_client.get("/types/{}/fields".format(self.type_id))

        SimpleTypeInfo.fields_cache[self.type_id] = fields

        return fields

    def is_data_table(self):
        type_dto = self.get_type(self.type_id)

        return type_dto['type_id'] == TypeInfo.DATATABLE_TYPE_ID

    def flatten(self, payload, translate_func=None):
        # Make sure we have fields for everything referenced in the message.  First, get all of the fields
        # from the types endpoint.  Note that this is cached and we don't specify for it to be refreshed.
        #
        all_fields = self.get_all_fields(refresh=False)

        # We need just the names for a comparison.
        #
        all_field_names = [field['name'] for field in all_fields]

        # Get all the fields that are included in the message.
        #
        message_field_names = self.get_message_field_names()

        # Make sure that we have all of the fields.  If we don't then something must have been added and we'll
        # refresh our list of fields.
        #
        if not set(message_field_names).issubset(set(all_field_names)):
            all_fields = self.get_all_fields(refresh=True)

        values = {}

        if self.is_data_table():
            # Data table metadata doesn't include an "id" field, but we're going to need it...so pass it on
            # to the caller in a magic 'id' field.
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
        if type_name.startswith('__'):
            return type_name.lstrip('_')
        return type_name

    def get_type(self, type_id):
        # Need to get the type.
        if type_id in TypeInfo.types_cache:
            type_dto = TypeInfo.types_cache[type_id]
        else:
            type_dto = self.rest_client.get("/types/{}".format(type_id))
            TypeInfo.types_cache[type_id] = type_dto

        return type_dto

    def get_type_name(self, type_id, for_dto=True):
        type_str = None

        if isinstance(type_id, int):
            if type_id in TypeInfo.builtin_types:
                type_str = TypeInfo.builtin_types[type_id]
            else:
                # Need to get the type from the server so we can get the name.
                type_dto = self.get_type(type_id)

                type_str = type_dto['type_name']

        elif isinstance(type_id, str):
            # type is specified by name.  some of the internal ones have __ as a prefix and we don't want that.
            type_str = type_id

        if type_str is None:
            raise LookupError("Unable to find type name from object type of {} ({})".format(type_id, type(type_id)))

        if for_dto:
            type_str = TypeInfo.pretify_type_name(type_str)

        return type_str

    def _get_raw_value_for_field(self, payload, field):
        if self.is_data_table():
            field_id = field['id']

            obj = payload['cells'][str(field_id)]['value']
        else:
            prefix = field.get('prefix')

            type_name = self.get_type_name(field['type_id'], for_dto=False)

            if prefix is None and type_name is 'incident' and not field['internal']:
                # This is lame and required only because the server isn't setting the prefix for custom fields.
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
                # Server returns date as milliseconds since epoch (1/1/1970), but Python wants it as seconds.
                # Then, convert to an ISO formatted string representation.
                value = datetime.utcfromtimestamp(value/1000).isoformat()

            if isinstance(value, list):
                # For now, squash lists into a joined string.  May need to actually return the list if the
                # callers are going to need to do something else with it (like write data to a join table).
                value = ', '.join(value)

            if input_type == 'textarea' and isinstance(value, dict):
                value = value['content']

            if input_type == 'number' and isinstance(value, dict):
                # TODO This is working around a server issue where the server specifies a 'number' type
                # TODO for a field that is really a select list.
                #
                value = value['id']

        return value


class SimpleTypeInfo(TypeInfo):
    def __init__(self, type_id, type_info_map, rest_client):
        super(SimpleTypeInfo, self).__init__(type_id, rest_client)

        self.type_info_map = type_info_map

    def get_select_value(self, raw_value, field):
        if isinstance(raw_value, dict):
            # Handle case where the select item is an object (we want to index into the field def
            # values by field value ID).
            raw_value = raw_value['id']

        type_name = self.get_type_name(self.type_id, for_dto=False)

        if type_name not in self.type_info_map:
            return raw_value

        field_name = field['name']

        fields = self.type_info_map[type_name]['fields']

        values_map = fields[field_name]['values']

        return self._find_select_value(raw_value, values_map)

    def get_message_field_names(self):
        type_name = self.get_type_name(self.type_id, for_dto=False)

        return list(self.type_info_map[type_name]['fields'].keys())

    @staticmethod
    def _find_select_value(raw_value, values_map):
        if not isinstance(raw_value, str):
            # Map keys must be strings for JSON data.
            raw_value = str(raw_value)

        if raw_value not in values_map:
            # Must be a NUMBER field.
            return raw_value

        # if the entry isn't in the values dict then we're really confused (and this will and should raise an exception)
        value_obj = values_map[raw_value]

        return value_obj['label']


class FullTypeInfo(TypeInfo):
    def __init__(self, type_id, rest_client, refresh, all_fields=None):
        super(FullTypeInfo, self).__init__(type_id, rest_client)

        if not all_fields:
            all_fields = self.get_all_fields(refresh)

        self.fields_map = {}

        for field in all_fields:
            field_name = field['name']

            self.fields_map[field_name] = field

    def get_message_field_names(self):
        # Just return all of the field names here.
        return list(self.fields_map.keys())

    def get_select_value(self, raw_value, field):
        if isinstance(raw_value, dict):
            raw_value = raw_value['id']

        field_name = field['name']

        value_dtos = self.fields_map[field_name]['values']

        value_dto = next(value for value in value_dtos if value['value'] == raw_value)

        return value_dto['label']
