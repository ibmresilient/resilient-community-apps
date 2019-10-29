#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""
    ResNLP
    -----
    Encapsulation of a NLP model trained by Resilient incident data.

    A subclass of NLPWord2Vec
"""
import pandas as pds
from fn_resilient_ml.lib.nlp.nlp_word2vec import NLPWord2Vec

class ResNLP(NLPWord2Vec):
    def __init__(self, inc_file, art_file=None):
        self.inc_file = inc_file
        self.art_file = art_file
        self.dataframe = None

    def load_data(self):
        """
        Template method to load data
        :return:
        """
        self.dataframe = pds.read_csv(self.data_file,
                                      sep=',',
                                      )


    def preprocess_data(self):
        """
        Template method to preprocess data
        :return:
        """