# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Generate Mock responses to simulate Remedy Datatable for Unit and function tests """

def mock_init():
    class MockDT(object):
        def __init__(self):
            pass
        def get_data(self, *args, **kwargs):
            pass
        def get_rows(self, *args, **kwargs):
            rows = [{"id":304, "cells": { "remedy_id": { "value": "INC000000000001"}}}]
            return rows
        def update_row(self, *args, **kwargs):
            pass
        def dt_add_rows(self, *args, **kwargs):
            response = {"status_code": 200, "content": "foo"}
    return MockDT()
