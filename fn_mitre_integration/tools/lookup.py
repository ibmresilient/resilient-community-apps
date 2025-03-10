# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
#
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
#

#
#   Debugging tool to lookup an item from MITRE ATT&CK STIX TAXII server
#

import sys
from fn_mitre_integration.lib.mitre_attack import MitreAttack
import json
from proxies import get_proxies

if len(sys.argv) < 2:
    print("Usage lookup.py item_name type_name[optional] collection_name[optional]")
    sys.exit()

item_name = sys.argv[1]
type_name = None
collection_name = None
if len(sys.argv) > 2:
    type_name = sys.argv[2]

if len(sys.argv) > 3:
    collection_name = sys.argv[3]

attack = MitreAttack(opts=None, function_opts=get_proxies())

attack.connect_server()

item = attack.lookup_item(item_name)

item_dict = json.loads(item.serialize())

print(item_dict)

