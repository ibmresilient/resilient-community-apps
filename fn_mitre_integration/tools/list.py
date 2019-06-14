#
# https://medium.com/mitre-attack/att-ck-content-available-in-stix-2-0-via-public-taxii-2-0-server-317e5c41e214
#
#   Need pip install stix2
#        pip install taxii2-client
#

#
#   Debugging tool to list out all the items
#   Example:
#   python list

from stix2 import TAXIICollectionSource, Filter
from taxii2client import Server

server = Server("https://cti-taxii.mitre.org/taxii/")

api_root = server.api_roots[0]

#
# Three collections: Enterprise ATT&CK, PRE-ATT&CK, MOBILE
#
for collection in api_root.collections:
    print(collection.title + ": " + collection.id)
    #collection = Collection("https://cti-taxii.mitre.org/stix/collections/95ecc380-afe9-11e4-9b6c-751b66dd541e/")

    # Supply the collection to TAXIICollection
    tc_source = TAXIICollectionSource(collection)

    # Create filters to retrieve content from Enterprise ATT&CK
    filter_objs = {"techniques": Filter("type", "=", "attack-pattern"),
        "mitigations": Filter("type", "=", "course-of-action"),
        "groups": Filter("type", "=", "intrusion-set"),
        "malware": Filter("type", "=", "malware"),
        "tools": Filter("type", "=", "tool"),
        "relationships": Filter("type", "=", "relationship")
    }

    # filter for tactics
    #fltr = Filter("type", "=", "tactic")
    #tactics = tc_source.query(fltr)


    attack = {}
    # Retrieve all Enterprise ATT&CK content
    
    for key in filter_objs:
        attack[key] = tc_source.query(filter_objs[key])
        print("For {}, there are {}".format(key, len(attack[key])))
        for item in attack[key]:
            if key=="techniques" and item["name"] == "Valid Accounts":
                print("Found: " + item["id"])
        
    # For visual purposes, print the first technique received   
    #print("There are {}: \n {}".format(count, attack["techniques"]))
