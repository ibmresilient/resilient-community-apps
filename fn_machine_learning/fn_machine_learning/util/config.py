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
    
[machine_learning]
#
#   Field  to predict
#
prediction=severity_code
#
#   Features to use
#       example: features=confirmed, incident_type_ids, negative_pr_likely
features=list_of_fields_for_features_separated_by_comma
#
#   Algorithms supported:
#       Logistic Regression, Decision Tree, Random Forest, Dummy Classifier
#       SVM, SVM with Gaussian kernel, GaussianNB, BernoulliNB, K-Nearest Neighbors
algorithm=Logistic Regression
#
#   Ensemble method is optional, it can be Bagging or Adaptive Boosting (Optional)
#
method=None
#
#   Split samples for testing. 0.5 means 50% of the samples will be used for testing
#
split=0.5

#
# Advanced options
#-----------------
#
#   1. Imbalance Class
#
#   Predicted data could be imbalanced. Uncomment one of the following option
#   to handle it
#
class_weight=balanced
#imbalance_upsampling=true
#
#   2. Data Preparation
#
#   Some prediction values could be misleading for the machine learning model
#   Put those values below. Samples with those values will be removed
#
unwanted_values=None
#
#   3. Filter (Optional)
#
#       * Time filter: format YYYY-mm-dd
#
#time_start=2018-10-01
#time_end=2018-10-08
#
#       * Count: Maximum number of samples to process
#
#max_count = 10000
"""
    return config_data
