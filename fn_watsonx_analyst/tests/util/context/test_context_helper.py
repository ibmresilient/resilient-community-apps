from typing import Any, Callable, List
from unittest.mock import patch

from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.config.loaders import load_data_config as orig_load_data_config
from tests import helper


def mocked_data():
    pass

def data_config_factory(incident_properties_values: List[str]) -> Callable[[Any], dict]:
    """create a patched version of the load_data_config function to use in patches"""
    def load_data_config(_ = None):
        config = orig_load_data_config("default")
        config["incident"]["properties"] = incident_properties_values
        return config
    return load_data_config


@patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
class TestContextHelper:

    sample_inc_data = {
        "name": "test",
        "description": "test long description. " * 30,
        "confirmed": True,
        "addr": "",
        "city": "Cork",
        "unkown_key": "unkown value",
        "properties": [],
    }

    sample_pbx_data = [{
        "playbook": {
            "name": "test",
            "unkown_key": "unkown_value"
        }
    }]

    sample_art_data = [{
        "attachment": {},
        "name": "test",
        "unkown_key": "unkown_value"
    }]

    sample_attach_data = [{
        "attachment": {},
        "name": "test",
        "unkown_key": "unkown_value"
    }]

    def test_cleanse_data(self):
        cleansed_tpl = ContextHelper().cleanse_data(
            self.sample_inc_data, self.sample_pbx_data, self.sample_art_data, self.sample_attach_data, None)

        for data in cleansed_tpl:
            if data:
                if isinstance(data, list):
                    assert data[0].get("unkown_key") is None
                else:
                    assert data.get("unkown_key") is None
            else:
                pass
    
    patch("fn_watsonx_analyst.util.ContextHelper.ContextHelper.__get_data", mocked_data)
    def test_build_full_data(self):
        ch = ContextHelper()

        ch.inc_data = {"name": "test incident"}
        ch.pbx_data = [{"name": "test pbx"}]
        ch.art_data = [{"name": "test pbx"}]
        ch.task_data = []
            
        assert ch.build_full_data() == {"incident": {**ch.inc_data, "artifacts": ch.art_data, "playbook_executions": ch.pbx_data, "tasktree": ch.task_data}}


    @patch("fn_watsonx_analyst.config.loaders.load_data_config", data_config_factory(["*"]))
    def test_cleanse_data_incident_properties_star(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True}
        }, None, None, None, None)

        assert "allowed_key" in incident['properties']

    @patch("fn_watsonx_analyst.util.ContextHelper.load_data_config", data_config_factory([]))
    def test_cleanse_data_incident_properties_none(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True}
        }, None, None, None, None)
        print(incident)

        assert "allowed_key" not in incident['properties']
    

    @patch("fn_watsonx_analyst.util.ContextHelper.load_data_config", data_config_factory(["allowed_key"]))
    def test_cleanse_data_incident_properties_specific(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True}
        }, None, None, None, None)

        assert "allowed_key" in incident['properties']

    @patch("fn_watsonx_analyst.util.ContextHelper.load_data_config", data_config_factory(["other_key"]))
    def test_cleanse_data_incident_properties_not_specified(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True}
        }, None, None, None, None)


        assert "allowed_key" not in incident['properties']

    @patch("fn_watsonx_analyst.util.ContextHelper.load_data_config", data_config_factory(["allowed_key", "other_key"]))
    def test_cleanse_data_incident_properties_multiple_included(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True, "other_key": False}
        }, None, None, None, None)


        assert "allowed_key" in incident['properties']
        assert "other_key" in incident['properties']

    @patch("fn_watsonx_analyst.util.ContextHelper.load_data_config", data_config_factory([]))
    def test_cleanse_data_incident_properties_multiple_excluded(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True, "other_key": False}
        }, None, None, None, None)


        assert "allowed_key" not in incident['properties']
        assert "other_key" not in incident['properties']

    @patch("fn_watsonx_analyst.util.ContextHelper.load_data_config", data_config_factory(["allowed_key"]))
    def test_cleanse_data_incident_properties_multiple_mixed(self):
        ch = ContextHelper()
        incident, _, _, _, _ = ch.cleanse_data({
            'properties': {'allowed_key': True, "other_key": False}
        }, None, None, None, None)


        assert "allowed_key" in incident['properties']
        assert "other_key" not in incident['properties']