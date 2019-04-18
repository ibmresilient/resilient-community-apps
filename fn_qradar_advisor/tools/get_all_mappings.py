# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from fn_qradar_advisor.lib.qradar_cafm_client import QRadarCafmClient
import sys
from ToolCommand import ToolCommand
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

"""
    Debugging tool. Used to extract all the mappings of QRadar rules to
    MITRE ATT&CK tactic.
    
    Usage:
        get_all_mappings.py -i <CAFM app id>
    or:
        get_all_mappings.py -i <CAFM app id> -r <rule name>
"""

HELP_STR = """
	Usage:\n
	\t get_all_mappings.py -i app_id -r <optional rule name>
	"""
arg_str = "hi:r:"
arg_list = ["help", "app_id", "rule"]


class SampleCmd(ToolCommand):
    def do_command(self):
        client = QRadarCafmClient(qradar_host=self.system_host,
                                     cafm_token=self.system_token,
                                     cafm_app_id=self.opts_dict["app_id"],
                                     cafile=False,
                                     log=logging)
        mappings = client.get_all_mapping()

        print("All mappings: {}".format(mappings))

        rule_name = self.opts_dict.get("rule", None)

        if rule_name is not None:
            tactic = client.find_tactic_mapping(rule_name)
            print("Tactic found: {}".format(tactic))


if __name__ == "__main__":
    sample_cmd = SampleCmd(HELP_STR)
    sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)