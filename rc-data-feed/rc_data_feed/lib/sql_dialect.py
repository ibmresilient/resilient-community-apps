"""This module contains all of the SqlDialect implementations that we support."""

import sqlite3
import pyodbc


class SqlDialect:
    """Base class for all SQL dialects that we will support."""
    def __init__(self):
        pass

    def get_upsert(self, table_name, field_names):
        """
        Gets SQL that implements an 'upsert' for the specified table name with
        the specified field names.

        :param table_name: The name of the table being inserted into/updated.
        :param field_names: The names of the files being inserted/updated.

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
    def get_upsert(self, table_name, field_names):
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
    def get_upsert(self, table_name, field_names):
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
