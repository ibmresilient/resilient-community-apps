# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint


class SearchMock(BasicResilientMock):

    @resilient_endpoint("POST", "/search_ex")
    def org_search(self, request):
        """ Callback for POST to /search_ex """
        search_data = {
            "results": [
            {
                "match_field_value": "<ResilientHighlight>rtfm.mit.edu</ResilientHighlight>",
                "inc_name": "http://pokeapi.co/99999",
                "task_id": None,
                "obj_id": 81,
                "obj_creator_id": 4,
                "inc_owner_id": 4,
                "type_id": "artifact",
                "org_id": 201,
                "task_name": None,
                "score": 8.889709,
                "result": {
                    "hits": [],
                    "hash": "07d3e3bfd5fcd91250aecaeed5b86bc0701aeb94ba0d79a15f62915a43dc57b1",
                    "description": None,
                    "created": 1520448663352,
                    "perms": None,
                    "creator": {},
                    "inc_id": 2114,
                    "value": "rtfm.mit.edu",
                    "properties": None,
                    "parent_id": None,
                    "attachment": None,
                    "inc_name": "http://pokeapi.co/99999",
                    "creator_principal": {},
                    "type": {
                        "name": "DNS Name",
                        "id": 2
                    },
                    "id": 81,
                    "actions": [],
                    "pending_sources": []
                },
                "obj_create_date": 1520448663352,
                "match_field_name": "Value",
                "inc_id": 2114
            }]}
        return requests_mock.create_response(request, status_code=200, json=search_data)

