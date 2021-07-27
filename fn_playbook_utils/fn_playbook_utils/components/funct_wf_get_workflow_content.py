# -*- coding: utf-8 -*-

"""AppFunction implementation"""
import xml.etree.ElementTree as ET
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
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

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self._app_configs_as_dict)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Call API implemtation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()

        ##############################################

        workflow_xml = get_workflow(self.rest_client(), fn_inputs.wf_workflow_id)
        if not workflow_xml:
            msg = "workflow_id not found: {}".format(fn_inputs.wf_workflow_id)
            yield self.status_message(msg)
            yield FunctionResult({}, success=False, reason=msg)

        # parse the xml
        tree = ET.ElementTree(ET.fromstring(workflow_xml))

        results = {}
        # walk the xml looking for the content we want
        for el in tree.find('{http://www.omg.org/spec/BPMN/20100524/MODEL}process').iter():
            # remove the name space
            _, has_namespace, postfix = el.tag.partition('}')
            if has_namespace:
                el.tag = postfix  # strip all namespaces

            if el.tag in ACTION_MAP.keys():
                type = ACTION_MAP[el.tag]
                if results.get(type):
                    results[type].append(el.attrib['name'])
                else:
                    results[type] = [ el.attrib['name'] ]

        yield FunctionResult(results)
