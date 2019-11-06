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
import json
import logging
from fn_resilient_ml.lib.nlp.nlp_word2vec import NLPWord2Vec
from fn_resilient_ml.lib.nlp.word_sentence_utils import WordSentenceUtils
from fn_resilient_ml.lib import util_functions
from fn_resilient_ml.lib.nlp.res_sif import ResSIF
from fn_resilient_ml.lib.nlp.res_sen2vec import ResSen2Vec
from fn_resilient_ml.lib.file_manage import FileManage

class ResNLP(NLPWord2Vec):
    def __init__(self, inc_file=None, art_file=None, in_log=None):
        self.inc_file = inc_file
        self.art_file = art_file
        self.dataframe = None
        self.artifacts = None

        self.sif = ResSIF()
        self.log = in_log if in_log else logging.getLogger(__name__)
        self.inc_ids = []
        super(ResNLP, self).__init__()

    def load_data(self):
        """
        Template method to load data
        :return:
        """
        self.dataframe = pds.read_csv(self.inc_file,
                                      sep=',',
                                      usecols=["id", "name", "description", "resolution_summary"],
                                      skipinitialspace=True,
                                      quotechar='"')
        try:
            # The artifacts are fetched using /search_ex. Make sure it is there.
            if self.art_file:
                self.artifacts = json.load(open(self.art_file, "r"))
        except Exception as e:
            self.artifacts = None
            self.log.info("Failed to load artifact file: {}".format(self.art_file))

    def preprocess_data(self):
        """
        Template method to preprocess data
        :return:
        """
        self.dataset = []
        self.inc_ids = []
        word_utils = WordSentenceUtils()
        row_count = self.dataframe.shape[0]

        for index in range(row_count):
            row = self.dataframe.iloc[index]
            #
            #   Retrieve the name, description, and resolution_summary from an incident
            #
            sentence = str(row["name"]) + " " + str(row["description"] + " " + str(row["resolution_summary"]))
            #
            #   Retrieve the artifact value and description from an incident
            #
            inc_id = int(row["id"])
            if self.artifacts is not None:
                artifact_des = util_functions.get_artifact_des(inc_id, self.artifacts)
                sentence += artifact_des
            ws = word_utils.get_words(sentence)

            self.inc_ids.append(inc_id)
            self.dataset.append(ws)

    def build(self):
        """
        Build word2vec, sif,
        :return:
        """
        #
        #   Build gensim word2vec model
        #
        self.build_model()
        #
        #   Build SIF
        #
        self.sif.build_sif(self.dataset)

    def save(self, w2v_file=None, sif_file=None, s2v_file=None):
        """
        Save word2vec, sif
        :return:
        """
        #
        #   Save gensim.word2vec
        #
        w2vfile = w2v_file if w2v_file else FileManage.DEFAULT_NLP_FILE
        self.save_model(w2vfile)
        #
        #   Save SIF data
        #
        siffile = sif_file if sif_file else FileManage.DEFAULT_SIF_FILE
        self.sif.save_sif(siffile)
        #
        #   Save vec cache
        #
        s2vfile = s2v_file if s2v_file else FileManage.DEFAULT_VEC_FILE
        sen2vec = ResSen2Vec(w2v=self.word2vec,
                             sif=self.sif,
                             log=self.log)
        sen2vec.cache_sentence_vectors(self.dataset, self.inc_ids, s2vfile)


