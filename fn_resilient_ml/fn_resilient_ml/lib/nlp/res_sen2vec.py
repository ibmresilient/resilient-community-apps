#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""
    ResSen2Vec
    ----------
    Based on word2vec, vectors for sentence will be computed, using SIF.

    This module relies on nlp_word2vec for word2vec, and res_sif for SIF
"""
import logging
import numpy as np
from fn_resilient_ml.lib.nlp.word_sentence_utils import WordSentenceUtils


class ResSen2Vec:
    # parameter used in compute frequency
    SIF_A = 1e-3

    def __init__(self, w2v, sif, log=None):
        # A NLPWord2Vec to get the vec for a word
        self.word2vec = w2v
        # A ResSIF used to get word count
        self.sif = sif
        # util to preprocess data
        self.utils = WordSentenceUtils()
        self.log = log if log else logging.getLogger(__name__)

    def get_vec_for_sentence(self, sentence):
        """

        :param sentence:
        :return:
        """
        words = self.utils.get_words(sentence)
        feature_size = self.word2vec.vector_size
        v = np.zeros(feature_size, dtype="float64")

        count = 0
        for word in words:
            word_count = self.sif.get_word_count(word)
            if word_count > 0:
                a_value = self.SIF_A/(self.SIF_A + word_count)
                vec = np.multiply(a_value, self.word2vec.get_vec(word))
                v = np.add(v, vec)
                count += 1

        # normalize it
        if count != 0:
            v = np.divide(v, count)

        return v

    def get_similarity(self, sentence1, sentence2):
        """
        Compute similarity of two sentences. It is the dot product of their vectors
        :param sentence1:
        :param sentence2:
        :return: float: similarity
        """
        vec1 = self.get_vec_for_sentence(sentence1)
        vec2 = self.get_vec_for_sentence(sentence2)

        sim = np.dot(vec1, vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))

        return sim

