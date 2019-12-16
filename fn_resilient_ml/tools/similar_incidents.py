#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Given a sentence, find top n (default to 5) similar incidents
#   Usage::
#       similar_incidents.py _input_sentence_
#
#   Needs w2v for word2v, sif for SIF, and vec for cached vecs
#

import argparse
from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.res_sen2vec import ResSen2Vec
from fn_resilient_ml.lib.nlp.res_sif import ResSIF
from fn_resilient_ml.lib.nlp.res_nlp import ResNLP

parser = argparse.ArgumentParser(description="Find top similar incidents for a sentence")
parser.add_argument("sentence",
                    help="input sentence")

parser.add_argument("-n", "--num",
                    help="number of top similar incidents to return",
                    default=5)

parser.add_argument("-s", "--sif",
                    help="SIF file",
                    default=FileManage.DEFAULT_SIF_FILE)
parser.add_argument("-w", "--w2v",
                    help="trained word2vec model",
                    default=FileManage.DEFAULT_NLP_FILE)
parser.add_argument("-v", "--vec",
                    help="saved vectors for incidents",
                    default=FileManage.DEFAULT_VEC_FILE)

args, unknown_args = parser.parse_known_args()
sentence = args.sentence
sif_file = args.sif
w2v_file = args.w2v
vec_file = args.vec
num = int(args.num)

sif = ResSIF()
sif.load_sif(sif_file)

w2v = ResNLP()
w2v.load_model(w2v_file)

vec = ResSen2Vec(w2v.word2vec, sif)
vec.load_s2v(vec_file)

closest = vec.get_closest(sentence, num)
print("Find top {} closest incidents: ".format(num))
print("------------------------------")
print("\n")


for inc in closest:
    print("\t{}\t\t{}".format(inc["ref"], inc["sim"]))
