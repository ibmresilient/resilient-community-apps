# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlDummyClassifier
    -----------------
    sklearn Dummy Classifier uses pure statistics to predict, without digging out the
    relation between the features and the predicting value.
    https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html

    This is the baseline for any meaningful machine learning model. If a ML model can
    find any meaningful/useful relation between the features and the predicting field,
    it will do better than this Dummy Classifier.

    We include this for advanced users. They can compare a real ML model with this to
    make sure that the model actually learns something useful from the data.
"""
from sklearn.dummy import DummyClassifier
from fn_machine_learning.lib.ml_model_common import MlModelCommon


class MlDummyClassifier(MlModelCommon, DummyClassifier):

    def __init__(self, strategy="stratified", log=None):
        """

        :param self:
        :param strategy: Possible choices
                "stratified": Predict by respecting the training set's class distribution
                "most_frequent": Always predict the majority
                "prior": Maximize the lass prior
                "uniform": Generates uniform prediction randomly
                "constant": Predict a given value always
        :param log:
        :return:
        """
        MlModelCommon.__init__(self, log=log)
        DummyClassifier.__init__(self, strategy=strategy)

    @staticmethod
    def get_name():
        """ Return the name of algorithm"""
        return "Dummy Classifier"

    def build(self, csv_file, features, prediction, test_prediction, unwanted_values=None):
        """
        Build the model

        :param csv_file:        CSV file for dataset
        :param features:        features for ML learning.
        :param prediction:      field to predict
        :param test_prediction: how to split the dataset
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

            if len(self.y_train) > 0:
                self.config.number_samples = len(self.y_train) + len(self.y_test)
                self.log.info("Using {} samples to train. ".format(len(self.y_train)))

                self.fit(self.X_train, self.y_train)
                y_predict = self.predict(self.X_test)

                self.compute_accuracy(predict=y_predict,
                                      actual=self.y_test)

            else:
                self.log.error("No sample to train the model")
        except Exception as e:
            self.log.error(str(e))
            raise e
