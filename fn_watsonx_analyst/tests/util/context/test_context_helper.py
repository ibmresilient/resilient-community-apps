from unittest.mock import patch

from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from tests import helper


def mocked_data():
    pass
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
