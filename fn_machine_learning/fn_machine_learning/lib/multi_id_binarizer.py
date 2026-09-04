# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    MultiIdBinarizer
    ----------------
    This is an extension of MultiLabelBinarizer.
    It can take a list of string like ["[1,2,3]", "[2]", "[5,6,7]"] directly from
    a CSV file, and binarizes them.

    Basically, MultiIdBinarizer needs to create 6 new features for the above example
    column. It uses the original column name. For example, if the original column name is
    "feature1", then this class is going to create 6 new features: "feature1_1", "feature1_2", "feature_3",
    "feature_5", "feature_6", "feature_7".
    Then the values for each of the three samples above will be translated into
                feature1    feature1_1  feature1_2  feature1_3  feature1_5 feature1_6   feature1_7
    Sample1     [1,2,3]         1           1           1           0           0           0
    Sample2     [2]             0           1           0           0           0           0
    Sample3     [5,6,7]         0           0           0           1           1           1

    Then feature1 is removed from the dataset after the translation

"""
import json
import logging


class MultiIdBinarizer(object):

    def __init__(self):
        self.new_col = []           # list of names of new cols
        self.mapping_dict = {}      # mapping between a value and a new col
        self.col_name = ""

    def fit(self, col, col_name):
        """

        :param col:         Column of a dataframe. It is a list of string, and each string
                            is also a list. Example of col: ["[1,2,3]", "[2]", "[5,6,7]"]
        :param col_name:    Column Name
        :return: None
            """
        log = logging.getLogger(__name__)
        self.col_name = col_name
        union_list = []
        try:
            for str_tmp in col:
                li = json.loads(str_tmp)
                union_list = MultiIdBinarizer.union(union_list, li)
        except Exception as e:
            log.error("Error " + str(e))

        for li_item in union_list:
            new_col_name = u"{ori_name}_{value}".format(ori_name=col_name,
                                                        value=str(li_item))
            self.mapping_dict[str(li_item)] = new_col_name
            self.new_col.append(new_col_name)

        return

    def transform(self, df, in_log=None):
        """

        :param df: dataframe to transform
        :param in_log:
        :return:
        """
        log = in_log if in_log else logging.getLogger(__name__)
        col = df[self.col_name]
        col_size = len(col)

        # Add new cols
        for name in self.new_col:
            df[name] = [0 for x in range(col_size)]

        for x in range(col_size):
            try:
                #
                # cik[x] could be a list
                #
                li = []
                if isinstance(col[x], list):
                    li = col[x]
                else:
                    li = json.loads(col[x])
                for val in li:
                    new_col_name = self.mapping_dict[str(val)]
                    df.loc[x, new_col_name] = 1

            except Exception as e:
                log.error("Error")

        df_new = df.drop(self.col_name, 1)
        return df_new

    @staticmethod
    def union(a, b):
        return list(set(a)|set(b))

    @staticmethod
    def is_multi_selection(col):
        """
        Check if col is one we can handler
        :param col:
        :return:
        """
        is_list = False
        try:
            multi_select = json.loads(col[0])
            if isinstance(multi_select, list):
                is_list = True
        except:
            # Assume that it is not a list
            is_list = False

        return is_list
