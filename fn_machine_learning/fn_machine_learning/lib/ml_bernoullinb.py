# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

from sklearn.naive_bayes import BernoulliNB
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier

import pandas as pds

import logging


class MlBernoulliNB(MlModelCommon, BernoulliNB):
    def __init__(self, imbalance_upsampling=None, class_weight=None, method=None, c=100.0, random_state=1, log=None):

        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)

        if method == "Bagging":
            model = BernoulliNB()
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            model = BernoulliNB()
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=10,
                                                      random_state=random_state)
        else:
            #
            # BernoulliNB does not support class_weight?
            #
            BernoulliNB.__init__(self)
            self.ensemble_method = None

    @staticmethod
    def get_name():
        return "BernoulliNB"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        This method builds a Bernoulli Naive Bayes
        http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html
        model.

        :param csv_file: CSV file with samples
        :param features: features to use
        :param prediction: field to predict
        :param test_prediction: how to split trainng/testing samples
        :param unwanted_values: Unwanted values for samples. Those samples will be removed
        :return:
        """
        try:
            self.extract_csv(csv_file, features, prediction)
            # Cleanup samples by removing samples with empty
            # features and unwanted values
            self.cleanup_samples(unwanted_values=unwanted_values)

            self.transform_numerical()
            self.split_samples(test_prediction)
            #
            # One way to compensate imbalance class is to do upsampling. Do
            # it if user specified this in
            #
            self.upsample_if_necessary()

            if len(self.y_train) > 0:
                self.config.number_samples = len(self.y_train) + len(self.y_test)
                self.log.info("Using {} samples to train. ".format(len(self.y_train)))
                if self.ensemble_method is not None:
                    self.ensemble_method.fit(self.X_train, self.y_train)
                else:
                    self.fit(self.X_train, self.y_train)

                #
                # Test model
                #
                if self.ensemble_method is not None:
                    y_predict = self.ensemble_method.predict(self.X_test)
                else:
                    y_predict = self.predict(self.X_test)

                self.compute_accuracy(predict=y_predict,
                                      actual=self.y_test)
            else:
                self.log.info("No samples to train the model")

        except Exception as e:
            self.log.exception(str(e))
            raise e

    def predict_result(self, input):
        """
        Input is a dict
        :param input:
        :return:
        """
        df = pds.DataFrame([input])
        #
        # We only care about the features
        #
        df = df[self.config.selected_features]

        df = self.transform_for_prediction(df)
        self.log.info("Using df {} to predict. ".format(str(df)))

        if self.ensemble_method is not None:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret
