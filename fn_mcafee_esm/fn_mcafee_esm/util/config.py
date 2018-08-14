# -*- coding: utf-8 -*-

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

# If your ESM server uses a cert which is not automatically trusted by your machine set trust_cert=False
trust_cert=[True|False]
"""
    return config_data
