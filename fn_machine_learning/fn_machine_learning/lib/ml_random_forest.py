# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

from fn_machine_learning.lib.ml_model_common import MlModelCommon
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import pandas as pds
import logging


class MlRandomForest(MlModelCommon, RandomForestClassifier):

    def __init__(self, method=None, log=None):
        MlModelCommon.__init__(self, method=method, log=log)
        #
        # Random forest is a special case of bagging of
        # decision tree. Might not make sense to
        # add ensemble method.
        #
        self.using_method = False
        RandomForestClassifier.__init__(self,
                                        n_estimators=100,
                                        random_state=99,
                                        class_weight="balanced")

    @staticmethod
    def get_name():
        return "Random Forest"

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
            # Need to handle missing values
            self.eliminate_missings()

            self.transform_numerical()
            self.split_samples(test_prediction)

            if len(self.y_train) > 0:
                self.fit(self.X_train, self.y_train)

                y_predict = self.predict(self.X_test)
                # ==
                pres = self.predict_proba(self.X_test)[:, 1]

                ytest = []
                for re in self.y_test:
                    if re == "yes":
                        ytest.append(True)
                    else:
                        ytest.append(False)

                from sklearn import metrics
                fpr, tpr, _ = metrics.roc_curve(ytest, pres)
                auc = metrics.auc(fpr, tpr)

                # ==
                self.compute_accuracy(predict=y_predict,
                                      actual=self.y_test)
            else:
                self.log.error("No samples to train the model")

        except Exception as e:
            self.log.error(str(e))
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
        df = df[self.features]

        df = self.transform_for_prediction(df)

        if self.using_method:
            ret = self.method.predict(df)
        else:
            ret = self.predict(df)

        return ret
