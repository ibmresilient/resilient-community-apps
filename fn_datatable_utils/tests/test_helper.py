# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint
from requests_mock import create_response
from json import dumps
from six import b

class DTResilientMock(BasicResilientMock):
    mock_data_table_rows = [
        {
            "dt_col_id": 3001,
            "dt_col_name": "Joe Blogs",
            "dt_col_email": "joe@example.com",
            "dt_col_status": "In Progress"
        },
        {
            "dt_col_id": 3002,
            "dt_col_name": "Mary Blogs",
            "dt_col_email": "mary@example.com",
            "dt_col_status": "In Progress"
        },
        {
            "dt_col_id": 3003,
            "dt_col_name": "Mary Blogs",
            "dt_col_email": "mary@example.com",
            "dt_col_status": "Active"
        }
    ]

    mock_data_table_updated_rows = [{
        "dt_col_id": 3002,
        "dt_col_name": "Mary Blogs",
        "dt_col_email": "mary@example.com",
        "dt_col_status": "Complete"
    }]

    mock_success_delete = {
        'message': None,
        'hints': [],
        'success': True,
        'title': None
    }

    @staticmethod
    def format_datatable_row(row, row_id):
        formatted_row = {}

        for key, value in row.items():
            formatted_row[key] = {
                "row_id": row_id,
                "id": key,
                "value": value
            }

        return {"id": row_id, "cells": formatted_row}

    @staticmethod
    def get_datatable_rows(rows):
        row_id = 0
        return_rows = []
        for row in rows:
            row_id += 1
            return_rows.append(
                DTResilientMock.format_datatable_row(row, row_id))
        return return_rows

    @resilient_endpoint("GET", r"/incidents/[0-9]+/table_data/mock_data_table\?handle_format=names$")
    def mock_datatable_get(self, request):
        """ Handle GET request for mock_data_table """

        data = {"rows": DTResilientMock.get_datatable_rows(
            self.mock_data_table_rows)}

        return create_response(request,
                               status_code=200,
                               content=b(dumps(data)))

    @resilient_endpoint("DELETE", r"/incidents/[0-9]+/table_data/mock_data_table/row_data/[0-9]\?handle_format=names$")
    def mock_datatable_delete_row(self, request):
        """ Handle DELETE request for mock_data_table """

        data = self.mock_success_delete

        return create_response(request,
                               status_code=200,
                               content=b(dumps(data)))

    @resilient_endpoint("PUT", r"/incidents/[0-9]+/table_data/mock_data_table/row_data/2\?handle_format=names$")
    def mock_datatable_put(self, request):
        """ Handle PUT request for mock_data_table """

        data = DTResilientMock.get_datatable_rows(
            self.mock_data_table_updated_rows)[0]

        return create_response(request,
                               status_code=200,
                               content=b(dumps(data)))

# This function is used in the update function pre-process script to help define the inputs
def dict_to_json_str(d):
    """Function that converts a dictionary into a JSON string.
       Supports types: basestring, bool, int and nested dicts.
       Does not support lists.
       If the value is None, it sets it to False."""

    json_entry = '"{}":{}'
    json_entry_str = '"{}":"{}"'
    entries = []

    for entry in d:
        key = entry
        value = d[entry]

        if not value:
            value = False

        if isinstance(value, list):
            raise ValueError('dict_to_json_str does not support Python Lists')

        try:
            basestring
        except NameError:
            basestring = str

        if isinstance(value, basestring):
            value = value.replace(u'"', u'\\"')
            entries.append(json_entry_str.format(key, value))

        elif isinstance(value, bool):
            value = 'true' if value else 'false'
            entries.append(json_entry.format(key, value))

        elif isinstance(value, dict):
            entries.append(json_entry.format(key, dict_to_json_str(value)))

        else:
            entries.append(json_entry.format(key, value))

    return '{} {} {}'.format('{', ','.join(entries), '}')
