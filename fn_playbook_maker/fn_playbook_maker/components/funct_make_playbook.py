# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""AppFunction implementation"""

import hashlib
import random
import string
import uuid
from os import path
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, global_jinja_env, make_payload_from_template
from fn_playbook_maker.lib.soar_common import SOARCommon

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
        self.init_jinja()

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
        soar_common = SOARCommon(self.rest_client())

        funct_list = []
        results = None
        if inputs.get("pbm_app_name"):
            funct_list = soar_common.get_function_info_by_app(inputs.get("pbm_app_name").strip())

        elif inputs.get("pbm_function_names"):
            for function in inputs.get("pbm_function_names").split(","):
                funct = soar_common.get_function_info(function.strip())
                funct_list.append(funct)

        else:
            results = FunctionResult({}, success=False,
                                    reason="either pbm_app_name or pbm_function_names required")

        if not results and funct_list:
            self.LOG.debug(funct_list)
            for funct_info in funct_list:
                try:
                    funct_info.update(inputs)  # add function inputs which will be used in templates
                    # generate the playbook xml uuids used throughout
                    funct_info['uuid_uuid'] = make_uuid(None)
                    funct_info["playbook_display_name"] = "Playbook_{}".format(funct_info['uuid_uuid'])
                    funct_info["playbook_uuid"] = "playbook_{}".format(funct_info['uuid_uuid']).replace("-", "_")
                    funct_info["script_uuid"] = make_uuid(None)
                    funct_info["playbook_name"] = "{} for {}".format(inputs.get('pbm_playbook_name'), funct_info["function_name"])
                    funct_info["playbook_name_api_name"] = funct_info["playbook_name"].replace(" ", "_")

                    # get fields for preprocessing script
                    funct_info['preprocessor_script'] = make_payload_from_template(None, PREPROCESSOR_SCRIPT_TEMPLATE, funct_info, return_json=True)

                    # build the xml compoment of the playbook
                    funct_info['playbook_xml'] = make_payload_from_template(None, PLAYBOOK_XML_TEMPLATE, funct_info, return_json=False)
                    # build the json structure for the .res file and this function
                    funct_info['playbook_json'] = make_payload_from_template(None, PLAYBOOK_JSON_TEMPLATE, funct_info, return_json=True)
                    export_res = make_payload_from_template(None, EXPORT_TEMPLATE, funct_info, return_json=True)

                    # add in the playbook xml content
                    export_res['playbooks'][0]['content']['xml'] = funct_info['playbook_xml']

                    self.LOG.debug(export_res)
                    # import the export_res file
                    soar_common.import_res(export_res)
                except Exception as err:
                    self.LOG.error(str(err))
                    export_res = {}

            results = FunctionResult(export_res)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield results

    def init_jinja(self):
        jinja_env = global_jinja_env()

        new_filters = {
            "make_uuid": make_uuid,
            "make_short_uuid": make_short_uuid
        }

        jinja_env.globals.update(new_filters)
        jinja_env.filters.update(new_filters)


def make_uuid(value, pattern="{}-{}-{}-{}-{}"):
    if value:
        ### produce an md5 hash of a string for use as a uuid
        uuid_hash = hashlib.md5(value.encode()).hexdigest()
        # return in format: c21308eb-e1ba-21a2-ac7c-12dff0794a60
        return pattern.format(uuid_hash[0:8], uuid_hash[8:12], uuid_hash[12:16], uuid_hash[16:20], uuid_hash[20:])
    else:
        return uuid.uuid4()


def make_short_uuid(_value, length=7):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
