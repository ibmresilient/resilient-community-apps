# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""
    Script to modify get package_name from commit message
    Takes 1 parameters:
        1: COMMIT_MSG: e.g 'INT-000: [fn_utilities] fix bug with - Bump to version 3.0.0'
"""

import sys
import re

args = sys.argv

assert len(args) == 2

SCRIPT_NAME = args[0]
COMMIT_MSG = args[1]

if COMMIT_MSG.startswith("Merge"):
    print("MERGE")
    exit(0)

regex = re.compile(r'(?:INT-\d+: \[)(.+)(?=])')
package_name = regex.match(COMMIT_MSG).groups()

if not isinstance(package_name, tuple) and len(package_name) != 1:
    # package_name could not be found in COMMIT_MSG
    print(1)

print(package_name[0])
