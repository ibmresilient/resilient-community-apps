# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

from sklearn.tree import DecisionTreeClassifier
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import pandas as pds
import logging


class MlDecisionTree(MlModelCommon, DecisionTreeClassifier):

    def __init__(self, method=None, random_state=10):
        MlModelCommon.__init__(self, method=method)
        self.using_method = False
        if method == "Bagging":
            model = DecisionTreeClassifier(min_samples_split=20,
                                           random_state=99)
            self.using_method = True
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            self.using_method = True
            model = DecisionTreeClassifier(min_samples_split=20,
                                           random_state=99)
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=50,
                                                      random_state=random_state)

        DecisionTreeClassifier.__init__(self,
                                        min_samples_split=20,
                                        random_state=99)

    @staticmethod
    def get_name():
        return "Decision Tree"

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
                log.info("No samples to train the model")

        except Exception as e:
            log.error(str(e))
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
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret


