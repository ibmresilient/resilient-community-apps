import os
import glob
import json
import pickle
import time
import pandas as pds
import logging
from fn_machine_learning.lib.multi_id_binarizer import MultiIdBinarizer

DATA_FOLDER_PATH = None

ACTIVE_MODEL_FILE = "active_model.json"

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
SUPPORTED_METHODS = [
    u"None",
    u"Bagging",
    u"Adaptive Boosting"
]
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
    mlconfig.model_name = ml_opt.get("algorithm", "").strip()
    mlconfig.addition_method = ml_opt.get("method", "").strip()
    mlconfig.predict_field = ml_opt.get("prediction", None)
    selected = ml_opt.get("features", []).split(',')
    mlconfig.split_percentage = float(ml_opt.get("split", 0.5))
    mlconfig.selected_features = []

    for select in selected:
        mlconfig.selected_features.append(select.strip())


def update_config_from_saved_model(model_file, mlconfig):

    model = pickle.load(open(model_file, "rb"))
    mlconfig.selected_features = list(model.features)
    mlconfig.predict_field = model.prediction
    mlconfig.model_name = model.get_name()
    mlconfig.split_percentage = 0.5
    try:
        mlconfig.addition_method = model.method_name
    except Exception:
        mlconfig.addition_method = None


def get_default_encoder(features, csv_file, separator=','):
    """
    Get the default preprocess for selected features
    :param features: selected features from the csv_file
    :param csv_file: csv file containing samples
    :return:
    """
    preprocess = {}
    log = logging.getLogger(__name__)

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
    re = {}
    count = {}
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
        re[key] = cor/count[key]

    return re




