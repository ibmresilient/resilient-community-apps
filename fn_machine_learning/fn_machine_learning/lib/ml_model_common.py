# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from fn_machine_learning.lib.data_preparation import DataPreparation
from fn_machine_learning.lib.multi_id_binarizer import MultiIdBinarizer
from fn_machine_learning.lib.normalization_encoder import ResNormalizationEncoder
import pandas as pds
import pickle
import datetime
import logging


class MlModelCommon(object):

    #
    # Support only one saved model at this point
    #
    FEATURES_FILE_NAME = "saved_feature.txt"

    def __init__(self, method=None):
        """
        Initialize
        """
        self.features = []
        self.prediction = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.X = None
        self.y = None
        self.df = None
        self.accuracy = 0.5
        self.separator = ','
        self.label_encoder = {}
        self.build_rimw = ""
        self.method_name = method
        self.ensemble_method = None
        self.number_samples = 0

    def set_build_time(self):
        self.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def extract_csv(self, csv_file, features, prediction):
        """

        :param csv_file:
        :param features:
        :param prediction:
        :return:
        """
        log = logging.getLogger(__name__)

        self.prediction = prediction
        self.features = list(features)

        all_fields = list(features)
        log.debug("All fields in csv: {}".format(str(all_fields)))
        all_fields.append(prediction)


        self.df = pds.read_csv(csv_file,
                               sep=self.separator,
                               usecols=all_fields,
                               skipinitialspace=True,
                               quotechar='"')
        #print(self.df)


    def eliminate_missings(self):
        """
        It is recommended to fix features/samples with missing values.
        One straightforward and simplest way is to eliminate all of them.
        If user wants to do imputing, he/she can do it to the input csv file
        first.
        :return:
        """
        self.df = self.df.dropna(axis=0)
        self.df = self.df.dropna(axis=1)

        self.X = self.df[self.features]
        self.y = self.df[self.prediction]

    def transform_numerical(self):
        #
        # https://stackoverflow.com/questions/28656736/using-scikits-labelencoder-correctly-across-multiple-programs
        #
        # Basically each categorical column needs one labelencoder
        #
        log = logging.getLogger(__name__)
        for col_name, col in self.X.iteritems():
            log.info("Column {col_name} is {col_type}".format(col_name=col_name,
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

        log.debug(self.X)

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
        log = logging.getLogger(__name__)
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
                       log.error("Unable to find lable encoder for " + col_name)
                except ValueError as e:
                    #
                    #
                    log.error("Need to handle new label for " + col_name)

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
        log = logging.getLogger(__name__)
        X = self.X.values
        y = self.y.values
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(X, y,
                             test_size=test_percentage,
                             random_state=0,
                             stratify=self.y)

        log.debug(self.y_train)

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
        log = logging.getLogger(__name__)
        #
        # Set build time
        #
        self.set_build_time()

        self.accuracy = accuracy_score(y_true=actual,
                              y_pred=predict)

        for t, p in zip(actual, predict):
            log.debug(str(t) + " : " + str(p) + "\n")
        return self.accuracy
