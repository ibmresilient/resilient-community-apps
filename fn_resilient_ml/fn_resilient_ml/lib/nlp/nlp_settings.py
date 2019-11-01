#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""
    NLPSettings:
    -----------
    This file contains the configuration settings for NLP. This can allow the
    user to change these in the future, by reading from app.config for example
    Singleton design pattern
"""


class NLPSettings:
    # 2-gram Phrases
    BIGRAM_MIN_COUNT = 3
    BIGRAM_THRESHOLD = 10

    # parameters for word2vec
    # https://radimrehurek.com/gensim/models/word2vec.html
    WORD2VEC_WINDOW = 10
    WORD2VEC_MIN_COUNT = 2
    WORD2VEC_SAMPLE = 1e-3
    WORD2VEC_ALPHA = 0.03
    WORD2VEC_MIN_ALPHA=0.0007
    WORD2VEC_NEGATIVE = 20
    WORD2VEC_PROGRESS_PER = 10000
    WORD2VEC_EPOCHS = 30
    WORD2VEC_REPORT_DELAY = 1
    WORD2VEC_FEATURE_SIZE = 50

    # singleton
    __instance = None

    @staticmethod
    def get_instance():
        if NLPSettings.__instance is None:
            NLPSettings.__instance = NLPSettings()

        return NLPSettings.__instance

    def update_settings(self, opt):
        """
        Update settings using information from app.config
        :param opt:
        :return:
        """
        self._w2v_feature_size = opt.get("word2vec_feature_size", NLPSettings.WORD2VEC_FEATURE_SIZE)

    def __init__(self):
        self._w2v_feature_size = NLPSettings.WORD2VEC_FEATURE_SIZE

    def bigram_min_count(self):
        return self.BIGRAM_MIN_COUNT

    def bigram_threshold(self):
        return self.BIGRAM_THRESHOLD

    def w2v_window(self):
        return self.WORD2VEC_WINDOW

    def w2v_min_count(self):
        return self.WORD2VEC_MIN_COUNT

    def w2v_sample(self):
        return NLPSettings.WORD2VEC_SAMPLE

    def w2v_alpha(self):
        return NLPSettings.WORD2VEC_ALPHA

    def w2v_min_alpha(self):
        return NLPSettings.WORD2VEC_MIN_ALPHA

    def w2v_negative(self):
        return NLPSettings.WORD2VEC_NEGATIVE

    def w2v_progress_per(self):
        return NLPSettings.WORD2VEC_PROGRESS_PER

    def w2v_epochs(self):
        return NLPSettings.WORD2VEC_EPOCHS

    def w2v_report_delay(self):
        return NLPSettings.WORD2VEC_REPORT_DELAY

    def w2v_feature_size(self):
        return self._w2v_feature_size
