# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
from sklearn.neighbors import KNeighborsClassifier
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from fn_machine_learning.lib.normalization_encoder import ResNormalizationEncoder
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import logging

class MlKNN(MlModelCommon, KNeighborsClassifier):
    """
    Support K-Nearest Neighbor algorithm
    """
    def __init__(self, random_state=1, n_neighbors=5, method=None, log=None):
        """

        :param random_state:
        :param n_neighbors:
        :param method:
        """
        MlModelCommon.__init__(self, method=method, log=log)
        self.using_method = False
        if method == "Bagging":
            model = KNeighborsClassifier(n_neighbors=n_neighbors,
                                         metric="minkowski")
            self.using_method = True
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            self.using_method = True
            model = KNeighborsClassifier(n_neighbors=n_neighbors,
                                         metric="minkowski")
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=10,
                                                      random_state=random_state)
        else:
            KNeighborsClassifier.__init__(self,
                                          n_neighbors=n_neighbors,
                                          metric="minkowski")

    @staticmethod
    def get_name():
        return u"K-Nearest Neighbor"

    def build(self, csv_file, features, prediction, test_prediction):
        """

        :param csv_file:
        :param features:
        :param prediction:
        :param test_prediction:
        :return:
        """
        try:
            self.extract_csv(csv_file, features, prediction)
            # Need to remove samples with missig values. If
            # customer has other ways to handle missing values,
            # he/she can upload a csv without missing values
            self.eliminate_missings()

            self.transform_numerical()
            self.split_samples(test_prediction)

            if len(self.y_train) > 0:
                self.log.info("Using {} samples to train. ".format(len(self.y_train)))
                if self.using_method:
                    self.ensemble_method.fit(self.X_train, self.y_train)
                else:
                    self.fit(self.X_train, self.y_train)

                #
                # Test model
                #
                if self.using_method:
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
        df = pds.DataFrame([input_dict])
        df = df[self.features]
        df = self.transform_for_prediction(df)
        if self.using_method:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret
