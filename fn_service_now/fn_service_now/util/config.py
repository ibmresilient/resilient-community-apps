# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_service_now"""

from __future__ import print_function


def config_section_data():
  """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
  """
  config_data = u"""[fn_service_now]
sn_host=https://instance.service-now.com
sn_api_uri=/api/x_ibmrt_resilient/api

# Name of the table in ServiceNow to sync with
# v1.0.0 only supports the incident table
sn_table_name=incident

# Username + Password of ServiceNow Integrator user who has the the "x_ibmrt_resilient.integrator" role
sn_username=<ServiceNow Username>
sn_password=<ServiceNow Password>
"""
  return config_data
