# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
from stix2 import TAXIICollectionSource, Filter, CompositeDataSource
from stix2.datastore.taxii import DataSourceError
from taxii2client import Server
import re

MITRE_TAXII_URL = "https://cti-taxii.mitre.org/taxii/"
MITRE_BASE_URL = "https://attack.mitre.org"
CODE_TAG = "tt"  # Some descriptions contain <code> html tag, which we update for platform's rich text


def sanitize_stix(text):
    """
    Applies all the sanitizations that so far came up:
    - Replaces <code> tags with <tt>
    - Creates HTML links from Markdown
    :param text:
    :return:
    """
    return replace_code_tags(replace_markdown_links(text))


def replace_markdown_links(text):
    """
    STIX descriptions/mitigations contain links in a Markdown format, which isn't supported on Resilient Side.
    We will take those, and convert them to HTML links
    :param text: text from stix
    :return: text with Markdown links converted to HTML links
    """
    return re.sub("\[(.*?)\]\((.*?)\)", r'<a href="\g<2>">\g<1></a>', text)


def replace_code_tags(text):
    """
    STIX description/mitigation, might contain HTML tag <code> to highlight the code, which doesn't work
    with out rich text, so we update it to something we support.
    :param text: text from stix
    :type text: str
    :return: text with unsupported tags replaced with supported
    """
    return re.sub("<(/*)code>", r"<\1{}>".format(CODE_TAG), text)


class MitreAttackBase(object):
    """
    Base class for creation of other MitreAttack types.
    To use, subclass and override MITRE_TYPE, and all other needed methods.
    """
    MITRE_TYPE = "replace"
    _cached_obj = None
    SECONDS_IN_A_DAY = 84600

    def __init__(self, doc):
        self._stix = doc
        self.collection = self.get_collection(doc)
        self.name = self.get_name(doc)
        self.id = self.get_id(doc)
        self.deprecated = self.get_deprecation(doc)
        self.description = doc.get("description", "")

        if self.deprecated:
            self.description = "Deprecated. " + self.description

    def dict_form(self):
        """
        Method to override to convert the data into what is expected.
        :return: dictionary with object's data
        """
        return {
            "name": self.name,
            "id": self.id
        }

    @staticmethod
    def object_to_dict(obj):
        """
        Takes STIX object's every value and copies it to a dictionary.
        We do so, because certain STIX objects are immutable.
        :param obj: STIX object
        :return: dict
        """
        res = {}
        for key in obj.keys():
            res[key] = obj[key]
        return res

    @staticmethod
    def get_deprecation(doc):
        return doc.get("x_mitre_deprecated", False)

    @staticmethod
    def get_collection(doc):
        """
        Gets collection that was added by lookup method.
        Override for classes with other definition.
        :param data: stix structured dictionary
        :type data: dict
        :return: collection where the object was found
        :rtype: str
        """
        return doc.get("collection", "")

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
        if not ext:
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
        all_items = [cls(x) for x in conn.get_items(type_filter)]  # create a list of class instances from query data
        return all_items

    @classmethod
    def get(cls, conn, name=None, id=None):
        """
        Queries and returns a list of instances that fit the given criteria.
        If id is given it will be prioritized, since id is unique to all collections, but the
        name doesn't have to be.
        :type conn: MitreAttackConnection
        :param name: name to query for
        :param id: id to query for
        :return: list of objects of the class requested
        """
        ext_id = id
        if name is None and ext_id is None:
            return None

        if ext_id is not None:
            objs = cls.get_by_id(conn, ext_id)
        else:
            objs = cls.get_by_name(conn, name)

        if objs is None:
            return None

        if not isinstance(objs, list):
            objs = [objs]
        return objs

    @classmethod
    def get_by_name(cls, conn, name):
        """
        Queries the connection to get instances of this class with given name.
        Since multiple types of objects can have the same name across collections, returns a list of objects.
        :param conn: Connection object
        :type conn: MitreAttackConnection
        :param type_id: name of the type to query
        :type type_id: str
        :return: list of objects of the class with given name
        :rtype: list(self.__class__)
        """
        name = name.strip()

        type_filter = Filter("type", "=", cls.MITRE_TYPE)
        name_filter = Filter("name", "=", name)
        items = conn.get_items([type_filter, name_filter])
        if not len(items):
            return None

        return [cls(x) for x in items]  # create a list of class instances from query data

    @classmethod
    def get_by_id(cls, conn, type_id):
        """
        Queries the connection to get a list of instances of this class with given type.
        List should have a length of 1, since ids are unique, but for purposes of being not
        being different with `get_by_name` returns a list.
        :param conn: Connection object
        :type conn: MitreAttackConnection
        :param type_id: id of the type to query
        :type type_id: str
        :return: list of instances of the class for given id
        :rtype: list(self.__class__)
        """
        type_id = type_id.strip()

        type_filter = Filter("type", "=", cls.MITRE_TYPE)
        id_filter = Filter("external_references.external_id", "=", type_id)
        items = conn.get_items([type_filter, id_filter])
        if not len(items):
            return None

        return [cls(item) for item in items]  # create a list of class instances from query data


class MitreAttackTactic(MitreAttackBase):
    MITRE_TYPE = "x-mitre-tactic"
    MITRE_URL_TYPE = "tactics"

    def get_url(self):
        """
        Get the url link for the current class.
        :return: url string
        :rtype: str
        """
        item_id = self.id
        url = "{}/{}/{}".format(MITRE_BASE_URL, self.MITRE_URL_TYPE, item_id)
        return url

    def get_techniques(self, conn):
        return MitreAttackTechnique.get_by_tactic(conn, self)

    def dict_form(self):
        return {
            "name": self.name,
            "id": self.id,
            "ref": self.get_url(),
            "collection": self.collection
        }


class MitreAttackTechnique(MitreAttackBase):
    MITRE_TYPE = "attack-pattern"

    def get_mitigations(self, conn):
        return MitreAttackMitigation.get_by_technique(conn, self)

    @classmethod
    def get_by_tactic(cls, conn, tactic):
        """
        Creates a filter for techniques related to the given tactic.
        :param conn: connection object for making requests
        :type conn: MitreAttackConnection
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

    def dict_form(self):
        refs = [{"url": r.get("url", "")} for r in self._stix["external_references"]]
        return {
            "name": self.name,
            "description": sanitize_stix(self.description),
            "external_references": refs,
            "x_mitre_detection": sanitize_stix(self._stix.get("x_mitre_detection", "")),
            "id": self.id,
            "collection": self.collection
        }


class MitreAttackMitigation(MitreAttackBase):
    MITRE_TYPE = "course-of-action"

    @classmethod
    def get_by_technique(cls, conn, technique):
        """
        Gets mitigations that mitigates provided technique
        :param conn: connection object for making requests
        :type conn: MitreAttackConnection
        :param technique: technique to mitigate
        :type technique: MitreAttackTechnique
        :return: List of mitigations for the given technique
        :rtype: list(MitreAttackMitigation)
        """
        if technique is None:
            return None
        res = [cls(x) for x in conn.get_related_to(technique._stix, "mitigates", target_only=True)]
        for mitigation in res:
            mitigation.collection = technique.collection
        return res

    def dict_form(self):
        return {
            "description": sanitize_stix(self.description),
            "name": self.name,
            "id": self.id,
            "collection": self.collection
        }


class MitreAttackGroup(MitreAttackBase):
    MITRE_TYPE = "intrusion-set"
    MITRE_URL_TYPE = "groups"

    def __init__(self, doc):
        super(MitreAttackGroup, self).__init__(doc)
        self.aliases = self.get_aliases(doc)
        self.technique_id = None

    def get_url(self):
        """
        Get the url link for the current class.
        :return: url string
        :rtype: str
        """
        item_id = self.id
        url = "{}/{}/{}".format(MITRE_BASE_URL, self.MITRE_URL_TYPE, item_id)
        return url

    @staticmethod
    def get_aliases(doc):
        return doc.get("aliases", [])

    @classmethod
    def get_by_technique(cls, conn, technique):
        """
        Get all the groups related to the given technique.
        :param conn: Mitre Connection
        :param technique: Technique which we need the software for
        :return: list of Group instances
        :rtype: list(MitreAttackGroup)
        """
        if technique is None:
            return None

        groups = conn.get_related_to(technique._stix, "uses", target_only=True)
        groups = filter(lambda x: x["type"] == cls.MITRE_TYPE, groups)
        groups = [cls(x) for x in groups]

        for group in groups:
            group.technique_id = technique.id

        return groups

    @classmethod
    def get_by_technique_intersection(cls, conn, techniques):
        """
        Given a list of techniques, find which groups use all of them.
        :param conn: :param conn: connection object for making requests
        :type conn: MitreAttackConnection
        :param techniques: techniques to intersect
        :type techniques: list(MitreAttackTechnique)
        :return:
        """
        if not techniques:
            return None
        # get groups that each techniques is associated with
        groups_per_technique = [cls.get_by_technique(conn, technique) for technique in techniques]

        # get a list of ids of groups using all the techniques
        intersection = cls.get_intersection_of_groups(groups_per_technique)
        groups = [x for x in groups_per_technique[0] if x.id in intersection]

        return groups

    @staticmethod
    def get_intersection_of_groups(groups_per_technique):
        """
        Given a list of groups using a technique per each technique, find which groups are in all of those lists,
        i.e. which groups use all of the given techniques.
        :param groups_per_technique: list of (list of groups) per technique
        :type groups_per_technique: list(list(MitreAttackGroup))
        :return: list of IDs of groups using all of the techniques
        :rtype: list(str)
        """
        # if there are groups using all the techniques, they all will also use the first technique
        intersection = set([x.id for x in groups_per_technique[0]])
        for group in groups_per_technique:
            intersection = intersection & set([x.id for x in group])  # intersection is an associative operation
        return intersection

    def dict_form(self):
        return {
            "technique": self.technique_id,
            "name": self.name,
            "id": self.id,
            "ref": self.get_url(),
            "description": sanitize_stix(self.description),
            "aliases": self.aliases
        }


class MitreAttackSoftware(MitreAttackBase):
    MITRE_TYPE = ["tool", "malware"]
    MITRE_URL_TYPE = "software"

    def __init__(self, doc):
        super(MitreAttackSoftware, self).__init__(doc)
        self.type = self.get_type(doc)
        self.platforms = self.get_platforms(doc)
        self.technique_id = None

    def get_url(self):
        """
        Get the url link for the current class.
        :return: url string
        :rtype: str
        """
        item_id = self.id
        url = "{}/{}/{}".format(MITRE_BASE_URL, self.MITRE_URL_TYPE, item_id)
        return url

    def get_platforms(selfs, doc):
        """
        Gets the software platforms from STIX document
        :param doc: Stix document
        :return: List of platforms that the software functions on
        :rtype: list
        """
        return doc.get("x_mitre_platforms", [])

    def get_type(self, doc):
        """
        Gets the type of the software.
        :param doc: Stix document
        :return: "malware" or "tool"
        """
        return doc.get("type", "")

    @classmethod
    def get_by_technique(cls, conn, technique):
        """
        Get all the software related to the given technique.
        :param conn: Mitre Connection
        :param technique: Technique which we need the software for
        :return: list of Software instances
        :rtype: list(MitreAttackSoftware)
        """
        if technique is None:
            return None

        soft = conn.get_related_to(technique._stix, "uses", target_only=True)  # get stix objects
        soft = filter(lambda x: x["type"] in cls.MITRE_TYPE, soft)  # filter to keep only software types
        soft = [cls(x) for x in soft]  # initialize class instances

        for s in soft:
            s.technique_id = technique.id

        return soft

    def dict_form(self):
        return {
            "technique": self.technique_id,
            "name": self.name,
            "id": self.id,
            "ref": self.get_url(),
            "description": sanitize_stix(self.description),
            "platforms": self.platforms,
            "type": self.type
        }


class MitreAttackConnection(object):
    """
    Collection of methods for extracting data from MitreServer.
    Includes the logic of using multiple data sources.
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
        server_url = MITRE_TAXII_URL if url is None else url
        self.attack_server = Server(server_url)
        api_root = self.attack_server.api_roots[0]
        # CompositeSource to query all the collections at once
        c_sources = [TAXIICollectionSource(collection) for collection in api_root.collections]
        self.composite_ds = CompositeDataSource()
        self.composite_ds.add_data_sources(c_sources)

    def get_items(self, filters):
        """
        Get items using filters, convert them to dictionaries.
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param filters: list of filter
        :return: list of dictionaries representing stix objects
        :rtype: list(dict)
        """
        if self.attack_server is None:
            self.connect_server()
        items = []
        for data_source in self.composite_ds.get_all_data_sources():
            try:
                ds_items = data_source.query(filters)
                updated_items = [MitreAttackBase.object_to_dict(x) for x in ds_items]
                for item in updated_items:
                    item["collection"] = data_source.collection.title
                items.extend(updated_items)
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
        Look up items using item name
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

        return items


class MitreAttack(object):
    """
    Facet class for accessing data from Mitre Attack
    """
    def __init__(self):
        self.conn = MitreAttackConnection()

    def get_technique(self, name=None, ext_id=None):
        """
        Use tech name or external id to retrieve a technique.
        :param name: name of the technique to look up
        :param ext_id: if of the technique to look up
        :return: List of dictionaries representing techniques that fit the query
        """
        if name is None and ext_id is None:
            return None
        tech = None
        if name is not None:
            tech = MitreAttackTechnique.get_by_name(self.conn, name)
        else:
            tech = MitreAttackTechnique.get_by_id(self.conn, ext_id)

        if tech is None:
            return None

        if not isinstance(tech, list):
            tech = [tech]
        return [repr(x) for x in tech]

    def get_all_tactics(self):
        """
        Get all tactics from all the collections
        :return:
        """
        return MitreAttackTactic.get_all(self.conn)

    def get_all_techniques(self):
        """
        Get all techniques from all the tactics from all the collections.
        :return:
        """
        return MitreAttackTechnique.get_all(self.conn)

    def get_tactic_url(self, name):
        tactic = MitreAttackTactic.get_by_name(self.conn, name)
        if tactic is None:
            return None
        return tactic.get_url()

    def get_tactic_techniques(self, tactic_name=None, tactic_id=None):
        """
        Returns a list of tactic's techniques. If multiple tactics have the same name
        the list will include techniques for each.
        :param tactic_name:
        :param tactic_id:
        :return:
        """
        if not tactic_name and not tactic_id:
            return None
        if tactic_id:
            tactic = MitreAttackTactic.get_by_id(self.conn, tactic_id)
        elif tactic_name:
            tactic = MitreAttackTactic.get_by_name(self.conn, tactic_name)
            if isinstance(tactic, list):
                res = []
                for t in tactic:
                    res.extend(self.get_tactic_techniques(tactic_id=t.id))
                return res

        if not tactic:
            return None
        return [repr(tech) for tech in MitreAttackTechnique.get_by_tactic(self.conn, tactic)]

    def get_technique_mitigations(self, tech_id=None, tech_name=None):
        """
        Returns a list of mitigations. If multiple techniques
        have the same name, combines the lists into 1.
        Reference:
        https://github.com/mitre/cti/blob/master/USAGE.md
        :param tech_id: STIX id for mitre tech
        :return:
        """
        tech = None
        if tech_id is not None:
            tech = MitreAttackTechnique.get_by_id(self.conn, tech_id)
        elif tech_name is not None:
            tech = MitreAttackTechnique.get_by_name(self.conn, tech_name)
            if isinstance(tech, list):
                res = []
                for t in tech:
                    res.extend(self.get_technique_mitigations(tech_id = t.id))
                return res

        if not tech:
            return None

        mitigations = MitreAttackMitigation.get_by_technique(self.conn, tech)
        if not len(mitigations):
            return None

        return mitigations
