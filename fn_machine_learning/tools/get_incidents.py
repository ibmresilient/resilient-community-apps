from ToolCommand import ToolCommand
import sys
import fn_machine_learning.lib.resilient_utils as resilient_utils
import resilient.co3base as resilient

HELP_STR = """
python get_incidents -p PASSWORD"""

arg_str = "hp:"
arg_list = ["help", "password"]


class SampleCmd(ToolCommand):

	def do_command(self):
		url = "https://{}:443".format(self.system_host)

		args = {"base_url":url,
				"org_name": self.system_org,
				"verify": self.system_verify}

		res_client = resilient.BaseClient(**args)
		res_client.connect(self.system_user, self.opts_dict["password"])
		resilient_utils.get_incidents(res_client, "tool_incident.csv")

		print("Done")

if __name__ == "__main__":
	sample_cmd = SampleCmd(HELP_STR)
	sample_cmd.run_command(sys.argv[1:], arg_str, arg_list)
