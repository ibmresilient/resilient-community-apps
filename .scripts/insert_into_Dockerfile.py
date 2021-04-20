# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""
    Script to insert into Dockerfile after line with given Keyword
    Takes 3 parameters:
        1: PATH_DOCKERFILE: e.g: "./Dockerfile"
        2: DOCKERFILE_KEYWORD: Keyword in line to insert after - e.g.: "registry.access.redhat.com"
        3: DOCKERFILE_WORDS_TO_INSERT: a JSON string with a list of the lines you want to insert
           Example:
           "[\"\\n\", \"COPY ./new_requirements.txt /tmp/new_requirements.txt\\n\", \"RUN pip install -r /tmp/new_requirements.txt\\n\"]"
"""

import sys
import os
import json

args = sys.argv

assert len(args) == 4

SCRIPT_NAME = args[0]
PATH_DOCKERFILE = args[1]
DOCKERFILE_KEYWORD = args[2]
DOCKERFILE_WORDS_TO_INSERT = args[3]

DOCKERFILE_WORDS_TO_INSERT = json.loads(DOCKERFILE_WORDS_TO_INSERT)

print("SCRIPT_NAME: {0}\nPATH_DOCKERFILE: {1}\nDOCKERFILE_KEYWORD: {2}\nDOCKERFILE_WORDS_TO_INSERT: {3}".format(
    SCRIPT_NAME, PATH_DOCKERFILE, DOCKERFILE_KEYWORD, DOCKERFILE_WORDS_TO_INSERT
))

print("Starting: {0}".format(os.path.basename(SCRIPT_NAME)))

assert os.path.isfile(PATH_DOCKERFILE)

original_dockerfile_lines = []
INSERT_INDEX = -1

with open(PATH_DOCKERFILE, mode="r") as dockerfile:
    print("Getting original Dockerfile lines from: {0}".format(PATH_DOCKERFILE))
    original_dockerfile_lines = dockerfile.readlines()

print("Looking for line with Keyword: '{0}'".format(DOCKERFILE_KEYWORD))
for i in range(len(original_dockerfile_lines)):
    if DOCKERFILE_KEYWORD in original_dockerfile_lines[i]:
        INSERT_INDEX = i
        print("Keyword found on line: '{0}'".format(INSERT_INDEX))
        break

if INSERT_INDEX == -1:
    raise ValueError("A line containing '{0}' in '{1}' could not be found".format(DOCKERFILE_KEYWORD, PATH_DOCKERFILE))

for w in range(len(DOCKERFILE_WORDS_TO_INSERT)):
    insert_line_index = INSERT_INDEX + w + 1
    print("Inserting line: {0!r} on line '{1}'".format(DOCKERFILE_WORDS_TO_INSERT[w], insert_line_index))
    original_dockerfile_lines.insert(insert_line_index, DOCKERFILE_WORDS_TO_INSERT[w])


with open(PATH_DOCKERFILE, mode="w") as dockerfile:
    print("Overwriting Dockerfile with new insertions")
    dockerfile.writelines(original_dockerfile_lines)

print("Done!")
