# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""Utility functions for Resilient API"""

from fn_machine_learning.lib.ml_logistic_regression import LogisticRegression
from fn_machine_learning.lib.ml_svm import MlSVC
from fn_machine_learning.lib.ml_decision_tree import MlDecisionTree
from fn_machine_learning.lib.ml_random_forest import MlRandomForest
from fn_machine_learning.lib.ml_gaussiannb import MlGaussianNB
from fn_machine_learning.lib.ml_bernoullinb import MlBernoulliNB
from fn_machine_learning.lib.ml_knn import MlKNN
import logging
import json
import urllib


def get_model(name, class_weight=None, method=None):
    model = None
    if name == "Logistic Regression":
        model = LogisticRegression(method=method, class_weight=class_weight)
    elif name == "SVM":
        model = MlSVC(method=method, class_weight=class_weight)
    elif name == "SVM with Gaussian kernel":
        model = MlSVC(kernel="rbf", method=method, class_weight=class_weight)
    elif name == "Decision Tree":
        model = MlDecisionTree(method=method, class_weight=class_weight)
    elif name == "Random Forest":
        model = MlRandomForest(method=method, class_weight=class_weight)
    elif name == "GaussianNB":
        model = MlGaussianNB(method=method, class_weight=class_weight)
    elif name == "BernoulliNB":
        model = MlBernoulliNB(method=method, class_weight=class_weight)
    elif name == MlKNN.get_name():
        model = MlKNN(method=method, class_weight=class_weight)

    return model


class MlSummary(object):
    def __init__(self):
        self.accuracy = 0.0
        self.prediction = ""
        self.build_time = ""


class MlConfig(object):

    ML_MODEL_LOGISTIC_REGRESSION = 0
    ML_MODEL_SVM = 1
    ML_MODEL_DECISION_TREE = 2
    ML_MODEL_RANDOM_FOREST = 3
    ML_MODEL_GAUSSIAN = 4

    NAME_MAPPING = {
        "Logistic Regression" : ML_MODEL_LOGISTIC_REGRESSION,
        "Decision Tree": ML_MODEL_DECISION_TREE,
        "Random Forest": ML_MODEL_RANDOM_FOREST
    }

    def __init__(self):
        self.data_file = None
        self.selected_features = []
        self.predict_field = None
        self.num_samples = 0
        self.split_percentage = 0.5
        self.model = self.ML_MODEL_LOGISTIC_REGRESSION
        self.model_name = "Logistic Regression"
        self.addition_method = None
        self.host = None
        self.separator = ','
        self.saved_models = []
        self.feature_preprocess = {}
        self.active_model = None
        self.rebuild_model = None

    def set_ml_model(self, name):
        self.model = self.NAME_MAPPING.get(name, self.ML_MODEL_LOGISTIC_REGRESSION)


def get_incidents(res_client, filename, max_count=None, in_log=None):
    """
    Convert JSON into CSV and save
    :param res_client: incidents in json format
    :param filename: file name for saving CSV
    :return:
    """
    log = in_log if in_log else logging.getLogger(__name__)

    # Read the fields of an incident
    inc_fields = res_client.get("/types/incident")

    fields_dict = inc_fields.get("fields", {})
    log.debug("Incident Fields: " + str(fields_dict))

    # Get all the incidents
    #ret = res_client.get("/incidents")
    ret = query_incidents(res_client=res_client,
                          max_count=max_count)

    with open(filename, "w") as outfile:
        # Write everything into a CSV file
        # Write header
        fields = list(fields_dict.keys())
        for field in fields[:-1]:
            outfile.write(field + ",")
        outfile.write(fields[-1] + '\n')

        inc_count = 0
        for inc in ret:
            field_count = 0
            for field in fields[:-1]:
                field_count = field_count + 1
                try:
                    value = str(inc.get(field, inc["properties"].get(field, "")))
                except UnicodeEncodeError:
                    value = inc.get(field, inc["properties"].get(field, "")).encode("ascii", "ignore").decode("ascii")
                except Exception:
                    value = ""
                #
                # Since we use csv, put quote if value contains \n or ,
                # value with those two special chars needs preprocessed
                # anyway
                #

                #
                # @TODO
                # It seems like there is a bug in pandas read_csv. Even though
                # quotechar is set to ", it still gets confused by the comma below:
                # "From: Faith Csikesz <faith@secretweaponleader.com>\\nTo: \\"Linda.Pham@ALLERGAN.com\\" <Linda.Pham@ALLERGAN.com>\\nSubject: Feedback Perceptions Survey for Claire Sears\\nDate: Thu, 16 Aug 2018 17:15:37 +0000\\n"
                # but it has no trouble with the comma below.
                # "Date: Wed, 27 Jun 2018 10:30:10 -0400\\nFrom: \\"Gartner Insights\\" <GartnerInsights@Gartner-promo.com>\\nSubject: Have You Explored Gartner Peer Insights Yet?\\nTo: ijessop@lifecell.com\\n"
                #
                # So by now we just remove the comma, since we don't handle NLS yet.
                #
                try:
                    tmp = json.loads(value)
                except Exception as e:
                    #
                    # value could be a list. Only replace for string
                    #
                    value = value.replace(',', ' ')
                #
                #
                # @TODO
                # If customer entered something wrong, like mismatched ' and ", the
                # value = json.dumps(value) won't help.
                #
                #if '"' in value:
                #    value = json.dumps(value)
                value = value.replace('"', ' ')
                if '\n' in value or ',' in value:
                    value = '"' + value + '"'
                outfile.write(value + ",")
            value = str(inc.get(fields[-1], ""))
            outfile.write(value + '\n')
            inc_count = inc_count + 1
            if max_count and inc_count >= max_count:
                log.info("Truncated samples at " + str(max_count))
                break

    return inc_count


def get_field_def(resilient_client, field, type_name, in_log=None):
    """
    Call the /types/{type}/fields/{field_name} to get the mapping
    between numerical value and label.
    Once a prediction is done, we will use this mapping to
    convert the numerical value back to label.
    :param resilient_client:
    :param field:
    :param type_name:
    :param in_log: log
    :return:
    """
    log = in_log if in_log else logging.getLogger(__name__)
    url_path = "/types/{}/fields/{}".format(type_name, field)
    json_dict = resilient_client.get(url_path)

    ret = {}
    if json_dict:
        log.debug("Field def: {}".format(json_dict))
        values = json_dict.get("values", [])
        for val in values:
            #
            #   For classification, we always assume prediction to be
            #   string. We forced it to be object type when
            #   we read using pandas.read_csv. So here we convert
            #   the value to string as well
            #
            ret[str(val["value"])] = val["label"]
    else:
        log.error("get_field_def for field = {}, and type = {} returned Null".format(field, type_name))

    return ret


def query_incidents(res_client, max_count=None, page_size=1000):
    """
    Use the query endpoint since we are going to down load
    large number of incidents.
    :param res_client:
    :param max_count:
    :param page_size:
    :return:
    """
    incidents = []
    url = "/incidents/query_paged?field_handle=-1&return_level=full"
    num_incidents = 0
    ret_num = 0
    done = False
    while not done:
        body = {
            "start": num_incidents,
            "length": page_size,
            "recordsTotal": page_size
        }
        ret = res_client.post(uri=url,
                              payload=body)

        data = ret.get("data", [])
        ret_num = len(data)
        if ret_num > 0:
            incidents.extend(data)
        else:
            #
            # No more to read.
            #
            done = True

        num_incidents = num_incidents + ret_num

        if max_count:
            if num_incidents >= max_count:
                #
                # Reach max_count set by user, stop now
                #
                done = True

    return incidents
