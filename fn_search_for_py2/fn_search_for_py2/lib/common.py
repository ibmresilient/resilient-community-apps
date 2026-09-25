# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order
"""
objective: this is a user-prompted tool to query apps for scripts, workflows and playbooks to detect python2
pre-requisites:
    - repo to search is cloned
usage:
    - python python </path/to/>search_for_py2_export_res.py </path/to/>customize.py


"""
# find ~/repos/resilient-community-apps -name 'customize.py' -exec python </path/to/>/search_for_py2_export_res.py {} \;

import base64
import logging
import json
import os
import sys
import re

from difflib import context_diff
from getpass import getpass
from io import open
from lib2to3 import refactor
from lxml import etree
from typing import Union, Tuple
from urllib.parse import unquote

from fn_search_for_py2.lib.soar_helper import SOARHelper
from resilient_lib import IntegrationError

INSTALL_FAILURES = False
# try:
#     from resilient import SimpleClient
# except:
#     print("install 'resilient' python package")
#     INSTALL_FAILURES = True

try:
    import requests
except:
    print("install 'requests' python package")
    INSTALL_FAILURES = True

# turn off warnings about certs
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if INSTALL_FAILURES:
    sys.exit(1)

LOG = logging.getLogger(__name__)

SCRIPT_TEXT = "script_text" # json key for script's content
FINAL_EXPRESSION_TEXT = "final_expression_text" # workflow condition
LANGUAGE = "language"
SCRIPT_LANGUAGE = "script_language"

AVAIL_FIXES = refactor.get_fixers_from_package("lib2to3.fixes")
AVAIL_FIXES.remove("lib2to3.fixes.fix_unicode")
PY_CONVERTER_IGNORE_UNICODE = refactor.RefactoringTool(AVAIL_FIXES)
UNICODE_FIX = ["lib2to3.fixes.fix_unicode"]
PY_CONVERTER_JUST_UNICODE = refactor.RefactoringTool(UNICODE_FIX)

IMPORT_DEFINITION = re.compile(r"ImportDefinition\(u{0,1}\"{3}(.*)\"{3}", re.MULTILINE+re.DOTALL)

EXPORT_RES = "export.res"
RES_EXT = ".res"
RESZ_EXT = ".resz"
EXPORT_RES_PATH = f"data/{EXPORT_RES}"

PYTHON2_REFERENCE = "python"
PYTHON3_REFERENCE = "python3"

QUOTED_PYTHON2 = f'"{PYTHON2_REFERENCE}"'
PY2_ITERS_LIST = ["iterkeys", "iteritems", "itervalues"]
JYTHON_REFERENCE = "java.util" # reduced from 'java.util.Date'

SCRIPTS_PATH = "scripts"
SCRIPTS_LOCAL_PATH = "local_scripts"
WORKFLOWS_PATH = "workflows"
PLAYBOOKS_PATH = "playbooks"

ATTRIBUTES = "attributes"
COMPONENTS = "components"

BPMN_SCHEMAS = [
    (
        "sub-playbooks",
        ".//{http://www.omg.org/spec/BPMN/20100524/MODEL}callActivity",
        ".//resilient:sub-playbook",
        "pre_processing",
        True),
    (
        "functions",
        ".//{http://www.omg.org/spec/BPMN/20100524/MODEL}serviceTask[@{http://resilient.ibm.com/bpmn}type='function']",
        ".//resilient:function",
        None,
        True
    ),
    (
        "sub-playbook end events",
        ".//{http://www.omg.org/spec/BPMN/20100524/MODEL}endEvent",
        ".//resilient:endEvent",
        None,
        False
    ),
    (
        "scripts",
        ".//{http://www.omg.org/spec/BPMN/20100524/MODEL}scriptTask",
        ".//resilient:script",
        None,
        False
    )
]

# messages
PY2_ITERS = "PY2_ITERS" # "Python2 iters found. Convert to use .items()"
PY2_UNICODE = "PY2_UNICODE" # "Unicode strings found ('u' string prefix). This can remain for Python3, and but cleaner to remove."
PY2_JAVA_UTIL_DATE = "PY2_JAVA_UTIL_DATE" # "'import java.util.Date' found. Change to 'from datetime import datetime' and datetime functions such as datetime.now()."
PY2_UNCONVERTIBLE = "PY2_UNCONVERTIBLE" # "Python3 conversion found significant changes. Please review and convert manually."
PY2_CONVERTIBLE = "PY2_CONVERTIBLE" # "Playbook set to run Python2. This playbook can be easily changed to use Python 2. Check function input scripts, local scripts, and scripts used in conditions. Mostly likely the only change needed is to convert all language settings to Python 3."


class FindPY2():
    def __init__(self, soar_helper: SOARHelper):
        self.soar_helper = soar_helper

    def analyze_scripts(self, inputs: dict) -> list:
        # unimplemented
        raise NotImplementedError()

    def get_script_content(self, element_id, element):
        # unimplemented
        raise NotImplementedError()

    def analyze_workflows(self, inputs: dict) -> list:
        # unimplemented
        raise NotImplementedError()

    def analyze_playbooks(self, inputs: dict) -> list:
        # unimplemented
        raise NotImplementedError()

    def start(self, inputs: dict) -> list:
        """
        Function: Search for scripts, workflows and playbooks which are set to use Python 2. Python 2 will be removed from SOAR in an upcoming release.
                - inputs.py2_search_tags
                - inputs.py2_item_id
                - inputs.py2_item_name
                - inputs.py2_item_type
        """

        # start the review
        py2_playbooks = py2_scripts = py2_workflows = {}
        if inputs.get("py2_item_type") in ["all", "script"]:
            py2_scripts = self.analyze_scripts(inputs)
        if inputs.get("py2_item_type") in ["all", "workflow"]:
            py2_workflows = self.analyze_workflows(inputs)
        if inputs.get("py2_item_type") in ["all", "playbook"]:
            py2_playbooks = self.analyze_playbooks(inputs)

        results = {
            "script": py2_scripts,
            "workflow": py2_workflows,
            "playbook": py2_playbooks
        }

        return results

    def _get_py2_result_template(self, name: str, display_name: str, tags: list) -> dict:
        return {
            "name": name,
            "display_name": display_name,
            "tags": tags,
            ATTRIBUTES: []
        }

    def _analyze_scripts(self, script_list: list) -> dict:
        py2_scripts = {}

        for script in script_list:
            py2_result = self._analyze_script(script)
            if py2_result:
                LOG.info("Py2 script found: %s", py2_result.get("display_name"))
                py2_scripts[script["id"]] = py2_result

        return py2_scripts

    def _analyze_script(self, script: dict) -> Union[dict, None]:
        result = self._get_py2_result_template(script["name"],
                                               script.get("display_name"),
                                               script["tags"])
        py2_found = False
        if LANGUAGE not in script or script.get(LANGUAGE) == PYTHON2_REFERENCE:
            py2_found = True

            script_content = self.get_script_content(script["id"], script)
            if self.is_py2_iters(script_content):
                result[ATTRIBUTES].append(PY2_ITERS)
            if JYTHON_REFERENCE in script_content:
                result[ATTRIBUTES].append(PY2_JAVA_UTIL_DATE)

            substantially_changed, only_unicode_changes = check_upgrade(script_content, script["name"])
            if substantially_changed:
                #result["diff"] = substantially_changed
                result[ATTRIBUTES].append(PY2_UNCONVERTIBLE)
            else:
                result[ATTRIBUTES].append(PY2_CONVERTIBLE)
            if only_unicode_changes:
                result[ATTRIBUTES].append(PY2_UNICODE)

        return result if py2_found else None

    def _analyze_workflows(self, workflow_list) -> dict:
        """list workflow by id, programmatic_name"""
        py2_workflows = {}

        for workflow in workflow_list:
            py2_result = self._analyze_workflow_playbook(workflow, False)
            if py2_result:
                LOG.info("Py2 workflow found: %s", py2_result.get("display_name"))
                py2_workflows[workflow["workflow_id"]] = py2_result

        return py2_workflows

    def _analyze_workflow_playbook(self, workflow_playbook: dict, is_playbook: bool) -> dict:
        result = self._get_py2_result_template(workflow_playbook["name"],
                                               workflow_playbook.get("display_name"),
                                               workflow_playbook["tags"])

        xml = workflow_playbook["content"]["xml"]
        is_jython = bool(JYTHON_REFERENCE in xml)
        is_py2_iters = self.is_py2_iters(xml)

        if is_jython:
            result[ATTRIBUTES].append(PY2_JAVA_UTIL_DATE)
        if is_py2_iters:
            result[ATTRIBUTES].append(PY2_ITERS)

        py2_unconvertible, py2_convertible, py2_unicode, found_py2_components = \
            self.analyze_bpmn(workflow_playbook)
        result[COMPONENTS] = found_py2_components
        
        if py2_unconvertible or is_jython or is_py2_iters:
            result[ATTRIBUTES].append(PY2_UNCONVERTIBLE if is_playbook else PY2_UNCONVERTIBLE)
        elif py2_convertible and not (is_jython or is_py2_iters):
            result[ATTRIBUTES].append(PY2_CONVERTIBLE if is_playbook else PY2_CONVERTIBLE)
        if py2_unicode:
            result[ATTRIBUTES].append(PY2_UNICODE)

        return result if result[ATTRIBUTES] else None

    def is_py2_iters(self, contents) -> bool:
        # any iter items?
        for item in PY2_ITERS_LIST:
            if item in contents:
                return True

        return False

    def _analyze_playbooks(self, playbook_list) -> dict:
        """list playbook by id, programmatic_name"""
        py2_playbooks = {}

        for playbook in [plbk for plbk in playbook_list if "content" in plbk]:
            py2_result = self._analyze_workflow_playbook(playbook, True)
            if py2_result:
                LOG.info("Py2 playbook found: %s", py2_result.get("display_name"))
                py2_playbooks[playbook["id"]] = py2_result

        return py2_playbooks

    def filter_on_tags(self, filter_tags: str, item_name: str, items_list: list) -> list:
        """filter item list either by app api_names or by the item_name

        :param filter_tags: comma separated list of app api_names
        :type filter_tags: str
        :param item_name: display name of item
        :type item_name: str
        :param items_list: list of scripts, workflows or playbooks to review
        :type items_list: list
        :return: filtered list
        :rtype: list
        """
        filtered_items = items_list.copy()

        # filter by item_name
        if item_name:
            filtered_items = [item for item in filtered_items if item.get("display_name", item.get("name")).lower() == item_name.strip().lower()]

        # filter by tags
        filter_tags_list = [tag.strip() for tag in (filter_tags.split(",") if filter_tags else [])]

        if not filter_tags_list:
            return filtered_items

        tag_filtered_items = []
        for item in filtered_items:
            for item_tag in item.get("tags", []):
                if item_tag.get("tag_handle") in filter_tags_list:
                    tag_filtered_items.append(item)
                    break # no need to review other tags for this item

        return tag_filtered_items

    def fix_py2_script(self, script: dict) -> Tuple[bool, dict]:
        changed = False
        if not script.get(LANGUAGE):
            script[LANGUAGE] = PYTHON3_REFERENCE
            changed = True
        elif script[LANGUAGE] == "python":
            script[LANGUAGE] = PYTHON3_REFERENCE
            changed = True

        if changed:
            script[SCRIPT_TEXT] = upgrade_script(script.get(SCRIPT_TEXT))

        return changed, script

    def fix_py2_bpmn(self, bpmn_item: dict) ->  Tuple[list, dict]:
        changed = False
        xml = bpmn_item["content"]["xml"]

        etree_xml = etree.XML(bytes(unquote(xml), "utf-8"))
        found_py2_components = [] # identify the part of the workflow, playbook found with py2

        is_changed, etree_xml = self._fix_py2_conditions(etree_xml)
        changed |= is_changed
        if is_changed:
            found_py2_components.append("conditions")

        for components_labels, analyze_schema, analyze_task_type, script_prefix, is_function in BPMN_SCHEMAS:
            is_changed, etree_xml = self._fix_py2_bpmn(bpmn_item,
                                                       etree_xml,
                                                       analyze_schema,
                                                       analyze_task_type,
                                                       script_prefix,
                                                       is_function)
            changed |= is_changed
            if is_changed:
                found_py2_components.append(components_labels)

        if changed:
            bpmn_item["content"]["xml"] = etree.tostring(etree_xml,
                                                         encoding=str,
                                                         method="xml")

        return found_py2_components, bpmn_item

    def _fix_py2_conditions(self, etree_xml) -> Tuple[bool, object]:
        condition_expressions = etree_xml.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}conditionExpression")
        is_changed = False
        for condition_expression in condition_expressions:
            condition_json = json.loads(condition_expression.text)

            is_changed = False
            for condition in [cond for cond in condition_json["conditions"] if "script" == cond["method"]]:
                if SCRIPT_LANGUAGE in condition and condition[SCRIPT_LANGUAGE] == PYTHON2_REFERENCE:
                    condition[SCRIPT_LANGUAGE] = PYTHON3_REFERENCE
                    is_changed = True
                if LANGUAGE in condition["value"] and condition["value"][LANGUAGE] == PYTHON2_REFERENCE:
                    for in_text in [SCRIPT_TEXT, FINAL_EXPRESSION_TEXT]:
                        if in_text in condition["value"]:
                            condition["value"][LANGUAGE] = PYTHON3_REFERENCE
                            condition["value"][in_text] = upgrade_script(condition["value"][in_text])
                            is_changed = True

            # if SCRIPT_LANGUAGE in condition_json and condition_json[SCRIPT_LANGUAGE] == PYTHON2_REFERENCE:
            #     condition_json[SCRIPT_LANGUAGE] = PYTHON3_REFERENCE
            #     is_changed = True

            condition_expression.text = json.dumps(condition_json)

        return is_changed, etree_xml

    def _fix_py2_bpmn(self, bpmn_item, etree_xml, find_query, findall_query, script_prefix, is_function=True) -> Tuple[bool, object]:
        changed = False
        ns = etree_xml.nsmap
        service_tasks = etree_xml.findall(find_query)
        for service_task in service_tasks:
            try:
                bpmn_task_list = service_task.findall(findall_query, ns)
            except SyntaxError:
                # this happens differences in workflows and playbooks
                bpmn_task_list = []

            for bpmn_task in bpmn_task_list:
                if bpmn_task.text:
                    task_json = json.loads(bpmn_task.text)
                    if is_function:
                        is_changed, task_json = self._fix_task_script(task_json, "pre_processing")
                        changed |= is_changed
                        is_changed, task_json = self._fix_task_script(task_json, "post_processing")
                        changed |= is_changed
                    else:
                        # a subplaybook callActivity or subplaybook endEvent
                        is_changed, task_json = self._fix_task_script(task_json, script_prefix)
                        changed |= is_changed

                    bpmn_task.text = json.dumps(task_json)
                else:
                    # need to handle external scripts separate from a playbook
                    is_changed, task_json = self._fix_external_script(bpmn_item, bpmn_task.get("uuid"))
                    changed |= is_changed

        # if this fixed back in xml format?
        return changed, etree_xml


    def _fix_task_script(self, task_json: dict, property_prefix: str) -> Tuple[bool, dict]:
        changed = False
        script_property_name = f"{property_prefix}_script" if property_prefix else "script"
        script_language_property_name = f"{script_property_name}_language"

        if script_property_name in task_json.keys():
            if not script_language_property_name in task_json or PYTHON3_REFERENCE != task_json[script_language_property_name]:
                changed = True
                task_json[script_language_property_name] = PYTHON3_REFERENCE

                task_json[script_property_name] = upgrade_script(task_json[script_property_name])
        return changed, task_json

    def _fix_external_script(self, bpmn_item, script_uuid: str) -> Tuple[bool, dict]:
        """ update an external script used in a playbook """
        changed = False

        script_json = self.get_script_by_uuid(bpmn_item, script_uuid)

        if not LANGUAGE in script_json or PYTHON3_REFERENCE != script_json[LANGUAGE]:
            changed = True
            script_json[LANGUAGE] = PYTHON3_REFERENCE

            script_json[SCRIPT_TEXT] = upgrade_script(script_json[SCRIPT_TEXT])
            self.soar_helper.put_script(script_json["id"], script_json)
        return changed, script_json

    def analyze_conditions(self, etree_xml) -> bool:
        is_py2 = False
        """ return True if python 2 found in a condition """
        condition_expressions = etree_xml.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}conditionExpression")
        for condition_expression in condition_expressions:
            condition_json = json.loads(condition_expression.text)

            for condition in [cond for cond in condition_json["conditions"] if "script" == cond["method"]]:
                if LANGUAGE in condition["value"] and condition["value"][LANGUAGE] == PYTHON2_REFERENCE:
                    LOG.info("Condition found as py2")
                    is_py2 |= True

            #if SCRIPT_LANGUAGE in condition_json and condition_json[SCRIPT_LANGUAGE] == PYTHON2_REFERENCE:
            #    is_py2 |= True

        return is_py2

    def analyze_bpmn(self, wrkflw_plybk) ->Tuple[Union[dict, None], Union[dict, None], Union[dict, None], list]:
        found_py2_components = []
        xml = wrkflw_plybk["content"]["xml"]

        etree_xml = etree.XML(bytes(unquote(xml), "utf-8"))

        conditions_use_python2 = self.analyze_conditions(etree_xml)
        if conditions_use_python2:
            found_py2_components.append("conditions")

        is_definite_py2 = is_py2_language = is_py2_unicode = False
        for components_labels, analyze_schema, analyze_task_type, script_prefix, is_function in BPMN_SCHEMAS:

            definite_py2, \
            py2_language, \
            py2_unicode = self._analyze_bpmn(wrkflw_plybk,
                                             etree_xml,
                                             analyze_schema,
                                             analyze_task_type,
                                             script_prefix,
                                             is_function)

            is_definite_py2 |= definite_py2
            is_py2_language |= py2_language
            is_py2_unicode |= py2_unicode

            if definite_py2 or py2_language:
                found_py2_components.append(components_labels)

        return (wrkflw_plybk if is_definite_py2 else None,
                wrkflw_plybk if is_py2_language or conditions_use_python2 else None,
                wrkflw_plybk if is_py2_unicode else None,
                found_py2_components)

    def _analyze_bpmn(self, wrkflw_plybk, etree_xml, find_query, findall_query, script_prefix, is_function=True) -> Tuple[bool, bool, bool]:
        py2_unconvertible = py2_convertible = py2_unicode = False

        ns = etree_xml.nsmap
        service_tasks = etree_xml.findall(find_query)
        for service_task in service_tasks:
            try:
                bpmn_tasks = service_task.findall(findall_query, ns)
            except SyntaxError:
                # this happens differences in workflows and playbooks
                bpmn_tasks = []

            for bpmn_task in bpmn_tasks:
                task_name = service_task.get("name")

                if is_function:
                    bpmn_json = json.loads(bpmn_task.text)
                    unicode_workflow_pre, is_py2_pre, diff_pre = \
                        self.analyze_bpmn_script(task_name, bpmn_json, "pre_processing")

                    unicode_workflow_post, is_py2_post, diff_post = \
                        self.analyze_bpmn_script(task_name, bpmn_json, "post_processing")

                    py2_unconvertible |= bool(diff_pre or diff_post)
                    py2_convertible |= (unicode_workflow_pre or unicode_workflow_post or is_py2_pre or is_py2_post)
                    py2_unicode |= (bool(unicode_workflow_pre) or bool(unicode_workflow_post))
                else:
                    # local scripts need to be loaded as they are not embedded in playbooks
                    if not bpmn_task.text:
                        external_script = self.get_script_by_uuid(wrkflw_plybk, bpmn_task.get("uuid"))

                        if not external_script:
                            LOG.warning(f"Unable to find script by UUID: {bpmn_task.get('uuid')}")
                            continue

                        is_py2 = False
                        unicode_playbook = False
                        diff = None
                        if not LANGUAGE in external_script or external_script.get(LANGUAGE) == PYTHON2_REFERENCE:
                            unicode_playbook, is_py2, diff_wo_unicode = \
                                self.analyze_script(external_script.get(SCRIPT_TEXT, ""), external_script.get("name"))

                            diff = None
                            if is_py2 and diff_wo_unicode:
                                diff = external_script.get("name")
                    else:
                        # in-line script. could be endEvent or callActivity
                        bpmn_json = json.loads(bpmn_task.text)
                        unicode_playbook, is_py2, diff = \
                            self.analyze_bpmn_script(None, bpmn_json, script_prefix)

                    py2_unconvertible |= bool(diff)
                    py2_convertible |= (unicode_playbook or is_py2)
                    py2_unicode |= bool(unicode_playbook)

        return (py2_unconvertible, py2_convertible, py2_unicode)

    def get_script_by_uuid(self, wrkflw_plybk, script_uuid: str) -> dict:
        # is it in "local_scripts"
        for script in wrkflw_plybk.get("local_scripts", []):
            if script.get("uuid") == script_uuid:
                return script

        return self.soar_helper.get_script_by_uuid(script_uuid)

    def analyze_bpmn_script(self, task_name: str, bpmn_json: dict, property_base_name: str) -> Tuple[Union[dict, None], bool, Union[dict, None]]:
        script_property_name = f"{property_base_name}_script" if property_base_name else "script"
        script_language_property_name = f"{script_property_name}_language"
        diff_property_name = f"{script_property_name}_diff"

        if script_property_name in bpmn_json and bpmn_json[script_property_name]:
            diff_w_unicode = 0
            py2_found = False
            if not script_language_property_name in bpmn_json or PYTHON3_REFERENCE != bpmn_json[script_language_property_name]:
                diff_w_unicode, py2_found, diff_wo_unicode = \
                    self.analyze_script(bpmn_json[script_property_name], task_name)

                if py2_found and diff_wo_unicode:
                    return diff_w_unicode, py2_found, {f"{task_name}_{diff_property_name}": diff_wo_unicode}

            return diff_w_unicode, py2_found, None
        return None, False, None

    def analyze_script(self, script_content:str, script_name) -> Tuple[bool, bool, list]:
        script_text_newline = end_script_with_newline(script_content)
        converted_wo_unicode, converted_w_unicode = test_upgrade_script(script_text_newline, script_name)
        if converted_wo_unicode:
            diff_wo_unicode = list(context_diff(script_text_newline.split("\n"), converted_wo_unicode.split("\n"), "Python2", "Python3"))
            diff_w_unicode = len(list(context_diff(script_text_newline.split("\n"), converted_w_unicode.split("\n"), "Python2", "Python3")))>0

            LOG.info("Script found with Py2: %s", script_name)
            return diff_w_unicode, True, diff_wo_unicode

        return False, False, None

class FindPY2_SOAR(FindPY2):
    def __init__(self, soar_helper: SOARHelper):
        super().__init__(soar_helper)

    def analyze_scripts(self, inputs: dict) -> dict:
        """list scripts by id, programmatic_name"""
        if inputs.get("py2_item_id") and inputs.get("py2_item_type") == "script":
            scripts_json = self.soar_helper.get_script(inputs.get("py2_item_id"))

            if not scripts_json:
                raise IntegrationError(f"Unable to locate script id: {inputs.get('py2_item_id')}")
            scripts_json = [scripts_json]
        elif not inputs.get("py2_item_id"):
            scripts_json = self.soar_helper.get_scripts()
        else:
            raise IntegrationError(f"'{inputs.get('py2_item_type')}' incorrect for id: {inputs.get('py2_item_id')}")

        return self._analyze_scripts(self.filter_on_tags(inputs.get("py2_search_tags"), inputs.get("py2_item_name"), scripts_json))

    def get_script_content(self, element_id, _element):
        script = self.soar_helper.get_script(element_id)
        return script.get(SCRIPT_TEXT)

    def analyze_workflows(self, inputs: dict):
        """list workflow by id, programmatic_name"""
        if inputs.get("py2_item_id") and inputs.get("py2_item_type") == "workflow":
            workflows_json = [self.soar_helper.get_workflow(inputs.get("py2_item_id"))]
        elif not inputs.get("py2_item_id"):
            workflows_json = self.soar_helper.get_workflows().get("entities", [])
        else:
            raise IntegrationError(f"'{inputs.get('py2_item_type')}' incorrect for id: {inputs.get('py2_item_id')}")

        return self._analyze_workflows(self.filter_on_tags(inputs.get("py2_search_tags"), inputs.get("py2_item_name"), workflows_json))

    def analyze_playbooks(self, inputs: dict):
        """list workflow by id, programmatic_name"""
        if inputs.get("py2_item_id") and inputs.get("py2_item_type") == "playbook":
            playbooks_json = [self.soar_helper.get_playbook(inputs.get("py2_item_id"))]
        elif not inputs.get("py2_item_id"):
            playbooks_json = self.soar_helper.get_playbooks().get("data", [])
        else:
            raise IntegrationError(f"'{inputs.get('py2_item_type')}' incorrect for id: {inputs.get('py2_item_id')}")

        return self._analyze_playbooks(self.filter_on_tags(inputs.get("py2_search_tags"), inputs.get("py2_item_name"), playbooks_json))

# class FindPY2_APP(FindPY2):
    # def __init__(self, soar_helper: SOARHelper, file_path: str, tags: str=""):
    #     super().__init__(soar_helper, tags)
    #     if not os.path.exists(file_path):
    #         print(f"file does not exist: {file_path}")
    #         sys.exit(1)

    #     # export.res file already in json format
    #     if EXPORT_RES in file_path:
    #         with open(file_path, "r", encoding="utf-8") as f:
    #             self.export_res = json.load(f)
    #     elif "customize.py" in file_path:
    #         # older customize.py files have embedded base64 encoded version of export.res
    #         with open(file_path, "r", encoding="utf-8") as f:
    #             export_res_customize = f.read()

    #         # older embedded code?
    #         match = IMPORT_DEFINITION.search(export_res_customize)
    #         if match:
    #             self.export_res = json.loads(base64.b64decode(match.group(1)))
    #         # newer logic referencing export.res file?
    #         elif EXPORT_RES_PATH in export_res_customize:
    #             # change the file_path to the export.res file for lookup
    #             file_path = os.path.join(os.path.dirname(file_path), EXPORT_RES_PATH)
    #             with open(file_path, "r", encoding="utf-8") as f:
    #                 self.export_res = json.load(f)
    #         else:
    #             # not clear what's needed
    #             print(f"No embedded data in file: {file_path}")
    #             sys.exit(1)
    #     else:
    #         print(f"Unrecognized file name: {file_path}")
    #         sys.exit(1)

    # def get_script_content(self, _element_id, element):
    #     return element.get(SCRIPT_TEXT)

    # def analyze_scripts(self):
    #     """list scripts by id, programmatic_name"""
    #     scripts_json = self.export_res.get(SCRIPTS_PATH) if self.export_res.get(SCRIPTS_PATH) else {}
    #     return self._analyze_scripts(scripts_json)

    # def analyze_workflows(self):
    #     workflow_json = self.export_res.get(WORKFLOWS_PATH) if self.export_res.get(WORKFLOWS_PATH) else {}
    #     return self._analyze_workflows(workflow_json)

    # def analyze_playbooks(self):
    #     playbook_json = self.export_res.get(PLAYBOOKS_PATH) if self.export_res.get(PLAYBOOKS_PATH) else {}
    #     return self._analyze_playbooks(playbook_json)

def check_upgrade(script_content: str, context: str) -> Tuple[list, bool]:
    script_content_newline = end_script_with_newline(script_content)
    converted_without_unicode, converted_w_unicode = test_upgrade_script(script_content_newline, context)
    unicode_changes_only = bool(converted_w_unicode != script_content_newline)
    if converted_without_unicode != script_content_newline:
        diff = list(context_diff(script_content.split("\n"), converted_without_unicode.split("\n"), "Python2", "Python3"))
        return diff, unicode_changes_only
    return None, unicode_changes_only

def test_upgrade_script(script_content: str, element_name: str) ->Tuple[str, str]:
    without_unicode = None
    unicode_only = None
    try:
        without_unicode = end_script_with_newline(script_content)
        without_unicode = str(PY_CONVERTER_IGNORE_UNICODE.refactor_string(without_unicode, "<test_upgrade_script>"))
    except Exception as pe:
        LOG.error("PY_CONVERTER_IGNORE_UNICODE Error for %s", element_name)
        LOG.error(str(pe))
        LOG.error(script_content)

    unicode_only = upgrade_script(script_content, test_upgrade=True)

    return without_unicode, unicode_only

def upgrade_script(script_content: str, test_upgrade=False) -> str:
    if not script_content:
        return None

    script_content_newline = end_script_with_newline(script_content) # ensure ends with newline for refactor_string method
    if test_upgrade:
        script_content_newline = script_content_newline.replace("java.util.date", "datetime")
    else:
        # py3 uses emailmessage.sender
        script_content_newline = script_content_newline.replace(".from", ".sender")
    try:
        refactor_script_content = str(PY_CONVERTER_JUST_UNICODE.refactor_string(script_content_newline.replace(".from", ".sender"), "<upgrade_script>"))
    except Exception as pe:
        LOG.error("PY_CONVERTER_JUST_UNICODE Error for %s", script_content_newline)
        LOG.error(str(pe))
        refactor_script_content = script_content

    return refactor_script_content


def add_diff(wrkflw_or_plbk, key, diff) -> None:
    if diff:
        if not wrkflw_or_plbk.get(key):
            wrkflw_or_plbk[key] = {}
        wrkflw_or_plbk[key] |= diff

def end_script_with_newline(script_content: str) -> str:
    """ ensure scripts end with a newline. This is necessary for refactor_string py2 to py3 transformation """
    if script_content and (script_content[-1] != "\n"):
        return f"{script_content}\n"
    return script_content

# if __name__ == "__main__":
#     clazz = None

#     if len(sys.argv) == 2:
#         # assume a file path
#         clazz = FindPY2_APP(sys.argv[1])
#     elif len(sys.argv) == 4:
#         # assume a SOAR host
#         base_url = sys.argv[1]
#         org = sys.argv[2]
#         user = sys.argv[3]
#         is_email_addr = user.find("@")

#         pwd = getpass(f"Please enter the password for {'user' if is_email_addr else 'api key'} {user}: ")

#         simple_client = SimpleClient(base_url=base_url, org_name=org, verify=False)
#         if is_email_addr:
#             simple_client.connect(user, pwd)
#         else:
#             simple_client.set_api_key(user, pwd)
#         clazz = FindPY2_SOAR(simple_client)
#     else:
#         print("*** Incorrect number of arguments")
#         print(f'Usage: {__file__} "https://<host>" "<org>" "<email | API key ID>" to query SOAR')
#         print(f'Usage: {__file__} "</path/to/customize.py | /path/to/export.res>" to query an App')
#         sys.exit(1)

#     py_list = clazz.start()
#     for category_key, category_values in [(cat_key, cat_values) for cat_key, cat_values in py_list.items() if cat_values]:
#         print(f"PY2 {category_key}s")
#         for item_id, item_info in category_values.items():
#             print(f"{item_info.get('name')}")
#             for attr in item_info.get("attributes", []):
#                 print(f"* {attr}")
