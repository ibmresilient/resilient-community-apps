#!/usr/bin/env python

"""
Simple script to patch an incident where you want "smart" handling of patch conflicts.  This example will always
add the supplied incident types to an incident, even if there's a conflicting change on the server.
"""
from __future__ import print_function
import co3 as resilient
import json
from six.moves import input

class ExampleArgumentParser(resilient.ArgumentParser):
    def __init__(self, config_file=None):
        super(ExampleArgumentParser, self).__init__(config_file=config_file)
    
        self.add_argument('--incid',
                          type=int,
                          required=True,
                          help="The incident ID to patch.")

        self.add_argument('--itype',
                          required=True,
                          action='append',
                          help="The names of the incident types to add (you can supply multiple --itype arguments)")

def main():
    """
    program main
    """

    parser = ExampleArgumentParser(config_file=resilient.get_config_file())
    opts = parser.parse_args()

    inc_id = opts["incid"]
    itypes = opts["itype"]

    # Create SimpleClient for a REST connection to the Resilient services
    client = resilient.get_client(opts)

    try:
        uri = '/incidents/{}?handle_format=names'.format(inc_id)

        incident = client.get(uri)

        # Create a patch object.  You need to pass it the base object (the thing being patched).
        patch = resilient.Patch(incident)

        # The initial patch will contain the change we want to make.
        old_itypes = incident["incident_type_ids"]

        patch.add_value("incident_type_ids", old_itypes + itypes)

        def patch_conflict_handler(response, patch_status, patch):
            # If this gets called then there was a patch conflict, we we need to
            # adjust the patch to include an update.  This only gets called if
            # a field we're trying to change has failed.  In that case the actual
            # value currently on the server is included in the patch_status object.
            #
            # You can retrieve the current server value using
            # patch_status.get_actual_current_value(field_name).  This
            # will return the actual value that exists on the server.
            #
            # In our case, we'll be appending to this value.
            #
            print("patch conflict detected, operation returned:  ")
            print(json.dumps(patch_status.to_dict(), indent=4))

            current_value = patch_status.get_actual_current_value("incident_type_ids")

            patch.exchange_conflicting_value(patch_status,
                                             "incident_type_ids",
                                             current_value + itypes)

        print("existing itypes: {}".format(old_itypes))
        print("wanted to add these: {}".format(itypes))

        print('''
At this point, we have a copy of the specified incident.  If you want to trigger a conflict to see
what will happen, then you can do so now.

Press the Enter key to continue''')
        input()

        client.patch_with_callback(uri, patch, patch_conflict_handler)

        # Confirm that our change was applied.  This is not something that you'd typically need to do since the
        # patch applied successfully, but this illustrates that the change was applied for the purposes of this
        # example.
        #
        new_itypes = client.get(uri)["incident_type_ids"]

        # Remove the original description, which will leave only our addition.
        print("itypes after update: {}".format(new_itypes))

        assert set(itypes).issubset(new_itypes)

    except resilient.co3.SimpleHTTPException as ecode:
        print("patch failed : {}".format(ecode))

if __name__ == "__main__":
    main()

