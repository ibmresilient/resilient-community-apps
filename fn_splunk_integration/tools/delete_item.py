#!/usr/bin/python
#
# Command line tool for deleting a threat intel item
#
# Use
#   python delete_item.py -h
# to see usage
#

import sys, getopt
from fn_splunk_integration.util.splunk_utils import SplunkUtils as SplunkUtils
import json

HELP_STRING = \
            "Usage:\n" \
            "\tpython delete_item.py\n" \
            "\t-s <splunk server:port, OR use SPLUNK_HOST env> \n" \
            "\t-u <splunk user, OR use SPLUNK_USER env> \n" \
            "\t-p <splunk password, OR use SPLUNK_PASSWORD env> \n" \
            "\t-t <type of intel: ip_intel, user_intel....>\n" \
            "\t-k <item key> \n" \
            "\t-v <Optional: True or False for verifying certificate. Default to False>"
splunk_server = ""
splunk_user = ""
splunk_password = ""
item_type = ""
item_key = ""
splunk_verify = True

def read_env():
    import os
    global splunk_user, splunk_server, splunk_password
    if "SPLUNK_HOST" in os.environ:
        splunk_server = os.environ["SPLUNK_HOST"]

    if "SPLUNK_USER" in os.environ:
        splunk_user = os.environ["SPLUNK_USER"]

    if "SPLUNK_PASSWORD" in os.environ:
        splunk_password = os.environ["SPLUNK_PASSWORD"]

def main(argv):
    global splunk_user, splunk_server, splunk_password
    try:
        opts, args = getopt.getopt(argv, "hs:u:p:t:k:v:",
                                   ["help", "server=", "user=", "password=", "type=", "key=", "verify="])
    except getopt.GetoptError:
        print(HELP_STRING)
        sys.exit(2)

    splunk_verify = False
    read_env()
    for opt, arg in opts:
        if opt == "-h":
            print(HELP_STRING)
            sys.exit()
        elif opt in ("-s", "--server"):
            splunk_server = arg
        elif opt in ("-u", "--user"):
            splunk_user = arg
        elif opt in ("-p", "--password"):
            splunk_password = arg
        elif opt in ("-t", "--type"):
            item_type = arg
        elif opt in ("-k", "--item_key"):
            item_key = arg
        elif opt in ("-v", "--verify"):
            if arg == "True":
                splunk_verify = True

    server_info= splunk_server.split(':')
    print("Using: " + splunk_server + ", user: " + splunk_user)
    result = ""
    try:
        splunk_utils = SplunkUtils(host=server_info[0],
                                   port=int(server_info[1]),
                                   username=splunk_user,
                                   password=splunk_password,
                                   verify=splunk_verify)

        result = splunk_utils.delete_threat_intel_item(item_type, item_key, splunk_verify)
        print(str(result))

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main(sys.argv[1:])
