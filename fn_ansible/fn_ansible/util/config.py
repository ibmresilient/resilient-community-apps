# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ansible"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ansible]
runner_dir=</full/path/to/your/ansible/directory>
artifact_dir=</full/path/to/artifacts/directory>
# change this value to trim the collection of previous process runs
artifact_retention_num=0
"""
    return config_data