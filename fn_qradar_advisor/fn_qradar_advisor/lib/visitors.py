# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.


class Visitor(object):
    # Visitor design pattern
    def __init__(self):
        self.changed = False

    def action(self, node):
        """
        override this one to perform an action on the input node
        :param node:
        :return:
        """
        return False

    def before_children(self, node):
        """
        override this if something needs to be done before
        traverse the children
        :param node:
        :return:
        """
        pass

    def after_children(self, node):
        """
        override this if something needs to be done after finishing
        traversing the children
        :param node:
        :return:
        """
        pass


class GetNodeVisitor(Visitor):
    """
    A visitor to look for a node with the given object id
    """
    def __init__(self, obj_id):
        self.obj_id = obj_id
        self.node = None

    def action(self, node):
        should_continue = True
        if node.id == self.obj_id:
            self.node = node
            should_continue = False

        return should_continue


