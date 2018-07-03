# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from visitors import Visitor
import resources


class HtmlGenVisitor(Visitor):
    """
    A visitor to generate a html list item for each node
    """

    def __init__(self, log):
        self.obj_count = 0
        self.link_count = 0
        self.html = ""
        self.log = log

    def action(self, node):
        if node.is_link:
            self.link_count = self.link_count + 1
        else:
            self.obj_count = self.obj_count + 1
        link = '<img src="{}" alt="link" style="width:15px; height:15px"/>'.format(resources.image_dict["link"]) if node.is_link else ""

        image = node.type
        value = node.name
        if node.type != "observed-data":
            if node.type in resources.image_dict:
                image = '<img src="{}" alt="{}" style="width:20px; height:20px"/>'.format(resources.image_dict[node.type], node.type)
        else:
            # an observable data. The objects is more interesting
            image = '<img src="{}" alt="{}" style="width:20px; height:20px"/>'.format(resources.image_dict[node.type], node.type)
            if len(node.objects) > 0:
                obj = node.objects["0"]
                type = obj.get("type", "observable-data")
                if type in resources.image_dict:
                    # object like ipv4 can have its own icon
                    image = '<img src="{}" alt="{}" style="width:20px; height:20px"/>'.format(resources.image_dict[type], type)
                else:
                    self.log.error("Unable to find image for type {}".format(type))
                    image = "[{}]".format(type)
                if type == "file":
                    value = obj.get("name", str(obj.get("hashes", "")))
                else:
                    value = obj.get("value", "")
            else:
                self.log.error("No objects found in observed-data: {}".format(str(node)))

            if value == "":
                self.log.error("No value found in node: {}".format(str(node)))

        self.html = self.html + "<li>" + image + " " + str(value) + link + "</li>"
        return True

    def before_children(self, node):
        self.html = self.html + '<ul style="list-style-type:none">'

    def after_children(self, node):
        self.html = self.html + "</ul>"
