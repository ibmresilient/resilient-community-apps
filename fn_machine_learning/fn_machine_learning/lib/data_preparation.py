# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
import pandas as pds
from sklearn.preprocessing import MinMaxScaler


class DataPreparation(object):

    @staticmethod
    def drop_samples_with_missing_value(df):
        """
        [Optional step in pre-processing samples]
        It is recommended to handle those samples with missing value(s) first.
        The easiest approach is just removing all of them
        :return:
        """
        df = df.dropna(axis=0)
        df = df.dropna(asix=1)

    @staticmethod
    def normalize_samples(samples):
        """
        Feature scaling is crucial for most learning models
        :param samples: samples to normalize
        :return: normalized samples
        """
        mms = MinMaxScaler()
        samples = mms.fit_transform(samples)
        return samples

    @staticmethod
    def one_hot_encoding(df, features):
        """
        One hot encoding
        :param df:
        :param features:
        :return:
        """
        return pds.get_dummies(df[features])

