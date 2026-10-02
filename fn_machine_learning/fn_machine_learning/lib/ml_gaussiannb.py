# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlGaussianNB
    ------------
    A machine learning model that uses the scikit-learn Gaussian Naive Bayes algorithm:
    https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html

    This algorithm can do partial fit, but not supported yet in our softeare.

"""
from sklearn.naive_bayes import GaussianNB
from fn_machine_learning.lib.ml_model_common import MlModelCommon
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import logging


class MlGaussianNB(MlModelCommon, GaussianNB):

    def __init__(self, imbalance_upsampling=None, class_weight=None, method=None, random_state=1, log=None):
        """
        Construtor

        :param imbalance_upsampling:    Use upsampling to compensate imbalanced dataset
        :param class_weight:            Use class_weight to compensate imbalanced dataset
        :param method:                  [Optional] Ensemble method
        :param random_state:            Random state
        :param log:                     Log
        """
        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)
        #
        #   GaussianNB does not support class_weight
        #
        if method == "Bagging":
            model = GaussianNB()
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=100,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            model = GaussianNB()
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=100,
                                                      random_state=random_state)
        else:
            self.ensemble_method = None
            GaussianNB.__init__(self)

    @staticmethod
    def get_name():
        """
        Return the name of the algorithm
        :return:
        """
        return "GaussianNB"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        Build this model.

        :param csv_file:            CSV file with samples
        :param features:            Features to build this model
        :param prediction:          Field to predict
        :param test_prediction:     How to split training/testing dataset
        :return:
        """
        try:
            self.extract_csv(csv_file, features, prediction)
            # Cleanup samples by removing samples with empty
            # features and unwanted values
            self.cleanup_samples(unwanted_values)

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
            self.log.error(e)
            raise e

    def predict_result(self, input):
        """
        This is the method to predict a "new" incident. Input is a dict

        :param input:       Incident in json dict
        :return:
        """
        df = pds.DataFrame([input])
        #
        #   We only care about the features
        #
        df = df[self.config.selected_features]
        #
        #   We need to do the same transformation as for the training dataset
        #
        df = self.transform_for_prediction(df)
        self.log.info("Using df {} to predict.".format(str(df)))

        if self.ensemble_method is not None:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret
