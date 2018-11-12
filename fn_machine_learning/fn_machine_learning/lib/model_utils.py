# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    model_utils
    -----------
    Collection of util functions related to ML model
"""
import json
import pickle
import pandas as pds
import logging
from fn_machine_learning.lib.multi_id_binarizer import MultiIdBinarizer
from sklearn.metrics import precision_score, recall_score, f1_score

#
#   All the algorithms supported by this integration package
#
SUPPORTED_ALGORITHMS = [
    u"Logistic Regression",
    u"SVM",
    u"SVM with Gaussian kernel",
    u"Decision Tree",
    u"Random Forest",
    u"GaussianNB",
    u"BernoulliNB",
    u"K-Nearest Neighbor"
]
#
#   Ensemble methods
#
SUPPORTED_METHODS = [
    u"None",
    u"Bagging",
    u"Adaptive Boosting"
]
#
#   Future features
#
SUPPORTED_PREPROCESS = [
    u"None",
    u"Min Max Scaler",
    u"One Hot Encoder",
    u"Label Encoder",
    u"Binarizer",
    u"Resilient Binarizer for multiple select",
    u"Multiple Label Binarizer"
]


def update_config_from_app_config(ml_opt, mlconfig):
    """
    Use data from app.config to update the mlconfig structure.
    The mlconfig structure is used to build a ML model

    This is used to build new ml model. We read config data
    from app.config, update mlconfig accordingly, and then build

    :param ml_opt:          Config data from app.config
    :param mlconfig:        mlconfig structure to update
    :return:
    """
    mlconfig.model_name = ml_opt.get("algorithm", "").strip()
    mlconfig.addition_method = ml_opt.get("method", "").strip()
    mlconfig.predict_field = ml_opt.get("prediction", None)
    selected = ml_opt.get("features", []).split(',')
    unwanted_values = ml_opt.get("unwanted_values", "").split(',')
    mlconfig.split_percentage = float(ml_opt.get("split", 0.5))
    mlconfig.class_weight = ml_opt.get("class_weight", None)
    imbalance_upsampling = ml_opt.get("imbalance_upsampling", None)
    if imbalance_upsampling and imbalance_upsampling.lower() == "true":
        mlconfig.imbalance_upsampling = True
    elif imbalance_upsampling and imbalance_upsampling.lower() == "false":
        mlconfig.imbalance_upsampling = False
    else:
        try:
            mlconfig.imbalance_upsampling = json.loads(imbalance_upsampling)
        except Exception as e:
            mlconfig.imbalance_upsampling = False

    mlconfig.selected_features = []

    for select in selected:
        mlconfig.selected_features.append(select.strip())

    mlconfig.unwanted_values = []

    for value in unwanted_values:
        mlconfig.unwanted_values.append(value.strip())


def update_config_from_saved_model(model_file, mlconfig):
    """
    Update mlconfig with config data from a saved model file.

    This is used to rebuild a model from a saved model file.
    We update the mlconfig structure using data from the saved model

    :param model_file:      saved model file
    :param mlconfig:        mlconfig to update
    :return:
    """
    model = pickle.load(open(model_file, "rb"))
    mlconfig.selected_features = list(model.config.selected_features)
    mlconfig.predict_field = model.config.predict_field
    mlconfig.class_weight = model.config.class_weight
    mlconfig.model_name = model.get_name()
    mlconfig.num_samples = model.config.number_samples
    mlconfig.imbalance_upsampling = model.config.imbalance_upsammpling
    mlconfig.unwanted_values = list(model.config.unwanted_values)
    mlconfig.split_percentage = 0.5
    try:
        mlconfig.addition_method = model.config.addition_method
    except Exception:
        mlconfig.addition_method = None


def get_default_encoder(features, csv_file, separator=',', in_log=None):
    """
    Get the default preprocess for selected features

    :param features:        selected features from the csv_file
    :param csv_file:        csv file containing samples
    :return:
    """
    preprocess = {}
    log = in_log if in_log else logging.getLogger(__name__)

    try:
        df = pds.read_csv(csv_file,
                          sep=separator,
                          usecols=features,
                          skipinitialspace=True,
                          quotechar='"')

        X = df[features]
        for col_name, col in X.iteritems():
            if col.dtype.name == "object":
                is_list = MultiIdBinarizer.is_multi_selection(col)
                if is_list:
                    preprocess[col_name] = u"object", u"Resilient Binarizer for multiple select"
                else:
                    preprocess[col_name] = u"object", u"Label Encoder"
            elif col.dtype.name == "float64":
                preprocess[col_name] = u"float64", u"Label Encoder"
            else:
                preprocess[col_name] = col.dtype.name, u"None"

    except Exception as e:
        log.error("Failed to read_csv: {f}\n Error: {err}".format(f=csv_file, err=str(e)))

    return preprocess


def analyze(y_true, y_pred):
    """
    Compute the accuracy for each value

    :param y_true:      List of actual value for prediction field. This is from the test data
    :param y_pred:      List of predicted value the model generate
    :return:
    """
    re = {}
    #
    #   count is a dict to store the count for each value
    #
    count = {}
    #
    #   correct is a dict to store the correct prediction for each value
    #
    correct = {}
    for t, p in zip(y_true, y_pred):
        if t in count:
            count[t] = count[t] + 1
        else:
            count[t] = 1

        if t == p:
            if t in correct:
                correct[t] = correct[t] + 1
            else:
                correct[t] = 1

    for key, value in count.iteritems():
        cor = correct.get(key, 0)
        re[key] = float(cor)/count[key]

    return re


def compute_recall(y_true, y_pred):
    """
    Use sklearn to compute recall:
    https://en.wikipedia.org/wiki/Precision_and_recall
    Recall is also called sensitivity.

    :param y_true:          The "true" value from the testing dataset
    :param y_pred:          The prediction given by the model for the testing dataset
    :return:
    """
    recall = recall_score(y_true=y_true,
                          y_pred=y_pred,
                          average="macro")
    return recall


def compute_precision(y_true, y_pred):
    """
    Compute precision:
    https://en.wikipedia.org/wiki/Precision_and_recall
    Precision is also called Positive Predictive Value.

    :param y_true:          The "true" value from the testing dataset
    :param y_pred:          The prediction given by the model for the testing dataset
    :return:                Precision score
    """
    return precision_score(y_true=y_true,
                           y_pred=y_pred,
                           average="macro")


def compute_f1(y_true, y_pred):
    """
    Compute F1-score:
    https://en.wikipedia.org/wiki/F1_score
    This is a measurement better than the overall accuracy because it takes in account
    of all the accuracy of all the values. It gives a more balanced view of the
    performance of a model, and it is also called the harmonic average of precision and
    recall.

    :param y_true:
    :param y_pred:
    :return:
    """
    return f1_score(y_true=y_true,
                    y_pred=y_pred,
                    average="macro")


def count_values(csv_file, field, in_log=None):
    """
    Read samples from the csv_file, and count values of the given field.

    This is used for detecting imbalanced dataset. Also user can use this
    to check if any value he/she wants to exclude. Things like Unknown is
    recommended to be excluded for example.

    :param csv_file:    Input CSV file with samples
    :param field:       Field to predict
    :param in_log:      Log
    :return:            dict of value counts
    """
    log = in_log if in_log else logging.getLogger(__name__)

    dataf = pds.read_csv(csv_file,
                         sep=',',
                         dtype={field: object},
                         skipinitialspace=True,
                         quotechar='"',
                         error_bad_lines=True)
    value_counts = dataf[field].value_counts()
    log.debug("Value counts of {} in {} is {}".format(field, csv_file, value_counts))

    return value_counts


