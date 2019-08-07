# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#

#
#   MitreAttack:
#   ------------
#

from stix2 import TAXIICollectionSource, Filter, CompositeDataSource
from taxii2client import Server

MITRE_URL = "https://cti-taxii.mitre.org/taxii/"

class MitreAttackBase(object):
    """
    Base class for creation of other MitreAttack types.
    To use, subclass and override MITRE_TYPE, and all other needed methods.
    """
    MITRE_TYPE = "replace"
    _cached_obj = {}

    def __init__(self, doc):
        self._stix = doc
        self.name = self.get_name(doc)
        self.id = self.get_id(doc)
        self.description = doc.get("description", "")
        if self.id is not None:
            self._cached_obj[self.id] = self
        if self.name is not None:
            self._cached_obj[self.name] = self

    @staticmethod
    def get_name(doc):
        """
        Gets name from STIX document for this particular class.
        Override for classes with other definition.
        :param doc: stix structured dictionary
        :type doc: dict
        :return: name of the object described by doc
        :rtype: str
        """
        return doc["name"]

    @staticmethod
    def get_id(doc):
        """
        Get id from STIX document for this particular class.
        Override for classes with other structure.
        :param doc: stix structured dictionary
        :type doc: dict
        :return: id of the object described by doc
        :rtype: str
        """
        ext = doc.get("external_references")
        if not ext or not len(ext):
            return None
        for i in ext:
            name = i.get("external_id")
            if name:
                return name
        return None

    @classmethod
    def get_all(cls, conn):
        """
        Query the connection for all the elements of the class's type.
        :return: list of class instances
        :rtype: list(self.__class__)
        """
        type_filter = Filter("type", "=", cls.MITRE_TYPE)
        return [cls(x) for x in conn.get_items(type_filter)]

    @classmethod
    def get_by_name(cls, conn, name):
        """
        Queries the connection to get an instance of this class with given name.
        :param conn: Connection object
        :type conn: MitreAttack
        :param type_id: name of the type to query
        :type type_id: str
        :return: instance of the class for given name
        :rtype: self.__class__
        """
        if name in cls._cached_obj:
            return cls._cached_obj[name]

        type_filter = Filter("type", "=", cls.MITRE_TYPE)
        name_filter = Filter("name", "=", name)
        items = conn.get_items([type_filter, name_filter])
        if not len(items):
            return None
        return cls(items[0])

    @classmethod
    def get_by_id(cls, conn, type_id):
        """
        Queries the connection to get an instance of this class with given type.
        :param conn: Connection object
        :type conn: MitreAttack
        :param type_id: id of the type to query
        :type type_id: str
        :return: instance of the class for given id
        :rtype: self.__class__
        """
        if type_id in cls._cached_obj:
            return cls._cached_obj[type_id]

        type_filter = Filter("type", "=", cls.MITRE_TYPE)
        id_filter = Filter("external_references.external_id", "=", type_id)
        items = conn.get_items([type_filter, id_filter])
        if not len(items):
            return None
        return cls(items[0])


class MitreAttackTactic(MitreAttackBase):
    MITRE_TYPE = "x-mitre-tactic"
    TACTIC_BASE_URL = "https://attack.mitre.org/tactics"

    def get_url(self):
        """
        Get the url link for the current class.
        :return: url string
        :rtype: str
        """
        item_id = self.id
        url = "{}/{}/".format(self.TACTIC_BASE_URL, item_id)
        return url

    def get_techniques(conn):
        return MitreAttackTechnique.get_by_tactic(conn, self)


class MitreAttackTechnique(MitreAttackBase):
    MITRE_TYPE = "attack-pattern"

    @classmethod
    def get_by_tactic(cls, conn, tactic):
        """
        Creates a filter for techniques related to the given tactic.
        :param conn: connection object for making requests
        :type conn: MitreAttack
        :param tactic: tactic which techniques interest us
        :type tactic: MitreAttachTactic
        :return: list of Technique instances related to tactic
        :rtype: list(MitreAttackTechnique)
        """
        kill_chain = tactic.name.replace(' ','-').lower()
        tact_filter = Filter("kill_chain_phases.phase_name", "=", kill_chain)
        tech_filter = Filter("type", "=", cls.MITRE_TYPE)
        techs = conn.get_items([tact_filter, tech_filter])
        if not techs:
            return None
        return [cls(x) for x in techs]

    def dict_repr(self):
        refs = [{"url": r.get("url", "")} for r in self._stix["external_references"]]
        return {
            "name": self.name,
            "description": self.description,
            "external_references": refs,
            "x_mitre_detection": self._stix.get("x_mitre_detection", ""),
            "mitre_tech_id": self.id
        }

class MitreAttack(object):
    """
    MitreAttack:
    -----------
    A facet class to encapsulate all the features related to fetching the
    MITRE STIX TAXII server
    """
    def __init__(self):
        self.attack_server = None
        self.composite_ds = None

    def connect_server(self, url=None):
        """
        Allow user to specify what url to use
        :param url:
        :return:
        """
        server_url = MITRE_URL if url is None else url
        self.attack_server = Server(server_url)
        api_root = self.attack_server.api_roots[0]
        # CompositeSource to query all the collections at once
        c_sources = [TAXIICollectionSource(collection) for collection in api_root.collections]
        self.composite_ds = CompositeDataSource()
        self.composite_ds.add_data_sources(c_sources)

    def lookup_item(self,
                    item_name,
                    type_name="attack-pattern"):
        """
        Look up an item using item name
        :param item_name:
        :param collection_title:
        :param type_name:
        :return:
        """
        query_filter = Filter("type", "=", type_name)
        name_filter = Filter("name", "=", item_name)
        items = self.get_items([query_filter, name_filter])

        if not len(items):
            return None

        return items[0]

    def get_technique(self, name=None, ext_id=None):
        """
        Use tech name or external id to retrieve tech
        :param name:
        :param ext_id:
        :return:
        """
        if name is None and ext_id is None:
            return None
        tech = None
        if name is not None:
            tech = MitreAttackTechnique.get_by_name(self, name)
        else:
            tech = MitreAttackTechnique.get_by_id(self, ext_id)

        return tech.dict_repr()

    def get_items(self, filters):
        """
        Get items using filters
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param filters: list of filter
        :return:
        """
        if self.attack_server is None:
            self.connect_server()
        items = self.composite_ds.query(filters)
        return items

    def get_all_tactics(self):
        return MitreAttackTactic.get_all(self)

    def get_all_techniques(self):
        """
        Get all techs
        :return:
        """
        return MitreAttackTechnique.get_all(self)

    def get_tactic_url(self, name):
        tactic = MitreAttackTactic.get_by_name(self, name)
        if tactic is None:
            return None
        return tactic.get_url()

    def get_tactic_techniques(self, tactic_name=None, tactic_id=None):
        if not tactic_name and not tactic_id:
            return None
        if tactic_name:
            tactic = MitreAttackTactic.get_by_name(self, tactic_name)
        elif tactic_id:
            tactic = MitreAttackTactic.get_by_id(self, tactic_id)
        if not tactic:
            return None
        return [tech.dict_repr() for tech in MitreAttackTechnique.get_by_tactic(self, tactic)]

    def get_tech_mitigation(self, tech_id=None, tech_name=None):
        """
        Get mitigation for a given tech
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param tech_id: STIX id for mitre tech
        :return:
        """
        tech = None
        if tech_id is not None:
            tech = MitreAttackTechnique.get_by_id(self, tech_id)
        elif tech_name is not None:
            tech = MitreAttackTechnique.get_by_name(self, tech_name)

        relations = self.composite_ds.relationships(tech._stix, "mitigates", target_only=True)

        filters = [
            Filter("type", '=', "course-of-action"),
            Filter("id", "in", [r.source_ref for r in relations])
            ]

        ret = self.get_items(filters)

        return ret[0].get("description", "")
