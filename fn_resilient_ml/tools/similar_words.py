#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Given a input word, found n top similar words using a given model
#   Usage:
#       similar_words _input_word -n 5 -m model_file
#
from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.nlp_word2vec import NLPWord2Vec

import numpy as np

import argparse

parser = argparse.ArgumentParser(description="Find top similar words")
parser.add_argument("word",
                    help="input word")
parser.add_argument("-n", "--number",
                    help="number of top similar words to return",
                    default=5)
parser.add_argument("-m", "--model",
                    help="word2vec model saved in txt format",
                    default=FileManage.DEFAULT_NLP_FILE)

args, unknown_args = parser.parse_known_args()

model_file = args.model
num_return = int(args.number)
word = args.word

print("similar-words:")
print("-------------")
print("Searching top {} word similar to {} using model {}".format(num_return, word, model_file))

def get_sim(v1, v1_norm, w):
    v2 = w2v.get_word_vec(w)
    v2_norm = np.linalg.norm(v2)
    if v1_norm == 0 or v2_norm == 0:
        sim = 0
    else:
        sim = np.dot(v1, v2) / (v1_norm * v2_norm)

    return {
        "word": w,
        "sim": sim
    }

w2v = NLPWord2Vec()
w2v.load_model(model_file)

v1 = w2v.get_word_vec(word)
v1_norm = np.linalg.norm(v1)
all_words = w2v.word2vec.index2word

closest = []
init = False
for w in all_words:
    d = get_sim(v1, v1_norm, w)

    if init is False:
        if len(closest) < num_return:
            closest.append(d)
        if len(closest) == num_return and init is False:
            closest.sort(key=lambda u:u["sim"])
            init = True
    else:
        if d["sim"] > closest[0]["sim"]:
            closest[0] = d
            closest.sort(key=lambda u:u["sim"])

for c in closest:
    print("{}: {}".format(c["word"], c["sim"]))
