#!/usr/bin/env python 

"""
Simple script to invite a user to the system
Takes 2 parameters on the command line
--email=<email address>
--role= <role>
where role is one of 
default, observer, administrator, master_administrator
"""

import sys
import getopt
from pprint import pprint
import co3 as resilient

# resilient configuration
CO3OPTS = {
    "userid":""  # resiilent user id
    "password":"" # Password for the resilient user
    "org_name":""  # Resilient organization
    "base_url":"https://"   # hostname of the resilient server
}

# template for the invite api 
invite = {
    "email": "", 
    "group_ids": None, 
    "roles": {
        "create_incs": True, 
        "observer": False, 
        "administrator": False, 
        "master_administrator": False
    }
}


def main():
    """
    program main
    """

    email = None
    role = None
    try:
        options, args = getopt.getopt(sys.argv[1:], "e:r:", ["email=", "role="])
    except  getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    for option, argument in options:
        if option in ("e", "--email"):
            email = argument
        if option in ("r", "--role"):
            role = argument

    if not email or not role or role not in ['observer', 'administrator', 'default', 'master_administrator']:
        print("Usage:{} [-e|--email=]<email> [-r|--role=]<default|observer|administrator|master_administrator").format(sys.argv[0])
        sys.exit(1)


    invite['email'] = email

    invite['roles']['observer'] = False
    invite['roles']['administrator'] = False
    invite['roles']['master_administrator'] = False

    if role != "default":
        invite['roles'][role] = True


    # Create SimpleClient and connect
    client = resilient.SimpleClient(org_name=CO3OPTS['org_name'], proxies=None, base_url=CO3OPTS['base_url'], verify=False)

    client.connect(CO3OPTS['userid'], CO3OPTS['password'])
    try:
        result = client.post('/invitations', invite)
        pprint(result,indent=5)
    except resilient.co3.SimpleHTTPException as ecode:
        print "invite failed : {}".format(ecode)

if __name__ == "__main__":
    main()
 
