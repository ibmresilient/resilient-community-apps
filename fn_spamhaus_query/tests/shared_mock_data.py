# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

class MockedResponse:
    def __init__(self, status_code=200, reason="OK", json={"resp": [1002]}):
        self.success = True
        self.status_code = status_code
        self.reason = reason
        self.json_data = json

    def json(self):
        return self.json_data
