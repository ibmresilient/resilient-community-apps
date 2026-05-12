# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlKNN
    -----
    A machine learning model uses the K-Nearest Neighbor algorithm.
    https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html


"""
from sklearn.neighbors import KNeighborsClassifier
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from fn_machine_learning.lib.normalization_encoder import ResNormalizationEncoder
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import logging

class MlKNN(MlModelCommon, KNeighborsClassifier):
    def __init__(self, imbalance_upsampling=None, class_weight=None, random_state=1, n_neighbors=5, method=None, log=None):
        """

        :param imbalance_upsampling:    Use upsampling to compensate imbalance
        :param class_weight:            Use class_weight to compensate imbalance
        :param random_state:            Random state
        :param n_neighbors:             Number of neighbor samples to use
        :param method:                  Ensemble method
        :param log:                     Log
        """
        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)

        #
        #   class_weight is not supported for KNN.
        #
        if method == "Bagging":
            model = KNeighborsClassifier(n_neighbors=n_neighbors,
                                         metric="minkowski")
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            model = KNeighborsClassifier(n_neighbors=n_neighbors,
                                         metric="minkowski")
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=10,
                                                      random_state=random_state)
        else:
            self.ensemble_method = None
            KNeighborsClassifier.__init__(self,
                                          n_neighbors=n_neighbors,
                                          metric="minkowski")

    @staticmethod
    def get_name():
        return u"K-Nearest Neighbor"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        Build this model.

        :param csv_file:        CSV file with samples/incidents
        :param features:        Features
        :param prediction:      Field tp predict
        :param test_prediction: How to split dataset
        :param unwanted_values: Sample with unwanted values will be removed
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
            # it if user specified this in app.config
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
                self.log.error("No sample to train the model")
        except Exception as e:
            self.log.error(str(e))
            raise e

    def predict_result(self, input_dict):
        """
        Use this model to make a prediction for the input incident

        :param input_dict:      Input incident in json dict
        :return:                Prediction
        """
        df = pds.DataFrame([input_dict])
        df = df[self.config.selected_features]
        df = self.transform_for_prediction(df)
        if self.ensemble_method is not None:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret
