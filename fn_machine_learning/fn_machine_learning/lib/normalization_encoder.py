# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    ResNormalizationEncoder
    -----------------------
    The sk-learn LabelEncoder can be used to normalize float values.
    But it just replaces values into new values with delta = 1.
    For example, a column of [1, 10, 100, 10000] will be normalized
    into [0, 1, 2, 3].
    So it does not proportionally scale down the different.
    It works well with some algorithms according to our tests. But
    it does not work so well with SVM.

    So here a scaler is implemented to proportionally normalize
    values.
    Now [1, 10, 100, 10000] will be normalized into
    [1/(10000-1), 10/(10000-1), 100/(10000-1), 10000/(10000-1)]
"""


class ResNormalizationEncoder(object):

    def __init__(self):
        self.max = 1.0
        self.min = 0.0

    def find_max_min(self, col):
        """
        Find the max and min in a give column

        :param col:         Input column
        :return:
        """
        self.max = max(col)
        self.min = min(col)

    def fit(self, col):
        """
        This is the public method of an encoder
        We just need to figure out the max and min when this one is called.
        It shall be called before the transform method.

        :param col:         Input column
        :return:
        """
        self.find_max_min(col)

    def transform(self, col):
        """
        This is called after the fit call. Scale the input column

        :param col:         Input column
        :return:            Scaled column
        """
        delta = self.max - self.min
        ret = []
        for val in col:
            tmp = (val - self.min)/delta
            ret.append(tmp)

        return ret
