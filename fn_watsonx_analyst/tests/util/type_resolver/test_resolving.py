"""Unit Tests for resolving SOAR Type IDs to the API Name for that type"""

import copy

from unittest.mock import patch

from fn_watsonx_analyst.util.ContextHelper import ContextHelper


def mock_get_data(_self, _res_client, _cache_obj, _watsonx_api_key) -> dict:
    return {
        "incident_types": {
            "11": {
                "id": 11,
                "enabled": True,
                "name": "Stolen documents / files / records",
                "description": None,
                "create_date": 1296778208935,
                "update_date": None,
                "parent_id": None,
                "hidden": False,
                "system": True,
                "uuid": "e7105d3b-f7bc-4680-8c2d-55d32e6787bb",
                "tags": [],
            },
            "21": {
                "id": 21,
                "enabled": True,
                "name": "Denial of Service",
                "description": None,
                "create_date": None,
                "update_date": None,
                "parent_id": None,
                "hidden": False,
                "system": True,
                "uuid": "e1b10c0c-21f8-4e3f-9f0f-40668ddd2a01",
                "tags": [],
            },
        }
    }


class TestPrompting:
    """Unit tests for Prompting class."""

    data = {
        "incident": {
            "id": 1,
            "name": "test123",
        }
    }

    @patch(
        "fn_watsonx_analyst.util.persistent_org_cache.PersistentCache.get_data",
        mock_get_data,
    )
    def test_single_incident_type(self):
        data = copy.deepcopy(self.data)
        data["incident"]["incident_type_ids"] = [11]

        result = ContextHelper().resolve_type_ids(data)
        assert result["incident"]["incident_type_ids"] == [
            "Stolen documents / files / records"
        ]


    @patch(
        "fn_watsonx_analyst.util.persistent_org_cache.PersistentCache.get_data",
        mock_get_data,
    )
    def test_multi_incident_type(self):
        data = copy.deepcopy(self.data)
        data["incident"]["incident_type_ids"] = [11, 21]

        result = ContextHelper().resolve_type_ids(data)
        assert result["incident"]["incident_type_ids"] == [
            "Stolen documents / files / records",
            "Denial of Service"
        ]
