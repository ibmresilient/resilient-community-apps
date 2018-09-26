# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for relation_visitor.py
#
from fn_qradar_advisor.lib.stix_tree import RelationVisitor
from fn_qradar_advisor.lib.tree_node import TreeNode
from fn_qradar_advisor.lib.stix_tree import MultiRootTree

import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)


class TestRelationVisitor(object):

    def test_link_node(self):
        """
        When visit a link node, the visitor.action should just return True to continue.
        No relation will be added to a link node. The relation will be added to the
        node it linked to.
        :return:
        """
        node = TreeNode()
        node.is_link = True

        v = RelationVisitor("", "", [], None, logging)

        assert v.action(node)

    def test_not_match(self):
        """
        If the node the visitor visits does not match either the source id or the destination
        id, it should just return True to continue
        :return:
        """
        node = TreeNode()
        node.id = "Node Id not match"

        v = RelationVisitor("source id", "dest id", [], None, logging)

        assert v.action(node)

    def test_match_source(self):
        """
        The node it visits match the source id
        :return:
        """
        #
        # A relation from relation_source_id to relation_dest_id
        #
        relation_source_id = "source object id"
        relation_dest_id = "dest object id"

        node = TreeNode()
        # The node match the source_id
        node.id = relation_source_id

        # This node is the root of the tree
        tree = MultiRootTree(node)

        # The dest node is in the objects list
        des_type = "file"
        des_name = "fake file name"
        des_node = {
            "id": relation_dest_id,
            "type": des_type,
            "name": des_name
        }
        stix_objects = []
        stix_objects.append(des_node)

        v = RelationVisitor(src_id=relation_source_id,
                            des_id=relation_dest_id,
                            stix_objects=stix_objects,
                            multi_root_tree=tree,
                            log=logging)

        ret = node.accept(v)

        #
        # A new tree node shall be created and added to the tree
        #
        assert len(node.children) == 1

        new_node = node.children[0]
        assert new_node.id == relation_dest_id
        assert new_node.type == des_type
        assert new_node.name == des_name
        assert not new_node.is_root
        assert not new_node.is_link
        # if we found, we shall stop
        assert not ret

    def test_match_destination(self):
        """
        The node it visits match the dest id
        :return:
        """
        #
        # A relation from relation_source_id to relation_dest_id
        #
        relation_source_id = "source object id"
        relation_dest_id = "dest object id"

        node = TreeNode()
        # The node to visit matches the dest id
        node.id = relation_dest_id

        # This node is the root of the tree
        tree = MultiRootTree(node)

        # The dest node is in the objects list
        src_type = "file"
        src_name = "fake file name"
        src_node = {
            "id": relation_source_id,
            "type": src_type,
            "name": src_name
        }
        stix_objects = []
        stix_objects.append(src_node)

        v = RelationVisitor(src_id=relation_source_id,
                            des_id=relation_dest_id,
                            stix_objects=stix_objects,
                            multi_root_tree=tree,
                            log=logging)

        ret = node.accept(v)

        #
        # A new tree node shall be inserted as the root
        #
        new_node = tree.roots[0]

        assert len(new_node.children) == 1

        assert new_node.id == relation_source_id
        assert new_node.type == src_type
        assert new_node.name == src_name
        assert new_node.is_root
        assert not new_node.is_link

        # the dest node is the child
        assert new_node.children[0] == node

        # if we found, we shall stop
        assert not ret

    def test_link_to_dest(self):
        #
        # A relation from relation_source_id to relation_dest_id
        #
        relation_source_id = "source object id"
        relation_dest_id = "dest object id"

        des_node = TreeNode()
        des_node.id = relation_dest_id
        src_node = TreeNode()
        src_node.id = relation_source_id

        # The tree has a parent node as the root and
        # and both source node and dest node are children of the parent node
        parent_node = TreeNode()
        tree = MultiRootTree(parent_node)
        parent_node.add_child(des_node)
        parent_node.add_child(src_node)



        v = RelationVisitor(src_id=relation_source_id,
                            des_id=relation_dest_id,
                            stix_objects=[],
                            multi_root_tree=tree,
                            log=logging)
        #
        # visit the des_node. Here both the src_node and the des_node
        # are already in the tree
        #
        ret = des_node.accept(v)

        #
        # A new link node will be added to the src node
        #
        assert len(src_node.children) == 1
        new_node = src_node.children[0]


        # This new node is a copy of the des node
        assert new_node.id == relation_dest_id
        assert new_node.type == des_node.type
        assert new_node.name == des_node.name
        assert not new_node.is_root
        assert new_node.is_link

        # if we found, we shall stop
        assert not ret

    def test_merge_source(self):
        """
        The node it visits match the dest id
        :return:
        """
        #
        # A relation from relation_source_id to relation_dest_id
        #
        relation_source_id = "source object id"
        relation_dest_id = "dest object id"

        source_node = TreeNode()
        source_node.id = relation_source_id

        des_node = TreeNode()
        des_node.id = relation_dest_id

        # This source node is the root of the tree
        tree = MultiRootTree(source_node)
        # The dest node is ANOTHER root of the tree
        tree.add_root(des_node)

        # a relation from the srouce node to the dest node
        v = RelationVisitor(src_id=relation_source_id,
                            des_id=relation_dest_id,
                            stix_objects=[],
                            multi_root_tree=tree,
                            log=logging)
        # visit the source node
        ret = source_node.accept(v)

        assert len(source_node.children) == 1

        # dest node shall be moved as a child of source node
        assert source_node.children[0] == des_node

        # The tree should have only one root now
        assert len(tree.roots) == 1

        # if we found, we shall stop
        assert not ret

    def test_source_link(self):
        #
        # A relation from relation_source_id to relation_dest_id
        #
        relation_source_id = "source object id"
        relation_dest_id = "dest object id"

        des_node = TreeNode()
        des_node.id = relation_dest_id
        src_node = TreeNode()
        src_node.id = relation_source_id

        # The tree has a parent node as the root and
        # and both source node and dest node are children of the parent node
        parent_node = TreeNode()
        tree = MultiRootTree(parent_node)
        parent_node.add_child(des_node)
        parent_node.add_child(src_node)

        v = RelationVisitor(src_id=relation_source_id,
                            des_id=relation_dest_id,
                            stix_objects=[],
                            multi_root_tree=tree,
                            log=logging)
        #
        # visit the src_node. Here both the src_node and the des_node
        # are already in the tree
        #
        ret = src_node.accept(v)

        #
        # A new link node will be added to the src node
        #
        assert len(src_node.children) == 1
        new_node = src_node.children[0]

        # This new node is a copy of the des node
        assert new_node.id == relation_dest_id
        assert new_node.type == des_node.type
        assert new_node.name == des_node.name
        assert not new_node.is_root
        assert new_node.is_link

        # if we found, we shall stop
        assert not ret