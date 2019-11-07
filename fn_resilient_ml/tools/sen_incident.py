#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Given a sentence and an incident id, check their similarity
#   Usage:
#       sen_incident.py _input_sentence_ -i incident id -v [optional]
#   Need w2v for word2v, sif for SIF, vec for caced vecs
#   if -v is used, need inc_ids.json and inc_sen.json
import argparse
import numpy as np
from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.res_sen2vec import ResSen2Vec
from fn_resilient_ml.lib.nlp.res_sif import ResSIF
from fn_resilient_ml.lib.nlp.res_nlp import ResNLP
from fn_resilient_ml.lib.nlp.word_sentence_utils import WordSentenceUtils
import json

parser = argparse.ArgumentParser(description="Find similarity between given sentence and incident")

parser.add_argument("sentence",
                    help="input sentence")

parser.add_argument("-i", "--incident",
                    help="incident id")

parser.add_argument("-s", "--sif",
                    help="SIF file",
                    default=FileManage.DEFAULT_SIF_FILE)
parser.add_argument("-w", "--w2v",
                    help="trained word2vec model",
                    default=FileManage.DEFAULT_NLP_FILE)
parser.add_argument("-v", "--vec",
                    help="saved vectors for incidents",
                    default=FileManage.DEFAULT_VEC_FILE)
parser.add_argument("-d", "--debug",
                    help="print extra debug information",
                    action="store_true")
parser.add_argument("-a", "--all_ids",
                    help="json file of list of all incident ids",
                    default="inc_ids.json")
parser.add_argument("-e", "--inc_sen",
                    help="json file of list of words for incidents",
                    default="inc_sen.json")

args, unknow_args = parser.parse_known_args()

sentence = args.sentence
inc_id = int(args.incident)
sif_file = args.sif
w2v_file = args.w2v
vec_file = args.vec
debug = args.debug
all_ids_file = args.all_ids
inc_sen_file = args.inc_sen
s_util = WordSentenceUtils()
sif = ResSIF()
sif.load_sif(sif_file)

w2v = ResNLP()
w2v.load_model(w2v_file)

vec = ResSen2Vec(w2v.word2vec, sif)
vec.load_s2v(vec_file)

inc_vec = vec.get_incident_vec(str(inc_id))
sen_vec = vec.get_vec_for_sentence(sentence)
sim = np.dot(inc_vec, sen_vec)/(np.linalg.norm(inc_vec) * np.linalg.norm(sen_vec))

print("Similarity between input incident and sentence:")
print("\t\t%-30s %s"%("similarity:", sim))

if debug:
    print("Debug information:")
    with open(inc_sen_file, "r") as infile:
        sentences = json.load(infile)
    with open(all_ids_file, "r") as infile:
        ids = json.load(infile)

    inc_id_index = None
    for i in range(len(ids)):
        if ids[i] == inc_id:
            inc_id_index = i
            break
    if inc_id_index is not None:
        inc_v = vec.get_vec_for_words(sentences[inc_id_index])
        sim1 = np.dot(inc_vec, inc_v)/(np.linalg.norm(inc_vec) * np.linalg.norm(inc_v))
        print("\trecompute incident vec, and check with cached one. Sim shall be close to 1:")
        print("\t\t%-30s %s" % ("recom sim:", sim1))

        wrd1 = None
        wrd2 = None
        sim_max = 0

        words_1 = s_util.get_words(sentence)
        words_2 = sentences[inc_id_index]

        for w1 in words_1:
            for w2 in words_2:
                try:
                    v1 = w2v.get_word_vec(w1)
                    v2 = w2v.get_word_vec(w2)
                    sim1 = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
                    if abs(sim1) > sim_max:
                        sim_max = abs(sim1)
                        wrd1 = w1
                        wrd2 = w2
                except:
                    pass
        if sim_max != 0:
            print("\ttop matching words:")
            print("\t\t%-30s %s" % ("sentence:", wrd1))
            print("\t\t%-30s %s" % ("incident:", wrd2))
            print("\t\t%-30s %s" % ("similarity:", sim_max))

        print("\tsentence top 5 word count:")
        s_count = [(w, sif.get_word_count(w)) for w in words_1]
        s_count.sort(key=lambda u: u[1])
        for i in range(min(5, len(s_count))):
            print("\t\t%-30s %s" % (s_count[i][0] + ':', s_count[i][1]))
        print("\tincident top 5 word count:")
        s_count = [(w, sif.get_word_count(w)) for w in words_2]
        s_count.sort(key=lambda u: u[1])
        for i in range(min(5, len(s_count))):
            print("\t\t%-30s %s" % (s_count[i][0] + ':', s_count[i][1]))

        count_threshold = 10
        v2_high = np.zeros(w2v.word2vec.vector_size)
        v2_low = np.zeros(w2v.word2vec.vector_size)
        high_count = 0
        low_count = 0

        for w2 in words_2:
            wc = sif.get_word_count(w2)
            a_value = ResSen2Vec.SIF_A/(ResSen2Vec.SIF_A + wc)
            try:
                w_v = w2v.get_word_vec(w2)
                if wc > count_threshold:
                    v2_high += np.multiply(a_value, w2v.get_word_vec(w2))
                    high_count += 1
                else:
                    v2_low += np.multiply(a_value, w2v.get_word_vec(w2))
                    low_count += 1
            except:
                pass

        if high_count > 0:
            v2_high /= high_count
        if low_count > 0:
            v2_low /= low_count
        sim_high = np.dot(v2_high, sen_vec)/(np.linalg.norm(v2_high) * np.linalg.norm(sen_vec))
        print("\tLow sim: {}".format(sim_high))