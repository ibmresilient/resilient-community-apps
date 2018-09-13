# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_machine_learning"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""
[machine_learning_predict]
# model file
active_model=path_and_file_name_of_saved_model_to_be_used_for_prediction
    
[machine_learning]
prediction=severity_code
features=incident_type_ids, confirmed, negative_pr_likely, nist_attack_vectors
algorithm=Logistic Regression
#method can be Bagging or Adaptive Boost
method=Adaptive Boosting
split=0.5
"""
    return config_data
