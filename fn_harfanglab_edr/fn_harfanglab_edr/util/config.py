# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_harfanglab_edr"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_harfanglab_edr when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_harfanglab_edr]
api_url=https://hurukai:8443/
api_key=<api key>
verify=false

# Optional proxy settings
#http_proxy=http://my-proxy:3128/
#https_proxy=http://my-proxy:3128/

# HarfangLab EDR poller settings
# Poller interval in seconds, comment out or set to 0 to disable poller
polling_interval=60

# Start fetching alerts whose creation date is higher than now minus <first_fetch> days.
first_fetch=10

# Fetch only security events with specific statuses (ACTIVE, CLOSED)
#alert_status=ACTIVE

# Comma-separated list of types of alerts to fetch (sigma, yara, hlai, vt, ransom, ioc, glimps, orion...).
#alert_type=sigma,yara,hlai,vt,ransom,ioc,glimps,orion

# Minimum severity of alerts to fetch (Informational, Low, Medium, High or Critical)
#min_severity=High

# Maximum number of alerts to fetch
#max_fetch=25

# Job timeout (default to 600)
#job_timeout=600

# Binary files can be downloaded and added to the incident attachments in zip format with a password protection (default: infected)
#archive_password=infected

#create_incident_template=
#update_incident_template=
#close_incident_template=
#agent_template=
"""
    return config_data
