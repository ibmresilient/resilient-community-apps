# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
from fn_remedy.lib.datatable import Datatable

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock

import pytest
import resilient
from mocks.datatable_mock import DTResilientMock
from mocks.datatable_mocked_inputs import *



class TestDataTable():

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
            mocked_res_client, inputs["incident_id"], inputs["dt_utils_datatable_api_name"])
        # Get the data table data
        dt.get_data()

        # Get the row
        row = dt.get_row(
            inputs["dt_utils_row_id"], inputs["dt_utils_search_column"], inputs["dt_utils_search_value"])
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
            mocked_res_client, inputs["incident_id"], inputs["dt_utils_datatable_api_name"])
        # Get the data table data
        dt.get_data()

        # Get rows
        rows = dt.get_rows(inputs["dt_utils_max_rows"], inputs["dt_utils_sort_by"],
                           inputs["dt_utils_sort_direction"],
                           inputs["dt_utils_search_column"], inputs["dt_utils_search_value"])

        assert rows
        assert len(rows[0]['cells'])

    def test_update_row(self):
        pass

    def test_delete(self):
        pass
