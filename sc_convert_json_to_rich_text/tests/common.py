import inspect
import logging
import os
import sys
if sys.version_info[0] == 2:
    import imp
else:
    import importlib

LOG = logging.getLogger(__name__)


class ScriptingError(Exception):
    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return repr(self.value)

class NamedProperty():
    def __init__(self, name, content):
        self.default = {}
        if name:
            setattr(self, name, content)
        else:
            self.default = content

    def __getitem__(self, name):
        # for []
        if getattr(self, name, None):
            return getattr(self, name)
        else:
            return self.default.get(name, None)

    def get(self, name):
        print(name)
        if getattr(self, name, None):
            return getattr(self, name)
        else:
            return self.default

class Results:
    def __init__(self, content, named=None):
        if named:
            self.results = NamedProperty(named, content)
        else:
            self.results = NamedProperty(None, content)

    def __getitem__(self, name):
        # for []
        return self.results.get(name)

class Workflow:
    def __init__(self, content, property=None):
        if property:
            self.properties = NamedProperty(property, content)
        else:
            self.properties = content

class Playbook:
    def __init__(self, content, function=None):
        self.functions = Results({})
        self.properties = {}
        if function:
            self.functions = Results(content, named=function)
        else:
            self.properties = content

    def __getitem__(self, name):
        # for []
        return self.properties.get(name)

class Incident:
    def addNote(self, text):
        LOG.info(text)

class Helper:
    def createRichText(self, text):
        pass
    def fail(self, message):
        raise ScriptingError(message)

def get_properties(json_dict):
    return json_dict.get('padding', 10), json_dict.get('separator','<br>'), json_dict.get('header'), \
           json_dict.get('json_omit_list',[]), json_dict.get('incident_field'), json_dict.get('json'), \
           json_dict.get('sort', False)

def get_module_class(file_name, incident=None, helper=None, workflow=None, playbook=None):
    abs_path = os.path.abspath(file_name)

    if sys.version_info[0] == 2:
        module = imp.load_source('convert_json_to_rich_text', abs_path)
    else:
        module_spec = importlib.util.spec_from_file_location(file_name, abs_path)
        module = importlib.util.module_from_spec(module_spec)

    module.incident = incident
    module.helper = helper
    module.workflow = workflow
    module.playbook = playbook

    if sys.version_info[0] >= 3:
        module_spec.loader.exec_module(module)

    cls = None
    for member in inspect.getmembers(module):
        if member[0] == "ConvertJson":
            cls = member[1]

    return cls
