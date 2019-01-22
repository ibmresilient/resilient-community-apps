"""Module contains SqlFeedDestinationBase, the base class for all SQL feed destinations."""

import logging
import json
import abc

from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo
from rc_data_feed.lib.sql_dialect import PostgreSQL96Dialect, SqliteDialect

LOG = logging.getLogger(__name__)


class SqlFeedDestinationBase(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """
    The base class for all SQL feed destinations.  This class handles as much of the work
    as possible, leaving only DB or DB library specific elements to subclasses.
    """

    AVAILABLE_DIALECTS = {
        "PostgreSQL96Dialect": PostgreSQL96Dialect,
        "SqliteDialect": SqliteDialect
    }

    def __init__(self, rest_client, options, dialect=None):
        super(SqlFeedDestinationBase, self).__init__()

        self.rest_client = rest_client

        if dialect:
            self.dialect = dialect
        else:
            dialect_name = options.get("sql_dialect")

            self.dialect = SqlFeedDestinationBase.AVAILABLE_DIALECTS[dialect_name]()

        self.created_tables = {}

    def _init_tables(self):
        types_map = self.rest_client.get('/types')

        for (type_name, type_dto) in list(types_map.items()):
            pretty_type_name = TypeInfo.pretify_type_name(type_name)

            parent_types = type_dto['parent_types']

            # Only create tables for the types that have incident or task as a parent
            # (or incident itself).
            if type_name == 'incident' or 'incident' in parent_types or 'task' in parent_types:
                all_fields = list(type_dto['fields'].values())

                self._create_or_update_table(pretty_type_name, all_fields)

    @abc.abstractmethod
    def _start_transaction(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _commit_transaction(self, context):
        raise NotImplementedError

    @abc.abstractmethod
    def _rollback_transaction(self, context):
        raise NotImplementedError

    @abc.abstractmethod
    def _execute_sql(self, cursor, sql, data=None):
        raise NotImplementedError

    def _create_or_update_table(self, type_name, all_fields):
        cursor = self._start_transaction()

        try:
            # id and inc_id are special fields.  We always add them.  Then we look at the
            # fields to add all the other fields.
            #
            if type_name not in self.created_tables:
                column_spec = {
                    "id": "integer primary key",
                    "inc_id": "integer"
                }

                ddl = self.dialect.get_create_table_if_not_exists(type_name, column_spec)

                self._execute_sql(cursor, ddl)

                self.created_tables[type_name] = list(column_spec.keys())

            for field in all_fields:
                field_name = field['name']

                # Add the column for the field if it hasn't been already.
                #
                if field_name not in self.created_tables[type_name]:
                    self._add_field_to_table(cursor, type_name, field)

                    # remember that we've added the field.
                    self.created_tables[type_name].append(field_name)

            self._commit_transaction(cursor)
        except Exception as db_exception:
            self._rollback_transaction(cursor)

            raise db_exception

    def _add_field_to_table(self, cursor, type_name, field):
        input_type = field['input_type']
        field_name = field['name']

        LOG.debug("adding field to table; type=%s; field=%s; type=%s", type_name, field_name, input_type)

        try:
            column_type = self.dialect.get_column_type(input_type)

            ddl = self.dialect.get_add_column_to_table(type_name,
                                                       field_name,
                                                       column_type)

            self._execute_sql(cursor, ddl)
        except Exception as db_exception:   # pylint: disable=broad-except
            # Disabled pylint's broad-except because we specifically want
            # to catch all exceptions and let the dialect determine if
            # it's one we want to bypass.
            #
            if not self.dialect.is_column_exists_exception(db_exception):
                raise db_exception

    def send_data(self, context, payload):
        # Create a flattened map where each key of the map is the field name.
        #
        flat_payload = context.type_info.flatten(payload, translate_func=TypeInfo.translate_value)

        # We'll use the type's name as the table name.
        #
        table_name = context.type_info.get_pretty_type_name()

        all_fields = context.type_info.get_all_fields(refresh=False)

        self._create_or_update_table(table_name, all_fields)

        all_field_names = [field['name'] for field in all_fields]

        if 'id' not in all_field_names:
            # id is not an explicit field - this happens for data tables.  Make sure it exists.
            #
            all_field_names.append('id')

            # Assuming all passed in payload data has an 'id' field here.  This is currently
            # the case for everything.
            #
            flat_payload['id'] = payload['id']

        # Always ensure a special inc_id field exists.  Note that in some cases
        # this may be set to None (e.g. for email message objects that are not
        # associated with any specific incident ID.
        #
        all_field_names.append('inc_id')

        flat_payload['inc_id'] = context.inc_id

        cursor = self._start_transaction()

        try:
            if context.is_deleted:
                LOG.debug("Deleting %s; id = %d", table_name, flat_payload['id'])

                self._execute_sql(
                    cursor,
                    self.dialect.get_delete(table_name),
                    [id]
                )
            else:
                LOG.debug("Inserting/updating %s; id = %d", table_name, flat_payload['id'])

                self._execute_sql(
                    cursor,
                    self.dialect.get_upsert(table_name, all_field_names),
                    self.dialect.get_parameters(all_field_names, flat_payload))

            self._commit_transaction(cursor)
        except Exception as db_exception:
            self._rollback_transaction(cursor)

            raise db_exception
