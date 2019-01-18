system_host_env = "MACHINE_LEARNING_HOST"
system_user_env = "MACHINE_LEARNING_USER"
system_org_env = "MACHINE_LEARNING_ORG"
system_verify_env = "MACHINE_LEARNING_VERIFY"
help_basic = "Use env vars MACHINE_LEARNING_HOST/MACHINE_LEARNING_TOKEN to specify login info"


class ToolCommand(object):

    help_string = None
    system_host = None
    system_verify = False

    def __init__(self, help_string, server_tool=True):
        import os
        if system_host_env in os.environ:
            self.system_host = os.environ[system_host_env]
        elif server_tool:
            print("Environment variable " + system_host_env + " is missing.")

        if system_user_env in os.environ:
            self.system_user = os.environ[system_user_env]
        elif server_tool:
            print("Environment variable " + system_user_env + " is missing")

        if system_org_env in os.environ:
            self.system_org = os.environ[system_org_env]
        elif server_tool:
            print("Environment variable " + system_org_env + " is missing")

        if system_verify_env in os.environ and os.environ[system_verify_env] == "True":
            self.system_verify = True

        self.help_string = help_basic + "\n" + help_string

        self.opts_dict = {}

    def run_command(self, argv, arg_str, arg_list):
        import sys, getopt

        try:
            opts, args = getopt.getopt(argv, arg_str, arg_list)
            arg_str_no_colon = arg_str.replace(':', '')
            for opt, arg in opts:
                if opt == "-h" or opt == "--help":
                    print(self.help_string)
                    sys.exit()
                else:
                    if len(opt) == 2 and opt[0] == '-':
                        index = arg_str_no_colon.find(opt[1])
                        name = arg_list[index]
                        self.opts_dict[name] = arg
                    elif opt[0] == '-' and opt[1] == '-':
                        name = opt[2:]
                        self.opts_dict[name] = arg

            self.do_command()
        except Exception as e:
            print(str(e))

    def do_command(self):
        """
        overide this to perform the command
        :return:
        """
        pass



