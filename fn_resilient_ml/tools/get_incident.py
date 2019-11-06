#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import os

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

args, unknown_args = parser.parse_known_args()
inc_id = int(args.id)
sen_file = args.sentence
ids_file = args.ids
vec_file = args.vec

with open(sen_file, "r") as infile:
    sentences = json.load(infile)
with open(ids_file, "r") as infile:
    ids = json.load(infile)

vecs = None
if os.path.exists(vec_file):
    with open(vec_file, "r") as infile:
        vecs = json.load(infile)

for i in range(len(ids)):
    if ids[i] == inc_id:
        print(sentences[i])


if vecs:
    i_id = str(inc_id)
    print(vecs[i_id][0])
    print(vecs[i_id][10])
    print(vecs[i_id][20])



