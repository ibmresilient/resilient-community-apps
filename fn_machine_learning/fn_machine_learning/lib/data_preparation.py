# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    DataPreparation
    ---------------
    Machine learning relies on good dataset. DataPreparation prepare
    the dataset before it is used for training a machine learning
    model.

    Data preparation includes the following steps:
        1. Clean up the dataset. Samples with blank values shall be removed
           according to recommendation from ML books
        2. String/Boolean values will be converted into integers
        3. Integer/flow values will be normalized, so samples can span
           out for easier identification/categorization
        4. Upsampling is used for imbalanced dataset
"""
import pandas as pds
from sklearn.preprocessing import MinMaxScaler


class DataPreparation(object):

    @staticmethod
    def drop_samples_with_missing_value(df):
        """
        [Optional step in pre-processing samples]
        It is recommended to handle those samples with missing value(s) first.
        The easiest approach is just removing all of them

        :param df:  input dataframe to process
        :return:
        """
        df = df.dropna(axis=0)
        df = df.dropna(asix=1)

    @staticmethod
    def normalize_samples(samples):
        """
        Feature scaling is crucial for most learning models

        :param samples:     samples to normalize
        :return:            normalized samples
        """
        mms = MinMaxScaler()
        samples = mms.fit_transform(samples)
        return samples

    @staticmethod
    def one_hot_encoding(df, features):
        """
        Use pandas function to do one hot encoding. Basically string features need to
        be converted/encoded into categorical integers.
        https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html

        :param df:          input dataframe of samples to handle
        :param features:    list of features to be encoded using one hot encoding
        :return:            encoded dataframe of samples
        """
        return pds.get_dummies(df[features])

    @staticmethod
    def upsample_minorities(df_training, imbalance_upsampling=None):
        """
        Note upsampling shall be down for training set ONLY.

        :param df_training:             dataframe for training
        :param prediction:              field to predict
        :param imbalance_upsampling:    None, True, False, or a dict
        :return:                        upsampled dataframe
        """

        if imbalance_upsampling is None or not imbalance_upsampling:
            # nothing to do
            return df_training

        if imbalance_upsampling == True:
            #
            # upsample every class to match the majority
            #
            counts = df_training.iloc[:, -1].value_counts()
            # first we need to figure out the count for the majority class
            maj_count = 0
            for itr in counts.iteritems():
                if itr[1] > maj_count:
                    maj_count = itr[1]

            # go through all the classes again and upsample if necessary
            dataf = pds.DataFrame()
            for itr in counts.iteritems():
                #
                # itr is a tuple (class_value, count)
                # Here we want to extract all the samples with the same
                # predicted value
                #
                class_df = df_training[df_training.iloc[:, -1] == itr[0]]
                if itr[1] < maj_count:
                    #
                    # Need to upsample it to maj_count
                    #
                    class_df = class_df.sample(maj_count,
                                               replace=True)

                dataf = pds.concat([dataf, class_df], axis=0)

            return dataf

        return df_training

    @staticmethod
    def remove_samples_with_values(data_frame, prediction, value_list):
        """
        Clean up the data_frame. Some of the values of the prediction can
        confuse the ML model. For example, unknowns.
        Customer can choose to remove those samples.

        :param data_frame:  dataframe to clean up
        :param prediction:  prediction
        :param value_list:  prediction values to remove
        :return:            cleaned up dataframe
        """

        dataf = data_frame
        for value in value_list:
            dataf = dataf[dataf[prediction] != value]

        # Need to re-arrange the index after dropping rows
        dataf.index = range(len(dataf))
        return dataf
