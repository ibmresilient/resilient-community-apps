# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
import pandas as pds
import json
import logging


class MultiIdBinarizer(object):
    """
    This is an extention to MultiLabelBinarizer. Instead of handling list
    of string, here we handle list of both strings and integers.
    Also we combine the csv list handler here. So it can handle directly
    a list as a string.
    """
    def __init__(self):
        self.new_col = []           # list of names of new cols
        self.mapping_dict = {}      # mapping between a value and a new col
        self.col_name = ""

    def fit(self, col, col_name):
        """

        :param col: Column of a dataframe. It is a list of string, and each string
        is also a list. Sample of col: ["[1,2,3]", "[2]", "[5,6,7]"]
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
