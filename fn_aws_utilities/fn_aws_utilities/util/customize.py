# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_aws_utilities"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_aws_utilities package
    """
    return {
        "package": u"fn_aws_utilities",
        "message_destinations": [u"fn_aws_utilities"],
        "functions": [u"fn_get_step_function_execution", u"fn_invoke_lambda", u"fn_invoke_step_function", u"fn_send_sms_via_sns"],
        "workflows": [u"example_invoke_aws_lambda_python_addition", u"example_invoke_step_function_asynchronous", u"example_invoke_step_function_synchronous", u"example_send_sms_incident"],
        "actions": [u"Example: Invoke AWS Lambda: Python Addition", u"Example: Invoke AWS Step Function: Asynchronous", u"Example: Invoke AWS Step Function: Synchronous", u"Example: Send AWS SMS"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 41.0.6783

    Contents:
    - Message Destinations:
        - fn_aws_utilities
    - Functions:
        - fn_get_step_function_execution
        - fn_invoke_lambda
        - fn_invoke_step_function
        - fn_send_sms_via_sns
    - Workflows:
        - example_invoke_aws_lambda_python_addition
        - example_invoke_step_function_asynchronous
        - example_invoke_step_function_synchronous
        - example_send_sms_incident
    - Rules:
        - Example: Invoke AWS Lambda: Python Addition
        - Example: Invoke AWS Step Function: Asynchronous
        - Example: Invoke AWS Step Function: Synchronous
        - Example: Send AWS SMS
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)