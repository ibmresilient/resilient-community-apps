# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Generate a default configuration-file section for fn_mcafee_esm"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mcafee_esm]
    
# url example: https://127.0.0.1
esm_url=<your_esm_url>
esm_username=<your_esm_username>
esm_password=<your_esm_password>

# If your ESM server uses a cert which is not automatically trusted by your machine, set verify_cert=False.
verify_cert=[True|False]

## ESM Polling settings
# How often polling should happen. Value is in seconds. To disable polling, set this to zero.
esm_polling_interval=0
#incident_template=<location_of_template_file>  # If not set uses default template.
"""
    return config_data
