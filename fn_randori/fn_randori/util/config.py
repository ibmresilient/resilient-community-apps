# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_randori"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_randori when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_randori]
# Randori API token
api_token=xxx
# Randori REST API endpoint
endpoint_url=https://app.randori.io
# Randori tenant name
tenant_name=xxx
# Randori REST API version
api_version=v1
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs.
polling_lookback=120
verify= false | /path/to/cafile.crt
# Optional: polling filters that can be applied when querying Randori for new targets or targets to be updated.
# Each filter is a tuple in the following format: ("field","operator","value")
# Where:
#   "field" in the Randori target field to be queried
#   "operator" is a string operator as defined in Randori (for example: "less", "less_or_equal", "equal") 
#   "value" is the value to be compared against in the query
# If more than one filter is needed separate each tuple with a comma
#polling_filters=("target_temptation","greater_or_equal",40),("status","equal",["Needs Resolution", "Needs Review"]),("authority","equal","True")
# Optional:
# soar_create_case_template
# soar_close_case_template
# soar_update_case_template
#
"""
    return config_data
