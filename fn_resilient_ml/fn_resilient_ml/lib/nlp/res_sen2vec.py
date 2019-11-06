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
import json

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
        self.sentence_vectors = []
        self.feature_size = 0

    def get_vec_for_words(self, words):
        """

        :param words:
        :return:
        """
        self.feature_size = self.word2vec.vector_size
        v = np.zeros(self.feature_size, dtype="float64")

        count = 0
        for word in words:
            word_count = self.sif.get_word_count(word)
            if word_count > 0:
                try:
                    a_value = self.SIF_A / (self.SIF_A + word_count)
                    vec = np.multiply(a_value, self.word2vec[word])
                    v = np.add(v, vec)
                    count += 1
                except Exception as e:
                    # Not an error if word is not in the vocab
                    self.log.debug("{} is not in the vocab of the word2vec model".format(word))

        # normalize it
        if count != 0:
            v = np.divide(v, count)

        return v

    def get_vec_for_sentence(self, sentence):
        """

        :param sentence:
        :return:
        """
        words = self.utils.get_words(sentence)
        return self.get_vec_for_words(words)

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

    def cache_sentence_vectors(self, dataset, inc_ids, s2v_file):
        """
        Compute vectors for all sentences in the dataset and cache it to a file.
        They will be used later to compute similarity
        :param dataset: sentences for incident. A sentence includes the name, description,
                        resolution_summary, artifact values, and artifact descriptions
        :param inc_ids: list of incident ids corresponding to the sentences above
        :param s2v_file: file to store cached vectors
        :return:
        """
        ret = False
        if len(inc_ids) != len(dataset):
            self.log.error("Data mismatched! {} sentences and {} incident ids".format(len(dataset), len(inc_ids)))
            return ret

        sen_vecs = {}
        for i in range(len(inc_ids)):
            sen_vecs[inc_ids[i]] = list(self.get_vec_for_words(dataset[i]))

        with open(s2v_file, "w") as outfile:
            json.dump(sen_vecs, outfile)
            ret = True

        return ret

    def load_s2v(self, s2v_file):
        """
        Load cached vectors

        :param s2v_file:
        :return:
        """
        ret = False
        with open(s2v_file, "r") as infile:
            self.sentence_vectors = json.load(infile)
            ret = True

        if len(self.sentence_vectors.keys()) > 0:
            key = next(iter(self.sentence_vectors))
            self.feature_size = len(self.sentence_vectors[key])
        return ret

    def get_incident_vec(self, inc_id):
        """
        Get the vector for the given incident
        :param inc_id: Incident ID
        :return:
        """
        v = np.zeros(self.feature_size, dtype="float64")
        return self.sentence_vectors.get(inc_id, v)

    def get_closest(self, sentence, num):
        v1 = self.get_vec_for_sentence(sentence)
        v1_norm = np.linalg.norm(v1)
        closest = []
        incident_ids = list(self.sentence_vectors.keys())
        for i in range(num):
            v2 = np.array(self.sentence_vectors[incident_ids[i]])

            v2_norm = np.linalg.norm(v2)
            if v1_norm == 0 or v2_norm == 0:
                sim = 0
            else:
                sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            closest.append({
                "ref": incident_ids[i],
                "sim": sim
            })

        closest.sort(key=lambda u:u["sim"])

        for i in range(num, len(self.sentence_vectors)):
            v2 = np.array(self.sentence_vectors[incident_ids[i]])
            v2_norm = np.linalg.norm(v2)
            if v1_norm == 0 or v2_norm == 0:
                sim = 0
            else:
                sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            if sim > closest[0]["sim"]:
                closest[0] = {
                    "ref": incident_ids[i],
                    "sim": sim
                }
                closest.sort(key=lambda u: u["sim"])

        return closest