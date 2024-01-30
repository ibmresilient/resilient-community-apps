#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#------------------------------------------------------------------------------------------
#
#   file_summary:
#   -------------
#
#   res-ml stores ml model and associated data in different files. This module contains logic
#   to generate a summary for one of those files
#
import os
import time
from gensim.models import KeyedVectors
import json
import pickle


class FileManage():
    DEFAULT_SIF_FILE = "resilient-sif.pkl"
    DEFAULT_VEC_FILE = "resilient-vec.json"
    DEFAULT_NLP_FILE = "resilient-w2v.txt"
    DEFAULT_PCA_FILE = "resilient-pca.json"
    DEFAULT_INCIDENT_FILE = "resilient-incidents.csv"
    DEFAULT_ARTIFACT_FILE = "resilient-artifacts.json"

    FILE_NAME_OUTPUT        = "File:                        {}"
    LAST_MODIFICATION_TIME  = "Last modification time:      {}"
    NUM_SENTENCES           = "Number of sentences:         {}"
    NUM_WORDS_OUTPUT        = "Number of words:             {}"
    FEATURE_DIMENSION       = "Feature dimensions:          {}"
    NUM_VECTORS_OUTPUT      = "Number of vectors:           {}"

    def __init__(self, filename):
        self.filename = filename

    def get_summary(self):
        """
        Get the summary of an input file
        :return: Array of strings
        """
        ret = []
        file_exits = os.path.exists(self.filename)

        if not file_exits:
            return ["File {} not found.".format(self.filename)]

        file_name, file_ext = os.path.splitext(self.filename)
        if file_ext == ".txt" and file_name.endswith("-w2v"):
            # This is a saved NLP model file
            ret = self.get_summary_nlp()
        elif file_ext == ".json" and file_name.endswith("-vec"):
            # This is a file with saved vectors of all sample incidents
            ret = self.get_summary_saved_vec()
        elif file_ext == ".pkl" and file_name.endswith("-sif"):
            # This is a file with word counts used for SIF
            ret = self.get_summary_sif()
        elif file_ext == ".json" and file_name.endswith("-pca"):
            ret  = self.get_summary_pca()
        else:
            ret = ["Unable to detect the file type."]
        return ret

    def get_summary_nlp(self):
        """
        Return a summary of a NLP model file
        :return:
        """
        ret = []
        try:
            word2vec = KeyedVectors.load_word2vec_format(self.filename, binary=False)
            mtime = self._get_mtime()
            dim_vectors = word2vec.vector_size
            word_count = len(word2vec.vectors)

            ret.append("---------------------------")
            ret.append("Summary for NLP model file:")
            ret.append("---------------------------")
            ret.append(self.FILE_NAME_OUTPUT.format(self.filename))
            ret.append(self.LAST_MODIFICATION_TIME.format(mtime))
            ret.append(self.FEATURE_DIMENSION.format(dim_vectors))
            ret.append(self.NUM_SENTENCES.format(word_count))
            ret.append("\n")
        except Exception as e:
            ret.append("Failed to read NLP model {}.".format(self.filename))
            ret.append("Error: {}".format(e))

        return ret

    def get_summary_saved_vec(self):
        """
        Return a brief summary of a vec file. A vec file is the cache of
        all vectors of incidents. So here we output the dimension of each
        vector, and the number of vectors (incidents).
        :return:
        """
        ret = []
        try:
            mtime = self._get_mtime()
            data = json.load(open(self.filename, 'r'))


            ret.append("------------------------------")
            ret.append("Summary for saved vector file:")
            ret.append("------------------------------")

            ret.append(self.FILE_NAME_OUTPUT.format(self.filename))
            ret.append(self.LAST_MODIFICATION_TIME.format(mtime))
            key = list(data.keys())[0]
            ret.append(self.FEATURE_DIMENSION.format(len(data[key])))
            ret.append(self.NUM_VECTORS_OUTPUT.format(len(data)))
            ret.append("\n")
        except Exception as e:
            ret.append("Failed to read saved vector file {}.".format(self.filename))
            ret.append("Error: {}".format(e))

        return ret

    def get_summary_sif(self):
        """
        A SIF (Smooth Inverse Frequency) file contains the word counts. As a brief
        summary, return the total count of words
        :return:
        """
        ret = []
        try:
            mtime = self._get_mtime()
            ret.append("---------------------")
            ret.append("Summary for SIF file:")
            ret.append("---------------------")

            sif = pickle.load(open(self.filename, "rb"))

            ret.append(self.FILE_NAME_OUTPUT.format(self.filename))
            ret.append(self.LAST_MODIFICATION_TIME.format(mtime))
            ret.append(self.NUM_WORDS_OUTPUT.format(len(sif)))
            ret.append("\n")
        except Exception as e:
            ret.append("Failed to read SIF file {}.".format(self.filename))
            ret.append("Error: {}".format(e))
        return ret

    def get_summary_pca(self):
        """
        A PCA (Principle Component Analysis) file contains the principle
        vector component to be removed.
        :return:
        """
        ret = []
        try:
            mtime = self._get_mtime()
            ret.append("---------------------")
            ret.append("Summary for PCA file:")
            ret.append("---------------------")

            data = json.load(open(self.filename, 'r'))

            ret.append(self.FILE_NAME_OUTPUT.format(self.filename))
            ret.append(self.LAST_MODIFICATION_TIME.format(mtime))
            ret.append(self.FEATURE_DIMENSION.format(len(data)))
            ret.append("\n")
        except Exception as e:
            ret.append("Failed to read SIF file {}.".format(self.filename))
            ret.append("Error: {}".format(e))
        return ret

    def _get_mtime(self):
        """
        Get the last modification time for a file, and return readable string.
        :return:
        """
        mtime = os.path.getmtime(self.filename)
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))
        return time_str