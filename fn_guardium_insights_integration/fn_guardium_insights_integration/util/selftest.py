# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn_guardium_insights_integration
    resilient-circuits selftest --print-env -l fn_guardium_insights_integration

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""
import logging
from fn_guardium_insights_integration.lib.insights_services import InsightsServices
import resilient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_guardium_insights_integration", {})
    try:
        log.info("Checking Guardium Insights connectivity and credentials...!")
        insights_service_obj = InsightsServices(options, log)
        insights_service_obj.list_all_reports()
        log.info("Checking Guardium Insights connectivity and credentials...OK")

        log.info("Checking Resilient Appliance connectivity and credentials")
        resilient.get_client(opts)
        log.info("Checking Resilient Appliance connectivity and credentials...OK")
        return {"state": "success", "reason": "Successful connection to third party endpoint"}
    except Exception as er:
        log.error(repr(er))
        return {"state": "failure", "reason": repr(er)}