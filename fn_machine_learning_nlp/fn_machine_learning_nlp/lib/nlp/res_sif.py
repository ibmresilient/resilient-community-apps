#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""
    ResSIF
    ------
    SIF: Smooth Inverse Frequency
    This is a module to build the SIF counts. Inverse means that the higher the frequency (of a word)
    in the sample dataset, the lower the importance in computing similarity.

    So this module takes a sample data and compute count for each work. The count can then be used to
    compute the frequency.
"""
import itertools
from collections import Counter
import pickle
import logging

class ResSIF:
    def __init__(self, log=None):
        # the
        self.sif = None
        self.log = log if log else logging.getLogger(__name__)

    def build_sif(self, dataset):
        """
        Count words in dataset
        :param dataset: Same format as the dataset used by nlp_word2vec model. It is an array of arrays of words
        :return:
        """
        self.sif = Counter(itertools.chain(*dataset))

    def save_sif(self, filename):
        """

        :param filename: output file using pickle to save
        :return:
        """
        saved = False
        with open(filename, "wb") as outfile:
            if self.sif:
                pickle.dump(self.sif, outfile, protocol=pickle.HIGHEST_PROTOCOL)
                saved = True

        if not saved:
            self.log.error("Failed to save sif to {}".format(filename))

    def load_sif(self, filename):
        """

        :param filename: pickle file for saved sif
        :return:
        """
        loaded = False
        with open(filename, "rb") as infile:
            self.sif = pickle.load(infile)
            if self.sif is not None:
                loaded = True
        if not loaded:
            self.log.error("Failed to load sif from file {}.".format(filename))
        return loaded

    def get_word_count(self, word):
        """
        Get word count
        :param word:
        :return: word count
        """
        wc = 0
        try:
            wc = self.sif[word]
        except Exception as e:
            # it is not an error. It is possible that the word is not in sif, just return 0
            wc = 0
            self.log.debug("Word {} is not in sif".format(word))

        return wc