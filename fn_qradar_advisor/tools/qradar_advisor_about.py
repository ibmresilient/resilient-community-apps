from ToolCommand import ToolCommand
import sys
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient
import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

HELP_STR = """
	Usage:\n
	\t qradar_advisor_about.py -i app_id
	"""
arg_str = "hi:"
arg_list = ["help", "app_id"]


class SampleCmd(ToolCommand):

	def do_command(self):
		client = QRadarAdvisorClient(qradar_host=self.system_host,
									 qradar_token=self.system_token,
									 advisor_app_id=self.opts_dict["app_id"],
									 cafile=False,
									 log=logging)
		client.get_csrf_token()

		print("The XSRF_TOKEN is {}".format(client.http_info.xsrf_token))

if __name__ == "__main__":
	sample_cmd = SampleCmd(HELP_STR)
	sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)