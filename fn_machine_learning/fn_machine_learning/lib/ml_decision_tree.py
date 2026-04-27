# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlDecisionTree
    --------------
    A machine model using Decision Tree algorithm for classification.
    https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

"""
from sklearn.tree import DecisionTreeClassifier
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import pandas as pds


class MlDecisionTree(MlModelCommon, DecisionTreeClassifier):

    def __init__(self, imbalance_upsampling=None, class_weight=None, method=None, random_state=10, log=None):

        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)

        if method == "Bagging":
            model = DecisionTreeClassifier(class_weight=class_weight,
                                           min_samples_split=20,
                                           random_state=99)
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            model = DecisionTreeClassifier(class_weight=class_weight,
                                           min_samples_split=20,
                                           random_state=99)
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=50,
                                                      random_state=random_state)
        else:
            self.ensemble_method = None
            DecisionTreeClassifier.__init__(self,
                                            class_weight=class_weight,
                                            min_samples_split=20,
                                            random_state=99)

    @staticmethod
    def get_name():
        """
        Return the name of the algorithm
        :return:
        """
        return "Decision Tree"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        This method builds the model

        :param csv_file:            CSV file for samples
        :param features:            list of features
        :param prediction:          field to predict
        :param test_prediction:     how to split training and test dataset
        :param unwanted_values:     Samples with these values will be excluded
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
                #
                # Check if we are using an ensemble method
                #
                if self.ensemble_method is not None:
                    self.ensemble_method.fit(self.X_train, self.y_train)
                else:
                    self.fit(self.X_train, self.y_train)

                #
                # Test the model using the test subset
                #
                if self.ensemble_method is not None:
                    y_predict = self.ensemble_method.predict(self.X_test)
                else:
                    y_predict = self.predict(self.X_test)

                # ==
                #   Reserved for AUC calculation. Watson uses AUC, so we can compare

                # pres = self.predict_proba(self.X_test)[:, 1]
                #
                # ytest = []
                # for re in self.y_test:
                #     if re == "yes":
                #         ytest.append(True)
                #     else:
                #         ytest.append(False)
                #
                # from sklearn import metrics
                # fpr, tpr, _ = metrics.roc_curve(ytest, pres)
                # auc = metrics.auc(fpr, tpr)

                # ==
                self.compute_accuracy(predict=y_predict,
                                      actual=self.y_test)
            else:
                self.log.info("No samples to train the model")

        except Exception as e:
            self.log.error(str(e))
            raise e

    def predict_result(self, input):
        """
        This is the method to predict a new incident using this trained/tested model.

        :param input:       incident to predict in json dict
        :return:            prediction in string
        """
        #
        #   First convert the json dict into a pandas dataframe
        #
        df = pds.DataFrame([input])
        #
        #   We only care about the features. Extract the features.
        #
        df = df[self.config.selected_features]
        #
        #   We need to pre-process this dataframe exactly like what we did
        #   for the training dataframe
        #
        df = self.transform_for_prediction(df)

        if self.ensemble_method is not None:
            ret = self.ensemble_method.predict(df)
        else:
            ret = self.predict(df)

        return ret


