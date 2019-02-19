"""This module contains all of the SqlDialect implementations that we support."""

import sqlite3
import pyodbc
from six import string_types


MAX_ORACLE_VARCHAR = 4000


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
            boolean='BOOLEAN'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'TEXT'

class ODBCDialectBase(SqlDialect):  # pylint: disable=abstract-method
    """
    Base class for all ODBC-based databases.  Note that this is an
    'abstract class' because we don't implement all of the methods in
    the ancestor class.
    """
    def get_delete(self, table_name):
        return 'delete from {0} where id = ?'.format(table_name)

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = list()

        for name in parameter_names:
            bind_parameters.append(parameters[name])

        return bind_parameters

class SqliteDialect(SqlDialect):
    """
    Dialect for SQLite database...note only use this if you are using the
    sqlite3 library directly.  If using SQLite with ODBC, you'll need a different
    dialect (which as of this writing does not exist).
    """
    def get_upsert(self, table_name, field_names, field_types):
        # The API wants :field_name for the bind parameters, so prepend that for all of the fields.
        #
        value_names = [':' + name for name in field_names]

        return 'insert or replace into {0} ({1}) values ({2})'.format(table_name,
                                                                      ','.join(field_names),
                                                                      ','.join(value_names))

    def get_delete(self, table_name):
        return 'delete from {0} where id = :id'.format(table_name)

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        specs = []

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        return 'create table if not exists {0} ({1})'.format(table_name, ','.join(specs))

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        return 'alter table {0} add column {1} {2}'.format(table_name,
                                                           column_name,
                                                           column_spec)

    def is_column_exists_exception(self, the_exception):
        return isinstance(the_exception, sqlite3.OperationalError)

    def get_parameters(self, parameter_names, parameters):
        # Sqlite supports named bound parameter (e.g. with ":parmname").
        return parameters


class PostgreSQL96Dialect(ODBCDialectBase):
    """
    PostgreSQL 9.6 dialect.  Note that you cannot use a DB less than 9.6 because we use the
    "insert/on conflict/do update" capability and that wasn't introduced until 9.6.
    """
    def get_upsert(self, table_name, field_names, field_types):
        # The pyodbc API wants ? for the bind parameters, so prepend that for all of the
        # fields.  Note that self.get_parameters will eventually be called and that will
        # ensure that binding is done in the right order (that the values for a field
        # correspond to the order in which it appears in our list of bind parameters).
        #
        value_placeholders = ['?' for name in field_names]

        # set field_name = EXCLUDED.field_name
        conflict_stmt = ['{0} = EXCLUDED.{0}'.format(field_name) for field_name in field_names]

        template = 'insert into {0} ({1}) values ({2}) on conflict (id) do update set {3}'

        return template.format(table_name,
                               ','.join(field_names),
                               ','.join(value_placeholders),
                               ','.join(conflict_stmt))

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        specs = []

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        return 'create table if not exists {0} ({1})'.format(table_name, ','.join(specs))

    def get_add_column_to_table(self, table_name, column_name, column_spec):
        return 'alter table {0} add column if not exists {1} {2}'.format(table_name,
                                                                         column_name,
                                                                         column_spec)

    def is_column_exists_exception(self, the_exception):
        # We use "add column if not exists" so we should never get an exception when adding columns.
        return False

    def configure_connection(self, connection):
        connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')  # pylint: disable=c-extension-no-member
        connection.setencoding(encoding='utf-8')

class MySqlDialect(ODBCDialectBase):
    def get_upsert(self, table_name, field_names, field_types):
        """
        Gets SQL that implements an 'upsert' for the specified table name with
        the specified field names.

                REPLACE into table (id, name, age) values(1, "A", 19)

        :param table_name: The name of the table being inserted into/updated.
        :param field_names: The names of the files being inserted/updated.

        :returns The SQL for the upsert.
        """

        value_placeholders = ['?' for name in field_names]
        template = 'replace into {0} ({1}) values ({2})'

        return template.format(table_name,
                               ','.join(field_names),
                               ','.join(value_placeholders))

    def get_delete(self, table_name):
        """
        Gets SQL that will delete from the specified table given an ID value.
            DELETE FROM `table_name` [WHERE condition];

        :param table_name: The name of the table from which the row is to be deleted.

        :returns The SQL for the delete (note that this will require a single bind
            parameter named "id"
        """
        return 'delete from {0} where id = ?'.format(table_name)

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        specs = []

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        return 'create table if not exists {0} ({1})'.format(table_name, ','.join(specs))

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
        return 'alter table {0} add column {1} {2}'.format(table_name,
                                                           column_name,
                                                           column_spec)

    def is_column_exists_exception(self, the_exception):    # pylint: disable=unused-argument,no-self-use
        """
        Determines if a given exception is due to an attempt to add a column that already exists.

        You only need to implement this if your SQL DDL returned by get_add_column_to_table can
        error if the column already exists.

        :param the_exception: The exception that occurred while attempting to add the column.

        :returns True if the exception was due to the column already existing; False otherwise.
        """
        return True

class SqlServerDialect(ODBCDialectBase):
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

        select_values = []
        clean_field_names = self.clean_keywords(field_names)
        for name in field_names:
            clean_name = self.clean_keywords(name)
            if field_types.get(name, '').startswith("date"):
                type = self.get_column_type(field_types[name])
                select_values.append("convert({}, ?, 126) as {}".format(type, clean_name))
            else:
                select_values.append("? as {}".format(clean_name))

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

        sql_stmt = template.format(table_name,
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
        return 'delete from {0} where id = ?;'.format(table_name)

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        specs = []

        for (key, value) in list(column_spec_dict.items()):
            specs.append("{0} {1}".format(key, value))

        cmd = """IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{0}' AND xtype='U')
    CREATE TABLE {0} (
        {1}
    );"""
        return cmd.format(table_name, ','.join(specs))

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
        sql_stmt =  'alter table {0} add {1} {2};'.format(table_name,
                                                          self.clean_keywords(column_name),
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

    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='INT',
            datepicker='DATE',
            datetimepicker='DATETIME2',
            boolean='BIT'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'TEXT'

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = list()

        for name in parameter_names:
            bind_parameters.append(parameters[name])

        return bind_parameters

    def clean_keywords(self, args):
        """
        cleanup keywords used which cannot be column names on this database
        :param args: list or individual field name
        :return: cleaned up list of field_name
        """
        RESERVE_LIST = ['add', 'all', 'alter', 'and', 'any', 'as', 'asc', 'authorization', 'backup', 'begin', 'between', 'break', 'browse',
                        'bulk', 'by', 'cascade', 'case', 'check', 'checkpoint', 'close', 'clustered', 'coalesce', 'collate', 'column', 'commit',
                        'compute', 'constraint', 'contains', 'containstable', 'continue', 'convert', 'create', 'cross', 'current', 'current_date',
                        'current_time', 'current_timestamp', 'current_user', 'cursor', 'database', 'dbcc', 'deallocate', 'declare', 'default',
                        'delete', 'deny', 'desc', 'disk', 'distinct', 'distributed', 'double', 'drop', 'dump', 'else', 'end', 'errlvl', 'escape',
                        'except', 'exec', 'execute', 'exists', 'exit', 'external', 'fetch', 'file', 'fillfactor', 'for', 'foreign', 'freetext',
                        'freetexttable', 'from', 'full', 'function', 'goto', 'grant', 'group', 'group', 'having', 'holdlock', 'identity',
                        'identitycol', 'identity_insert', 'if', 'in', 'index', 'inner', 'insert', 'intersect', 'into', 'is', 'join', 'key',
                        'kill', 'left', 'like', 'lineno', 'load', 'merge', 'national', 'nocheck', 'nonclustered', 'not', 'null', 'nullif', 'of',
                        'off', 'offsets', 'on', 'open', 'opendatasource', 'openquery', 'openrowset', 'openxml', 'option', 'or', 'order', 'outer',
                        'over', 'percent', 'pivot', 'plan', 'precision', 'primary', 'print', 'proc', 'procedure', 'public', 'raiserror', 'read',
                        'readtext', 'reconfigure', 'references', 'replication', 'restore', 'restrict', 'return', 'revert', 'revoke', 'right',
                        'rollback', 'rowcount', 'rowguidcol', 'rule', 'save', 'schema', 'securityaudit', 'select', 'semantickeyphrasetable',
                        'semanticsimilaritydetailstable', 'semanticsimilaritytable', 'session_user', 'set', 'setuser', 'shutdown', 'some',
                        'statistics', 'system_user', 'table', 'tablesample', 'textsize', 'then', 'to', 'top', 'tran', 'transaction', 'trigger',
                        'truncate', 'try_convert', 'tsequal', 'union', 'unique', 'unpivot', 'update', 'updatetext', 'use', 'user', 'values',
                        'varying', 'view', 'waitfor', 'when', 'where', 'while', 'with', 'within', 'writetext']

        def clean_field_name(field_name):
            """
            inner routine to convert keywords
            :param field_name:
            :return: field_name so not to conflict with a keyword
            """
            if field_name in RESERVE_LIST:
                return field_name+"_"
            else:
                return field_name

        if type(args) == list:
            new_args = []
            for arg in args:
                new_args.append(clean_field_name(arg))

            return new_args
        else:
            return clean_field_name(args)


class OracleDialect(ODBCDialectBase):
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

        select_values = []
        clean_field_names = self.clean_keywords(field_names)
        for name in field_names:
            clean_name = self.clean_keywords(name)
            if field_types.get(name, '').startswith("date"):
                select_values.append("to_date(?, 'YYYY-MM-DD\"T\"HH24:MI:SS.######') as {}".format(clean_name))
            elif field_types.get(name, '') == "datetimepicker":
                select_values.append("to_timestamp(?, 'YYYY-MM-DD\"T\"HH24:MI:SS.######') as {}".format(clean_name))
            else:
                select_values.append("? as {}".format(clean_name))

        value_setters = ["target.{0} = source.{0}".format(name.lower()) if name != "id" else None for name in clean_field_names]
        filtered_value_setters = filter(None, value_setters)

        value_placeholders = ['source.{}'.format(name.lower()) for name in clean_field_names]

        template = """MERGE INTO {0} target 
        USING (
               SELECT {1} FROM dual
              ) source
        ON (target.id = source.id)
        WHEN MATCHED THEN  UPDATE SET {2}
        WHEN NOT MATCHED THEN  INSERT ({3}) VALUES ({4});
        """

        sql_stmt = template.format(table_name,
                                   ','.join(select_values),
                                   ','.join(filtered_value_setters),
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
        return 'delete from {0} where id = ?;'.format(table_name)

    def get_create_table_if_not_exists(self, table_name, column_spec_dict):
        """Gets SQL that will create the specified table if it doesn't exist already.

        :param table_name: The name of the table to create.
        :param column_spec_dict: A dict containing the column name to column spec
            mapping.  For example, it will contain something like {'id': 'integer
            primary key'}."""
        specs = []

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

        return cmd.format(table_name, ','.join(specs))

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
        sql_stmt =  'alter table {0} add {1} {2};'.format(table_name,
                                                          self.clean_keywords(column_name),
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

    def get_column_type(self, input_type):  # pylint: disable=no-self-use
        """
        Gets the DB column type for the specified Resilient 'input type'

        :param input_type: The Resilient input type value (e.g. datepicker, boolean, number,
            text, text_area, etc.)

        :returns The DB type to use for this dialect.
        """
        type_dict = dict(
            number='INT',
            datepicker='DATE',
            datetimepicker='TIMESTAMP',
            boolean='NUMBER(1)'
        )

        if input_type in type_dict:
            return type_dict[input_type]

        return 'VARCHAR2(4000)'

    def get_parameters(self, parameter_names, parameters):
        # Need to get a list that contains all the values in the same order as parameter_names.
        bind_parameters = list()

        for name in parameter_names:
            if isinstance(parameters[name], bool):
                bind_parameters.append(1 if parameters[name] else 0)
            else:
                bind_parameters.append(parameters[name][:MAX_ORACLE_VARCHAR] if isinstance(parameters[name], string_types) else parameters[name])

        return bind_parameters

    def clean_keywords(self, args):
        """
        cleanup keywords used which cannot be column names on this database
        :param args: list or individual field name
        :return: cleaned up list of field_name
        """
        RESERVE_LIST = ['access', 'add', 'all', 'alter', 'and', 'any', 'as', 'asc', 'audit', 'between', 'by', 'char', 'check', 'cluster',
                        'column', 'comment', 'compress', 'connect', 'create', 'current', 'date', 'decimal', 'default', 'delete', 'desc',
                        'distinct', 'drop', 'else', 'exclusive', 'exists', 'file', 'float', 'for', 'from', 'grant', 'group', 'having',
                        'identified', 'immediate', 'in', 'increment', 'index', 'initial', 'insert', 'integer', 'intersect', 'into', 'is',
                        'level', 'like', 'lock', 'long', 'maxextents', 'minus', 'mlslabel', 'mode', 'modify', 'noaudit', 'nocompress',
                        'not', 'nowait', 'null', 'number', 'of', 'offline', 'on', 'online', 'option', 'or', 'order', 'pctfree', 'prior',
                        'privileges', 'public', 'raw', 'rename', 'resource', 'revoke', 'row', 'rowid', 'rownum', 'rows', 'select', 'session',
                        'set', 'share', 'size', 'smallint', 'start', 'successful', 'synonym', 'sysdate', 'table', 'then', 'to', 'trigger',
                        'uid', 'union', 'unique', 'update', 'user', 'validate', 'values', 'varchar', 'varchar2', 'view', 'whenever', 'where',
                        'with']

        def clean_field_name(field_name):
            """
            inner routine to convert keywords
            :param field_name:
            :return: field_name so not to conflict with a keyword
            """
            if field_name in RESERVE_LIST:
                return field_name+"_"
            else:
                return field_name

        if type(args) == list:
            new_args = []
            for arg in args:
                new_args.append(clean_field_name(arg))

            return new_args
        else:
            return clean_field_name(args)
