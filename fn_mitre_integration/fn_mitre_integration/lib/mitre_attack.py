# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
from stix2 import TAXIICollectionSource, Filter, CompositeDataSource
from stix2.datastore.taxii import DataSourceError
from taxii2client import Server
import time

MITRE_URL = "https://cti-taxii.mitre.org/taxii/"


class MitreAttackBase(object):
    """
    Base class for creation of other MitreAttack types.
    To use, subclass and override MITRE_TYPE, and all other needed methods.
    """
    MITRE_TYPE = "replace"
    _cached_obj = {"all": None, "id": {}, "name": {}, "last": time.time()}
    SECONDS_IN_A_DAY = 84600

    def __init__(self, doc):
        if time.time() - self._cached_obj["last"] > self.SECONDS_IN_A_DAY:
            self._reset_cache()

        self._stix = doc
        self.name = self.get_name(doc)
        self.id = self.get_id(doc)
        self.description = doc.get("description", "")

        if self.id is not None:
            self._cached_obj["id"][self.id] = self
        if self.name is not None:
            self._cached_obj["name"][self.name] = self

    @classmethod
    def _reset_cache(cls):
        cls._cached_obj = {"all": None, "id": {}, "name": {}, "last": time.time()}

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
        if cls._cached_obj["all"] is not None:
            return cls._cached_obj["all"]

        type_filter = Filter("type", "=", cls.MITRE_TYPE)
        all = [cls(x) for x in conn.get_items(type_filter)]
        cls._cached_obj["all"] = all
        return all

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
        if name in cls._cached_obj["name"]:
            return cls._cached_obj["name"][name]

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
        if type_id in cls._cached_obj["id"]:
            return cls._cached_obj["id"][type_id]

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
        if tactic is None:
            return None
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


class MitreAttackMitigation(MitreAttackBase):
    MITRE_TYPE = "course-of-action"

    @classmethod
    def get_by_technique(cls, conn, technique):
        """
        Gets mitigations that mitigates provided technique
        :param conn: connection object for making requests
        :type conn: MitreAttack
        :param technique: technique to mitigate
        :type technique: MitreAttackTechnique
        :return: List of mitigations for the given technique
        :rtype: list(MitreAttackMitigation)
        """
        if technique is None:
            return None
        return [cls(x) for x in conn.get_related_to(technique._stix, "mitigates", target_only=True)]


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

    def get_items(self, filters):
        """
        Get items using filters
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param filters: list of filter
        :return: list of objects
        :rtype: list(dict)
        """
        if self.attack_server is None:
            self.connect_server()
        items = []
        for data_source in self.composite_ds.get_all_data_sources():
            try:
                ds_items = data_source.query(filters)
                items.extend(ds_items)
            except DataSourceError as e:
                # happens if data_source finds no elements with given filter
                pass
        return items

    def get_related_to(self, *args, **kwargs):
        """
        Facade for `related_to` of composite data source. Needed to abstract out DataSource from
        classes using AttackMitre.
        :return: objects with the provided relationships
        """
        if self.attack_server is None:
            self.connect_server()
        return self.composite_ds.related_to(*args, **kwargs)

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

        if tech is not None:
            return tech.dict_repr()
        return None

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

    def get_technique_mitigation(self, tech_id=None, tech_name=None):
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

        if not tech:
            return None

        mitigations = MitreAttackMitigation.get_by_technique(self, tech)
        return mitigations[0].description
