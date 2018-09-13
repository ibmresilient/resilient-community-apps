# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
from sklearn.svm import SVC
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from fn_machine_learning.lib.normalization_encoder import ResNormalizationEncoder
import pandas as pds
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
import logging

class MlSVC(MlModelCommon, SVC):
    """
    Support Vector Machine algorithm.
    """
    def __init__(self, kernel="linear", C=1.0, random_state=1, method=None):
        """

        :param kernel:
        :param C:
        :param random_state:
        """
        self.kernel = kernel
        MlModelCommon.__init__(self, method=method)
        self.using_method = False
        if method == "Bagging":
            model = SVC(kernel=kernel,
                        C=C,
                        random_state=random_state)
            self.using_method = True
            self.ensemble_method = BaggingClassifier(base_estimator=model,
                                                     n_estimators=10,
                                                     random_state=random_state)
        elif method == "Adaptive Boosting":
            self.using_method = True
            model = SVC(kernel=kernel,
                        probability=True,
                        C=C,
                        random_state=random_state)
            self.ensemble_method = AdaBoostClassifier(base_estimator=model,
                                                      n_estimators=10,
                                                      random_state=random_state)
        else:
            SVC.__init__(self,
                         kernel=kernel,
                         C=C,
                         random_state=random_state)

    def get_name(self):
        if self.kernel == "linear":
            return "SVM"
        else:
            return "SVM with Gaussian kernel"


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
            # Need to remove samples with missig values. If
            # customer has other ways to handle missing values,
            # he/she can upload a csv without missing values
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
                log.error("No sample to train the model")
        except Exception as e:
            log.error(str(e))
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

    def get_encoder_for_float(self):
        return ResNormalizationEncoder()
