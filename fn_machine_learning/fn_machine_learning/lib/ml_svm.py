# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlSVC
    -----
    Machine learning model using Support Vector Machine algorithm.
    https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

    This package support both the orginal (linear) SVM and the SVM with
    Gaussian kernel
"""
from sklearn.svm import SVC
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from fn_machine_learning.lib.normalization_encoder import ResNormalizationEncoder
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier


class MlSVC(MlModelCommon, SVC):

    def __init__(self, imbalance_upsampling=None, class_weight=None, kernel="linear", C=1.0, random_state=1, method=None, log=None):
        """
        :param imbalance_upsampling:    Use upsampling to compensate imbalanced dataset
        :param class_weight:            Use class_weight to compensate imbalanced dataset
        :param kernel:                  "linear" or "rbf" for Gaussian kernel
        :param C:                       Not supported yet
        :param random_state:            Random state
        :param method:                  Bagging or Adaptive Boost
        :param log:                     Log
        """
        self.kernel = kernel
        MlModelCommon.__init__(self,
                               imbalance_upsampling=imbalance_upsampling,
                               class_weight=class_weight,
                               method=method,
                               log=log)
        if method == "Bagging":
            model = SVC(kernel=kernel,
                        class_weight=class_weight,
                        C=C,
                        random_state=random_state)
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            model = SVC(kernel=kernel,
                        class_weight=class_weight,
                        C=C,
                        random_state=random_state)
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=10,
                                                      random_state=random_state)
        else:
            self.ensemble_method = None
            SVC.__init__(self,
                         kernel=kernel,
                         class_weight=class_weight,
                         C=C,
                         random_state=random_state)

    def get_name(self):
        """
        Return the name of algorithm
        :return:
        """
        if self.kernel == "linear":
            return "SVM"
        else:
            return "SVM with Gaussian kernel"

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
        Use this model to predict a new incident

        :param input_dict:      Input incident
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

    def get_encoder_for_float(self):
        """
        According to our test, normalized float features is better for SVM.
        :return:
        """
        return ResNormalizationEncoder()
