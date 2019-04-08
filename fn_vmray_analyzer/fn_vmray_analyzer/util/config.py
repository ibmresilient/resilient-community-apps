# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_vmray_analyzer"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_vmray_analyzer]
# Your VMRay Analyzer API Key                                                         
vmray_api_key=

# Your VMRay Server URL, using https://cloud.vmray.com if empty.
vmray_analyzer_url=https://cloud.vmray.com
             
# Amount of time in seconds to wait until checking if the report is ready again.
vmray_analyzer_report_request_timeout=60 
"""
    return config_data