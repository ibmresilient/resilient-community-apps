# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from visitors import GetNodeVisitor
from html_gen_visitor import HtmlGenVisitor
from tree_node import TreeNode
from relation_visitor import RelationVisitor
import stix_utils


class MultiRootTree(object):

    def __init__(self, node):
        self.roots = []
        self.add_root(node)

    def accept(self, visitor):
        """
        Accept a visitor
        :param visitor:
        :return:
        """
        for root in self.roots:
            should_continue = root.accept(visitor)
            if not should_continue:
                break

    def add_root(self, node):
        """
        # Add the input node to the root list
        :param node:
        :return:
        """
        node.is_root = True
        self.roots.append(node)

    def remove_root(self, node):
        """
        Remove a root from the root list
        :param node:
        :return:
        """
        self.roots.remove(node)


def build_tree(stix_objects, log):
    tree = None
    #
    # Find the first SDO to init a tree
    #
    for obj in stix_objects:
        if obj["type"] != "relationship" and obj["type"] != "sighting":
            tree = MultiRootTree(TreeNode().init_with_object(obj))
            break
    if tree is None:
        print("Failed to start up a tree")

    while handle_relations(stix_objects, tree, log):
        pass

    handle_sightings(stix_objects, tree, log)

    return tree


def handle_relations(stix_objects, tree, log):
    found_relationship = False
    for obj in stix_objects:
        if obj["type"] == "relationship":
            found_relationship = True
            visitor = RelationVisitor(src_id=obj["source_ref"],
                                      des_id=obj["target_ref"],
                                      stix_objects=stix_objects,
                                      multi_root_tree=tree,
                                      log=log)

            tree.accept(visitor)
            if visitor.changed:
                # relationship used. Remove it
                stix_objects.remove(obj)

    return found_relationship


def handle_sightings(stix_objects, tree, log):
    for obj in stix_objects:
        if obj["type"] == "sighting":
            #
            # add a sighting node to the root
            #
            node = TreeNode(obj_type=obj["type"],
                            obj_id=obj["id"],
                            name=obj["id"],  # sighting has no name, stix2 sample uses id instead
                            description="",
                            objects=obj.get("objects", []),
                            is_link=False)
            tree.add_root(node)

            sight_ref_created_by = None
            try:
                sighting_of_ref = stix_utils.find_object_by_id(stix_objects, obj["sighting_of_ref"])
                sight_ref_created_by = sighting_of_ref["created_by_ref"]
            except Exception as e:
                sight_ref_created_by = None

            sight_of_visitor = RelationVisitor(src_id=obj["id"],
                                               des_id=obj["sighting_of_ref"],
                                               stix_objects=stix_objects,
                                               multi_root_tree=tree,
                                               log=log)
            tree.accept(sight_of_visitor)
            if sight_of_visitor.changed:
                #
                # indicator created by
                #
                if sight_ref_created_by:
                    ref_created_by_visitor = RelationVisitor(src_id=obj["sighting_of_ref"],
                                                             des_id=sight_ref_created_by,
                                                             stix_objects=stix_objects,
                                                             multi_root_tree=tree,
                                                             log=log)
                    tree.accept(ref_created_by_visitor)
                #
                # Saw relation
                #
                for sighted_ref in obj["where_sighted_refs"]:
                    saw_visitor = RelationVisitor(src_id=sighted_ref,
                                                  des_id=obj["id"],
                                                  stix_objects=stix_objects,
                                                  multi_root_tree=tree,
                                                  log=log)
                    tree.accept(saw_visitor)
                #
                # Sighting object created by
                #
                created_by_visitor = RelationVisitor(src_id=obj["id"],
                                                     des_id=obj["created_by_ref"],
                                                     stix_objects=stix_objects,
                                                     multi_root_tree=tree,
                                                     log=log)
                tree.accept(created_by_visitor)


def extract_object(stix_objects, multi_root_tree, object_id, log):
    node = None
    existing_node = False

    #
    # try the multi_root_tree first
    #
    visitor = GetNodeVisitor(object_id)
    multi_root_tree.accept(visitor)

    if visitor.node:
        node = visitor.node
        # A node already exists in the tree
        existing_node = True
    else:
        # Now look for it from the stix objects
        for obj in stix_objects:
            if obj["id"] == object_id:
                node = TreeNode().init_with_object(obj, log)
                stix_objects.remove(obj)
                break

        if not node:
            log.error("{} can not be found in objects or the tree".format(object_id))

    return existing_node, node


def get_html(stix, log):
    """
    Generate a html string for a stix bundle. Use a structure similar to a
    folder tree to represent the stix bundle.
    :param stix:
    :param log:
    :return:
    """
    # Use the json dict directly
    objects = stix["objects"]
    stix_tree = build_tree(objects, log)
    html = ""
    trees = stix_tree.roots
    for subtree in trees:
        html = html + "<ul>"
        html_visitor = HtmlGenVisitor(log)
        subtree.accept(html_visitor)
        html = html + html_visitor.html + "</ul>"

    html = html + "<p>There are {} objects and {} links</p>".format(str(html_visitor.obj_count), str(html_visitor.link_count))

    return html

