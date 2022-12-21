# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

class MockedResponse:
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = "mock data"

    def json(self):
        return {"mock": "data"}
