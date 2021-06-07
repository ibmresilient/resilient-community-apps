#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Command line tool for adding a new threat intel item
#
# Use
#   python ariel_search -h
# to see usage
#

import sys, getopt
sys.path.append("../fn_qradar_integration/util")
from qradar_utils import QRadarClient as QRadarClient
from ToolCommand import ToolCommand

HELP_STRING = \
            "Usage:\n" \
            "\tpython ariel_search.py\n" \
            "\t-f <file for query string, to get search_id>\n"

arg_str ="hf:"
arg_list = ["help", "file"]

class ArialSearch(ToolCommand):
    def do_command(self):
        qradar_client = QRadarClient(host=self.system_host,
                                     username=self.system_user,
                                     password=self.system_password,
                                     token=None,
                                     cafile=self.system_verify)

        with open(self.opts_dict["file"], "r") as infile:
            query_string = infile.read()
        print(query_string)

        resp = qradar_client.ariel_search(query_string)


        print resp.text

if __name__ == "__main__":
    arial_search = ArialSearch(HELP_STRING)
    arial_search.run_command(sys.argv[1:], arg_str, arg_list)