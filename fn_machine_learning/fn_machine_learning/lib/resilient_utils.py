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
from fn_machine_learning.lib.ml_dummy_classifier import MlDummyClassifier
import logging
import csv


def get_model(name, imbalance_upsampling=None, class_weight=None, method=None):
    """
    Factory design pattern. Use name to get the corresponding ML model object

    :param name:                    Name of algorithm
    :param imbalance_upsampling:    Apply upsampling to compensate imbalanced dataset
    :param class_weight:            Apply class_weight approach to compensate imbalanced dataset
    :param method:                  Optional ensemble method
    :return:                        A model object built
    """
    model = None
    if name == "Logistic Regression":
        model = LogisticRegression(method=method,
                                   imbalance_upsampling=imbalance_upsampling,
                                   class_weight=class_weight)
    elif name == "SVM":
        model = MlSVC(method=method,
                      imbalance_upsampling=imbalance_upsampling,
                      class_weight=class_weight)
    elif name == "SVM with Gaussian kernel":
        model = MlSVC(kernel="rbf",
                      method=method,
                      imbalance_upsampling=imbalance_upsampling,
                      class_weight=class_weight)
    elif name == "Decision Tree":
        model = MlDecisionTree(method=method,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight)
    elif name == "Random Forest":
        model = MlRandomForest(method=method,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight)
    elif name == "GaussianNB":
        model = MlGaussianNB(method=method,
                             imbalance_upsampling=imbalance_upsampling,
                             class_weight=class_weight)
    elif name == "BernoulliNB":
        model = MlBernoulliNB(method=method,
                              imbalance_upsampling=imbalance_upsampling,
                              class_weight=class_weight)
    elif name == MlKNN.get_name():
        model = MlKNN(method=method,
                      imbalance_upsampling=imbalance_upsampling,
                      class_weight=class_weight)
    elif name == MlDummyClassifier.get_name():
        model = MlDummyClassifier()

    return model


def write_to_csv(incidents, fields_dict, filename, max_count=None, filter=None, in_log=None):
    """
    Write incidents to a CSV file according to the field definition.
    This function is factorized out intentionally for better unit test.

    :param incidents:       list of incidents in json
    :param fields_dict:     field definitions in json dict
    :param filename:        filename for CSV file to save samples
    :param max_count:       max count for incidents to save
    :param filter:          filter for incidents
    :param in_log:          log
    :return:                number of incidents saved to the CSV file
    """
    log = in_log if in_log else logging.getLogger(__name__)
    #
    #   Keep a count for samples
    #
    inc_count = 0
    with open(filename, "wb") as outfile:
        #
        #   Write everything into a CSV file, since scikit-learn uses CSV format for samples
        #
        fields = list(fields_dict.keys())
        csv_writer = csv.DictWriter(outfile,
                                    fieldnames=fields,
                                    dialect="excel")
        csv_writer.writeheader()

        for inc in incidents:
            #
            #   Call filter to figure if we want to keep this incident/sample
            #
            if filter is not None:
                shall_include = filter.shall_include_incident(inc)
                if not shall_include:
                    #
                    #   Filter it out. Continue to the next
                    #
                    continue

            new_dict = {}
            for field in fields:
                try:
                    #
                    #   The field could be a custom field, if so read from properties.
                    #
                    value = str(inc.get(field, inc["properties"].get(field, "")))
                except UnicodeEncodeError:
                    value = inc.get(field, inc["properties"].get(field, "")).encode("ascii", "ignore").decode("ascii")
                except Exception as e:
                    log.exception("Exception in reading incident field {}: {}".format(field, str(e)))
                    value = ""
                new_dict[field] = value

            csv_writer.writerow(new_dict)

            inc_count = inc_count + 1
            if max_count and inc_count >= max_count:
                log.info("Truncated samples at " + str(max_count))
                break

    return inc_count


def get_incidents(res_client, filename, max_count=None, filter=None, in_log=None):
    """
    Convert JSON into CSV and save, since scikit-learn uses CSV.

    :param res_client:  resilient client used to query incidents
    :param filename:    CSV file to save to
    :param max_count:   max count of incidents/samples to handle
    :param filter:      filter for incidents/sample
    :param in_log:      log
    :return:            incidents/samples count
    """
    log = in_log if in_log else logging.getLogger(__name__)

    # Read the fields of an incident
    inc_fields = res_client.get("/types/incident")

    fields_dict = inc_fields.get("fields", {})
    log.debug("Incident Fields: " + str(fields_dict))

    # Get all the incidents
    ret = query_incidents(res_client=res_client,
                          max_count=max_count,
                          in_log=log)

    inc_count = write_to_csv(incidents=ret,
                             fields_dict=fields_dict,
                             filename=filename,
                             max_count=max_count,
                             filter=filter,
                             in_log=in_log)
    return inc_count


def get_field_def(resilient_client, field, type_name, in_log=None):
    """
    Call the /types/{type}/fields/{field_name} to get the mapping
    between numerical value and label.
    Once a prediction is done, we will use this mapping to
    convert the numerical value back to label.

    :param resilient_client:    Resilient client used to retrieve field definition
    :param field:               Field we want the mapping for
    :param type_name:           Built-in type. For example "incident"
    :param in_log:              log
    :return:                    dict for translating numerical back to label for given field
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
            #@TODO: Need to revisit this when we need to support regression
            #
            ret[str(val["value"])] = val["label"]
    else:
        log.error("get_field_def for field = {}, and type = {} returned Null".format(field, type_name))

    return ret


def query_incidents(res_client, max_count=None, page_size=1000, in_log=None):
    """
    Use the query endpoint since we are going to down load
    large number of incidents.

    :param res_client:  Resilient client used to download incidents
    :param max_count:   Max count for incidents to handle
    :param page_size:   Number of incident to download for each call
    :return:            All downloaded incidents in json
    """
    log = in_log if in_log else logging.getLogger(__name__)
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
            log.debug("Downloaded {} incidents, total now {} ...".format(ret_num, ret_num + num_incidents))
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
