from ToolCommand import ToolCommand
import sys
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)
import json

HELP_STR = """
	Usage:\n
	\t offense_analysis.py -i app_id -o offense_id -r True_or_False
	"""
arg_str = "hi:o:r:"
arg_list = ["help", "app_id", "offense_id", "restart_if_exist"]


class SampleCmd(ToolCommand):

    def do_command(self):
        client = QRadarAdvisorClient(qradar_host=self.system_host,
                                     qradar_token=self.system_token,
                                     advisor_app_id=self.opts_dict["app_id"],
                                     cafile=False,
                                     log=logging)
        offense_id = self.opts_dict["offense_id"]
        restart_if_existed = self.opts_dict.get("restart_if_exist", "False") == "True"

        stix_json = client.offense_analysis(offense_id=offense_id,
                                            restart_if_existed=restart_if_existed)

        print(json.dumps(stix_json))

if __name__ == "__main__":
	sample_cmd = SampleCmd(HELP_STR)
	sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)

