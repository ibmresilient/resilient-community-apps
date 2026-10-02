from .common import Incident, Helper, Workflow, Playbook, get_module_class

test_playbook_failure_payload = {
    "success": False, 
    "reason": "This is not good",
    "content": None
}

test_playbook_success_payload = {
    "success": True, 
    "reason": None,
    "content": {"success": True}
}

cls = get_module_class('convert_json_to_rich_text.py',
                       incident=Incident(),
                       helper=Helper(),
                       workflow=None,
                       playbook=Playbook({'convert_json_to_rich_text': test_playbook_failure_payload})
                      )

def test_playbook_failure():
    convert = cls()
    converted_json = convert.convert_json_to_rich_text(None)
    assert not converted_json

def test_playbook_success():
    convert = cls()
    converted_json = convert.convert_json_to_rich_text(test_playbook_success_payload)
    assert  converted_json == "<strong>success</strong>: True<br /><strong>reason</strong>: None<br /><strong>content</strong>: <div style='padding:10px'><strong>success</strong>: True</div>"
