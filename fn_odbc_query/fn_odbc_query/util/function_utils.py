# -*- coding: utf-8 -*-
#
# Copyright IBM Corp. - Confidential Information
#
import json
try:
    from json import JSONDecodeError
except:
    JSONDecodeError = ValueError

def str_to_bool(v):
    """
    Cast string 'true'/'True' value to boolean.
    :param v
    :return: boolean
    """
    return v.lower() == "true"


def prepare_sql_parameters(*argv):
    """
    Prepare a list of non None value or blank "Falsy" parameters.
    :param *argv - sql_condition_value1, sql_condition_value2,
    sql_condition_value3: values used to substitute
    :return: list
    """
    sql_params = [condition for condition in argv if condition]

    return sql_params


def validate_data(sql_restricted_sql_statements, sql_query):
    """
    Validate if query is allowed.
    :param sql_restricted_sql_statements: string of restricted SQL statements - configuration settings
    :param sql_query: sql statement - function input

    """
    # Convert to a list/call json.loads if sql_restricted_sql_statements is not None and is not empty string.
    if sql_restricted_sql_statements:

        # Make sure user defined restricted sql statements are in valid JSON format.
        # Defined as a list using square brackets, separated by a comma.
        # Example ["delete", "update", "insert"]
        try:
            restricted_list = json.loads(sql_restricted_sql_statements)
        except JSONDecodeError as e:
            raise ValueError("Restricted SQL statements must be defined in valid JSON format. Error: {}".format(str(e)))

        if type(restricted_list) is not list:
            raise ValueError("Restricted SQL statements must be defined in valid JSON format as a list using square brackets.")

        # Check if any of NOT allowed statement are included in the sql_query
        for item in restricted_list:
            if item.strip().lower() in sql_query.lower():
                raise Exception("User does not have permission to perform {} action.".format(item.strip()))


def prepare_results(cursor_description, rows):
    """
    Generate result in JSON format with an entry consisting of key value pairs.
    :param cursor_description: a tuple with query result columns
    :param rows: list of returned sql query values
    :return: dictionary
    """
    if rows is None or len(rows) == 0:
        return {"entries": None}

    # List of column names from SQL result to use as dictionary keys
    dt_column_keys = [column[0] for column in cursor_description]

    # Build dictionary: key-value pairs consisting of column name - row value
    entries_data_list = []
    for row in rows:
        entries_data_list.append(dict(zip(dt_column_keys, row)))

    entries = {"entries": [entry for entry in entries_data_list]}

    return entries


def get_type_sql_statement(sql_query):
    """
    Check what SQL statement is executed. Return first word from sql_query.
    sql_query cannot be None or empty string, validation in fn_odbc_query_function().
    :param sql_query
    :return: str
    """
    return sql_query.split(None, 1)[0].lower()
