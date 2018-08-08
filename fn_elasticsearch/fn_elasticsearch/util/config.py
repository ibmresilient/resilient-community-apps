  # -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Generate a default configuration-file section for fn_elasticsearch"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_elasticsearch]
es_datastore_url = <ELASTICSEARCH_URL>
es_datastore_scheme = <https OR http>
es_auth_username = <ELASTICSEARCH_USERNAME>
es_auth_password = <ELASTICSEARCH_PASSWORD>
es_cafile = <CA_FILE_TO_BE_USED>
"""
    return config_data
    