# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Module contains SqlFeedDestinationBase, the base class for all SQL feed destinations."""
import abc
import logging
import traceback

from retry import retry
from threading import Lock
from typing import Tuple
from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo
from .sql_dialect import PostgreSQL96Dialect, SqliteDialect, MySqlDialect, SqlServerDialect, OracleDialect

LOG = logging.getLogger(__name__)
# 08S01 = connection lost, 08003 = Connection not open, HY000 - catch all error
# 42703 - column not found. Maybe due to threads not having correct db schema
# 42P01 - table not found.
PYODBC_CONNECTION_LOST = ('08001', '08S01', '08003', 'HY000', '42703', '42P01', 'ORA-00054')

class RetrySendDataException(Exception):
    """Class used to signal a retry of an operation to ensure transactional completeness

    :param Exception:
    :type Exception:
    """

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

        self.exclude_fields = self._get_exclude_incident_fields(options)
        LOG.info("Excluding incident fields: %s", self.exclude_fields)

        self.sqlparams_helper = self.dialect.get_sqlparams_helper()

        # table column listing needed for multi-threaded lookup
        # This is needed to minimize the number of times the schema of db table is updated
        self.TABLE_SCHEMA_LOOKUP_LOCK = Lock()
        self.TABLE_SCHEMA_LOOKUP = {} # structure: { "<table_name>": {<column_name>:<input_type>} }

        # thread lock used to limit the number of simultaneous updates needed to database tables
        self.UPDATE_LOCK = Lock()
        self.UPDATE_TABLE_LOCK = {}

    def _get_exclude_incident_fields(self, options: dict) -> list:
        """read file of excluded fields for db column filtering

        :param options: app.config settings
        :type options: dict
        :return: excluded fields or [] when no file is specified
        :rtype: list
        """

        file_path = options.get("exclude_incident_fields_file")
        exclude_fields = []
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # remove any blank lines
                    exclude_fields = [line.strip() for line in f.read().splitlines() if line]
            except FileNotFoundError:
                LOG.error("Unable to read exclude_incident_fields_file: %s", file_path)

        return exclude_fields

    def _init_tables(self):
        if self.rest_client_helper:
            types_map = self.rest_client_helper.get('/types')

            for (type_name, type_dto) in list(types_map.items()):
                pretty_type_name = TypeInfo.pretify_type_name(type_name)

                parent_types = type_dto['parent_types']

                # Only create tables for the types that have task as a parent
                # incident table is not created as it requires the filtered list of fields
                if 'incident' in parent_types or 'task' in parent_types:
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
    def _close_transaction(self):
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

    def get_table_lock(self, table_name) -> Lock:
        """get a table specific lock for use when updating the table schema

        :param table_name: name of table
        :type table_name: str
        :return: lock for table updates
        :rtype: threading.Lock
        """
        with self.UPDATE_LOCK:
            if not self.UPDATE_TABLE_LOCK.get(table_name):
                self.UPDATE_TABLE_LOCK[table_name] = Lock()

            return self.UPDATE_TABLE_LOCK[table_name]

    def is_table_found(self, table_name: str) -> bool:
        return self.TABLE_SCHEMA_LOOKUP.get(table_name)

    def is_field_found(self, table_name: str, field_name: str, field_type) -> Tuple[bool, bool]:
        """determine if the field name already exist in the db table

        :param table_name: object name is identical to table name
        :type table_name: str
        :param field_name: field name in object
        :type field_name: str
        :return: <field found>, <field_type same> True if field already added to the db table
        :rtype: bool, bool
        """
        with self.TABLE_SCHEMA_LOOKUP_LOCK:
            if not self.TABLE_SCHEMA_LOOKUP.get(table_name):
                self.TABLE_SCHEMA_LOOKUP[table_name] = {field_name: field_type}
                return False, False   # not found

            field_found = (field_name in self.TABLE_SCHEMA_LOOKUP[table_name])

            field_type_same = (self.TABLE_SCHEMA_LOOKUP[table_name].get(field_name) == field_type)
            # always update
            self.TABLE_SCHEMA_LOOKUP[table_name][field_name] = field_type # add/update

            return field_found, field_type_same

    # may not be needed per is_field_found @cached(cache=LRUCache(100), key=cache_key)
    @retry(RetrySendDataException, tries=2, delay=5, backoff=3, logger=LOG)
    def _create_or_update_table(self, type_name, all_fields):

        # if locked, bypass any schema updates
        if not self.get_table_lock(type_name).locked():
            with self.get_table_lock(type_name):
                cursor = None
                try:
                    cursor = self._start_transaction()
                    # id and inc_id are special fields.  We always add them.  Then we look at the
                    # fields to add all the other fields.
                    #
                    if not self.is_table_found(type_name):
                        column_spec = {
                            "id": "integer primary key",
                            "inc_id": "integer"
                        }

                        ddl = self.dialect.get_create_table_if_not_exists(type_name, column_spec)

                        self._execute_sql(cursor, ddl)

                        # add in the initial columns
                        for k in column_spec:
                            self.is_field_found(type_name, k, 'number')

                    for field in all_fields:
                        field_name = field['name']
                        field_type = field['input_type']

                        # Add the column for the field if it hasn't been already.
                        #
                        field_found, field_type_same = self.is_field_found(type_name, field_name, field_type)
                        if not field_found or not field_type_same:
                            self._add_field_to_table(cursor, type_name, field)

                        elif field_name != 'id' and not field_type_same:
                            LOG.warning("Field %s.%s type changed. Will be altered to %s",
                                        type_name, field_name, field_type)

                    self._commit_transaction(cursor)
                except Exception as err:
                    LOG.error(traceback.format_exc())
                    LOG.error("_create_or_update_table exception: %s", err)
                    if err.args and err.args[0] in PYODBC_CONNECTION_LOST:
                        LOG.warning("ODBC Connection lost, reestablishing connection")
                        # try reestablishing the connection
                        self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)
                        cursor = None
                        # trigger a restart of this operation
                        raise RetrySendDataException

                    try:
                        if cursor:
                            self._rollback_transaction(cursor)
                    except Exception:
                        pass # nosec
                    finally:
                        self._close_transaction()  # this will remove the connection from the thread
                        cursor = None
                    # end with this error
                    raise err
                finally:
                    if cursor:
                        cursor.close()

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

    @retry(RetrySendDataException, tries=3, delay=5, backoff=3, logger=LOG)
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

        # exclude the incident fields indicated in app.config exclude file
        if table_name == 'incident':
            flat_payload_filtered = context.type_info.filter_incident_fields(flat_payload,
                                                                             self.exclude_fields)
        else:
            flat_payload_filtered = flat_payload

        all_fields = context.type_info.get_all_fields_for_timeseries(payload, refresh=False)

        # trim all_fields to the flat_payload_filtered list
        all_fields_filtered = [item for item in all_fields if item["name"] in flat_payload_filtered]

        self._create_or_update_table(table_name, all_fields_filtered)

        all_field_names = [field['name'] for field in all_fields_filtered]

        # some data types, such as datetime, will need a conversion routine
        all_field_types = {field['name']: field['input_type'] for field in all_fields_filtered}

        if 'id' not in all_field_names:
            # id is not an explicit field - this happens for data tables.  Make sure it exists.
            #
            all_field_names.append('id')

            # Assuming all passed in payload data has an 'id' field here.  This is currently
            # the case for everything.
            #
            flat_payload_filtered['id'] = payload['id']

        # Always ensure a special inc_id field exists.  Note that in some cases
        # this may be set to None (e.g. for email message objects that are not
        # associated with any specific incident ID.
        #
        if 'inc_id' not in all_field_names:
            all_field_names.append('inc_id')

        flat_payload_filtered['inc_id'] = context.inc_id

        cursor = None
        try:
            cursor = self._start_transaction()
            if context.is_deleted:
                LOG.info("Deleting %s; id = %d", table_name, flat_payload_filtered['id'])

                sql = self.dialect.get_delete(table_name)
                params = {'id': flat_payload_filtered['id']}
                if self.sqlparams_helper:
                    sql, params = self.sqlparams_helper.format(sql, params)
                LOG.debug("{}:{}".format(sql, params))
                self._execute_sql(cursor,
                                  sql,
                                  params)
            else:
                LOG.info("Inserting/updating %s; id = %d [%s]",
                            table_name, flat_payload_filtered['id'], type(self.dialect).__name__)

                # reduce data of attachments which are empty
                non_null_payload = {}
                for key, value in flat_payload_filtered.items():
                    if all_field_types.get(key) == 'blob':
                        if value is not None:
                            non_null_payload[key] = value
                    else:
                        non_null_payload[key] = value

                sorted_keys = sorted(list(set(non_null_payload.keys()) & set(all_field_names)))

                upsert_stmt = self.dialect.get_upsert(table_name, sorted_keys, all_field_types)
                upsert_params = self.dialect.get_parameters(sorted_keys, non_null_payload)

                self._execute_sql(cursor,
                                  upsert_stmt,
                                  upsert_params)

            self._commit_transaction(cursor)
        except Exception as err:
            LOG.error("send_data exception: %s", err)
            LOG.debug(flat_payload_filtered)
            'non_null_payload' in locals() and LOG.debug(non_null_payload)
            'upsert_stmt' in locals() and LOG.debug(upsert_stmt)
            'upsert_params' in locals() and LOG.debug(upsert_params)

            if err.args and err.args[0] in PYODBC_CONNECTION_LOST:
                LOG.warning("ODBC Connection lost, reestablishing connection")
                # try reestablishing the connection
                self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)
                cursor = None
                # trigger a restart of this operation
                raise RetrySendDataException

            # some other error which we should just abort
            try:
                if cursor:
                    self._rollback_transaction(cursor)
            except Exception:
                pass # nosec
            finally:
                self._close_transaction() # this will remove the connection from the thread
                cursor = None
            # end with this error
            raise err

        finally:
            if cursor:
                cursor.close()
