# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import stix_utils


class TreeNode(object):

    def __init__(self, obj_type="", obj_id="", name="", description="", objects={}, is_link=False, log=None):
        self.type = obj_type
        self.id = obj_id
        self.name = name
        self.description = description
        self.is_link = is_link
        self.is_root = False
        self.children = []
        self.objects = dict(objects)
        self.log = log

        super(TreeNode, self).__init__()

    def accept(self, visitor):
        """

        :param visitor:
        :return:
        """
        # Take action on self node first
        should_continue = visitor.action(self)

        # If should_continue, then go to children one by one
        if should_continue:
            if len(self.children) > 0:
                visitor.before_children(self)
                for child in self.children:
                    if should_continue:
                        should_continue = child.accept(visitor)
                    else:
                        break
                visitor.after_children(self)
        return should_continue

    def add_child(self, node):
        """
        Add a child to the child tree
        :param node:
        :return:
        """
        if node:
            self.children.append(node)
        else:
            self.log.error("Adding a None child")

    def copy(self):
        """
        Return a copy of itself
        :return:
        """
        node = TreeNode(obj_type=self.type,
                        obj_id=self.id,
                        name=self.name,
                        description=self.description,
                        objects=self.objects)
        return node

    def init_with_object(self, stix_obj, log=None):
        """
        Init a tree node with a stix obj
        :param stix_obj:
        :return:
        """
        if log:
            self.log = log
        self.id = stix_obj["id"]
        self.name = stix_utils.get_observable_description(stix_obj, self.log)
        self.type = stix_utils.get_obserable_type(stix_obj, self.log)
        self.description = stix_obj.get("description", "")
        self.objects = stix_obj.get("objects", {})
        self.is_root = False
        self.is_link = False
        return self
