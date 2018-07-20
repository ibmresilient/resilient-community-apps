from ToolCommand import ToolCommand
import sys
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

HELP_STR = """
	Usage:\n
	\t quick_search.py -i app_id -s search_value
	"""
arg_str = "hi:s:"
arg_list = ["help", "app_id", "search"]


class SampleCmd(ToolCommand):

    def do_command(self):
        client = QRadarAdvisorClient(qradar_host=self.system_host,
                                     qradar_token=self.system_token,
                                     advisor_app_id=self.opts_dict["app_id"],
                                     cafile=False,
                                     log=logging)
        resp = client.quick_search(self.opts_dict["search"])
        print(str(resp))


if __name__ == "__main__":
	sample_cmd = SampleCmd(HELP_STR)
	sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)