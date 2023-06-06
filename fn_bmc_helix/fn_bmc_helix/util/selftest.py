# -*- coding: utf-8 -*-
import logging

from resilient_lib import RequestsCommon, validate_fields, str_to_bool
from fn_bmc_helix.lib.helix.HelixAPIClient import HelixClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

CONFIG_DATA_SECTION = "fn_bmc_helix"
FORM_NAME = "HPD:IncidentInterface_Create"

def selftest_function(opts):
    """
    Tests connectivity to the BMC Helix API by querying for the schema
    of the standard HPD:IncidentInterface_Create form. The method
    returns success if BMC Helix gives a 200 Response.
    """
    app_configs = opts.get(CONFIG_DATA_SECTION, {})

    # Get and validate app configs
    validate_fields([
        {"name": "helix_host", "placeholder": "<example.domain>"},
        {"name": "helix_user", "placeholder": "<example_user>"},
        {"name": "helix_password", "placeholder": "xxx"}],
        app_configs)

    host = app_configs.get("helix_host")
    user = app_configs.get("helix_user")
    password = app_configs.get("helix_password")
    port = app_configs.get("helix_port", None)
    verify = str_to_bool(app_configs.get("verify", "true"))

    rc = RequestsCommon(opts=opts)

    try:
        client = HelixClient(host, user, password, rc, port=port, verify=verify)
        schema, status_code = client.get_form_schema(FORM_NAME)

        if status_code == 200:
            return {
                "state": "success",
                "reason": "Successfully connected to the BMC Helix REST API."
            }
        return {
            "state": "failure",
            "reason": "Unexpected response from BMC Helix: {}".format(status_code)
        }
    except Exception as e:
        return {
            "state": "failure",
            "reason": e
        }
