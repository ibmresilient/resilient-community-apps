# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from fn_qradar_advisor.lib.qradar_cfma_client import QRadarCfmaClient
import sys
from ToolCommand import ToolCommand
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

HELP_STR = """
	Usage:\n
	\t get_all_mappings.py -i app_id
	"""
arg_str = "hi:"
arg_list = ["help", "app_id"]


class SampleCmd(ToolCommand):
    def do_command(self):
        client = QRadarCfmaClient(qradar_host=self.system_host,
                                     cfma_token=self.system_token,
                                     cfma_app_id=1051,
                                     cafile=False,
                                     log=logging)
        mappings = client.get_all_mapping()

        print("All mappings: {}".format(mappings))



if __name__ == "__main__":
    sample_cmd = SampleCmd(HELP_STR)
    sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)