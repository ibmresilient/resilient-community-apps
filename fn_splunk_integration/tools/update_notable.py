#!/usr/bin/python

#
# Command tool for updating notable event using SplunkUtils from fn_splunk_integration
#
# Use
#   python update_notable.py -h
# to see usage
#

import sys, getopt
from fn_splunk_integration.util.splunk_utils import SplunkUtils as SplunkUtils

HELP_STRING = \
            "Usage:\n" \
            "\tpython update_notable.py\n" \
            "\t-s <splunk server:port (optional), OR use SPLUNK_HOST envar> \n" \
            "\t-u <splunk user (optional), OR use SPLUNK_USER envar> \n" \
            "\t-p <splunk password (optional), OR use SPLUNK_PASSWORD envar> \n" \
            "\t-i <notable event ID> \n" \
            "\t-t <noteble event status: 2 for In Progress; 5 for Close>\n" \
            "\t-c <notable event comment>\n" \
            "\t-v <True or False for verifying certificate (optional). Default to False>"

splunk_server = ""
splunk_user = ""
splunk_password=""
notable_status = 0
notable_comment = ""
notable_id = ""
splunk_verify = False

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
    global splunk_user, splunk_server, splunk_password, splunk_verify
    try:
        opts, args = getopt.getopt(argv, "hs:u:p:i:t:c:v:",
                                   ["help", "server=", "user=", "password=", "id=", "status=", "comment=", "verify="])
    except getopt.GetoptError:
        print(HELP_STRING)
        sys.exit(2)

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
        elif opt in ("-i", "--id"):
            notable_id = arg
        elif opt in ("-t", "--status"):
            notable_status = int(arg)
        elif opt in ("-c", "--comment"):
            notable_comment = arg
        elif opt in ("-v", "--verify"):
            if arg == "True":
                splunk_verify = True

    server_info= splunk_server.split(':')

    result = ""
    try:
        splunk_utils = SplunkUtils(host=server_info[0],
                                   port=int(server_info[1]),
                                   username=splunk_user,
                                   password=splunk_password,
                                   verify=splunk_verify)

        result = splunk_utils.update_notable(event_id=notable_id,
                                             comment=notable_comment,
                                             status=notable_status,
                                             cafile=splunk_verify)
        print(str(result))

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main(sys.argv[1:])
