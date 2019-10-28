#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#

"""
    WordSentenceUtils
    -------------------
    Collection of functions in preprocessing sentences and words
"""
# nltk
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
# BeautifulSoup to clean up html tags. MIT license
from bs4 import BeautifulSoup

class WordSentenceUtils:
    def __init__(self):
        nltk.download("wordnet")
        nltk.download("stopwords")
        nltk.download('averaged_perceptron_tagger')
        self.remove_list = ", . ; ? ~ ! * ) ( { } $ # @ < > ] [".split()
        self.lem = WordNetLemmatizer()

    @staticmethod
    def _convert(nlk_tag):
        """
        Convert nlk tag to wordnet flag
        :param nlk_tag:
        :return:
        """
        if nlk_tag.startswith('J'):
            return wordnet.ADJ
        elif nlk_tag.startswith('V'):
            return wordnet.VERB
        elif nlk_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    def clean_str(self, sentence):
        """
        Remove some symbols
        :param sentence:
        :return:
        """
        for w in self.remove_list:
            sentence = sentence.replace(w, ' ')
        return sentence

    def get_words(self, sentence):
        """

        :param sentence:
        :return:
        """
        soup = BeautifulSoup(sentence)
        sentence = soup.get_text()
        sentence = self.clean_str(sentence)
        words = sentence.lower().split()
        nltk_tag = nltk.pos_tag(words)

        ws = [self.lem.lemmatize(w, self._convert(t)) for w, t in nltk_tag if w not in stopwords.words("english")]

        return ws



