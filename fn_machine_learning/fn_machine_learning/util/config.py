# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_machine_learning"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""
[machine_learning_predict]
#   The folder for saved models
model_dir=path to the folder of saved machine learning models you built

"""
    return config_data
