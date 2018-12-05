# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from visitors import Visitor
from visitors import GetNodeVisitor
import stix_tree


class RelationVisitor(Visitor):
    #
    # A RelationVisitor is built on a stix relationship. It will create the destination(or source) node
    # when it visits a node that match the source ( or destination) id of the corresponding
    # relation
    #
    def __init__(self, src_id, des_id, stix_objects, multi_root_tree, log):
        self.source_id = src_id
        self.target_id = des_id
        self.objects = stix_objects
        self.multi_root_tree = multi_root_tree
        self.changed = False
        self.log = log

    def action(self, node):
        """

        :param node:
        :return:
        """
        if node.is_link:
            #
            # This node is a link, so it is linked to a "real" node somewhere
            # The relation will ba applied to "real" node, not here. Return
            # True to continue
            #
            return True

        should_continue = False

        # this node matches the source_id
        if node.id == self.source_id:
            #
            # find the target_id from list or the existing tree
            # add target_id here as child
            #
            existing, target_node = stix_tree.extract_object(stix_objects=self.objects,
                                                              multi_root_tree=self.multi_root_tree,
                                                              object_id=self.target_id,
                                                              log=self.log)
            if existing:
                should_merge = False
                if target_node.is_root:
                    # the target node is a root
                    check_visitor = GetNodeVisitor(self.source_id)
                    target_node.accept(check_visitor)
                    if not check_visitor.node:
                        should_merge = True

                if should_merge:
                    target_node.is_root = False
                    node.add_child(target_node)
                    self.multi_root_tree.remove_root(target_node)
                else:
                    # A node in the tree is pointing to another node in the tree
                    link_node = target_node.copy()
                    link_node.is_link = True
                    node.add_child(link_node)
            else:
                node.add_child(target_node)
            self.changed = True
        elif node.id == self.target_id:
            #
            # find the target_id from the list or the existing tree
            # target_id node become a new root
            #
            existing, source_node = stix_tree.extract_object(stix_objects=self.objects,
                                                              multi_root_tree=self.multi_root_tree,
                                                              object_id=self.source_id,
                                                              log=self.log)
            #
            # if node is a root node and if node is in different tree of source_node,
            # we can merge two branches
            #
            should_merge = False
            if node.is_root:
                check_visitor = GetNodeVisitor(self.source_id)
                node.accept(check_visitor)
                if not check_visitor.node:
                    should_merge = True
            if should_merge:
                source_node.add_child(node)
                node.is_root = False
                self.multi_root_tree.remove_root(node)
            else:
                # add a link
                target_node = node.copy()
                target_node.is_link = True
                source_node.add_child(target_node)

            if not existing:
                # Source node is a new node not in the tree
                self.multi_root_tree.add_root(source_node)

            self.changed = True
        else:
            # This relation has nothing to do with this node
            should_continue = True

        return should_continue
