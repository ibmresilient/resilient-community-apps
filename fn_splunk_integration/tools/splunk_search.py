#!/usr/bin/python

#
# Command line tool to perform a splunk search using SplunkClient from fn_splunk_integration
#
#
# Usage as debug tool:
#   * From the log file, extract the splunk query. Look for line like this
#        2018-03-07 13:55:49,855 INFO [splunk_search] Splunk query to be executed: search index = _internal source=*splunkd* AND clientip=127.0.0.1
#   * Save the query string (in this example "search index = _internal source=*splunkd* AND clientip=127.0.0.1") into a file
#   * Run this file. Example:
#       sys_test_splunk_client.py -s your_splunk_hostname:port_number -u username -p password -f file_name_of_the_above_file
#   * Result will be print to the command line window. This is the result we return to Resilient
#
#
# Usage as system/compatibility tests:
#   * Install proper Splunk SDK for test
#   * Test different Splunk servers we need to verify
#

import sys, getopt
from fn_splunk_integration.util.splunk_utils import SplunkClient as SplunkClient


HELP_STRING = \
    "Usage: \n" \
    "\tpython splunk_search.py \n" \
    "\t-s <splunk server:port, OR use SPLUNK_HOST envvar> \n" \
    "\t-u <splunk user, OR use SPLUNK_USER envvar> \n" \
    "\t-p <splunk password, OR use SPLUNK_PASSWORD envvar> \n" \
    "\t-f <splunk query file>"

splunk_server = ""
splunk_user = ""
splunk_password=""
query_file = ""

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
        opts, args = getopt.getopt(argv, "hs:u:p:f:", ["help", "server=", "user=", "password=", "file="])
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
        elif opt in ("-f", "--file"):
            query_file = arg

    server_info= splunk_server.split(':')

    splunk_client = SplunkClient(host=server_info[0],
                                 port=int(server_info[1]),
                                 username=splunk_user,
                                 password=splunk_password)

    query_string = None

    try:
        with open(query_file, 'r') as fin:
            query_string = fin.read()
    except IOError:
        print("Error to read: %s. Please make sure it is created with the query to be executed." % query_file)
        sys.exit(1)

    try:
        result = splunk_client.execute_query(query_string)
    except Exception as e:
        print(str(e))
    print(str(result))

if __name__ == "__main__":
    main(sys.argv[1:])
