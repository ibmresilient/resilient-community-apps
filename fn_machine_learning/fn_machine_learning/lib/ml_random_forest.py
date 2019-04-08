# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlRandomForest
    --------------
    Machine learning model using Random Forest algorithm.
    https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

    Note that Random Forest is basically an ensemble method of Decision Tree. So it does not make sense
    provide ensemble method on top of Random Forest.

"""
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from sklearn.ensemble import RandomForestClassifier
import pandas as pds


class MlRandomForest(MlModelCommon, RandomForestClassifier):

    def __init__(self, imbalance_upsampling=None, class_weight=None, method=None, log=None):
        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)
        #
        # Random forest is a special case of bagging of
        # decision tree. Might not make sense to
        # add ensemble method.
        #
        self.ensemble_method = None
        RandomForestClassifier.__init__(self,
                                        class_weight=class_weight,
                                        n_estimators=100,
                                        random_state=99)

    @staticmethod
    def get_name():
        """
        Return the name of algorithm
        :return:
        """
        return "Random Forest"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        Build this model

        :param csv_file:
        :param features:
        :param prediction:
        :param test_prediction:
        :param unwanted_values: Samples with these unwanted predicted values will be removed
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
        Use this model to predict a new incident
        :param input:       New incident to predict
        :return:            Prediction in string
        """
        df = pds.DataFrame([input])
        #
        # We only care about the features
        #
        df = df[self.config.selected_features]
        df = self.transform_for_prediction(df)
        ret = self.predict(df)

        return ret
