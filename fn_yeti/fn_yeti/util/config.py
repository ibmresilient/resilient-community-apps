# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_yeti"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_yeti when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_yeti]
url=<yeti_instance_url> # ex. http://localhost:8080/api
username=<yeti_instance_username> 
password=
apikey=<apikey_value>
"""
    return config_data
