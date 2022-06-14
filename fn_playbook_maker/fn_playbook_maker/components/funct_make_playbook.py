# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""AppFunction implementation"""

import hashlib
import random
import re
import string
import traceback
import uuid
from os import path
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import global_jinja_env, make_payload_from_template
from fn_playbook_maker.lib.soar_common import SOARCommon

REMOVE_SPECIAL = re.compile(r'(?:[^a-zA-Z0-9_])', re.IGNORECASE)

PACKAGE_NAME = "fn_playbook_maker"
FN_NAME = "make_playbook"

TEMPLATES_DIR = path.join(path.dirname(path.abspath(__file__)), "templates")
PLAYBOOK_XML_TEMPLATE = path.join(TEMPLATES_DIR, "playbook_xml.jinja")
PLAYBOOK_JSON_TEMPLATE = path.join(TEMPLATES_DIR, "playbook_json.jinja")
EXPORT_TEMPLATE = path.join(TEMPLATES_DIR, "export_res.jinja")
PREPROCESSOR_SCRIPT_TEMPLATE = path.join(TEMPLATES_DIR, "preprocessor_script.jinja")

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'make_playbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.soar_common = SOARCommon(self.rest_client())

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create playbook(s) based on specific apps and functions
        Inputs:
            -   fn_inputs.pbm_playbook_name
            -   fn_inputs.pbm_app_name
            -   fn_inputs.pbm_activation_type
            -   fn_inputs.pbm_playbook_type
            -   fn_inputs.pbm_function_names
            -   fn_inputs.pdm_activation_fields
            -   fn_inputs.pbm_add_to_same_playbook
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        inputs = fn_inputs._asdict()

        function_input_list = []
        results = None
        if inputs.get("pbm_app_name"):
            function_input_list = self.soar_common.get_function_info_by_app(inputs.get("pbm_app_name").strip())

        elif inputs.get("pbm_function_names"):
            for function in inputs.get("pbm_function_names").split(","):
                funct = self.soar_common.get_function_info(function.strip())
                if funct:
                    function_input_list.append(funct)
                else:
                    results = FunctionResult({}, success=False,
                                             reason="Function not found: {}".format(function))
                    break

        else:
            results = FunctionResult({}, success=False,
                                     reason="Either pbm_app_name or pbm_function_names required")

        # no errors and functions found?
        if not results and function_input_list:
            self.LOG.debug(function_input_list)

            result_list = []
            # add to same playbook?
            if inputs.get('pbm_add_to_same_playbook'):
                playbook_payload, export_res, err_msg = make_export_res(inputs, function_input_list)
                if err_msg:
                    self.LOG.error(err_msg)
                else:
                    result_list.append(self.import_playbook(playbook_payload, export_res))
            else:
                # separate playbooks
                for funct_info in function_input_list:
                    playbook_payload, export_res, err_msg = make_export_res(inputs, [funct_info])
                    if err_msg:
                        self.LOG.error(err_msg)
                    else:
                        self.LOG.info("Creating playbook '%s' for function '%s'",
                                        playbook_payload['playbook_info']['playbook_name'],
                                        funct_info.get('function_name'))
                        result_list.append(self.import_playbook(playbook_payload, export_res))

            results = FunctionResult(result_list)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield results

    def import_playbook(self, playbook_payload, export_res):
        self.LOG.debug(export_res)
        try:
            result_bool = self.soar_common.import_res(export_res)

            # get the playbook id
            playbook_id = None
            if result_bool:
                playbook_id = self.get_playbook_id(playbook_payload)

        except Exception as err:
            self.LOG.error(str(err))
            self.LOG.debug(traceback.format_exc())
            result_bool = False
            playbook_id: None

        return {
                "playbook_name": playbook_payload.get('playbook_info', {}).get('playbook_name'),
                "success": result_bool,
                "id": playbook_id
            }

    def get_playbook_id(self, playbook_payload):
        try:
            playbook_info = self.soar_common.get_playbook_by_api_name(playbook_payload.get('playbook_info', {}).get('playbook_name_api_name'))
            if playbook_info:
                return playbook_info.get('id')
        except Exception:
            pass

        return None


def make_playbook_info(inputs, funct_info_list):
    playbook_info = {

    }
    playbook_payload = {
        "inputs": inputs,
        "functions": funct_info_list,
        "playbook_info": playbook_info
    }

    clean_playbook_name = inputs.get('pbm_playbook_name').replace('"', '\\"')
    # generate the playbook xml uuids used throughout
    if inputs.get('pbm_add_to_same_playbook'):
        playbook_info["playbook_name"] = clean_playbook_name
    else:
        playbook_info["playbook_name"] = "{} for {}".format(clean_playbook_name, funct_info_list[0]["function_name"])
    playbook_info["playbook_name_api_name"] = REMOVE_SPECIAL.sub('', playbook_info["playbook_name"].replace(' ', '_').lower())

    # function based uuid's
    playbook_info['uuid_uuid'] = make_uuid(None)
    playbook_info["playbook_display_name"] = "Playbook_{}".format(playbook_info['uuid_uuid'])
    playbook_info["playbook_uuid"] = "playbook_{}".format(playbook_info['uuid_uuid']).replace("-", "_")

    # initialize per function
    for funct in funct_info_list:
        funct["script_uuid"] = make_uuid(None)

    return playbook_payload

def make_export_res(inputs, function_input_list):
    templates = MakeTemplates()
    try:
        playbook_payload = make_playbook_info(inputs, function_input_list)
        # build the preprocessor script and XML data
        for funct_info in playbook_payload['functions']:
            playbook_payload['current_function'] = funct_info
            # get fields for preprocessing script
            funct_info['preprocessor_script'] = templates.make_function_preprocessing_script(playbook_payload)

        # build the xml component for the playbook (all functions)
        playbook_json = templates.make_playbook_json(playbook_payload)
        playbook_xml = templates.make_playbook_xml(playbook_payload)
        export_res = templates.make_initial_export_res(playbook_json, playbook_xml)

        return playbook_payload, export_res, None

    except Exception as err:
        return None, None, "{}\n{}".format(str(err), traceback.format_exc())

class MakeTemplates():
    def __init__(self):
        jinja_env = global_jinja_env()

        new_filters = {
            "make_uuid": make_uuid,
            "make_short_uuid": make_short_uuid
        }

        jinja_env.globals.update(new_filters)
        jinja_env.filters.update(new_filters)

    def make_function_preprocessing_script(self, playbook_payload):
        """build the post processing script for a given function

        Args:
            playbook_payload (dict): entire playbook data needed for creating an export.res file

        Returns:
            dict: data structure which represents a post-processing script in a playbook
        """
        return make_payload_from_template(None, PREPROCESSOR_SCRIPT_TEMPLATE, playbook_payload, return_json=True)

    def make_playbook_json(self, playbook_payload):
        """build the definition of a playbook

        Args:
            playbook_payload (dict): entire playbook data needed for creating an export.res file

        Returns:
            dict: data structure which represents playbook
        """
        return  {
                    'playbook_json': make_payload_from_template(None, PLAYBOOK_JSON_TEMPLATE, playbook_payload, return_json=True)
                }

    def make_playbook_xml(self, playbook_payload):
        """build the definition of a playbook call structure in XML

        Args:
            playbook_payload (dict): entire playbook data needed for creating an export.res file

        Returns:
            str: data structure of a playbook for the BPMN engine
        """
        return make_payload_from_template(None, PLAYBOOK_XML_TEMPLATE, playbook_payload, return_json=False)

    def make_initial_export_res(self, playbook_json, playbook_xml):
        """build the initial export.res file with most the of parts are in place

        Args:
            playbook_json (dict): see make_playbook_json

        Returns:
            dict: data structure of a playbook for the BPMN engine
        """
        export_res = make_payload_from_template(None, EXPORT_TEMPLATE, playbook_json, return_json=True)
        # add in the playbook xml content
        if playbook_xml:
            export_res['playbooks'][0]['content']['xml'] = playbook_xml
        return export_res


## J I N J A   F I L T E R S
def make_uuid(value, pattern="{}-{}-{}-{}-{}"):
    if value:
        ### produce an md5 hash of a string for use as a uuid
        uuid_hash = hashlib.md5(value.encode()).hexdigest()
        # return in format: c21308eb-e1ba-21a2-ac7c-12dff0794a60
        return pattern.format(uuid_hash[0:8], uuid_hash[8:12], uuid_hash[12:16], uuid_hash[16:20], uuid_hash[20:])

    return uuid.uuid4()


def make_short_uuid(_value, length=7):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
