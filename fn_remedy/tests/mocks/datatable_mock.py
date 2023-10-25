# (c) Copyright IBM Corp. 2021. All Rights Reserved.
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint
import requests_mock
import json
import six


class DTResilientMock(BasicResilientMock):
    """DTResilientMock a Mock class which inherits the base
    endpoints and adds mock endpoints for the DataTable object
    for testing.

    :param BasicResilientMock: A mock object which covers some of the most common endpoints, this class inherits from it to avoid you needing to use it seperately
    :type BasicResilientMock: object
    """
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

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

    @resilient_endpoint("DELETE", r"/incidents/[0-9]+/table_data/mock_data_table/row_data/[0-9]\?handle_format=names$")
    def mock_datatable_delete_row(self, request):
        """ Handle DELETE request for mock_data_table """

        data = self.mock_success_delete

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

    @resilient_endpoint("PUT", r"/incidents/[0-9]+/table_data/mock_data_table/row_data/2\?handle_format=names$")
    def mock_datatable_put(self, request):
        """ Handle PUT request for mock_data_table """

        data = DTResilientMock.get_datatable_rows(
            self.mock_data_table_updated_rows)[0]

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

