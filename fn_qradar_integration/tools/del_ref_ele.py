#!/usr/bin/python
#
# Command line tool for adding a new threat intel item
#
# Use
#   python del_ref_ele.py -h
# to see usage
#

import sys, getopt
sys.path.append("../fn_qradar_integration/util")
from qradar_utils import QRadarClient as QRadarClient
from ToolCommand import ToolCommand

HELP_STRING = \
            "Usage:\n" \
            "\tpython del_ref_ele.py\n" \
            "\t-r <Reference set name\n" \
            "\t-v <Value>\n"

arg_str = "hr:v:"
arg_list = ["help", "reference", "value"]

class DelRefEle(ToolCommand):
    def do_command(self):
        qradar_client = QRadarClient(host=self.system_host,
                                     username=self.system_user,
                                     password=self.system_password,
                                     token=None,
                                     cafile=self.system_verify)

        resp = qradar_client.delete_ref_element(self.opts_dict["reference"],
                                                self.opts_dict["value"])

        print(resp.text)

if __name__ == "__main__":
    delcmd = DelRefEle(HELP_STRING)
    delcmd.run_command(sys.argv[1:], arg_str, arg_list)