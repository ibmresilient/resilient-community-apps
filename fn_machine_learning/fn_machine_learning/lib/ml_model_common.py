# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MlModelCommon
    -------------
    Superclass for all individual machine model.

    It contains common methods and variables.
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

from fn_machine_learning.lib.data_preparation import DataPreparation
from fn_machine_learning.lib.multi_id_binarizer import MultiIdBinarizer
from fn_machine_learning.lib.ml_config import MlConfig
import pandas as pds
import pickle
import datetime
import logging
import fn_machine_learning.lib.model_utils as model_utils
import numpy


class MlModelCommon(object):
    """
    Super class of all the ml models we support
    """

    def __init__(self, imbalance_upsampling=False, class_weight=None, method=None, log=None):
        """
        Initialize
        """
        self.config = MlConfig()
        self.config.imbalance_upsampling = imbalance_upsampling
        self.config.class_weight = class_weight
        self.config.addition_method = method

        #
        # Dataset
        #
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.X = None
        self.y = None
        self.df = None

        self.log = log

        self.ensemble_method = None
        self.label_encoder = {}

    def set_log(self, log):
        """
        Set the log to use
        :param log:
        :return:
        """
        self.log = log

    def set_build_time(self):
        """
        Record the build time. This will be written into the saved model file for record
        :return:
        """
        self.config.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def extract_csv(self, csv_file, features, prediction):
        """
        Extract dataframe from the given CSV file. This dataframe then contains the samples
        used to build the model later

        :param csv_file:        CSV file with samples
        :param features:        Features to use to build
        :param prediction:      Field to predict
        :return:
        """
        self.config.predict_field = prediction
        self.config.selected_features = list(features)

        all_fields = list(features)
        self.log.debug("All fields in csv: {}".format(str(all_fields)))
        all_fields.append(prediction)

        #
        # Use pandas.read_csv to load samples.
        #@TODO: right now we force the prediciton type to object (string)
        # Need to revisit this when we need to predict regression later
        #
        self.df = pds.read_csv(csv_file,
                               sep=self.config.separator,
                               usecols=all_fields,
                               dtype={prediction:object},
                               skipinitialspace=True,
                               quotechar='"')

    def cleanup_samples(self, unwanted_values=None):
        """
        It is recommended to fix features/samples with missing values.
        One straightforward and simplest way is to eliminate all of them.
        If user wants to do imputing, he/she can do it to the input csv file
        first.
        Also, user can remove samples with unwanted values for the predict field.
        Samples with those values will be excluded in fitting the model.

        :param unwanted_values:         list of unwanted values of the predict field.
        :return:
        """
        self.df = self.df.dropna(axis=0)
        self.df = self.df.dropna(axis=1)

        self.config.unwanted_values = unwanted_values

        if unwanted_values is not None:
            self.df = DataPreparation.remove_samples_with_values(data_frame=self.df,
                                                                 prediction=self.config.predict_field,
                                                                 value_list=unwanted_values)

        self.X = self.df[self.config.selected_features]
        self.y = self.df[self.config.predict_field]

    def transform_numerical(self):
        """
        Each categorical column needs one label encoder.
        https://stackoverflow.com/questions/28656736/using-scikits-labelencoder-correctly-across-multiple-programs

        A label encoder convert a string value (of features) into integers.
        :return:
        """
        for col_name, col in self.X.iteritems():
            self.log.debug("Column {col_name} is {col_type}".format(col_name=col_name,
                                                                    col_type=col.dtype.name))
            #
            # For numerical column labelencoder is used to normalize the column
            # And for categorical column, it is used to transform to numerical labels.
            #
            # https://www.analyticsvidhya.com/blog/2016/07/practical-guide-data-preprocessing-python-scikit-learn/
            # This link prefers only doing label encoding for categorical columns
            # The numerical column, once normalized, has a big chance to get new (unseen) labels
            # during prediction later.
            if col.dtype.name == "object":
                #
                # For multi selection, col is a list. Use
                # json to load it and check if it is a list
                #
                is_list = MultiIdBinarizer.is_multi_selection(col)

                if is_list:
                    #
                    # Multi select is 2 dimensional
                    #
                    le = MultiIdBinarizer()
                    le.fit(col, col_name)
                    self.X = le.transform(self.X)
                else:
                    le = LabelEncoder()
                    le.fit(col)
                    self.X[col_name] = le.transform(self.X[col_name])
                self.label_encoder[col_name] = le
            elif col.dtype.name == "float64":
                #
                #   Normalize it
                # http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
                # Note that labelencoder can be used to normalize as well
                # labelencoder is good except SVM.
                #

                # So here will use template method design pattern and let the subclass to decide
                # what label encoder to use
                le = self.get_encoder_for_float()

                le.fit(col)
                self.X[col_name] = le.transform(self.X[col_name])
                self.label_encoder[col_name] = le

        self.log.debug(self.X)

    def get_encoder_for_float(self):
        """
        Template Method design method.

        Most algorithm works well with sklearn LabelEncoder.
        Some (SVM category?) work better with normalization
        By default, this method returns LabelEncoder.

        Override it in subclass if a specific algorithm wants
        something else

        :return:        The encoder to be used for float
        """
        return LabelEncoder()

    def transform_for_prediction(self, df):
        """
        Transform the input dataframe before applying ml model on it

        This dataframe needs to be transformed exactly like how we treated the
        training dataset/dataframe before we fit the model.

        :param df:      Dataframe we need to predict
        :return:
        """
        for col_name, col in df.iteritems():
            if col.dtype.name == "object" or col.dtype.name == "float64":
                try:
                    le = self.label_encoder.get(col_name, None)
                    if le:
                        if isinstance(le, MultiIdBinarizer):
                            df = le.transform(df)
                        elif le:
                            df[col_name] = le.transform(df[col_name])
                    else:
                        self.log.error("Unable to find label encoder for " + col_name)
                except ValueError as e:
                    #
                    #
                    self.log.error("Need to handle new label for " + col_name)

        return df

    def one_hot_encoding(self, features):
        #
        # The problem for this approach is that we need to use the
        # same one_hot_encoding to handle both the test/training
        # data and the new sample to predict. When we need
        # to handle a new sample, how can we do the same thing as
        # the training/test data?
        #
        self.X = DataPreparation.one_hot_encoding(self.X, features)

    def split_samples(self, test_percentage=0.5):
        """
        Split the samples into training and testing subsets.

        The training subset is used to fit and train the model, and the testing
        subset is used to validate the model, and compute measurements like
        overall accuracy/F1.

        :param test_percentage:     The percentage for testing subset
        :return:
        """
        X = self.X.values
        y = self.y.values
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(X, y,
                             test_size=test_percentage,
                             random_state=0,
                             stratify=self.y)

        self.log.debug(self.y_train)

    def upsample_if_necessary(self):
        """
        To handle imbalance class, one approach is to do upsampling. Basically we just
        make multiple copies of each minority sample, so that the count of the minority
        sample is the same as the majority samples.

        Note: You should always split the sample first and then upsample the training
        set only. No need to upsample the testing set.

        :return:
        """
        X = pds.DataFrame(data=self.X_train)
        y = pds.DataFrame(data=self.y_train)
        data_training = pds.concat([X, y],
                                   axis=1)
        data_up = DataPreparation.upsample_minorities(data_training,
                                                      imbalance_upsampling=self.config.imbalance_upsampling)

        self.X_train = data_up.iloc[:, :-1]
        self.y_train = data_up.iloc[:, -1]
        self.log.debug(self.y_train.value_counts())

    def save_to_file(self, file_name):
        """
        Save this model to a file using pickle.

        :param file_name:   Name of the file to be used for saving
        :return:
        """
        #
        #   No need to save these. They are not used in prediction
        #
        self.X_test = None
        self.X = None
        self.y = None
        self.X_train = None
        self.y_train = None
        self.y_test = None
        self.df = None
        self.log = None

        pickle.dump(self, open(file_name, "wb"))

    @staticmethod
    def load_from_file(file_name):
        """
        Read a model from a file. Deserialize it.

        :param file_name:   Name of the saved model file
        :return:
        """
        model = pickle.load(open(file_name, "rb"))
        return model

    def compute_accuracy(self, predict, actual):
        """
        Compute the overall accuracy and other measurement, by comparing predict and actual

        :param predict:         This is a list of the predictions the model gives for the testing
                                data subset.
        :param actual:          This is the actual/true result of the testing dataset
        :return:                Measurements
        """
        #
        #   Set build time. This will be saved to the model file for record
        #
        self.set_build_time()
        #
        #   Overall accuracy
        #
        self.config.accuracy = accuracy_score(y_true=actual,
                                              y_pred=predict)

        #
        #   For imbalanced dataset, more measurements
        #
        self.config.analysis = model_utils.analyze(y_true=actual,
                                                   y_pred=predict)
        self.config.precision = model_utils.compute_precision(y_true=actual,
                                                              y_pred=predict)

        self.config.recall = model_utils.compute_recall(y_true=actual,
                                                        y_pred=predict)

        self.config.f1 = model_utils.compute_f1(y_true=actual,
                                               y_pred=predict)


        #
        # This is very expensive. Do it only if debug is enabled
        #
        if self.log.isEnabledFor(logging.DEBUG):
            for t, p in zip(actual, predict):
                self.log.debug(str(t) + " : " + str(p) + "\n")

        return self.config.accuracy

    def predict_result(self, input_dict):
        """
        Override this in subclass if necessary
        :return:
        """
        return []

    def predict_map(self, input_dict, mapping):
        """

        :param input_dict:
        :param mapping:
        :return:
        """
        res = self.predict_result(input_dict)
        #
        #   res could be a numpy.ndarray
        #
        if isinstance(res, numpy.ndarray):
            predict = mapping.get(res[0], res[0])
        else:
            predict = mapping.get(res, res)

        return predict

