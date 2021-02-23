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

    def test_get_row(self):
        pass


    def test_get_rows(self):
        pass

    def test_update_row(self):
        pass

    def test_delete(self):
        pass
