"""Unit tests for ContextHelper"""

import json
import pytest

from fn_watsonx_analyst.util.ContextHelper import ContextHelper


@pytest.fixture(name = "context_helper")
def fixture_context_helper():
    """Fixture to create an instance of ContextHelper"""
    return ContextHelper()

@pytest.mark.parametrize("input_data, target, replacement, expected_output", [
    # Test case 1: Simple string replacement inside dictionary
    ({"key": "Email Attachment"}, "Email Attachment", "File", {"key": "File"}),

    # Test case 2: Case-insensitive replacement
    ({"key": "email attachment"}, "Email Attachment", "File", {"key": "File"}),

    # Test case 3: String inside a nested dictionary
    ({"incident": {"type": "Email Attachment"}}, "Email Attachment", "File", {"incident": {"type": "File"}}),

    # Test case 4: String inside a list of dictionaries
    ({"incident": {"artifacts": [{"type": "Email Attachment"}, {"type": "Not Relevant"}]}},
     "Email Attachment", "File",
     {"incident": {"artifacts": [{"type": "File"}, {"type": "Not Relevant"}]}}),

    # Test case 5: String in a deep nested structure
    ({"level1": {"level2": {"level3": "Email Attachment"}}},
     "Email Attachment", "File",
     {"level1": {"level2": {"level3": "File"}}}),

    # Test case 6: No replacement needed
    ({"incident": {"artifacts": [{"type": "File"}]}}, "Email Attachment", "File", {"incident": {"artifacts": [{"type": "File"}]}}),

    # Test case 7: String inside a list
    (["Email Attachment", "Another String"], "Email Attachment", "File", ["File", "Another String"]),

    # Test case 8: Mixed types (should be ignored)
    ({"key": 123, "list": [None, True, 4.5, "Email Attachment"]},
     "Email Attachment", "File",
     {"key": 123, "list": [None, True, 4.5, "File"]}),

    # Test case 9: Multiple occurrences in different places
    ({"incident": {"artifacts": [{"type": "Email Attachment", "desc": "Email Attachment"}, {"type": "Not Relevant"}]}},
     "Email Attachment", "File",
     {"incident": {"artifacts": [{"type": "File", "desc": "File"}, {"type": "Not Relevant"}]}}),

    # Test case 10: Empty dictionary (edge case)
    ({}, "Email Attachment", "File", {}),

    # Test case 11: Empty list (edge case)
    ([], "Email Attachment", "File", []),

])

def test_replace_string_in_values(context_helper, input_data, target, replacement, expected_output):
    result = ContextHelper.replace_string_in_values(context_helper, input_data, target, replacement)
    assert result == expected_output

def test_artifact_cleanse(context_helper: ContextHelper):
    artifact = {
        "value": "artifact1",
        "type": 1,
        "unused_value": "test123"
    }

    _, _, art_data, _, _ = context_helper.cleanse_data(None, None, [artifact], None, None)

    assert "unused_value" not in art_data[0]
    assert "value" in art_data[0]
    assert "type" in art_data[0]

def test_incident_cleanse(context_helper: ContextHelper):
    incident = {
        "name": "incident",
        "description": "description",
        "unused": "test",
        "confirmed": False
    }

    inc_data, _, _, _, _ = context_helper.cleanse_data(incident, None, None, None, None)

    assert "unused" not in inc_data
    assert "name" in inc_data
    assert "description" in inc_data
    assert "incident_disposition" in inc_data

def test_phase_with_child_phase(context_helper: ContextHelper):

    task_tree = [{'child_cats': [{'child_cats': [], 'child_tasks': [{'name': 'Investigate Exposure of Personal Information/Data', 'inc_id': 2099, 'inc_owner_id': 5, 'due_date': 1746536400000, 'required': True, 'owner_id': 5, 'user_notes': None, 'status': 'C', 'frozen': False, 'owner_fname': 'Thomas', 'owner_lname': 'Galligan', 'init_date': 1744371950513, 'active': True, 'src_name': None, 'inc_name': 'Suspected Phising Attack', 'instr_text': None, 'instructions': None, 'form': 'data_compromised, determined_date', 'members': None, 'perms': {'read': True, 'write': True, 'comment': True, 'assign': True, 'close': True, 'change_members': True, 'attach_file': True, 'read_attachments': True, 'delete_attachments': True, 'playbook_progress_enabled': False, 'change_header': True}, 'notes': [], 'closed_date': 1746540899320, 'actions': [], 'playbooks': [], 'phase_id': 1019, 'category_id': 104, 'notes_count': 1, 'attachments_count': 0, 'task_layout': None, 'auto_deactivate': True, 'creator_principal': {'id': 5, 'type': 'user', 'name': 'thomas@co3sys.com', 'display_name': 'Thomas Galligan'}, 'timeframe_name': None, 'manual_predefined': False, 'regs': {'88': 'Data Breach Best Practices'}, 'custom': False, 'id': 32, 'inc_training': False, 'cat_name': 'Respond', 'description': '', 'at_id': None, 'private': None}], 'name': 'Data Breach - Organizational', 'parent_id': None, 'phase_id': None, 'category_id': 104, 'id': None, 'status': 'C'}], 'child_tasks': [], 'name': 'Respond', 'parent_id': None, 'phase_id': 1019, 'category_id': None, 'id': None, 'status': 'C'}]

    _, _, _, _, task_data = context_helper.cleanse_data(None, None, None, None, task_tree)

    assert len(task_data) == 1

    assert "phase_name" in task_data[0]
    assert "name" not in task_data[0]

    assert "child_phases" in task_data[0]
    assert len(task_data[0]["child_phases"])
    assert "phase_name" in task_data[0]["child_phases"][0]
    assert "complete" in task_data[0]["child_phases"][0]['tasks'][0]
