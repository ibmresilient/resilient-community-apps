#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Given an input word, find its word count. This determines the contribution to the similarity
#   calculation. Note that the higher the word count the less important it is
#   Usage:
#       check_sif.py _input_word -m (optional) model_file

from fn_resilient_ml.lib.file_manage import FileManage
from fn_resilient_ml.lib.nlp.res_sif import ResSIF
from fn_resilient_ml.lib.nlp.res_sen2vec import ResSen2Vec
import argparse

parser = argparse.ArgumentParser(description="Find word count from SIF")
parser.add_argument("word",
                    help="input word")
parser.add_argument("-s", "--sif",
                    help="sif file serialized using python pickle",
                    default=FileManage.DEFAULT_SIF_FILE)

args, unknown_args = parser.parse_known_args()

word = args.word
sif_file = args.sif

print("check-sif:")
print("----------")
print("Check SIF word count for \'{}\' using sif file {}:\n".format(word, sif_file))

sif = ResSIF()
sif.load_sif(sif_file)

count = sif.get_word_count(word)
coefficient = ResSen2Vec.SIF_A/(ResSen2Vec.SIF_A + count)
print("\tword count:\t\t\t{}".format(count))
print("\tcoefficient:\t\t\t{}".format(coefficient))