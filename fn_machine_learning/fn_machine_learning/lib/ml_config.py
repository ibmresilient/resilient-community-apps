# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#


class MlConfig(object):
    """
    This is basically a struct for organizing config data
    of a model
    """
    def __init__(self):
        # Data source
        self.data_file = None
        self.host = None
        self.separator = ','
        self.number_samples = 0

        self.selected_features = []
        self.predict_field = None
        self.model_name = "Logistic Regression"
        self.addition_method = None
        self.split_percentage = 0.5

        # Summary
        self.accuracy = 0.0
        self.analysis = None
        self.build_time = ""

        #
        #   Advanced (optional)
        #   1. Imbalance handling
        #
        self.class_weight = None
        self.imbalance_upsampling = None
        #
        #   2.Data proprocessing.
        #   Need this when rebuild from file
        #
        self.unwanted_values = None
        #
        #   3. Future features
        #
        self.feature_preprocess = {}

