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
from fn_resilient_ml.lib.file_manage import FileManage
import json
from sklearn.decomposition import PCA
from nltk.corpus import words as nltk_words
import nltk
import math

class ResSen2Vec:
    # parameter used in compute frequency
    SIF_A = 1e-3
    COUNT_THRESHOLD = 200

    def __init__(self, w2v, sif, log=None):
        # A NLPWord2Vec to get the vec for a word
        self.word2vec = w2v
        # A ResSIF used to get word count
        self.sif = sif
        # util to pre-process data
        self.utils = WordSentenceUtils()
        self.log = log if log else logging.getLogger(__name__)
        self.sentence_vectors = []
        self.feature_size = 0
        # download nltk resource if necessary
        nltk.download('words', quiet=True)
        self.setofwords = set(nltk_words.words())

        # pca vector
        self.pca_u = []

    def get_vec_for_words(self, words):
        """
        Here is the implementation of SIF (Smooth Inverse Frequency)
        :param words:
        :return:
        """
        self.feature_size = self.word2vec.vector_size
        # This is the accumulator. Initialize to zero vector first
        v = np.zeros(self.feature_size, dtype="float64")

        # given words of a sentence, now we are ready to compute the
        # vector for this sentence.
        count = 0               # count of how many words contributing to this sentence
        for word in words:
            if word in self.setofwords:
                # We only care about words in nltk words set
                word_count = self.sif.get_word_count(word)
                if word_count > 0:
                    # some words have unreasonably low count and adjust it a little bit
                    if word_count < self.COUNT_THRESHOLD:
                        word_count = self.COUNT_THRESHOLD - (self.COUNT_THRESHOLD - word_count)/2
                    try:
                        # This is the SIF method
                        a_value = self.SIF_A / (self.SIF_A + word_count)
                        vec = np.multiply(a_value, self.word2vec[word])
                        # accumulate it
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

    def remove_pca(self, vecs):
        """
        Remove the principle component from the vectors. This follows the recommendation of
        "A SIMPLE BUT TOUGH-TO-BEAT BASELINE FOR SENTENCE EMBEDDINGS",
        The reason according to them is that all vectors contain a common principle component
        that comes from common words. Here we use sk-learn PCA to do so
        :param vecs: input vectors
        :return: vectors with principle component removed
        """
        pca = PCA()
        pca.fit(np.array(vecs))
        u = pca.components_[0]

        # Need to store this PCA for later use when we compare incidents
        with open(FileManage.DEFAULT_PCA_FILE, 'w') as outfile:
            ul = list(u)
            json.dump(ul, outfile)

        u = np.multiply(u, np.transpose(u))

        # Corner case for small number of dataset. Pad with 0
        if len(u) < self.word2vec.vector_size:
            for i in range(self.word2vec.vector_size - len(u)):
                u = np.append(u, 0)

        ret = []
        for v in vecs:
            sub = np.multiply(u, v)
            ret.append(np.subtract(v, sub))

        return ret

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

        all_vecs = []
        for i in range(len(inc_ids)):
            all_vecs.append(self.get_vec_for_words(dataset[i]))

        vecs = self.remove_pca(all_vecs)

        sen_vecs = {}
        for i in range(len(inc_ids)):
            sen_vecs[inc_ids[i]] = list(vecs[i])

        # Cache the vector representation for incidents
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

    def load_pca(self, pca_file):
        """
        Load pca vector from file
        :param pca_file:
        :return:
        """
        with open(pca_file, "r") as infile:
            u = json.load(infile)
            self.pca_u = np.multiply(u, np.transpose(u))

    def get_incident_vec(self, inc_id):
        """
        Get the vector for the given incident
        :param inc_id: Incident ID
        :return:
        """
        v = np.zeros(self.feature_size, dtype="float64")
        return self.sentence_vectors.get(inc_id, v)

    def get_highest_inc_id(self):
        """
        Get the highest incident id in the vec file. This is the last incident in the
        vector cache file
        :return:
        """
        incident_ids = list(self.sentence_vectors.keys())
        return max(incident_ids)

    def get_closest(self, sentence, other_incidents, num, search_inc_id):
        """
        Given a sentence (such as the description of a new incident), find _num_ of closest (old) incidents
        :param sentence:            Description of the new incident
        :param other_incidents:     incidents created after the model is built
        :param num:                 number of incidents to return
        :param search_inc_id:       incident id of the (new) incident
        :return:
        """
        v1 = self.get_vec_for_sentence(sentence)
        # subtract pca
        sub = np.multiply(self.pca_u, v1)
        v1 = np.subtract(v1, sub)
        v1_norm = np.linalg.norm(v1)

        closest = []
        incident_ids = list(self.sentence_vectors.keys())
        for i in range(num):
            v2 = np.array(self.sentence_vectors[incident_ids[i]])

            v2_norm = np.linalg.norm(v2)
            if v1_norm == 0 or v2_norm == 0:
                sim = 0
            else:
                sim = np.dot(v1, v2) / (v1_norm * v2_norm)
            closest.append({
                "ref": incident_ids[i],
                "sim": sim,
                "vec": v2
            })

        closest.sort(key=lambda u:u["sim"])

        for i in range(num, len(self.sentence_vectors)):
            v2 = np.array(self.sentence_vectors[incident_ids[i]])
            v2_norm = np.linalg.norm(v2)
            if v1_norm == 0 or v2_norm == 0:
                sim = 0
            else:
                sim = np.dot(v1, v2) / (v1_norm * v2_norm)
            if sim > closest[0]["sim"]:
                closest[0] = {
                    "ref": incident_ids[i],
                    "sim": sim,
                    "vec": v2
                }
                closest.sort(key=lambda u: u["sim"])

        for i in range(len(other_incidents)):
            inc_id, inc_sentence = other_incidents[i]
            if search_inc_id is not None and search_inc_id != inc_id:
                #
                #   The (new) incident is also created after the
                #   nlp model was built. So it is most likely included
                #   in other_incidents. We don't need to include that
                #   in the return.
                #
                v2 = self.get_vec_for_sentence(inc_sentence)
                # subtract pca
                sub = np.multiply(self.pca_u, v2)
                v2 = np.subtract(v2, sub)
                v2_norm = np.linalg.norm(v2)
                if v1_norm == 0 or v2_norm == 0:
                    sim = 0
                else:
                    sim = np.dot(v1, v2) / (v1_norm * v2_norm)
                if sim > closest[0]["sim"]:
                    closest[0] = {
                        "ref": inc_id,
                        "sim": sim,
                        "vec": v2
                    }
                    closest.sort(key=lambda u: u["sim"])

        # Find the keywords that contribute the most to the similarity
        self.find_keywords(sentence, closest)

        return closest

    def find_keywords(self, sentence, closest):
        """
        For each incident in closest,  find words in sentence with highest contribution.

        :param sentence: description of the input (new) incident
        :param closest: the top closest incidents found
        :return: add "keywords" to each closest incident
        """
        w_util = WordSentenceUtils()
        words = w_util.get_words(sentence)
        for cl in closest:
            v2_1 = cl["vec"]
            v2_norm_1 = np.linalg.norm(v2_1)
            word_sim = []
            for w in words:
                try:
                    wc = self.sif.get_word_count(w)
                    if wc < self.COUNT_THRESHOLD:
                        wc = self.COUNT_THRESHOLD - (self.COUNT_THRESHOLD - wc)/2

                    a_value = ResSen2Vec.SIF_A / (ResSen2Vec.SIF_A + wc)
                    w_v = self.word2vec[w]
                    sub = np.multiply(self.pca_u, w_v)
                    w_v = np.subtract(w_v, sub)

                    sim = a_value * np.dot(w_v, v2_1) / (np.linalg.norm(w_v) * v2_norm_1)
                    word_sim.append((sim, w))
                except:
                    pass
            word_sim.sort(key=lambda u: u[0])
            top_5 = word_sim[:5]
            cl["keywords"] = ', '.join([ws[1] for ws in top_5])
