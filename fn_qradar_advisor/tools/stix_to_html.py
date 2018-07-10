from fn_qradar_advisor.lib import stix_tree
import json
import logging
from ToolCommand import ToolCommand
import sys

logging.basicConfig(filename="testing.log", level=logging.DEBUG)
HELP_STR = """
    Usage:\n
    \tstix_to_html.py -i stix_file_name -o html_filename
    """
arg_str = "hi:o:"
arg_list = ["help", "input", "output"]


class SampleCmd(ToolCommand):
    def do_command(self):
        stix_filename = self.opts_dict["input"]
        html_filename = self.opts_dict["output"]

        with open(stix_filename, "r") as infile:
            stix_json = json.load(infile)

            html_string = stix_tree.get_html(stix_json, logging)

            with open(html_filename, "w") as outfile:
                outfile.write(html_string)

if __name__ == "__main__":
	sample_cmd = SampleCmd(HELP_STR)
	sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)