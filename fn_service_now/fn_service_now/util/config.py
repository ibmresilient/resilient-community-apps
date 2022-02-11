# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_service_now"""


def config_section_data():
    """Produce the default configuration section for app.config,
        when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_service_now]
sn_host=https://instance.service-now.com
sn_api_uri=/api/x_ibmrt_resilient/api

# Name of the table in ServiceNow to sync with.
# as of v2.0.0 the incident table and the sn_si_incident table are supported
# (NOTE: ServiceNow Security Incident Response module is required for sn_si_incident)
sn_table_name=incident

# Username + Password of ServiceNow Integrator user who has the the "x_ibmrt_resilient.integrator" role
sn_username=<ServiceNow Username>
sn_password=<ServiceNow Password>

# (ONLY FOR CP4S with custom endpoint) Enter the custom cases-rest prefix of your CP4S instance
# ex: if host is my-cases-rest.cp4s.ibmsecurity.com, cp4s_cases_prefix=my-cases-rest
# If you don't have a custom cases rest endpoint there is no need to use this config value
#cp4s_cases_prefix=<CP4S Cases Rest Custom Prefix>
"""
    return config_data
