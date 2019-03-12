#!/usr/bin/env python

"""
Simple script to create a new incident.
"""
from __future__ import print_function
import time
import logging
import resilient
import configparser
from fn_risk_fabric.util.risk_fabric import get_action_plans, set_action_plan_comment


logging.basicConfig()


class ExampleArgumentParser(resilient.ArgumentParser):
    """Arguments for this command-line application, extending the standard Resilient arguments"""

    def __init__(self, config_file=None):
        super(ExampleArgumentParser, self).__init__(config_file=config_file)

        self.add_argument('--itype', '-t',
                          action='append',
                          help="The incident type(s).  Multiple arguments may be supplied.")

        self.add_argument('--queue', '-q',
                          required=True,
                          help="The action plan queue.")


def main():
    """
    program main
    """

    config_file = resilient.get_config_file()
    parser = ExampleArgumentParser(config_file)
    opts = parser.parse_args()

    inc_types = opts["itype"]
    inc_queue = opts["queue"]

    # Create SimpleClient for a REST connection to the Resilient services
    client = resilient.get_client(opts)

    # Discovered Date will be set to the current time
    time_now = int(time.time() * 1000)

    try:
        uri = '/incidents'

        rf_config = configparser.ConfigParser()
        rf_config.read(config_file)
        rf_opts = dict(rf_config.items('fn_risk_fabric'))
        result = get_action_plans(rf_opts)

        for ap in result:

            if 'AssignToQueueName' in ap and ap['AssignToQueueName'] == inc_queue:

                # Construct the basic incident DTO that will be posted
                description = ap['Notes'] if 'Notes' in ap else ""
                ActionPlanGUID = ap['ActionPlanGUID']
                properties = {
                    "rf_actionplanguid": ActionPlanGUID
                }
                new_incident = {"name": ap['Title'],
                        "description": description,
                        "incident_type_ids": inc_types,
                        "properties": properties,
                        "discovered_date": time_now}

                # Create the incident
                incident = client.post(uri, new_incident)
                inc_id = incident["id"]

                params = {
                    'ActionPlanGUID': ActionPlanGUID,
                    'Comment': "Created Resilient Incident ID #" + str(inc_id)
                }
                result = set_action_plan_comment(rf_opts, params)

                print("Created incident {}".format(inc_id))


    except resilient.SimpleHTTPException as ecode:
        print("create failed : {}".format(ecode))

if __name__ == "__main__":
    main()
