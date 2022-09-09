# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for html_gen_visitor.py
#
# html_gen_visitor is a visitor that generate a html representation of a stix tree.
#
#
from fn_qradar_advisor.lib.tree_node import TreeNode
from fn_qradar_advisor.lib.stix_tree import MultiRootTree
from fn_qradar_advisor.lib.html_gen_visitor import HtmlGenVisitor
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)


class TestHtmlGenVisitor(object):
    def test_no_value(self):
        #
        # This should not happen, but if a stix object has type, but not name,
        # we show a type icon with empty value
        #
        visitor = HtmlGenVisitor(log=logging)

        type = "file"
        root1 = TreeNode(obj_type="observed-data",
                         obj_id="",
                         objects={"0":
                             {
                                 "type": type,
                                 "value": ""
                             }
                         },
                         name="")
        tree = MultiRootTree(root1)

        tree.accept(visitor)

        assert type in visitor.html

    def test_no_image_found(self):
        """

        :return:
        """
        visitor = HtmlGenVisitor(log=logging)
        fake_name = "Fake name"
        fake_type = "fake_type"
        root1 = TreeNode(obj_type="observed-data",
                          obj_id="",
                          objects={"0":
                                  {
                                      "type":fake_type,
                                       "value":fake_name
                                  }
                          },
                          name=fake_name)
        tree = MultiRootTree(root1)

        tree.accept(visitor)

        #
        # Even if we can't find the image associate with it, we shall still show the
        # stix object
        #
        assert fake_name in visitor.html
        assert fake_type in visitor.html

    def test_empty_observed_data(self):
        visitor = HtmlGenVisitor(log=logging)
        fake_name = "Fake name"
        type = "observed-data"
        root1 = TreeNode(obj_type=type,
                         obj_id="",
                         objects={
                         },
                         name=fake_name)
        tree = MultiRootTree(root1)

        tree.accept(visitor)

        #
        # If the objects field of an observed-data is empyt, we show it as
        # type=observed-data, and value=name
        #
        assert fake_name in visitor.html
        assert type in visitor.html

    def test(self):
        """
        Use the following tree for test
        root1
            child1
                child2
                child3
                    child4
            child5
                child6
                child2(link)
        root2
            child7
        :return:
        """

        root1 = TreeNode(obj_type="indicator",
                         obj_id="",
                         name="root1")
        root2 = TreeNode(obj_type="identity",
                         obj_id="",
                         name="root2")
        #
        # 1. First build a tree
        #
        tree = MultiRootTree(root1)

        tree.add_root(root2)

        child1 = TreeNode(obj_type="malware",
                          obj_id="",
                          name="child1")

        root1.add_child(child1)

        child2 = TreeNode(obj_type="indicator",
                          obj_id="",
                          name="child2")

        child1.add_child(child2)

        child3 = TreeNode(obj_type="malware",
                          obj_id="",
                          name="child3")
        child1.add_child(child3)

        child4 = TreeNode(obj_type="observed-data",
                          obj_id="",
                          objects={"0":
                                  {
                                      "type":"file",
                                       "name":"child4"
                                  }
                          },
                          name="child4")
        child3.add_child(child4)

        child5 = TreeNode(obj_type="file",
                          obj_id="",
                          name="child5")

        root1.add_child(child5)

        child6 = TreeNode(obj_type="observed-data",
                          obj_id="",
                          objects={"0":
                                  {
                                      "type":"ipv4-addr",
                                       "value":"child6"
                                  }
                          },
                          name="child6")

        child5.add_child(child6)
        child2_link = TreeNode(obj_type="indicator",
                          obj_id="",
                          name="child2")
        child2_link.is_link = True
        child5.add_child(child2_link)

        child7 = TreeNode(obj_type="ipv4-addr",
                          obj_id="",
                          name="child7")
        root2.add_child(child7)

        #
        # Use a html_gen_visitor to parse the tree
        #
        visitor = HtmlGenVisitor(logging)

        tree.accept(visitor=visitor)

        #
        # Output the html file
        #
        with open("TestGenHtml.html", "w") as outfile:
            outfile.write(visitor.html)
            # Visually verify that the output html
            # shows a tree similar to the one above

        assert "root1" in visitor.html
        assert "root2" in visitor.html

        for x in range(1, 7, 1):
            # assert each child is there
            name = "child" + str(x)
            assert name in visitor.html
