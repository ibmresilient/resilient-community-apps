# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#

#
#   MitreAttack:
#   ------------
#

from stix2 import TAXIICollectionSource, Filter
from taxii2client import Server

MITRE_URL = "https://cti-taxii.mitre.org/taxii/"
TACTIC_BASE_URL = "https://attack.mitre.org/tactics"

class MitreAttackTactic(object):
    """
    Note that this class is necessary because the current MITRE STIX TAXII server
    does not provide tactic information yet.
    """

    mitre_tactics = []

    @staticmethod
    def populate():
        """
        Populate a static list
        :return:
        """
        MitreAttackTactic.mitre_tactics = [
        ]

    @staticmethod
    def get_id(name):
        """
        Given a tactic name, return the id
        :param name: tactic name
        :return: id
        """
        id = None
        for tactic in MitreAttackTactic.mitre_tactics:
            #
            # Just in case the name is case-insensitive
            #
            if name.lower() == tactic.name.lower():
                id = tactic.id
                break

        return id

    @staticmethod
    def get_name(id):
        """
        Given a tatic id, return the name
        :param id: tactic id
        :return: name
        """
        name = None
        for tactic in MitreAttackTactic.mitre_tactics:
            if id.lower() == tactic.id.lower():
                name = tactic.name
                break

        return name

    def __init__(self, name=None, id=None, description=""):
        """
        :param name:
        :param id:
        :param description:
        """
        self.name = name
        self.id = id
        self.description = description

"""
    MitreAttack:
    -----------
    
    A facet class to encapsulate all the features related to fetching the
    MITRE STIX TAXII server
"""


class MitreAttack(object):
    """
    Facet design pattern. Outside calls shall go through this class
    """
    def __init__(self):
        MitreAttackTactic.populate()
        self.attack_server = None
        self.collection_dict = {}

    def connect_server(self, url=None):
        """
        Allow user to specify what url to use
        :param url:
        :return:
        """
        server_url = MITRE_URL if url is None else url
        self.attack_server = Server(server_url)
        api_root = self.attack_server.api_roots[0]

        for collection in api_root.collections:
            self.collection_dict[collection.title] = collection

    def lookup_item(self,
                    item_name,
                    collection_title="Enterprise ATT&CK",
                    type_name="attack-pattern"):
        """
        Look up an item using item name
        :param item_name:
        :param collection_title:
        :param type_name:
        :return:
        """
        ret_item = None
        if self.attack_server is None:
            self.connect_server()
        try:
            collection = self.collection_dict[collection_title]
            tc_source = TAXIICollectionSource(collection)
            query_filter = Filter("type", "=", type_name)

            attack = tc_source.query(query_filter)
            for item in attack:
                if item["name"] == item_name:
                    ret_item = item
                    break
        except:
            ret_item = None

        return ret_item

    @staticmethod
    def get_all_tactics():
        """
        Get all the tactics
        :return:
        """
        return MitreAttackTactic.mitre_tactics

    @staticmethod
    def get_tactic_url(tactic_name):
        """
        Get the url link for a tactic
        :param tactic_name:
        :return:
        """
        t_id = MitreAttackTactic.get_id(tactic_name)
        if t_id is None:
            return None

        url = "{}/{}/".format(TACTIC_BASE_URL, t_id)

        return url

    def get_tech(self, name=None, ext_id=None):
        """
        Use tech name or external id to retrieve tech
        :param name:
        :param ext_id:
        :return:
        """
        if name is None and ext_id is None:
            return None

        type_filter = Filter("type", '=', "attack-pattern")

        filt = None
        if name is not None:
            filt = Filter("name", '=', name)
        else:
            filt = Filter("external_references.external_id", '=', ext_id)

        items = self.get_items([type_filter, filt])

        tech = {}

        if items is not None:
            mitre_tech_id = ""
            refs = []
            for r in items[0]["external_references"]:
                ref = {
                    "url": r.get("url", "")
                }
                if r.get("source_name", None) == "mitre-attack":
                    mitre_tech_id = r.get("external_id", "")

                refs.append(ref)
            tech = {
                "name": items[0].get("name", ""),
                "description": items[0].get("description", ""),
                "external_references": refs,
                "x_mitre_detection": items[0].get("x_mitre_detection", ""),
                "mitre_mitigation" : self.get_tech_mitigation(tech_id=mitre_tech_id),
                "mitre_tech_id": mitre_tech_id
            }

        return tech

    def get_items(self, filters, collection_title="Enterprise ATT&CK"):
        """
        Get items using filters
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param filters: list of filter
        :return:
        """
        if self.attack_server is None:
            self.connect_server()

        collection = self.collection_dict[collection_title]
        tc_source = TAXIICollectionSource(collection)

        items = tc_source.query(filters)

        return items

    def get_all_techniques(self):
        """
        Get all techs
        :return:
        """
        return self.get_items([Filter("type", '=', "attack-pattern")])

    def get_tactic_techniques(self, tactic_name=None, tactic_id=None):
        """
        Get all the techniques for a give tactic
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md

        :param tactic_name: tactic name
        :param tactic_id:   tactic ID
        :return:            techs
        """

        if self.attack_server is None:
            self.connect_server()
        #
        # STIX type for technique is attack-pattern
        #
        tech_filter = Filter("type", "=", "attack-pattern")
        #
        # Find name if id is given
        #
        if tactic_name is None:
            if tactic_id is not None:
                tactic_name = MitreAttackTactic.get_name(tactic_id)

        #
        #   Not found in MITRE document. We actually need to use lower case for the tactic
        #   name, and also replace space with -.
        #
        t_name = tactic_name.replace(' ', '-')
        t_name = t_name.lower()
        tactic_filter = Filter("kill_chain_phases.phase_name", "=", t_name)
        #
        #   Only look for Enterprise ATT&CK at this point
        #
        collection_title = "Enterprise ATT&CK"
        collection = self.collection_dict[collection_title]
        tc_source = TAXIICollectionSource(collection)
        mitre_techs = tc_source.query([tech_filter,
                                      tactic_filter])

        #
        # The returned AttackPattern is not serializable. Pick the fields we want
        #
        techs = []
        for mitre_tech in mitre_techs:
            refs = []
            mitre_tech_id = ""
            for r in mitre_tech["external_references"]:
                ref = {
                    "url": r.get("url", "")
                }
                if r.get("source_name", None) == "mitre-attack":
                    mitre_tech_id = r.get("external_id", "")

                refs.append(ref)
            tech = {
                "name":                 mitre_tech.get("name", ""),
                "description":          mitre_tech.get("description", ""),
                "external_references":  refs,
                "x_mitre_detection":    mitre_tech.get("x_mitre_detection", ""),
                "mitre_tech_id":        mitre_tech_id
            }
            techs.append(tech)

        return techs

    def get_external_id(self, mitre_tech):
        """
        Figure out the MITRE ATT&CK tech id, which is not in the
        STIX struture
        :param mitre_tech:
        :return:
        """
        mitre_tech_id = None
        for r in mitre_tech["external_references"]:
            if r.get("source_name", None) == "mitre-attack":
                mitre_tech_id = r.get("external_id", "")
                break
        return mitre_tech_id

    def get_tech_mitigation(self, tech_id=None, tech_name=None):
        """
        Get mitigation for a given tech
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param tech_id: STIX id for mitre tech
        :return:
        """

        # Connect first if not already
        if self.attack_server is None:
            self.connect_server()
        collection_title = "Enterprise ATT&CK"
        collection = self.collection_dict[collection_title]
        tc_source = TAXIICollectionSource(collection)

        # Need to get the obj first and then the STIX id
        tech_filter = None
        if tech_id is not None:
            tech_filter = Filter("external_references.external_id", '=', tech_id)
        elif tech_name is not None:
            tech_filter = Filter("name", '=', tech_name)

        filt = [
            Filter("type", '=', "attack-pattern"),
            tech_filter
        ]
        tech = tc_source.query(filt)

        relations = tc_source.relationships(tech[0].id, "mitigates", target_only=True)

        filters = [
            Filter("type", '=', "course-of-action"),
            Filter("id", "in", [r.source_ref for r in relations])
        ]

        ret = tc_source.query(filters)

        return ret[0].get("description", "")
