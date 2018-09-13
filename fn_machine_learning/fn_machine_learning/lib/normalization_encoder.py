# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#


class ResNormalizationEncoder(object):
    """
    LabelEncoder can be used to normalize float values.
    But it just replaces values into new values with delta = 1
    So it does not proportionally scale down the different.
    It works well with some algorithms according to our tests. But
    it does not work so well with SVM.
    So here a scaler is implemented to proportionally normalize
    values
    """
    def __init__(self):
        self.max = 1.0
        self.min = 0.0

    def find_max_min(self, col):
        """

        :return:
        """
        self.max = max(col)
        self.min = min(col)

    def fit(self, col):
        self.find_max_min(col)

    def transform(self, col):
        delta = self.max - self.min
        ret = []
        for val in col:
            tmp = (val - self.min)/delta
            ret.append(tmp)

        return ret
