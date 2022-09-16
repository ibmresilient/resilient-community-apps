# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for relation_visitor.py
#
import sys
import copy
import json
from fn_qradar_advisor.lib.tree_node import TreeNode
from fn_qradar_advisor.lib import stix_tree
from fn_qradar_advisor.lib.visitors import GetNodeVisitor
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

def verify_tree(stix_objects, trees):
    """
    Verify a tree against the stix objects we got from a stix file.
    :param stix_objects: stix objects from stix file
    :param trees: trees built from the stix_objects
    :return: error message. Empty if there is no error
    """
    object_count = 0
    relationship_count = 0
    error_msg = ""
    for obj in stix_objects:
        visitor = GetNodeVisitor(obj["id"])
        trees.accept(visitor)
        if not visitor.node:
            if obj["type"] == "relationship":
                # This is fine. Relationship is not shown as list item
                relationship_count = relationship_count + 1
            else:
                # This is an object in the objects list, but not in the trees we built
                error_msg = error_msg + "\nObject {} is not found in the tree".format(obj["id"])
        else:
            object_count = object_count + 1

    print("There are {} objects and {} relationships".format(str(object_count), str(relationship_count)))

    return error_msg

class TestStixTree(object):

    def test_relation_tree(self):
        with open(sys.path[0] + "/relation_sample.stix", "r") as infile:
            stix_sample = json.load(infile)

        dict_copy = copy.deepcopy(stix_sample)

        tree = stix_tree.build_tree(stix_objects=dict_copy["objects"],
                                    log=logging)

        dict_copy2 = copy.deepcopy(stix_sample)
        ret = verify_tree(stix_objects=dict_copy2["objects"],
                                    trees=tree)
        #
        # verify that there is no error message
        #
        assert ret == ""

        html = stix_tree.get_html(stix_sample, logging)

        with open(sys.path[0] + "/relation_sample.html", "w") as outfile:
            outfile.write(html)

    def test_sighting_tree(self):
        """
        This is a sub tree of a sample stix from QRadar Advisor
        :return:
        """
        stix_sample = {}

        with open(sys.path[0] + "/sample1.stix", "r") as infile:
            stix_sample = json.load(infile)

        dict_copy = copy.deepcopy(stix_sample)

        tree = stix_tree.build_tree(stix_objects=dict_copy["objects"],
                                    log=logging)

        dict_copy2 = copy.deepcopy(stix_sample)
        ret = verify_tree(stix_objects=dict_copy2["objects"],
                                    trees=tree)
        #
        # verify that there is no error message
        #
        assert ret == ""

        html = stix_tree.get_html(stix_sample, logging)

        with open(sys.path[0] + "/sample1.html", "w") as outfile:
            outfile.write(html)

        print("Done")

    def test_empty_tree(self):
        obj = {"type": "relationship"}

        # Only relationship in the objects list, can't build tree
        ret = stix_tree.build_tree([obj], logging)

        assert not ret

    def test_extract_failure(self):
        """
        Try to extract non-existing node
        :return:
        """
        root = TreeNode()
        root.id = "root id"
        tree = stix_tree.MultiRootTree(root)

        obj = {
            "id": "Other obj id"
        }
        stix_objects = [obj]

        existing, node = stix_tree.extract_object(stix_objects, tree, "id not exist", logging)

        assert not existing
        assert not node

    def test_get_sight_ref_created_by_failed(self):
        # obj has no "sighting_of_ref
        # then get_sight_ref_created_by will fail
        obj = {
            "id": "obj id",
        }
        obj1 = {
            "id": "obj1"
        }
        stix_objects = [obj1]

        ret = stix_tree.get_sight_ref_created_by(stix_objects, obj, logging)
        assert not ret

