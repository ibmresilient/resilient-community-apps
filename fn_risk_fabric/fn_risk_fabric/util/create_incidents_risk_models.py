#!/usr/bin/env python

"""
Simple script to create a new incident.
"""
from __future__ import print_function
import time
import logging
import resilient
import ConfigParser
from fn_risk_fabric.util.risk_fabric import get_risk_model_instances


logging.basicConfig()


class ExampleArgumentParser(resilient.ArgumentParser):
    """Arguments for this command-line application, extending the standard Resilient arguments"""

    def __init__(self, config_file=None):
        super(ExampleArgumentParser, self).__init__(config_file=config_file)

        self.add_argument('--itype', '-t',
                          action='append',
                          help="The incident type(s).  Multiple arguments may be supplied.")

        self.add_argument('--limit', '-l',
                          required=True,
                          help="Limit imported risk model instances.")


def main():
    """
    program main
    """

    config_file = resilient.get_config_file()
    parser = ExampleArgumentParser(config_file)
    opts = parser.parse_args()

    inc_types = opts["itype"]
    inc_limit = opts["limit"]

    # Create SimpleClient for a REST connection to the Resilient services
    client = resilient.get_client(opts)

    # Discovered Date will be set to the current time
    time_now = int(time.time() * 1000)

    try:
        uri = '/incidents'

        rf_config = ConfigParser.ConfigParser()
        rf_config.read(config_file)
        rf_opts = dict(rf_config.items('fn_risk_fabric'))
        params = {
            'Limit': inc_limit
        }
        result = get_risk_model_instances(rf_opts, params)

        for ap in result['Records']:

            # Construct the basic incident DTO that will be posted
            inc_name = ap['RiskModelName']
            inc_description = ap['Threats'] + ', ' + ap['FocusEntityCaption'] + ', #' + str(ap['ID'])
            new_incident = {"name": inc_name,
                    "description": inc_description,
                    "incident_type_ids": inc_types,
                    "discovered_date": time_now}

            # Create the incident
            incident = client.post(uri, new_incident)
            inc_id = incident["id"]

            print("Created incident {}".format(inc_id))


    except resilient.SimpleHTTPException as ecode:
        print("create failed : {}".format(ecode))

if __name__ == "__main__":
    main()
