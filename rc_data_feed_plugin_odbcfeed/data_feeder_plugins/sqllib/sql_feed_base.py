# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Module contains SqlFeedDestinationBase, the base class for all SQL feed destinations."""
import abc
import logging

from cachetools import cached, LRUCache
from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo
from .sql_dialect import PostgreSQL96Dialect, SqliteDialect, MySqlDialect, SqlServerDialect, OracleDialect

LOG = logging.getLogger(__name__)
PYODBC_CONNECTION_LOST = ('08S01', '08003', 'HY000') # 08S01 = connection lost, 08003 = Connection not open, HY000 - catch all error

class SqlFeedDestinationBase(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """
    The base class for all SQL feed destinations.  This class handles as much of the work
    as possible, leaving only DB or DB library specific elements to subclasses.
    """

    AVAILABLE_DIALECTS = {
        "PostgreSQL96Dialect": PostgreSQL96Dialect,
        "SqliteDialect": SqliteDialect,
        "MariaDBDialect": MySqlDialect,
        "MySQLDialect": MySqlDialect,
        "SQLServerDialect": SqlServerDialect,
        "OracleDialect": OracleDialect
    }

    def __init__(self, rest_client_helper, options, dialect=None):
        super(SqlFeedDestinationBase, self).__init__()

        self.rest_client_helper = rest_client_helper

        if dialect:
            self.dialect = dialect
        else:
            dialect_name = options.get("sql_dialect")

            if dialect_name is None or SqlFeedDestinationBase.AVAILABLE_DIALECTS.get(dialect_name) is None:
                raise ValueError("sql_dialect is incorrect: {}".format(dialect_name))

            self.dialect = SqlFeedDestinationBase.AVAILABLE_DIALECTS[dialect_name]()

        self.created_tables = {}
        self.sqlparams_helper = self.dialect.get_sqlparams_helper()

    def _init_tables(self):
        if self.rest_client_helper:
            types_map = self.rest_client_helper.get('/types')

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

    @abc.abstractmethod
    def _reinit(self, connect_str, uid, pwd, dialect=None):
        raise NotImplementedError

    def cache_key(self, type_name, all_fields):
        # serialize the fields so that we can create a hash key
        # new fields in an object will produce a new hash key which will trigger the new field to be
        #   added to the db table schema
        field_list = [item['name'] for item in all_fields]
        field_list.append(type_name)
        field_list.append(id(self)) # needed to make multiple instances of this plugin unique for the cache

        hash_key = abs(hash(frozenset(field_list)))
        LOG.debug("hash_key (%s): %s", type_name, hash_key)
        return hash_key

    @cached(cache=LRUCache(100), key=cache_key)
    def _create_or_update_table(self, type_name, all_fields):

        for retry in range(2):
            try:
                cursor = self._start_transaction()
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

                    self.created_tables[type_name] = column_spec.copy()

                for field in all_fields:
                    field_name = field['name']
                    field_type = field['input_type']

                    # Add the column for the field if it hasn't been already.
                    #
                    if field_name not in self.created_tables[type_name].keys():
                        self._add_field_to_table(cursor, type_name, field)

                        # remember that we've added the field.
                        self.created_tables[type_name][field_name] = field['input_type']
                    elif field_name != 'id' and field_type != self.created_tables[type_name][field_name]:
                        LOG.warning("Field %s.%s type was %s. Will be altered to %s",
                                    type_name, field_name, self.created_tables[type_name][field_name], field_type)

                self._commit_transaction(cursor)
                break
            except Exception as err:
                LOG.error("_create_or_update_table exception: %s", err)
                if err.args and err.args[0] in PYODBC_CONNECTION_LOST:
                    LOG.warning("ODBC Connection lost, reestablishing connection")
                    # try reestablishing the connection
                    self.connection = self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)
                else:
                    try:
                        if cursor:
                            self._rollback_transaction(cursor)
                        raise err
                    except Exception:
                        pass # nosec


    def _add_field_to_table(self, cursor, type_name, field):
        input_type = field['input_type']
        field_name = field['name']

        LOG.info("adding field to table; type=%s; field=%s; type=%s", type_name, field_name, input_type)

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
                LOG.error(ddl)
                raise db_exception

    def send_data(self, context, payload):
        # We'll use the type's name as the table name.
        #

        # Create a flattened map where each key of the map is the field name.
        #
        flat_payload = context.type_info.flatten(payload,
                                               translate_func=getattr(self.dialect,
                                                                      'mapped_translate_value',
                                                                      TypeInfo.translate_value))
        table_name = context.type_info.get_pretty_type_name()

        all_fields = context.type_info.get_all_fields(refresh=False)

        self._create_or_update_table(table_name, all_fields)

        all_field_names = [field['name'] for field in all_fields]

        # some data types, such as datetime, will need a conversion routine
        all_field_types = dict()
        for field in all_fields:
            all_field_types[field['name']] = field['input_type']

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
        if 'inc_id' not in all_field_names:
            all_field_names.append('inc_id')

        flat_payload['inc_id'] = context.inc_id

        for retry in range(2):
            try:
                cursor = self._start_transaction()
                if context.is_deleted:
                    LOG.info("Deleting %s; id = %d", table_name, flat_payload['id'])

                    sql = self.dialect.get_delete(table_name)
                    params = {'id': flat_payload['id']}
                    if self.sqlparams_helper:
                        sql, params = self.sqlparams_helper.format(sql, params)
                    LOG.debug("{}:{}".format(sql, params))
                    self._execute_sql(
                        cursor,
                        sql,
                        params
                    )
                else:
                    LOG.info("Inserting/updating %s; id = %d [%s]",
                             table_name, flat_payload['id'], type(self.dialect).__name__)

                    # reduce data of attachments which are empty
                    non_null_payload = {}
                    for key, value in flat_payload.items():
                        if all_field_types.get(key) == 'blob':
                            if value is not None:
                                non_null_payload[key] = value
                        else:
                            non_null_payload[key] = value

                    sorted_keys = sorted(list(set(non_null_payload.keys()) & set(all_field_names)))

                    upsert_stmt = self.dialect.get_upsert(table_name, sorted_keys, all_field_types)
                    upsert_params = self.dialect.get_parameters(sorted_keys, non_null_payload)

                    self._execute_sql(
                        cursor,
                        upsert_stmt,
                        upsert_params)

                self._commit_transaction(cursor)
                break
            except Exception as err:
                LOG.error("send_data exception: %s", err)
                LOG.debug (flat_payload)
                'non_null_payload' in locals() and LOG.debug(non_null_payload)
                'upsert_stmt' in locals() and LOG.debug(upsert_stmt)
                'upsert_params' in locals() and LOG.debug(upsert_params)

                if err.args and err.args[0] in PYODBC_CONNECTION_LOST:
                    LOG.warning("ODBC Connection lost, reestablishing connection")
                    # try reestablishing the connection
                    self.connection = self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)
                else:
                    try:
                        if cursor:
                            self._rollback_transaction(cursor)
                        raise err
                    except Exception:
                        pass # nosec
