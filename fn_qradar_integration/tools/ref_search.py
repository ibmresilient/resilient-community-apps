#!/usr/bin/python
#
# Command line tool for adding a new threat intel item
#
# Use
#   python ref_search -h
# to see usage
#

import sys, getopt
sys.path.append("../fn_qradar_integration/util")
from qradar_utils import QRadarClient as QRadarClient
from ToolCommand import ToolCommand

HELP_STRING = \
            "Usage:\n" \
            "\tpython ref_search.py\n" \
            "\t-r <Reference set name\n" \
            "\t-f <Filter>"

arg_str = "hr:f:"
arg_list = ["help", "reference", "filter"]

class SearchCmd(ToolCommand):
    def do_command(self):
        qradar_client = QRadarClient(host=self.system_host,
                                     username=self.system_user,
                                     password=self.system_password,
                                     token=None,
                                     cafile=self.system_verify)

        resp = qradar_client.search_ref_set(self.opts_dict["reference"],
                                            self.opts_dict["filter"])

        print(resp.text)

if __name__ == "__main__":
    search_cmd = SearchCmd(HELP_STRING)
    search_cmd.run_command(sys.argv[1:], arg_str, arg_list)