# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_guardium_insights_integration"""

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
    Parameters required reload codegen for the fn_guardium_insights_integration package
    """
    return {
        "package": u"fn_guardium_insights_integration",
        "message_destinations": [u"guardium_insights_integration"],
        "functions": [u"function_guardium_insights_block_user", u"function_guardium_insights_classification_report", u"function_guardium_insights_populate_breach_data_types"],
        "workflows": [u"workflow_guardium_insights_block_user", u"workflow_guardium_insights_classification_report", u"workflow_guardium_insights_populate_breach_data_types"],
        "actions": [u"Guardium Insights Block User", u"Guardium Insights classification report data", u"Guardium Insights populate breach data types"],
        "incident_fields": [u"field_guardium_insights_config_id", u"field_guardium_insights_global_id", u"field_guardium_insights_what", u"field_guardium_insights_when", u"field_guardium_insights_where", u"field_guardium_insights_who", u"field_guardium_insights_why", u"guardium_insights_event_id"],
        "incident_artifact_types": [],
        "datatables": [u"guardium_insights_classification_report"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 36.0.5634

    Contents:
    - Message Destinations:
        - guardium_insights_integration
    - Functions:
        - function_guardium_insights_block_user
        - function_guardium_insights_classification_report
        - function_guardium_insights_populate_breach_data_types
    - Workflows:
        - workflow_guardium_insights_block_user
        - workflow_guardium_insights_classification_report
        - workflow_guardium_insights_populate_breach_data_types
    - Rules:
        - Guardium Insights Block User
        - Guardium Insights classification report data
        - Guardium Insights populate breach data types
    - Incident Fields:
        - field_guardium_insights_config_id
        - field_guardium_insights_global_id
        - field_guardium_insights_what
        - field_guardium_insights_when
        - field_guardium_insights_where
        - field_guardium_insights_who
        - field_guardium_insights_why
        - guardium_insights_event_id
    - Data Tables:
        - guardium_insights_classification_report
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)