#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""
    NLPWord2Vec
    -----------
    NLP model using gensim word2vec
    This a super class that encapsulates the common logic of building a NLP model using word2vec. The
    subclass shall implement the logic to read in dataset using to build the NLP model
"""
from abc import abstractmethod
from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.nlp_settings import NLPSettings
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import gensim
import numpy as np
import multiprocessing
import logging


class NLPWord2Vec:
    def __init__(self, model_name=None, log=None):
        # word2vec model. It is a gensim.models.Word2Vec
        self.word2vec = None
        #
        # dataset used to train the word2vec model
        # It is a list of list of words. Ex.[[security, incident],[window, mac, linux], ....]
        # Data shall be preprocessed by subclass
        #
        self.dataset = []
        # model name. This is used to save the model into a file
        self.model_name = model_name
        self.log = log if log else logging.getLogger(__name__)
        self.feature_size = 0

    @abstractmethod
    def preprocess_data(self):
        """
        Use Template Method design pattern to allow subclass to customize the preprocess step.

        Subclass shall implement this method to read in data, preprocess it as necessary and generate
        self.dataset for this class to consume. This class uses dataset directly.
        :return:
        """
        return

    @abstractmethod
    def load_data(self):
        """
        Template Method design pattern. Subclass must implment
        this to load data.
        :return:
        """
        return

    def save_model(self, w2v_file):
        """
        Save the NLP model into a txt file.
        :return:
        """
        model_file = w2v_file
        if self.model_name is not None:
            model_file = self.model_name + "-w2v.txt"

        self.word2vec.wv.save_word2vec_format(model_file, binary=False)

    def load_model(self, file_name=None):
        """
        Load a saved model
        :param file_name: [optional] model file. Use default if None
        :return:
        """
        model_file = file_name if file_name else FileManage.DEFAULT_NLP_FILE
        try:
            self.word2vec = KeyedVectors.load_word2vec_format(model_file, binary=False)
        except Exception as e:
            self.log.error("Failed to load a saved model {}".format(model_file))

    def build_model(self):
        """

        :return:
        """
        # call template method to load and preprocess data
        self.load_data()
        self.preprocess_data()

        # get the settings for NLP
        nlp_settings = NLPSettings.get_instance()
        self.feature_size = nlp_settings.w2v_feature_size()

        bigram = gensim.models.phrases.Phrases(self.dataset,
                                               min_count=nlp_settings.bigram_min_count(),
                                               threshold=nlp_settings.bigram_threshold())

        bigram = gensim.models.phrases.Phraser(bigram)

        tokenized_corpus = bigram[self.dataset]

        word2vec = Word2Vec(size=self.feature_size,
                            window=nlp_settings.w2v_window(),
                            min_count=nlp_settings.w2v_min_count(),
                            sample=nlp_settings.w2v_sample(),
                            alpha=nlp_settings.w2v_alpha(),
                            min_alpha=nlp_settings.w2v_min_alpha(),
                            negative=nlp_settings.w2v_negative(),
                            workers=multiprocessing.cpu_count() - 1)
        # Build Vocabulary
        word2vec.build_vocab(tokenized_corpus,
                             progress_per=nlp_settings.w2v_progress_per())
        # Train
        word2vec.train(tokenized_corpus,
                       total_examples=word2vec.corpus_count,
                       epochs=nlp_settings.w2v_epochs(),
                       report_delay=nlp_settings.w2v_report_delay())

        self.word2vec = word2vec

    def get_word_vec(self, word):
        """
        Get the vector (word embedding) for a word
        :param word:
        :return:
        """
        vec = np.zeros(self.feature_size, dtype="float64")
        try:
            vec = self.word2vec[word]
        except Exception as e:
            # Note, this is not an error. Just log debug info
            self.log.debug("Word {} not found in built model".format(word))
        return vec
