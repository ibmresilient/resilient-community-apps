import json
import os

MOCK_SCRIPT = "data/mock_script.json"

def read_sample_file(rel_file_path, replace_py3=False):
    base_path = os.path.dirname(__file__)
    workflow_path = os.path.join(base_path, rel_file_path)
    return _read_json_file(workflow_path, replace_py3)

def _read_json_file(full_filepath, replace_py3=False):
    with open(full_filepath, 'r') as f:
        sample_json = f.read()

    if replace_py3:
        sample_json = sample_json.replace('"python', '"python3')
        
    return json.loads(sample_json)

class MockSOAR():
    def __init__(self, return_script_py2=False):
        self.return_script_py2 = return_script_py2

    def get_script_by_uuid(self, uuid):
        sample_script = read_sample_file(MOCK_SCRIPT)
        if self.return_script_py2:
            sample_script["language"] = "python"
        else:
            sample_script["language"] = "python3"

        return sample_script

    def put_script(self, id, script_json):
        return script_json

    def put_workflow(self, id, workflow_json):
        return workflow_json

    def put_playbook(self, id, playbook_json):
        return playbook_json
