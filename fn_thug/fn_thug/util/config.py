# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_thug"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_thug]
thug_dir=Absolute path to a directory that can be mounted into a docker container. Go to Docker -> Preferences -> File Sharing to configure.
"""
    return config_data