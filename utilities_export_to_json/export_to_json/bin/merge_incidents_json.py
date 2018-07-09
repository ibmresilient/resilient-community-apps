#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import resilient
import json
import os


class ExportArgumentParser(resilient.ArgumentParser):
    def __init__(self, config_file=None):
        super(ExportArgumentParser, self).__init__(config_file=config_file)

        self.add_argument('first_json_file',
                          help="The first JSON filename.")

        self.add_argument('second_json_file',
                          help="The second JSON filename.")

        self.add_argument('output_json_file',
                          help="The output JSON filename.")


def get_json_from_file(filename):
    if os.path.isfile(filename):
        with open(filename, "r") as json_file:
            try:
                return json.load(json_file)
            except ValueError:
                raise Exception(("Parsing file {} for JSON failed.".format(filename)))
    else:
        raise Exception(("File {} not found.".format(filename)))

    return None


def main():
    parser = ExportArgumentParser(config_file=resilient.get_config_file())
    opts = parser.parse_args()

    first_json = get_json_from_file(opts.get("first_json_file"))
    second_json = get_json_from_file(opts.get("second_json_file"))

    if first_json is None or second_json is None:
        raise Exception("Invalid file provided.")

    if first_json.get("incidents") is None or second_json.get("incidents") is None:
        raise Exception("Invalid JSON provided, incidents object not found.")

    first_incidents = first_json.get("incidents")

    second_incidents_array = second_json.get("incidents")
    second_incidents = []

    for incident in second_incidents_array:
        incident_id = incident.get("id")
        if incident_id is not None:
            second_incidents.append(incident_id)

    incidents = []

    for incident in first_incidents:
        incident_id = incident.get("id")
        # if valid incident
        if incident_id is None:
            continue

        # if the incident already exists, we don't want to add it
        if incident_id not in second_incidents:
            incidents.append(incident)

    incidents += second_incidents_array

    with open(opts.get("output_json_file"), "w") as outfile:
        json.dump({"incidents": incidents}, outfile)
        outfile.write("\n")

    print("Successfully merged JSON files into {}.".format(opts.get("output_json_file")))


if __name__ == "__main__":
    main()
