#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""
    Debugging tool:
    example:
    get_tactic_url.py "Initial Access"
"""
import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
import json
from proxies import get_proxies

if len(sys.argv) < 2:
    print("Usage get_tactic_url.py tactic_name")
    sys.exit()

tactic_name = sys.argv[1]

url = MitreAttack(opts=None, function_opts=get_proxies()).get_tactic_url(tactic_name)

print(url)