# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""AppFunction implementation"""
import xml.etree.ElementTree as ET
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_playbook_utils.lib.common import get_workflow

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "wf_get_workflow_content"

ACTION_MAP = {
    'callActivity': 'Workflows',
    'serviceTask': 'Functions',
    'scriptTask': 'Scripts',
    'userTask': 'Tasks'
}


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'wf_get_workflow_content'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the content of functions, scripts, tasks and sub-workflows used within a workflow
        Inputs:
            -   fn_inputs.wf_workflow_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        workflow_xml = get_workflow(self.rest_client(), fn_inputs.wf_workflow_id)
        if not workflow_xml:
            msg = "workflow_id not found: {}".format(fn_inputs.wf_workflow_id)
            yield self.status_message(msg)
            yield FunctionResult({}, success=False, reason=msg)
        else:
            results = get_workflow_elements(workflow_xml)
            yield FunctionResult(results)

def get_workflow_elements(xml, action_map=ACTION_MAP):
    """[parse the xml for a workflow and extract the names of it's elements: artifacts,
        tasks, attachements, scripts, sub-workflows]

    Args:
        xml ([string]): [xml data for workflow]
        action_map ([list], optional): [list of elements to extract]. Defaults to ACTION_MAP.
    """
    # parse the xml
    tree = ET.ElementTree(ET.fromstring(xml))

    results = {}
    # walk the xml looking for the content we want
    for el in tree.find('{http://www.omg.org/spec/BPMN/20100524/MODEL}process').iter():
        # remove the name space
        _, has_namespace, postfix = el.tag.partition('}')
        if has_namespace:
            el.tag = postfix  # strip all namespaces

        if el.tag in ACTION_MAP.keys():
            el_type = ACTION_MAP[el.tag]
            if results.get(el_type):
                results[el_type].append(el.attrib['name'])
            else:
                results[el_type] = [ el.attrib['name'] ]

    return results
