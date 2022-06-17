# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_google_cloud_scc"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_google_cloud_scc when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_google_cloud_scc]
# path to google application credentials JSON file
google_application_credentials_path=
# organization id of your google cloud organization (found in the cloud console UI)
google_cloud_organization_id=
# optional findings filter -- used when poller is active and is default if no filter is provided on manual actions
# findings_filter=

# Optional override value for templates used for creating/updating/closing SOAR cases
#soar_create_case_template=
#soar_update_case_template=
#soar_close_case_template=

# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs.
polling_lookback=120
cafile=/path/to/cafile.crt or false
"""
    return config_data
