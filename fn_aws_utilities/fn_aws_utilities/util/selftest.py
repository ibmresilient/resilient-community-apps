# -*- coding: utf-8 -*-

import logging
from fn_aws_utilities.util.aws_lambda_api import AWSLambda

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Calls the lightweight get_account_settings() endpoint to confirm AWS account access
    """
    app_configs = opts.get("fn_aws_utilities", {})

    try:
        lamb = AWSLambda(app_configs.get("aws_access_key_id"), app_configs.get("aws_secret_access_key"), app_configs.get("aws_region_name"))

        acct_settings = lamb.aws_client.get_account_settings()
        if isinstance(acct_settings , dict) and "AccountUsage" in acct_settings:
            return {"state": "success"}
        else:
            return {"state": "failure", "reason": "Could not retrieve account settings for AWS client"}

    except Exception as e:
        return {"state": "failure", "status_code": str(e)}
