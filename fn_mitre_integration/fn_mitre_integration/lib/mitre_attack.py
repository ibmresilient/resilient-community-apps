# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

#
#   MitreAttack:
#   ------------
#

from stix2 import TAXIICollectionSource, Filter
from taxii2client import Server

MITRE_URL = "https://cti-taxii.mitre.org/taxii/"


class MitreAttackTactic(object):
    mitre_tactics = []

    @staticmethod
    def populate():
        """
        Populate a static list
        :return:
        """
        MitreAttackTactic.mitre_tactics = [
            MitreAttackTactic("Initial Access",
                              "TA0001",
                              """The initial access tactic represents the vectors 
                              adversaries use to gain an initial foothold within a network. """),
            MitreAttackTactic("Execution",
                              "TA0002",
                              """The execution tactic represents techniques that result in execution 
                              of adversary-controlled code on a local or remote system. This tactic 
                              is often used in conjunction with initial access as the means of executing 
                              code once access is obtained, and lateral movement to expand access to remote 
                              systems on a network. """),
            MitreAttackTactic("Persistence",
                              "TA0003",
                              """Persistence is any access, action, or configuration change to a system that 
                              gives an adversary a persistent presence on that system. Adversaries will often 
                              need to maintain access to systems through interruptions such as system restart
                              to restart or alternate backdoor for them to regain access. """),
            MitreAttackTactic("Privilege Escalation",
                              "TA0004"),
            MitreAttackTactic("Defense Evasion",
                              "TA0005"),
            MitreAttackTactic("Credential Access",
                              "TA0006"),
            MitreAttackTactic("Discovery",
                              "TA0007"),
            MitreAttackTactic("Lateral Movement",
                              "TA0008"),
            MitreAttackTactic("Collection",
                              "TA0009"),
            MitreAttackTactic("Exfiltration",
                              "TA0010"),
            MitreAttackTactic("Command and Control",
                              "TA0011")
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


    def __init__(self, name=None, id=None, description=""):
        """
        :param name:
        :param id:
        :param description:
        """
        self.name = name
        self.id = id
        self.description = description


class MitreAttack(object):
    """
    Facet design pattern.
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

        :param item_name:
        :param collection_title:
        :param type_name:
        :return:
        """
        ret_item = None
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

        :return:
        """
        return MitreAttackTactic.mitre_tactics

    @staticmethod
    def get_tactic_url(tactic_name):
        t_id = MitreAttackTactic.get_id(tactic_name)
        if t_id is None:
            return None

        BASE_URL = "https://attack.mitre.org/tactics"
        url = "{}/{}/".format(BASE_URL, t_id)

        return url

    def get_tactic_techniques(self, tactic_name):
        """
        https://github.com/mitre/cti/blob/master/USAGE.md

        :param tactic_name:
        :return:
        """

        if self.attack_server is None:
            self.connect_server()
        #
        # STIX type for technique is attack-pattern
        #
        tech_filter = Filter("type", "=", "attack-pattern")
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
        # The AttackPattern is not serializable. Pick the fields we want
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
                "name":                 mitre_tech["name"],
                "description":          mitre_tech["description"],
                "external_references":  refs,
                "x_mitre_detection":    mitre_tech["x_mitre_detection"],
                "mitre_tech_id":        mitre_tech_id
            }
            techs.append(tech)

        return techs

    def get_tech_mitigation(self, tech_id):
        """
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
        filt = [
            Filter("type", '=', "attack-pattern"),
            Filter("external_references.external_id", '=', tech_id)
        ]
        tech = tc_source.query(filt)


        relations = tc_source.relationships(tech[0].id, "mitigates", target_only=True)

        filters = [
            Filter("type", '=', "course-of-action"),
            Filter("id", "in", [r.source_ref for r in relations])
        ]

        ret = tc_source.query(filters)

        return ret[0].get("description", "")
