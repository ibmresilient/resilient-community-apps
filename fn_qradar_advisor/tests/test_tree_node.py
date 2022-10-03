# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for tree_node.py
#
from fn_qradar_advisor.lib.tree_node import TreeNode
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

class TestTreeNode(object):

    def test_tree_node_copy(self):
        orig_node = TreeNode(obj_type="fake type",
                             obj_id="fake id",
                             name="fake name",
                             description="fake desc",
                             objects={"0":{"type":"fake obj type"}},
                             is_link=True,
                             log=None)

        copy_node = orig_node.copy()

        assert orig_node.type == copy_node.type
        assert orig_node.id == copy_node.id
        assert orig_node.name == copy_node.name
        assert orig_node.description == copy_node.description
        assert orig_node.objects == copy_node.objects

    def test_init_with_object(self):
        """

        :return:
        """
        objects={"0":{"type": "file"}}
        stix_obj = {
            "id": "stix id",
            "type": "domain-name",
            "name": "mydomain.com",
            "objects": objects
        }

        node = TreeNode().init_with_object(stix_obj)

        assert node.type == stix_obj["type"]
        assert node.name == stix_obj["name"]
        assert node.objects == objects
        assert node.is_link == False
        assert node.is_root == False

    def test_add_node(self):
        parent_node = TreeNode()
        parent_node.log = logging

        parent_node.add_child(None)

        assert len(parent_node.children) == 0