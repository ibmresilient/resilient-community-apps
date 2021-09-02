# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""
    Script to update given attribute in setup.py file
    Takes 3 parameters:
        1: PATH_SETUP_PY_FILE: e.g: "./setup.py"
        2: ATTRIBUTE_TO_EDIT: Attribute name to update: e.g. "version"
        3: NEW_ATTRIBUTE_VALUE: the full value of the new line e.g. "version=\"1.2.1234\","
"""

import sys
import os

args = sys.argv

assert len(args) == 4

SCRIPT_NAME = args[0]
PATH_SETUP_PY_FILE = args[1]
ATTRIBUTE_TO_EDIT = args[2]
NEW_ATTRIBUTE_VALUE = args[3]

print("SCRIPT_NAME: {0}\nPATH_SETUP_PY_FILE: {1}\nATTRIBUTE_TO_EDIT: {2}\nNEW_ATTRIBUTE_VALUE: {3}".format(
    SCRIPT_NAME, PATH_SETUP_PY_FILE, ATTRIBUTE_TO_EDIT, NEW_ATTRIBUTE_VALUE
))

print("Starting: {0}".format(os.path.basename(SCRIPT_NAME)))

assert os.path.isfile(PATH_SETUP_PY_FILE)
ATTRIBUTE_TO_EDIT = "{0}=".format(ATTRIBUTE_TO_EDIT)

original_setup_py_lines = []
INSERT_INDEX = -1

with open(PATH_SETUP_PY_FILE, mode="r") as setup_py_file:
    print("Getting original setup_py lines from: {0}".format(PATH_SETUP_PY_FILE))
    original_setup_py_lines = setup_py_file.readlines()

print("Looking for line with attribute: '{0}'".format(ATTRIBUTE_TO_EDIT))
for i in range(len(original_setup_py_lines)):
    if ATTRIBUTE_TO_EDIT in original_setup_py_lines[i]:
        INSERT_INDEX = i
        print("Attribute found on line: '{0}'".format(INSERT_INDEX))
        current_attribute = original_setup_py_lines[i].strip()
        original_setup_py_lines[i] = original_setup_py_lines[i].replace(current_attribute, NEW_ATTRIBUTE_VALUE)
        break

if INSERT_INDEX == -1:
    raise ValueError("A line containing '{0}' in '{1}' could not be found".format(ATTRIBUTE_TO_EDIT, PATH_SETUP_PY_FILE))

with open(PATH_SETUP_PY_FILE, mode="w") as setup_py_file:
    print("Overwriting setup.py file with attribute updated")
    setup_py_file.writelines(original_setup_py_lines)

print("Done!")
