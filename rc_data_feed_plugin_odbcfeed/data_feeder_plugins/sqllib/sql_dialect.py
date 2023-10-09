# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""This module contains all of the SqlDialect implementations that we support."""

import copy
import logging
import sqlite3
import pyodbc
import sys
import sqlparams
from six import string_types
from rc_data_feed.lib.type_info import TypeInfo

LOG = logging.getLogger(__name__)

MAX_ORACLE_VARCHAR = 2000
MAX_MARIADB_TEXT = 32000  # roughly 1/2 of 65535 limit to account for unicode
ENCODING="utf-8"
ORACLE_ENCODING="utf-16le"

class SqlDialect:
    """Base class for all SQL dialects that we will support."""
    def __init__(self):
        pass

    def get_upsert(self, table_name, field_names, field_types):
        """
        Gets SQL that implements an 'upsert' for the specified table name with
        the specified field names.

        :param table_name: The name of the table being inserted into/updated.
        :param field_names: The names of the files being inserted/updated.
        :param field_types: The field types needed for specific type conversions

        :returns The SQL for the upsert.
        """
        raise NotImplementedError

    def get_delete(self, table_name):
        """
        Gets SQL that will delete from the specified table given an ID value.

        :param table_name: The name of the table from which the row is to be deleted.

        :returns The SQL for the delete (note that this will require a single bind
            parameter named "id"
        """
        raise NotImplementedError

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        raise NotImplementedError

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        """
        Gets the SQL DDL needed to adds a column to the specified table_name for this dialect.

        Ideally the returned DDL will not error if the column already exists.  However, if it
        is expected to generate an error, then you must also override is_column_exists_exception
        method to allow the exception to be bypassed.

        :param table_name: The name of the table to which the column is to be added.
        :param column_name: The name of the column to add.
        :param column_spec: The specification of the column to add (e.g. 'text' or 'text not null'.

        :returns The SQL DDL needed to add the column.
        """
        raise NotImplementedError

    def is_column_exists_exception(self, the_exception):    # pylint: disable=unused-argument,no-self-use
        """
        Determines if a given exception is due to an attempt to add a column that already exists.

        You only need to implement this if your SQL DDL returned by get_add_column_to_table can
        error if the column already exists.

        :param the_exception: The exception that occurred while attempting to add the column.

        :returns True if the exception was due to the column already existing; False otherwise.
        """
        return False

    def get_parameters(self, parameter_names, parameters):
        """
        Get's the parameter values as the particular SQL access library wants them.
        For example, pyodbc wants a list of values while SQLite wants a dict of named
        parameters.  This is in the dialect class because the dialect is the thing
        that returns the SQL and it will either be positional (using a '?' character) or
        reference names (e.g. ':inc_id')

        :param parameter_names: The names of the parameters.  Note that the order may
            be important here.  If your dialect is returning SQL with positional bind
            parameters then the order of parameter_names will dictate
            the order of the parameter values that you need to return.

        :param parameters: The actual object dict containing the parameters.  The key
            for the dict is the parameter names.

        :returns The parameter values in a format consistent with how you're handling
            bind parameters in this dialect class.
        """
        raise NotImplementedError

    def configure_connection(self, connection):
        """
        Configures the connection.  Useful if you want to set the default charset
        for the connection or something like that.

        :param connection: The connection object.
        """

    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='INTEGER',
            datepicker='DATE',
            datetimepicker='TIMESTAMP',
            boolean='BOOLEAN',
            blob='BLOB'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'TEXT'

    def clean_keywords(self, reserved_words, args):
        """
        cleanup keywords used which cannot be column names on this database
        :param reserved_words: list of words which cannot be used for this database
        :param args: list or individual field name
        :return: cleaned up list of field_name
        """

        def clean_field_name(field_name):
            """
            inner routine to convert keywords
            :param field_name:
            :return: field_name so not to conflict with a keyword
            """
            if field_name.lower() in reserved_words:
                return field_name.lower()+"_"

            return field_name.lower()

        if type(args) == list:
            new_args = []
            for arg in args:
                new_args.append(clean_field_name(arg))

            return new_args

        return clean_field_name(args)

    def get_sqlparams_helper(self):
        return sqlparams.SQLParams('named', 'qmark')

    @staticmethod
    def make_blob(type_info, field, value):
        return value.hex()

class ODBCDialectBase(SqlDialect):  # pylint: disable=abstract-method
    """
    Base class for all ODBC-based databases.  Note that this is an
    'abstract class' because we don't implement all of the methods in
    the ancestor class.
    """
    def get_delete(self, table_name):
        return 'delete from {0} where id = :id'.format(table_name) # nosec

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = list()

        for name in parameter_names:
            bind_parameters.append(parameters[name])

        return bind_parameters

class SqliteDialect(SqlDialect):
    RESERVE_LIST = []
    def __init__(self):
        self.mapped_translate_value = translate_value_for_blob(SqliteDialect.make_blob)

    """
    Dialect for SQLite database...note only use this if you are using the
    sqlite3 library directly.  If using SQLite with ODBC, you'll need a different
    dialect (which as of this writing does not exist).
    """
    def get_upsert(self, table_name, field_names, field_types):
        # The API wants :field_name for the bind parameters, so prepend that for all of the fields.
        #
        value_names = [':' + name for name in field_names]
        clean_table_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        return 'insert or replace into {0} ({1}) values ({2})'.format(clean_table_name,
                                                                      ','.join(field_names),
                                                                      ','.join(value_names))

    def get_delete(self, table_name):
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        return 'delete from {0} where id = :id'.format(clean_name) # nosec

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        specs = []
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        return 'create table if not exists {0} ({1})'.format(clean_name, ','.join(specs))

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        return 'alter table {0} add column {1} {2}'.format(table_name,
                                                           column_name,
                                                           column_spec)

    def is_column_exists_exception(self, the_exception):
        return isinstance(the_exception, sqlite3.OperationalError)

    def get_parameters(self, parameter_names, parameters):
        # Sqlite supports named bound parameter (e.g. with ":parmname").
        return parameters

    @staticmethod
    def make_blob(type_info, field, value):
        """[convert byte array into format required by the blob db type]

        Args:
            value ([byte array]): [description]

        Returns:
            converted format for specific database
        """
        return sqlite3.Binary(value)


class PostgreSQL96Dialect(ODBCDialectBase):
    """
    PostgreSQL 9.6 dialect.  Note that you cannot use a DB less than 9.6 because we use the
    "insert/on conflict/do update" capability and that wasn't introduced until 9.6.
    """

    RESERVE_LIST = [ 'all', 'analyse', 'analyze', 'and', 'any', 'array', 'as', 'asc', 'asymmetric', 'authorization', 'binary',
                     'both', 'case', 'cast', 'check', 'collate', 'collation', 'column', 'concurrently', 'constraint', 'create',
                     'cross', 'current_catalog', 'current_date', 'current_role', 'current_schema', 'current_time',
                     'current_timestamp', 'current_user', 'default', 'deferrable', 'desc', 'distinct', 'do', 'else', 'end',
                     'except', 'false', 'fetch', 'for', 'foreign', 'freeze', 'from', 'full', 'grant', 'group', 'having',
                     'ilike', 'in', 'initially', 'inner', 'intersect', 'into', 'is', 'isnull', 'join', 'lateral', 'leading',
                     'left', 'like', 'limit', 'localtime', 'localtimestamp', 'natural', 'not', 'notnull', 'null', 'offset',
                     'on', 'only', 'or', 'order', 'outer', 'overlaps', 'placing', 'primary', 'references', 'returning', 'right',
                     'select', 'session_user', 'similar', 'some', 'symmetric', 'table', 'tablesample', 'then', 'to', 'trailing',
                     'true', 'union', 'unique', 'user', 'using', 'variadic', 'verbose', 'when', 'where', 'window', 'with'
                    ]

    def __init__(self):
        self.mapped_translate_value = translate_value_for_blob(PostgreSQL96Dialect.make_blob)

    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='BIGINT',
            datepicker='DATE',
            datetimepicker='TIMESTAMPTZ',
            boolean='BOOLEAN',
            blob='bytea'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'TEXT'

    def get_upsert(self, table_name, field_names, field_types):
        # The pyodbc API wants ? for the bind parameters, so prepend that for all of the
        # fields.  Note that self.get_parameters will eventually be called and that will
        # ensure that binding is done in the right order (that the values for a field
        # correspond to the order in which it appears in our list of bind parameters).
        #
        value_placeholders = ['?' for name in field_names]
        clean_table_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        clean_field_names = self.clean_keywords(self.RESERVE_LIST, field_names)

        # set field_name = EXCLUDED.field_name
        conflict_stmt = ['{0} = EXCLUDED.{0}'.format(field_name) for field_name in clean_field_names]

        template = 'insert into {0} ({1}) values ({2}) on conflict (id) do update set {3}'

        return template.format(clean_table_name,
                               ','.join(clean_field_names),
                               ','.join(value_placeholders),
                               ','.join(conflict_stmt))

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        specs = []
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        return 'create table if not exists {0} ({1})'.format(clean_name, ','.join(specs))

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        return 'alter table {0} add column if not exists {1} {2}'.format(clean_name,
                                                                         self.clean_keywords(self.RESERVE_LIST, column_name),
                                                                         column_spec)

    def is_column_exists_exception(self, the_exception):
        # We use "add column if not exists" so we should never get an exception when adding columns.
        return False

    def configure_connection(self, connection):
        connection.setdecoding(pyodbc.SQL_WCHAR, encoding=ENCODING)  # pylint: disable=c-extension-no-member
        if sys.version_info.major == 2: # to set encoding on python 2
            connection.setencoding(str, encoding=ENCODING)
            connection.setencoding(unicode, encoding=ENCODING)
        else: # an issue and try encoding without specifying fromtype
            connection.setencoding(encoding=ENCODING)

    @staticmethod
    def make_blob(type_info, field, value):
        return value


class MySqlDialect(ODBCDialectBase):
    RESERVE_LIST = ['add', 'all', 'alter', 'analyze', 'and', 'as', 'asc', 'auto_increment', 'bdb', 'berkeleydb', 'between', 'bigint',
                    'binary', 'blob', 'both', 'btree', 'by', 'cascade', 'case', 'change', 'char', 'character', 'check', 'collate', 'column',
                    'columns', 'constraint', 'create', 'cross', 'current_date', 'current_time', 'current_timestamp', 'database', 'databases',
                    'day_hour', 'day_minute', 'day_second', 'dec', 'decimal', 'default', 'delayed', 'delete', 'desc', 'describe', 'distinct',
                    'distinctrow', 'div', 'double', 'drop', 'else', 'enclosed', 'errors', 'escaped', 'exists', 'explain', 'false', 'fields',
                    'float', 'for', 'force', 'foreign', 'from', 'fulltext', 'function', 'geometry', 'grant', 'group', 'hash', 'having',
                    'help', 'high_priority', 'hour_minute', 'hour_second', 'if', 'ignore', 'in', 'index', 'infile', 'inner', 'innodb',
                    'insert', 'int', 'integer', 'interval', 'into', 'is', 'join', 'key', 'keys', 'kill', 'leading', 'left', 'like', 'limit',
                    'lines', 'load', 'localtime', 'localtimestamp', 'lock', 'long', 'longblob', 'longtext', 'low_priority', 'master_server_id',
                    'match', 'mediumblob', 'mediumint', 'mediumtext', 'middleint', 'minute_second', 'mod', 'mrg_myisam', 'natural', 'not',
                    'null', 'numeric', 'on', 'optimize', 'option', 'optionally', 'or', 'order', 'outer', 'outfile', 'precision', 'primary',
                    'privileges', 'procedure', 'purge', 'read', 'real', 'references', 'regexp', 'rename', 'replace', 'require', 'restrict',
                    'returns', 'revoke', 'right', 'rlike', 'rtree', 'select', 'set', 'show', 'smallint', 'some', 'soname', 'spatial',
                    'sql_big_result', 'sql_calc_found_rows', 'sql_small_result', 'ssl', 'starting', 'straight_join', 'striped', 'table',
                    'tables', 'terminated', 'text', 'then', 'tinyblob', 'tinyint', 'tinytext', 'to', 'trailing', 'true', 'types', 'union', 'unique',
                    'unlock', 'unsigned', 'update', 'usage', 'use', 'user_resources', 'using', 'values', 'varbinary', 'varchar', 'varcharacter',
                    'varying', 'warnings', 'when', 'where', 'with', 'write', 'xor', 'year_month', 'zerofill']
    def __init__(self):
        self.mapped_translate_value = translate_value_for_blob(MySqlDialect.make_blob)

    def get_upsert(self, table_name, field_names, field_types):
        """
        Gets SQL that implements an 'upsert' for the specified table name with
        the specified field names.

                REPLACE into table (id, name, age) values(1, "A", 19)

        :param table_name: The name of the table being inserted into/updated.
        :param field_names: The names of the files being inserted/updated.

        :returns The SQL for the upsert.
        """
        clean_table_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        clean_field_names = self.clean_keywords(self.RESERVE_LIST, field_names)

        value_placeholders = []
        for name in field_names:
            if field_types.get(name, '') == "datetimepicker":
                value_placeholders.append("convert(?, datetime)")
            else:
                value_placeholders.append("?")

        template = 'replace into {0} ({1}) values ({2})'

        return template.format(clean_table_name,
                               ','.join(clean_field_names),
                               ','.join(value_placeholders))

    def get_delete(self, table_name):
        """
        Gets SQL that will delete from the specified table given an ID value.
            DELETE FROM `table_name` [WHERE condition];

        :param table_name: The name of the table from which the row is to be deleted.

        :returns The SQL for the delete (note that this will require a single bind
            parameter named "id"
        """
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        return 'delete from {0} where id = :id'.format(clean_name) # nosec

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        specs = []
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        return 'create table if not exists {0} ({1})'.format(clean_name, ','.join(specs))

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        """
        Gets the SQL DDL needed to adds a column to the specified table_name for this dialect.

        Ideally the returned DDL will not error if the column already exists.  However, if it
        is expected to generate an error, then you must also override is_column_exists_exception
        method to allow the exception to be bypassed.

        :param table_name: The name of the table to which the column is to be added.
        :param column_name: The name of the column to add.
        :param column_spec: The specification of the column to add (e.g. 'text' or 'text not null'.

        :returns The SQL DDL needed to add the column.
        """
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        sql_stmt =  'alter table {0} add {1} {2};'.format(clean_name,
                                                          self.clean_keywords(self.RESERVE_LIST, column_name),
                                                          column_spec)

        return sql_stmt

    def is_column_exists_exception(self, the_exception):    # pylint: disable=unused-argument,no-self-use
        """
        Determines if a given exception is due to an attempt to add a column that already exists.

        You only need to implement this if your SQL DDL returned by get_add_column_to_table can
        error if the column already exists.

        :param the_exception: The exception that occurred while attempting to add the column.

        :returns True if the exception was due to the column already existing; False otherwise.
        """
        return True

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = list()

        for name in parameter_names:
            bind_parameters.append(parameters[name][:MAX_MARIADB_TEXT] if isinstance(parameters[name], string_types) else parameters[name])

        return bind_parameters

    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='BIGINT',
            datepicker='DATE',
            datetimepicker='DATETIME',
            boolean='TINYINT',
            blob='BLOB'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'TEXT'

    def configure_connection(self, connection):
        connection.setdecoding(pyodbc.SQL_WCHAR, encoding=ENCODING)  # pylint: disable=c-extension-no-member
        if sys.version_info.major == 2: # to set encoding on python 2
            connection.setencoding(str, encoding=ENCODING)
            connection.setencoding(unicode, encoding=ENCODING)
        else: # an issue and try encoding without specifying fromtype
            connection.setencoding(encoding=ENCODING)

    @staticmethod
    def make_blob(type_info, field, value):
        return value

class SqlServerDialect(ODBCDialectBase):
    RESERVE_LIST = ['absolute', 'action', 'ada', 'add', 'all', 'allocate', 'alter', 'and', 'any', 'are', 'as', 'asc',
                    'assertion', 'at', 'authorization', 'avg', 'begin', 'between', 'bit', 'bit_length', 'both', 'by',
                    'cascade', 'cascaded', 'case', 'cast', 'catalog', 'char', 'character', 'character_length', 'char_length',
                    'check', 'close', 'coalesce', 'collate', 'collation', 'column', 'commit', 'connect', 'connection',
                    'constraint', 'constraints', 'continue', 'convert', 'corresponding', 'count', 'create', 'cross',
                    'current', 'current_date', 'current_time', 'current_timestamp', 'current_user', 'cursor', 'date',
                    'day', 'deallocate', 'dec', 'decimal', 'declare', 'default', 'deferrable', 'deferred', 'delete',
                    'desc', 'describe', 'descriptor', 'diagnostics', 'disconnect', 'distinct', 'domain', 'double', 'drop',
                    'else', 'end', 'end-exec', 'escape', 'except', 'exception', 'exec', 'execute', 'exists', 'external',
                    'extract', 'false', 'fetch', 'first', 'float', 'for', 'foreign', 'fortran', 'found', 'from', 'full',
                    'get', 'global', 'go', 'goto', 'grant', 'group', 'having', 'hour', 'identity', 'immediate', 'in',
                    'include', 'index', 'indicator', 'initially', 'inner', 'input', 'insensitive', 'insert', 'int',
                    'integer', 'intersect', 'interval', 'into', 'is', 'isolation', 'join', 'key', 'language', 'last',
                    'leading', 'left', 'level', 'like', 'local', 'lower', 'match', 'max', 'min', 'minute', 'module',
                    'month', 'names', 'national', 'natural', 'nchar', 'next', 'no', 'none', 'not', 'null', 'nullif',
                    'numeric', 'octet_length', 'of', 'on', 'only', 'open', 'option', 'or', 'order', 'outer', 'output',
                    'overlaps', 'pad', 'partial', 'pascal', 'position', 'precision', 'prepare', 'preserve', 'primary',
                    'prior', 'privileges', 'procedure', 'public', 'read', 'real', 'references', 'relative', 'restrict',
                    'revoke', 'right', 'rollback', 'rows', 'rule', 'schema', 'scroll', 'second', 'section', 'select', 'session',
                    'session_user', 'set', 'size', 'smallint', 'some', 'space', 'sql', 'sqlca', 'sqlcode', 'sqlerror',
                    'sqlstate', 'sqlwarning', 'substring', 'sum', 'system_user', 'table', 'temporary', 'then', 'time',
                    'timestamp', 'timezone_hour', 'timezone_minute', 'to', 'trailing', 'transaction', 'translate',
                    'translation', 'trim', 'true', 'union', 'unique', 'unknown', 'update', 'upper', 'usage', 'user',
                    'using', 'value', 'values', 'varchar', 'varying', 'view', 'when', 'whenever', 'where', 'with',
                    'work', 'write', 'year', 'zone']

    def get_upsert(self, table_name, field_names, field_types):
        """
        Gets SQL that implements an 'upsert' for the specified table name with
        the specified field names.

                REPLACE into table (id, name, age) values(1, "A", 19)

        :param table_name: The name of the table being inserted into/updated.
        :param field_names: The names of the files being inserted/updated.
        :param field_types: dictionary of field type, some of which need special processing, such as datetime

        :returns The SQL for the upsert.
        """
        clean_table_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        select_values = []
        for name in field_names:
            clean_name = self.clean_keywords(self.RESERVE_LIST, name)
            if field_types.get(name, '').startswith("date"):
                type = self.get_column_type(field_types[name])
                select_values.append("convert({}, ?, 126) as {}".format(type, clean_name))
            else:
                select_values.append("? as {}".format(clean_name))

        clean_field_names = self.clean_keywords(self.RESERVE_LIST, field_names)
        value_setters = ["[target].{0} = [source].{0}".format(name.lower()) for name in clean_field_names]
        value_placeholders = ['[source].{}'.format(name.lower()) for name in clean_field_names]

        template = """
        MERGE INTO {0} as [target] USING (
               SELECT {1}
            ) AS [source]
        ON [target].id = [source].id
        WHEN MATCHED THEN  UPDATE SET {2}
        WHEN NOT MATCHED THEN  INSERT ({3}) VALUES ({4});
        """

        sql_stmt = template.format(clean_table_name,
                               ','.join(select_values),
                               ','.join(value_setters),
                               ','.join(clean_field_names),
                               ','.join(value_placeholders))

        return sql_stmt

    def get_delete(self, table_name):
        """
        Gets SQL that will delete from the specified table given an ID value.
            DELETE FROM `table_name` [WHERE condition];

        :param table_name: The name of the table from which the row is to be deleted.

        :returns The SQL for the delete (note that this will require a single bind
            parameter named "id"
        """
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        return 'delete from {0} where id = :id;'.format(clean_name) # nosec

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        specs = []
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        cmd = """IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{0}' AND xtype='U')
    CREATE TABLE {0} (
        {1}
    );"""
        return cmd.format(clean_name, ','.join(specs))

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        """
        Gets the SQL DDL needed to adds a column to the specified table_name for this dialect.

        Ideally the returned DDL will not error if the column already exists.  However, if it
        is expected to generate an error, then you must also override is_column_exists_exception
        method to allow the exception to be bypassed.

        :param table_name: The name of the table to which the column is to be added.
        :param column_name: The name of the column to add.
        :param column_spec: The specification of the column to add (e.g. 'text' or 'text not null'.

        :returns The SQL DDL needed to add the column.
        """
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        sql_stmt =  'alter table {0} add {1} {2};'.format(clean_name,
                                                          self.clean_keywords(self.RESERVE_LIST, column_name),
                                                          column_spec)

        return sql_stmt

    def is_column_exists_exception(self, the_exception):    # pylint: disable=unused-argument,no-self-use
        """
        Determines if a given exception is due to an attempt to add a column that already exists.

        You only need to implement this if your SQL DDL returned by get_add_column_to_table can
        error if the column already exists.

        :param the_exception: The exception that occurred while attempting to add the column.

        :returns True if the exception was due to the column already existing; False otherwise.
        """
        if "Column names in each table must be unique" in str(the_exception):
            return True

        LOG.error(the_exception)
        return False

    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='BIGINT',
            datepicker='DATE',
            datetimepicker='DATETIME2',
            boolean='BIT',
            blob='VARBINARY(max)'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'NTEXT'

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = list()

        for name in parameter_names:
            bind_parameters.append(parameters[name])

        return bind_parameters


class OracleDialect(ODBCDialectBase):
    RESERVE_LIST = ['access', 'add', 'all', 'alter', 'and', 'any', 'arraylen', 'as', 'asc',
                    'audit', 'between', 'by', 'char', 'check', 'cluster', 'column', 'comment',
                    'compress', 'connect', 'create', 'current', 'date', 'decimal', 'default',
                    'delete', 'desc', 'distinct', 'drop', 'else', 'exclusive', 'exists', 'file',
                    'float', 'for', 'from', 'grant', 'group', 'having', 'identified', 'immediate',
                    'in', 'increment', 'index', 'initial', 'insert', 'integer', 'intersect',
                    'into', 'is', 'level', 'like', 'lock', 'long', 'maxextents', 'minus',
                    'mode', 'modify', 'noaudit', 'nocompress', 'not', 'notfound', 'nowait',
                    'null', 'number', 'of', 'offline', 'on', 'online', 'option', 'or', 'order',
                    'pctfree', 'prior', 'privileges', 'public', 'raw', 'rename', 'resource',
                    'revoke', 'row', 'rowid', 'rowlabel', 'rownum', 'rows', 'start', 'select',
                    'session', 'set', 'share', 'size', 'smallint', 'sqlbuf', 'successful', 'synonym',
                    'sysdate', 'table', 'then', 'to', 'trigger', 'uid', 'union', 'unique', 'update',
                    'user', 'validate', 'values', 'varchar', 'varchar2', 'view', 'whenever', 'where',
                    'with'
                    ]

    def get_upsert(self, table_name, field_names, field_types):
        """
        Gets SQL that implements an 'upsert' for the specified table name with
        the specified field names.

                REPLACE into table (id, name, age) values(1, "A", 19)

        :param table_name: The name of the table being inserted into/updated.
        :param field_names: The names of the files being inserted/updated.
        :param field_types: dictionary of field type, some of which need special processing, such as datetime

        :returns The SQL for the upsert.
        """
        clean_table_name = self.clean_keywords(self.RESERVE_LIST, table_name)

        # if we're dealing with a blob table column, just do an insert (no update)
        if any([bool(field_types.get(name, '') == "blob") for name in field_names]):
            select_values, clean_field_names = self.get_select_value(field_names, field_types, False)
            template = "INSERT INTO {0} ({1}) VALUES ({2})"

            sql_stmt = template.format(clean_table_name,
                                       ','.join(clean_field_names),
                                       ','.join(select_values))
            LOG.debug(sql_stmt)
        else:
            select_values, clean_field_names = self.get_select_value(field_names, field_types, True)
            value_setters = ["target.{0} = source.{0}".format(name.lower()) if name != "id" else None for name in clean_field_names]
            filtered_value_setters = filter(None, value_setters)

            value_placeholders = ['source.{}'.format(name.lower()) for name in clean_field_names]

            template = """MERGE INTO {0} target
                USING (
                    SELECT {1} FROM dual
                    ) source
                ON (target.id = source.id)
                WHEN MATCHED THEN  UPDATE SET {2}
                WHEN NOT MATCHED THEN  INSERT ({3}) VALUES ({4})
            """

            sql_stmt = template.format(clean_table_name,
                                        ','.join(select_values),
                                        ','.join(filtered_value_setters),
                                        ','.join(clean_field_names),
                                        ','.join(value_placeholders))

        return sql_stmt

    def get_select_value(self, field_names, field_types, include_alias):
        """[build the sql field defintions to use]

        Args:
            field_names ([dict]): [object field names]
            field_types ([dict]): [type information for object]
            include_alias ([bool]): [true to include an 'as <field_name>' alias]

        Returns:
            [list]: [field definitions for sql stmt]
        """
        select_values = []
        clean_field_names = self.clean_keywords(self.RESERVE_LIST, field_names)
        for name in field_names:
            clean_name = self.clean_keywords(self.RESERVE_LIST, name)
            alias = " as {clean_name}"
            if field_types.get(name, '') == "datepicker":
                sql_field = "to_date(:{clean_name}, 'YYYY-MM-DD\"T\"HH24:MI:SS.######')"
            elif field_types.get(name, '') == "datetimepicker":
                sql_field = "to_timestamp_tz(:{clean_name}, 'YYYY-MM-DD\"T\"HH24:MI:SS.FFTZH:TZM')"
            #elif field_types.get(name, '') == "blob":
            #    sql_field = "hextoraw(:{clean_name})"
            else:
                sql_field = ":{clean_name}"

            sql_field = "{}{}".format(sql_field, alias) if include_alias else sql_field
            select_values.append(sql_field.format(clean_name=clean_name))

        return select_values, clean_field_names

    def get_delete(self, table_name):
        """
        Gets SQL that will delete from the specified table given an ID value.
            DELETE FROM `table_name` [WHERE condition];

        :param table_name: The name of the table from which the row is to be deleted.

        :returns The SQL for the delete (note that this will require a single bind
            parameter named "id"
        """
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        return 'delete from {0} where id = :id'.format(clean_name) # nosec

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        specs = []
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)


        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        cmd = """declare
v_sql LONG;
begin

v_sql:='create table {}
  (
  {}
  )';
execute immediate v_sql;

EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE = -955 THEN
        NULL; -- suppresses ORA-00955 exception
      ELSE
         RAISE;
      END IF;
END; """

        formatted = cmd.format(clean_name, ','.join(specs))
        return formatted

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        """
        Gets the SQL DDL needed to adds a column to the specified table_name for this dialect.

        Ideally the returned DDL will not error if the column already exists.  However, if it
        is expected to generate an error, then you must also override is_column_exists_exception
        method to allow the exception to be bypassed.

        :param table_name: The name of the table to which the column is to be added.
        :param column_name: The name of the column to add.
        :param column_spec: The specification of the column to add (e.g. 'text' or 'text not null'.

        :returns The SQL DDL needed to add the column.
        """
        clean_name = self.clean_keywords(self.RESERVE_LIST, table_name)
        sql_stmt =  'alter table {0} add {1} {2}'.format(clean_name,
                                                         self.clean_keywords(self.RESERVE_LIST, column_name),
                                                         column_spec)

        return sql_stmt

    def is_column_exists_exception(self, the_exception):    # pylint: disable=unused-argument,no-self-use
        """
        Determines if a given exception is due to an attempt to add a column that already exists.

        You only need to implement this if your SQL DDL returned by get_add_column_to_table can
        error if the column already exists.

        :param the_exception: The exception that occurred while attempting to add the column.

        :returns True if the exception was due to the column already existing; False otherwise.
        """

        return bool('ORA-01430' in str(the_exception))


    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='NUMBER(16)',
            datepicker='DATE',
            datetimepicker='TIMESTAMP',
            boolean='NUMBER(1)',
            blob='BLOB'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'NVARCHAR2(2000)'

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = {}

        for name in parameter_names:
            clean_name = self.clean_keywords(self.RESERVE_LIST, name)
            if isinstance(parameters[name], bool):
                bind_parameters[clean_name] = 1 if parameters[name] else 0
            else:
                bind_parameters[clean_name] = parameters[name][:MAX_ORACLE_VARCHAR] \
                                                   if isinstance(parameters[name], string_types) else parameters[name]

        return bind_parameters


    def configure_connection(self, connection):
        return True
        """
        connection.setdecoding(pyodbc.SQL_WCHAR, encoding=ORACLE_ENCODING)  # pylint: disable=c-extension-no-member
        if sys.version_info.major == 2: # to set encoding on python 2
            connection.setencoding(str, encoding=ORACLE_ENCODING)
            connection.setencoding(unicode, encoding=ORACLE_ENCODING)
        else: # an issue and try encoding without specifying fromtype
            connection.setencoding(encoding=ORACLE_ENCODING)
        """

    def get_sqlparams_helper(self):
        return None

def translate_value_for_blob(blob_func):
    """[define mappings for Resilient fields to db fields]

    Args:
        blob_func ([method]): [method to run when encountering a blob field type]

    Returns:
        [object]: [translated field ready for the specific db]
    """
    mapping = TypeInfo.get_default_mapping()
    mapping['blob'] = blob_func

    def translate_value(type_info, field, value):
        chged_value = copy.copy(value)
        if chged_value is not None:
            input_type = field['input_type']
            if input_type in mapping:
                chged_value = mapping[input_type](type_info, field, chged_value)
            elif input_type != 'none':
                LOG.warning("Unable to find a mapping for field type: %s", input_type)

            if isinstance(chged_value, list):
                chged_value = mapping["list"](type_info, field, chged_value)

        return chged_value

    return translate_value
