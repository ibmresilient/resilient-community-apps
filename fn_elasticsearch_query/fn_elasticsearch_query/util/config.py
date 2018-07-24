# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_elasticsearch_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_elasticsearch_query]
es_datastore_url = 192.x.x.x:PORT
es_datastore_scheme = https
es_auth_username = elastic
es_auth_password = XXXX
es_cafile = None
"""
    return config_data