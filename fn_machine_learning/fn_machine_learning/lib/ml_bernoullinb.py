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
    def __init__(self, method=None, c=100.0, random_state=1):
        MlModelCommon.__init__(self, method=method)
        self.using_method = False
        if method == "Bagging":
            model = BernoulliNB()
            self.using_method = True
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                            n_estimators=10,
                                            random_state=random_state)
        elif method == "Adaptive Boosting":
            self.using_method = True
            model = BernoulliNB()
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                            n_estimators=10,
                                            random_state=random_state)
        else:
            BernoulliNB.__init__(self)

    @staticmethod
    def get_name():
        return "BernoulliNB"

    def build(self, csv_file, features, prediction, test_prediction):
        """

        :param csv_file:
        :param features:
        :param prediction:
        :param test_prediction:
        :return:
        """
        try:
            log = logging.getLogger(__name__)
            self.extract_csv(csv_file, features, prediction)
            # Need to handle missing values
            self.eliminate_missings()

            self.transform_numerical()
            self.split_samples(test_prediction)

            if len(self.y_train) > 0:
                log.info("Using {} samples to train. ".format(len(self.y_train)))
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
                log.info("No samples to train the model")

        except Exception as e:
            log.exception(str(e))
            raise e

    def predict_result(self, input):
        """
        Input is a dict
        :param input:
        :return:
        """
        log = logging.getLogger(__name__)
        df = pds.DataFrame([input])
        #
        # We only care about the features
        #
        df = df[self.features]

        df = self.transform_for_prediction(df)
        log.info("Using df {} to predict. ".format(str(df)))

        if self.using_method:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret