# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for visitors.py
#
from fn_qradar_advisor.lib.visitors import Visitor
from fn_qradar_advisor.lib.visitors import GetNodeVisitor
from fn_qradar_advisor.lib.tree_node import TreeNode

class TestVisitors(object):

    def test_base_visitor(self):
        """
        Verify that the default behavior
        :return:
        """
        class DefaultVisitor(Visitor):
            """
            Nothing has been overriden. Only default behavior
            """
            def __init__(self):
                super(DefaultVisitor, self).__init__()

        v = DefaultVisitor()

        should_continue = v.action(None)

        #
        # The default behavoir of action is returning not to continue
        #
        assert not should_continue

        try:
            # The default implementation of these two methods has no side effect.
            v.before_children(None)
            v.after_children(None)
            assert True
        except Exception as e:
            assert False

    def test_get_node_visitor_not_found(self):

        node_with_diff_id = TreeNode(obj_type=None,
                                     obj_id="fake id")

        #
        # this visitor looks for an object id different from the node
        #
        v = GetNodeVisitor("other obj id")

        ret = v.action(node_with_diff_id)

        #
        # if the id does not match, we shall continue
        #
        assert ret == True
        assert not v.node

    def test_get_node_visitor_found(self):
        obj_id = "object id to look for"
        node_with_same_id = TreeNode(obj_type=None,
                                     obj_id=obj_id)

        #
        # this visitor looks for an object id different from the node
        #
        v = GetNodeVisitor(obj_id)

        ret = v.action(node_with_same_id)

        #
        # if the id matches, we shall stop and store the node
        #
        assert ret == False
        assert v.node == node_with_same_id

    def test_get_node_visitor_break(self):
        """
        parent
            child1 (with match id)
            child2
        :return:
        """
        matched_obj_id = "matched obj id"
        parent = TreeNode(obj_type=None,
                          obj_id="fake id")
        child1 = TreeNode(obj_type=None,
                          obj_id=matched_obj_id)
        child2 = TreeNode(obj_type=None,
                          obj_id="fake id2")
        parent.add_child(child1)
        parent.add_child(child2)

        v = GetNodeVisitor(matched_obj_id)
        parent.accept(v)

        assert v.node == child1
