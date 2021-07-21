# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""
    Script to modify versions of a requirements.txt file
    Takes 3 parameters:
        1: PATH_CURRENT_REQ_FILE
        2: PATH_NEW_REQ_FILE
        3: PACKAGES_TO_CHANGE: a JSON string with a list of the package(s) you want
           to update if found with a "name" and "version" key. Example:
           [{\"name\":\"resilient\",\"version\":\"40.1.1880\"},{\"name\":\"resilient-circuits\",\"version\":\"40.1.1880\"},{\"name\":\"resilient-lib\",\"version\":\"40.1.1880\"}]
"""

import sys
import json
import os

DOUBLE_EQUALS = "=="

args = sys.argv

assert len(args) == 4

SCRIPT_NAME = args[0]
PATH_CURRENT_REQ_FILE = args[1]
PATH_NEW_REQ_FILE = args[2]
PACKAGES_TO_CHANGE = args[3]

PACKAGES_TO_CHANGE = json.loads(PACKAGES_TO_CHANGE)

print("SCRIPT_NAME: {0}\nPATH_CURRENT_REQ_FILE: {1}\nPATH_NEW_REQ_FILE: {2}\nPACKAGES_TO_CHANGE: {3}".format(
    SCRIPT_NAME, PATH_CURRENT_REQ_FILE, PATH_NEW_REQ_FILE, PACKAGES_TO_CHANGE
))

print("Starting: {0}".format(os.path.basename(SCRIPT_NAME)))

assert os.path.isfile(PATH_CURRENT_REQ_FILE)

with open(PATH_CURRENT_REQ_FILE, mode="r") as current_req_file:

    while True:

        file_line = current_req_file.readline()

        # IF EOF break
        if not file_line:
            break

        # Handle only 'normal' dependencies
        if DOUBLE_EQUALS in file_line:
            dep = file_line.split(DOUBLE_EQUALS)

            for p in PACKAGES_TO_CHANGE:
                if p.get("name", "") == dep[0]:
                    print("Updating '{0}' to version '{1}'".format(p.get("name"), p.get("version")))
                    file_line = "{0}=={1}\n".format(p.get("name"), p.get("version"))

            with open(PATH_NEW_REQ_FILE, "a") as new_req_file:
                new_req_file.write(file_line)

print("Done! - new requirements file at: {0}".format(PATH_NEW_REQ_FILE))
