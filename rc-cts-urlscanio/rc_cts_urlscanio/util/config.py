# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_cts_urlscanio"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[urlscanio]

# Define the API URL
urlscan_io_search_api_url=https://urlscan.io/api/v1/search/
urlscan_io_result_api_url=https://urlscan.io/api/v1/result/

# Optional setting
# Number of results returned. 
# Comment out this line to return 100 results - the default.
#urlscan_io_search_size=10
    """
    return config_data
