#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   Given two sentences, compute the similarity.
#   Use w2v for word2vec, sif for SIF.
#

import argparse
import numpy as np
from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.res_sen2vec import ResSen2Vec
from fn_resilient_ml.lib.nlp.res_sif import ResSIF
from fn_resilient_ml.lib.nlp.res_nlp import ResNLP
from fn_resilient_ml.lib.nlp.word_sentence_utils import WordSentenceUtils
parser = argparse.ArgumentParser(description="Compute similarity between two sentences")
parser.add_argument("sentence1",
                    help="sentence 1")
parser.add_argument("sentence2",
                    help="sentence 2")

parser.add_argument("-s", "--sif",
                    help="SIF file",
                    default=FileManage.DEFAULT_SIF_FILE)
parser.add_argument("-w", "--w2v",
                    help="trained word2vec model",
                    default=FileManage.DEFAULT_NLP_FILE)
parser.add_argument("-v", "--verbose",
                    action="store_true")

args, unknown_args = parser.parse_known_args()

COEFFICIENT_TEMPLATE = u"""\t\t%-30s %s"""

sen1 = args.sentence1
sen2 = args.sentence2
sif_file = args.sif
w2v_file = args.w2v
verbose = args.verbose

sif = ResSIF()
sif.load_sif(sif_file)

w2v = ResNLP()
w2v.load_model(w2v_file)

s2v = ResSen2Vec(w2v=w2v.word2vec,
                 sif=sif)

sim = s2v.get_similarity(sen1, sen2)

s_util = WordSentenceUtils()

words_1 = s_util.get_words(sen1)
words_2 = s_util.get_words(sen2)

print("\nsen_sim:")
print("--------")

print("\tsentence 1 coefficients:")
for w in words_1:
    c = ResSen2Vec.SIF_A/(ResSen2Vec.SIF_A + sif.get_word_count(w))
    print(COEFFICIENT_TEMPLATE%(w + ':', c))

print("\tsentence 2 coefficients:")
for w in words_2:
    c = ResSen2Vec.SIF_A/(ResSen2Vec.SIF_A + sif.get_word_count(w))
    print(COEFFICIENT_TEMPLATE%(w + ":", c))

wrd1 = None
wrd2 = None
sim_max = 0
if verbose:
    for w1 in words_1:
        for w2 in words_2:
            try:
                v1 = w2v.get_word_vec(w1)
                v2 = w2v.get_word_vec(w2)
                sim1 = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                if abs(sim1) > sim_max:
                    sim_max = abs(sim1)
                    wrd1 = w1
                    wrd2 = w2
            except:
                pass
    if sim_max != 0:
        print("\ttop matching words:")
        print("\t\t%-30s %s"%("sentence1:", wrd1))
        print("\t\t%-30s %s"%("sentence2:", wrd2))
        print("\t\t%-30s %s"%("similarity:", sim_max))

print("\tsentence similarity:")
print("\t\t%-30s %s"%("similarity:", sim))


