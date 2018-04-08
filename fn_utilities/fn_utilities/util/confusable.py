#!/usr/bin/env python
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

""" Table of confusable characters """

import unicodedata
import sys
import json
import ast
import requests
import pkg_resources

if sys.version_info[0] >= 3:
    unichr = chr


class Confusable(object):

    """
    >>> u"Apple" == Confusable().skeleton(u"Apple")
    True

    >>> u"Apple" == Confusable().skeleton(u"\\uFF21pple") # fullwidth latin
    True

    >>> u"Apple" == Confusable().skeleton(u"\\u0391p\\u03C1le") # greek
    True

    >>> u"Apple" == Confusable().skeleton(u"\\u0410p\\u0440le") # cyrillic
    True

    """
    def __init__(self):
        self.lookup_file = pkg_resources.resource_filename("fn_utilities", "data/confusable.dat")
        self.lookup_table = None

    def _load(self):
        if self.lookup_table is None:
            # Load the lookup table
            with open(self.lookup_file, "r") as datafile:
                self.lookup_table = json.load(datafile)

    def skeleton(self, input):
        """Produce a 'skeleton' that can be tested for confusability"""
        # Take the input string and produce the 'skeleton'
        # per http://unicode.org/reports/tr39/#Confusable_Detection
        self._load()
        normal = unicodedata.normalize("NFD", input)
        flattened = u"".join(self.lookup(char) for char in normal)
        skeleton = unicodedata.normalize("NFD", flattened)
        return skeleton

    def lookup(self, char):
        """Lookup a single character for the skeleton"""
        try:
            return self.lookup_table[char]
        except KeyError:
            return char

    def build_lookup(self):
        """Build the lookup table from its source"""
        table = {}
        resp = requests.get("http://www.unicode.org/Public/security/latest/confusables.txt")
        resp.encoding = "utf-8-sig"
        data = resp.text
        for line in data.split("\n"):
            # Strip comments
            i = line.find('#')
            if i >= 0:
                line = line[:i]
            if line == "":
                continue

            # Split on semicolons
            char1, mapchars, _ = line.split(";")

            # These are hex values, convert to integers for easier lookup
            key = ast.literal_eval("u'\\u{}'".format(char1.strip()))
            literal = u"".join(["u'\\u{}'".format(mapchar.strip())
                                for mapchar in mapchars.strip().split(" ")])
            table[key] = ast.literal_eval(literal)

        # Write the lookup table to disk
        with open(self.lookup_file, "w") as datafile:
            json.dump(table, datafile)


if __name__ == "__main__":
    # Rebuild the lookup table from its source
    Confusable().build_lookup()
    # Run doctests
    import doctest
    doctest.testmod()
