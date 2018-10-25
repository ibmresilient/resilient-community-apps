# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
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
        self.log = log

    def set_build_time(self):
        self.config.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def extract_csv(self, csv_file, features, prediction):
        """

        :param csv_file:
        :param features:
        :param prediction:
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
        #print(self.df)

    def cleanup_samples(self, unwanted_values=None):
        """
        It is recommended to fix features/samples with missing values.
        One straightforward and simplest way is to eliminate all of them.
        If user wants to do imputing, he/she can do it to the input csv file
        first.
        Also, user can remove samples with unwanted values
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
        #
        # https://stackoverflow.com/questions/28656736/using-scikits-labelencoder-correctly-across-multiple-programs
        #
        # Basically each categorical column needs one labelencoder
        #
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
                #le = LabelEncoder()
                #
                # Our own
                #
                #le = ResNormalizationEncoder()

                le = self.get_encoder_for_float()

                le.fit(col)
                self.X[col_name] = le.transform(self.X[col_name])
                self.label_encoder[col_name] = le

        self.log.debug(self.X)

    def get_encoder_for_float(self):
        """
        Most algorithm works well with sklearn LabelEncoder.
        Some (SVM category?) works well with normalization
        By default, this method returns LabelEncoder.
        Override it in subclass if a specific algorithm wants
        something else
        :return:
        """
        return LabelEncoder()

    def transform_for_prediction(self, df):
        """
        Transform the input df before applying ml model on it
        :param df:
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

        :param test_percentage:
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
        To handle imbalance class, one approach is to do
        upsampling.

        Note: You should always split the sample first and then only
        upsample the training set.
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
        Save this model to a file
        :param file_name:
        :return:
        """
        #
        #   No need to save these
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
        Read a model from a file
        :param file_name:
        :return:
        """
        model = pickle.load(open(file_name, "rb"))
        return model

    def compute_accuracy(self, predict, actual):
        """

        :param predict:
        :param actual:
        :return: accuracy percentage
        """
        #
        # Set build time
        #
        self.set_build_time()

        self.config.accuracy = accuracy_score(y_true=actual,
                                              y_pred=predict)

        self.config.analysis = model_utils.analyze(y_true=actual,
                                                   y_pred=predict)
        self.config.precision = model_utils.compute_precision(y_true=actual,
                                                              y_pred=predict)

        self.config.recall = model_utils.compute_recall(y_true=actual,
                                                        y_pred=predict)

        self.config.f1 = model_utils.comput_f1(y_true=actual,
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
        Override this in subclass
        :return:
        """
        return []

    def predict_map(self, input_dict, mapping):
        res = self.predict_result(input_dict)
        #
        #   res could be a numpy.ndarray
        #
        if isinstance(res, numpy.ndarray):
            predict = mapping.get(res[0], res[0])
        else:
            predict = mapping.get(res, res)

        return predict

