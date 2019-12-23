#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import os
from fn_resilient_ml.lib.nlp.res_sif import ResSIF

from fn_resilient_ml.lib.file_manage import FileManage

parser = argparse.ArgumentParser(description="Find words of an incident")
parser.add_argument("-i", "--id",
                    help="incident id")
parser.add_argument("-s", "--sentence",
                    help="sentence word file in json",
                    default="inc_sen.json")
parser.add_argument("-d", "--ids",
                    help="json file for incident ids",
                    default="inc_ids.json")
parser.add_argument("-v", "--vec",
                    help="vec file for incidnets",
                    default=FileManage.DEFAULT_VEC_FILE)
parser.add_argument("-f", "--sif",
                    help="sif file",
                    default=FileManage.DEFAULT_SIF_FILE)

args, unknown_args = parser.parse_known_args()
inc_id = int(args.id)
sen_file = args.sentence
ids_file = args.ids
vec_file = args.vec
sif_file = args.sif

with open(sen_file, "r") as infile:
    sentences = json.load(infile)
with open(ids_file, "r") as infile:
    ids = json.load(infile)

vecs = None

sif = ResSIF()
loaded = sif.load_sif(sif_file)

if loaded:
    w_c = []
    sens = [sentences[i] for i in range(len(ids)) if ids[i] == inc_id]
    for w in sens[0]:
        w_c.append((w, sif.get_word_count(w)))

    w_c.sort(key=lambda u:u[1])
    for w in w_c:
        print("%-20s %d"%(w[0], w[1]))
else:
    for i in range(len(ids)):
        if ids[i] == inc_id:
            print(sentences[i])
            break

if os.path.exists(vec_file):
    with open(vec_file, "r") as infile:
        vecs = json.load(infile)

if vecs:
    i_id = str(inc_id)
    print(vecs[i_id][0])
    print(vecs[i_id][10])
    print(vecs[i_id][20])



