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
                return json.loads(json_file.read().replace("\n", ""))
            except ValueError:
                return None

    return None


def main():
    parser = ExportArgumentParser(config_file=resilient.get_config_file())
    opts = parser.parse_args()

    first_json = get_json_from_file(opts.get("first_json_file"))
    second_json = get_json_from_file(opts.get("second_json_file"))

    if first_json is None or second_json is None:
        raise Exception("Invalid file provided.")

    if first_json.get("incidents") is None or second_json.get("incidents") is None:
        raise Exception("Invalid JSON provided.")

    first_incidents = first_json.get("incidents")
    second_incidents = second_json.get("incidents")

    incidents = second_incidents

    for incident in first_incidents:
        # if valid incident
        if incident.get("id") is None:
            continue

        found_incident = False
        for existing_incident in incidents:
            # if they're the same incident
            if incident.get("id") == existing_incident.get("id"):
                found_incident = True
                break

        # if the incident already exists, we don't want to add it
        if found_incident is True:
            continue

        incidents.append(incident)

    with open(opts.get("output_json_file"), "w") as outfile:
        json.dump({"incidents": incidents}, outfile)
        outfile.write("\n")

    print("Successfully merged JSON files.")


if __name__ == "__main__":
    main()
