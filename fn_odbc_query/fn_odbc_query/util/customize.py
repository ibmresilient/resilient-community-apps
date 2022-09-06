# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_odbc_query"""

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
    Parameters required reload codegen for the fn_odbc_query package
    """
    return {
        "package": u"fn_odbc_query",
        "message_destinations": [u"fn_odbc_query"],
        "functions": [u"fn_odbc_query"],
        "workflows": [u"example_odbc_delete_postgresql", u"example_odbc_insert_postgresql", u"example_odbc_select_postgresql", u"example_odbc_update_postgresql"],
        "actions": [u"Example ODBC DELETE PostgreSQL", u"Example ODBC INSERT PostgreSQL", u"Example ODBC SELECT PostgreSQL", u"Example ODBC UPDATE PostgreSQL"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"sql_query_results_dt"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - fn_odbc_query
    - Functions:
        - fn_odbc_query
    - Workflows:
        - example_odbc_delete_postgresql
        - example_odbc_insert_postgresql
        - example_odbc_select_postgresql
        - example_odbc_update_postgresql
    - Rules:
        - Example ODBC DELETE PostgreSQL
        - Example ODBC INSERT PostgreSQL
        - Example ODBC SELECT PostgreSQL
        - Example ODBC UPDATE PostgreSQL
    - Data Tables:
        - sql_query_results_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)