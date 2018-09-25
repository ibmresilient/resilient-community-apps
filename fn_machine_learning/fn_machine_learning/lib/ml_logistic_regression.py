# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
from sklearn.linear_model import LogisticRegression as LgRegression
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from fn_machine_learning.lib.data_preparation import DataPreparation
import logging
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier


class LogisticRegression(MlModelCommon, LgRegression):
    """
    Logistic Regression algorithm for Machine Learning
    """
    def __init__(self, method=None, c=100.0, random_state=1, log=None):
        """
        Initialize the model
        :param c:
        :param random_state:
        """
        self.c = c
        self.random_state = random_state
        MlModelCommon.__init__(self, method=method, log=log)
        self.using_method = False
        if method == "Bagging":
            model = LgRegression(C=c, random_state=random_state)
            self.using_method = True
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                            n_estimators=200,
                                            random_state=random_state)
        elif method == "Adaptive Boosting":
            self.using_method = True
            model = LgRegression(C=c, random_state=random_state)
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                            n_estimators=200,
                                            random_state=random_state)
        else:
            LgRegression.__init__(self,
                                  C=c,
                                  random_state=random_state,
                                  class_weight='balanced')

    @staticmethod
    def get_name():
        return "Logistic Regression"

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
            self.log.debug("Eliminate samples with missing feature(s).")
            self.eliminate_missings()

            # self.one_hot_encoding(features)
            self.log.debug("Transform numerical.")
            self.transform_numerical()
            self.log.debug("Split samples at " + str(test_prediction))
            self.split_samples(test_prediction)

            #
            # Train model using training data
            #
            if len(self.y_train) > 0:
                self.log.info("Using {} samples to train.".format(str(len(self.y_train))))
                if self.using_method:
                    self.ensemble_method.fit(self.X_train, self.y_train)
                else:
                    self.fit(self.X_train, self.y_train)

                #
                # Test model
                #
                if self.using_method:
                    y_predict = self.ensemble_method.predict(self.X_test)
                    pres = self.ensemble_method.predict_proba(self.X_test)[:, 1]
                else:
                    y_predict = self.predict(self.X_test)
                    pres = self.predict_proba(self.X_test)[:, 1]
#==
                #
                #   IBM Watson uses AUC to measure the performance of a model
                #   To compare against IBM Watson we compute AUC here as well
                #
                ytest = []
                for re in self.y_test:
                    if re == "yes":
                        ytest.append(True)
                    else:
                        ytest.append(False)



                from sklearn import metrics
                fpr, tpr, _ = metrics.roc_curve(ytest, pres)
                auc = metrics.auc(fpr, tpr)

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
        Input will be a dict
        :param input:
        :return:
        """
        df = pds.DataFrame([input])
        df = df[self.features]
        df = self.transform_for_prediction(df)
        self.log.info("dataframe used to predict: " + str(df))

        if self.using_method:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret
