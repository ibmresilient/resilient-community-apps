# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    LogisticRegression
    ------------------
    A machine learning using Logistic Regression for classification:
    http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

    Also two possible (optional) ensemble methods:
        1. Bagging
        2. Adaptive Boost

"""
from sklearn.linear_model import LogisticRegression as LgRegression
from fn_machine_learning.lib.ml_model_common import MlModelCommon
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier


class LogisticRegression(MlModelCommon, LgRegression):

    def __init__(self, imbalance_upsampling=None, class_weight=None, method=None, c=100.0, random_state=1, log=None):
        """
        Initialize the model
        :param imbalance_upsampling:    Using upsampling to compensate imbalanced dataset
        :param class_weight:            It can be None, "balanced", or a dict. Used for imbalance class
        :param method:                  Optional ensemble method
        :param c:                       Not supported yet.
        :param random_state:            Random state
        :param log:                     log
        """
        self.c = c
        self.random_state = random_state
        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)

        if method == "Bagging":
            model = LgRegression(C=c,
                                 class_weight=class_weight,
                                 random_state=random_state)
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=200,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            model = LgRegression(C=c,
                                 class_weight=class_weight,
                                 random_state=random_state)
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=200,
                                                      random_state=random_state)
        else:
            self.ensemble_method = None
            LgRegression.__init__(self,
                                  C=c,
                                  random_state=random_state,
                                  class_weight=class_weight)

    @staticmethod
    def get_name():
        """Return the name of the algorithm"""
        return "Logistic Regression"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        Build this model
        :param csv_file:        CSV file with samples
        :param features:        Features for building this model
        :param prediction:      Field to predict
        :param test_prediction: How to split samples
        :param unwanted_values: Samples with unwanted values will be removed
        :return:
        """
        try:
            self.extract_csv(csv_file, features, prediction)
            # Need to handle missing values
            self.log.debug("Eliminate samples with missing feature(s).")
            # Cleanup samples by removing samples with empty
            # features and unwanted values
            self.cleanup_samples(unwanted_values)

            # self.one_hot_encoding(features)
            self.log.debug("Transform numerical.")
            self.transform_numerical()
            self.log.debug("Split samples at " + str(test_prediction))
            self.split_samples(test_prediction)
            #
            # One way to compensate imbalance class is to do upsampling. Do
            # it if user specified this in
            #
            self.upsample_if_necessary()

            #
            #   Train model using training data
            #
            if len(self.y_train) > 0:
                self.config.number_samples = len(self.y_train) + len(self.y_test)
                self.log.info("Using {} samples to train.".format(str(len(self.y_train))))
                if self.ensemble_method is not None:
                    self.ensemble_method.fit(self.X_train, self.y_train)
                else:
                    self.fit(self.X_train, self.y_train)

                #
                #   Test model
                #
                if self.ensemble_method is not None:
                    y_predict = self.ensemble_method.predict(self.X_test)
                    pres = self.ensemble_method.predict_proba(self.X_test)[:, 1]
                else:
                    y_predict = self.predict(self.X_test)
                    pres = self.predict_proba(self.X_test)[:, 1]
#==
                #
                #   IBM Watson uses AUC to measure the performance of a model
                #   To compare against IBM Watson we compute AUC here as well
                #   Reserved for future tests
                #
                # ytest = []
                # for re in self.y_test:
                #     if re == "yes":
                #         ytest.append(True)
                #     else:
                #         ytest.append(False)
                #
                #
                #
                # from sklearn import metrics
                # fpr, tpr, _ = metrics.roc_curve(ytest, pres)
                # auc = metrics.auc(fpr, tpr)

#==
                #
                # Accuracy
                #
                self.compute_accuracy(predict=y_predict,
                                      actual=self.y_test)
            else:
                self.log.info("Nothing to train the model")

        except Exception as e:
            self.log.exception(str(e))
            raise e

    def predict_result(self, input):
        """
        Use this model to predict a new incident.

        :param input:       Incident in json dict
        :return:            Prediction
        """
        df = pds.DataFrame([input])
        df = df[self.config.selected_features]
        df = self.transform_for_prediction(df)
        self.log.info("dataframe used to predict: " + str(df))

        if self.ensemble_method is not None:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret
