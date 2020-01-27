# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_resilient_ml"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""
[fn_resilient_ml]
#
# Required. The (absolute) path to the folder of the saved NLP model
#
model_path=path_of_the_saved_models
num_top_similar_incidents=5

#
#   Advanced configuration
#-------------------------
# Use the followings to optimize the performance of a NLP model
#
# Number of features for NLP word2vec model.
num_features=50
"""
    return config_data
