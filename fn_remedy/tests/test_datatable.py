# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
from fn_remedy.lib.datatable import Datatable

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock

import json
import pytest
import resilient
from mocks.datatable_mocked_inputs import *

@pytest.fixture(scope="class")
def mocked_res_client():
    """mocked_res_client a pytest fixture which
    uses the resilient package to get a mocked client.
    Calls resilient.get_client() with mocked user values
    and also passes a custom mock module 
    which has definitions to mock certain
    Resilient/CP4S Datatable endpoints

    :return: A mocked ResClient
    :rtype: SimpleClient
    """
    mocked_res_client = resilient.get_client({
        "email": "info@example.com",
        "host": "example.com",
        "password": "example",
        "org": "example_rg",
        "resilient_mock": "mocks.datatable_mock.DTResilientMock"})
    return mocked_res_client


class TestDataTable():
    """TestDataTable a Test Module
    which is used verify functionality 
    of the Datatable class. 

    Each test uses a pytest fixture - mocked_res_client
    This fixture instantiates a resilient_client with mocked info
    and a custom test class which has extra endpoints for datatable functions.
    """

    def test_get_row(self, mocked_res_client):
        """test_get_row gathers both a mocked input and output
        initializes a datatable object with some mocked inputs
        and then attempts to call get_row with the other
        mocked inputs.

        Afterwards verify the result with the mocked outputs

        :param mocked_res_client: A instance of ResClient with mocked values and a custom Datatable Resilient Mock for endpoints
        :type mocked_res_client: fixture
        """
        inputs = GET_ROW_MOCKED_INPUT
        output = GET_ROW_MOCKED_OUTPUT

        dt = Datatable(
            mocked_res_client, inputs["incident_id"], inputs["datatable_datatable_api_name"])
        # Get the data table data
        dt.get_data()

        # Get the row
        row = dt.get_row(
            inputs["datatable_row_id"], inputs["datatable_search_column"], inputs["datatable_search_value"])
        assert row is not None
        assert row['id'] == output['id']

    def test_get_rows(self, mocked_res_client):
        """test_get_rows gathers both a mocked input and output
        initializes a datatable object with some mocked inputs
        and then attempts to call get_rows with the other
        mocked inputs.

        Afterwards verify the result with the mocked outputs

        :param mocked_res_client: A instance of ResClient with mocked values and a custom Datatable Resilient Mock for endpoints
        :type mocked_res_client: fixture
        """
        inputs = GET_ROWS_MOCKED_INPUT
        output = GET_ROWS_MOCKED_OUTPUT

        dt = Datatable(
            mocked_res_client, inputs["incident_id"], inputs["datatable_datatable_api_name"])
        # Get the data table data
        dt.get_data()

        # Get rows
        rows = dt.get_rows(inputs["datatable_max_rows"], inputs["datatable_sort_by"],
                           inputs["datatable_sort_direction"],
                           inputs["datatable_search_column"], inputs["datatable_search_value"])

        assert rows
        assert len(rows[0]['cells']) == len(output[0]['cells'])

    def test_update_row(self, mocked_res_client):
        """test_update_row gathers both a mocked input and output
        initializes a datatable object with some mocked inputs
        and then attempts to call update_row with the other
        mocked inputs.

        Afterwards verify the result with the mocked outputs

        :param mocked_res_client: A instance of ResClient with mocked values and a custom Datatable Resilient Mock for endpoints
        :type mocked_res_client: fixture
        """
        inputs = UPDATE_ROW_MOCKED_INPUT
        output = UPDATE_ROW_MOCKED_OUTPUT

        dt = Datatable(
            mocked_res_client, inputs["incident_id"], inputs["datatable_datatable_api_name"])

        # Get the data table data
        dt.get_data()

        # Update the row
        updated_row = dt.update_row(
            inputs["datatable_row_id"], inputs["datatable_cells_to_update"])

        assert updated_row
        
        for cell_key in updated_row['cells'].keys():
            assert cell_key in output['cells'].keys()
            assert updated_row['cells'][cell_key]['value'] == output['cells'][cell_key]['value']

    def test_delete(self, mocked_res_client):
        """test_delete_row gathers both a mocked input and output
        initializes a datatable object with some mocked inputs
        and then attempts to call delete_row with the other
        mocked inputs.

        Afterwards verify the result with the mocked outputs

        :param mocked_res_client: A instance of ResClient with mocked values and a custom Datatable Resilient Mock for endpoints
        :type mocked_res_client: fixture
        """
        inputs = DELETE_ROW_MOCKED_INPUT

        dt = Datatable(
            mocked_res_client, inputs["incident_id"], inputs["datatable_datatable_api_name"])

        # Get the data table data
        dt.get_data()

        # Update the row
        deleted_row = dt.delete_row(inputs["datatable_row_id"])

        with pytest.raises(ValueError):
            dt.get_row(inputs["datatable_row_id"])

        assert deleted_row
