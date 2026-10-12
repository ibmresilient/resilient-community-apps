#!/usr/bin/python
#
# Command line tool for adding a new threat intel item
#
# Use
#   python qradar_client -h
# to see usage
#

import sys, getopt
sys.path.append("../fn_qradar_integration/util")
from qradar_utils import QRadarClient as QRadarClient
from ToolCommand import ToolCommand

HELP_STRING = \
            "Usage:\n" \
            "\tpython qradar_client.py\n" \
            "\t-v [Show versions]\n"

arg_str = "hv"
arg_list =["help", "version"]

class VersionCmd(ToolCommand):
    def do_command(self):
        qradar_client = QRadarClient(host=self.system_host,
                                     username=self.system_user,
                                     password=self.system_password,
                                     token=None,
                                     cafile=self.system_verify)

        resp = qradar_client.get_versions()

        print(resp.text)

if __name__ == "__main__":
    ver_cmd = VersionCmd(HELP_STRING)
    ver_cmd.run_command(sys.argv[1:], arg_str, arg_list)



