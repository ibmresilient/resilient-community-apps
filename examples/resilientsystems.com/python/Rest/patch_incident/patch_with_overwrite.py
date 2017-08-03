#!/usr/bin/env python

"""
Simple script to patch an incident, sending only certain values (not the entire incident).
"""
from __future__ import print_function
import co3 as resilient

class ExampleArgumentParser(resilient.ArgumentParser):
    def __init__(self, config_file=None):
        super(ExampleArgumentParser, self).__init__(config_file=config_file)
    
        self.add_argument('--incid', type=int, required=True, help="The incident ID to patch.")
        self.add_argument('--desc', required=True, help="The new description to set for the incident.")

def main():
    """
    program main
    """

    parser = ExampleArgumentParser(config_file=resilient.get_config_file())
    opts = parser.parse_args()

    # Create SimpleClient for a REST connection to the Resilient services
    client = resilient.get_client(opts)

    inc_id = opts["incid"]
    desc = opts["desc"]

    try:
        uri = '/incidents/{}'.format(inc_id)

        incident = client.get(uri)

        # Create a patch object.  You need to pass it the base object (the thing being patched).  This
        # object contains the old values, which are sent to the server.
        patch = resilient.Patch(incident)

        patch.add_value("description", desc)

        print('''
At this point, we have a copy of the specified incident.  If you want to trigger a conflict to see
what will happen, then you can do so now.

Press the Enter key to continue''')
        input()

        # Apply the patch and overwrite any conflicts.
        client.patch(uri, patch, overwrite_conflict=True)

        # Confirm that our change was applied.  This is not something that you'd typically need to do since the
        # patch applied successfully, but this illustrates that the change was applied for the purposes of this
        # example.
        assert desc == client.get(uri)["description"]

    except resilient.co3.SimpleHTTPException as ecode:
        print("patch failed : {}".format(ecode))

if __name__ == "__main__":
    main()

