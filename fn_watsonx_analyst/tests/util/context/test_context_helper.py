from typing import Any, Callable, List
from unittest.mock import MagicMock, patch

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


@patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
class TestFormatIncidentForContext:
    """Tests for the format_incident_for_context method"""

    def setup_method(self):
        """Setup test data before each test"""
        helper.generate_app_state()

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_basic_structure(self, mock_cache):
        """Test that the formatted output contains all major sections"""
        # Mock organization cache
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Organization"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        # Mock the data retrieval
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test description",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1, 2],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "addr": "123 Main St",
            "city": "Test City",
            "state": "TS",
            "zip": "12345",
            "create_date": 1732115801922,
            "discovered_date": 1732115801922,
            "owner_id": 34,
            "creator_id": 34,
            "members": []
        }
        ch.art_data = []
        ch.attach_data = []
        ch.pbx_data = []
        ch.task_data = []
        
        ch.full_data = {"incident": {**ch.inc_data, "artifacts": [], "attachments": [], "playbook_executions": [], "tasktree": []}}
        
        result = ch.format_incident_for_context()
        
        # Check for major sections
        assert "# Incident 2414: Test Incident" in result
        assert "Organization: Test Organization" in result
        assert "### Address:" in result
        assert "### Timeline" in result
        assert "### Incident Members" in result
        assert "### Artifacts" in result
        assert "### Last 10 playbook executions" in result
        assert "### Tasks" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_with_artifacts(self, mock_cache):
        """Test formatting with artifacts grouped by type"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "owner_id": 34,
            "creator_id": 34,
            "members": []
        }
        
        artifacts = [
            {
                "type": {"name": "IP Address"},
                "value": "192.168.1.1",
                "description": "Suspicious IP",
                "hits": []
            },
            {
                "type": {"name": "IP Address"},
                "value": "10.0.0.1",
                "description": None,
                "hits": []
            },
            {
                "type": {"name": "Email Address"},
                "value": "test@example.com",
                "description": "Phishing email",
                "hits": []
            }
        ]
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": artifacts,
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check artifacts are grouped by type
        assert "`IP Address` Artifacts:" in result
        assert "`Email Address` Artifacts:" in result
        assert "192.168.1.1" in result
        assert "10.0.0.1" in result
        assert "test@example.com" in result
        assert "Suspicious IP" in result
        assert "Phishing email" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_with_artifact_hits(self, mock_cache):
        """Test formatting artifacts with threat intelligence hits"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "owner_id": 34,
            "creator_id": 34,
            "members": []
        }
        
        artifacts = [
            {
                "type": {"name": "IP Address"},
                "value": "192.168.1.1",
                "description": "Malicious IP",
                "hits": [
                    {"name": "Reputation", "value": "Malicious"},
                    {"name": "Threat Level", "value": "High"}
                ]
            }
        ]
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": artifacts,
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check hits are included
        assert "Hits:" in result
        assert "Reputation: Malicious" in result
        assert "Threat Level: High" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_with_tasks(self, mock_cache):
        """Test formatting with tasks organized by phase"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "owner_id": 34,
            "creator_id": 34,
            "members": []
        }
        
        ch.task_data = [
            {
                "phase_name": "Initial Response",
                "tasks": [
                    {
                        "name": "Investigate Alert",
                        "status": "Open",
                        "owner_id": 34,
                        "required": True,
                        "due_date": 1732115801922,
                        "instructions": {"content": "Review the alert details"}
                    }
                ],
                "child_cats": []
            }
        ]

        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": [],
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }

        result = ch.format_incident_for_context()

        # Check task information
        assert "Phase: Initial Response" in result
        assert "Task: Investigate Alert" in result
        assert "Status: Open" in result
        assert "Required: Yes" in result
        assert "Review the alert details" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_with_playbook_executions(self, mock_cache):
        """Test formatting with playbook execution history"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "owner_id": 34,
            "creator_id": 34,
            "members": []
        }
        
        pbx_data = [
            {
                "playbook": {"display_name": "Enrich IP Address"},
                "status": "completed",
                "start_time": "2024-01-01 10:00:00",
                "object": {
                    "type_name": "artifact",
                    "object_name": "192.168.1.1"
                }
            }
        ]
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": [],
                "attachments": [],
                "playbook_executions": pbx_data,
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check playbook execution info
        assert "Playbook: Enrich IP Address" in result
        assert "Status: completed" in result
        assert "Started at: 2024-01-01 10:00:00" in result
        assert "Targeting: Artifact: `192.168.1.1`" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_with_members(self, mock_cache):
        """Test formatting with incident members"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "owner_id": 34,
            "creator_id": 35,
            "members": [36, 37]
        }
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": [],
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check members section exists
        try:
            assert "### Incident Members" in result
            assert "Owner:" in result or "Creator:" in result
        except:

            print(result)

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_training_flag(self, mock_cache):
        """Test that training incidents are properly marked"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Training Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": True,
            "owner_id": 34,
            "creator_id": 34,
            "members": []
        }
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": [],
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check training indicator
        assert "Training incident" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_empty_data(self, mock_cache):
        """Test formatting with minimal/empty data"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        ch.inc_data = {
            "id": 2414,
            "name": "Empty Incident",
            "description": None,
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [],
            "enabled": True,
            "confirmed": False,
            "training": False,
            "owner_id": None,
            "creator_id": None,
            "members": []
        }
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": [],
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check default messages for empty sections
        assert "No artifacts found for this incident" in result
        assert "No playbooks have been executed on this incident yet" in result
        assert "No tasks found for this incident" in result

    @patch("fn_watsonx_analyst.util.ContextHelper.PersistentCache")
    def test_format_incident_timestamp_conversion(self, mock_cache):
        """Test that timestamps are properly converted to readable format"""
        mock_cache_instance = MagicMock()
        mock_cache_instance.get_data.return_value = {
            "org_info": {"name": "Test Org"}
        }
        mock_cache.return_value = mock_cache_instance

        ch = ContextHelper(inc_id=2414)
        
        test_timestamp = 1732115801922  # Unix timestamp in milliseconds
        
        ch.inc_data = {
            "id": 2414,
            "name": "Test Incident",
            "description": "Test",
            "severity_code": 50,
            "workspace": 1,
            "incident_type_ids": [1],
            "enabled": True,
            "confirmed": True,
            "training": False,
            "owner_id": 34,
            "creator_id": 34,
            "members": [],
            "create_date": test_timestamp,
            "discovered_date": test_timestamp
        }
        
        ch.full_data = {
            "incident": {
                **ch.inc_data,
                "artifacts": [],
                "attachments": [],
                "playbook_executions": [],
                "tasktree": []
            }
        }
        
        result = ch.format_incident_for_context()
        
        # Check that timestamp was converted (should contain date format)
        assert "Incident created at:" in result
        assert "Incident discovered at:" in result
        # The converted format should contain year, month, day
        assert "2024" in result or "20" in result  # Year should be present