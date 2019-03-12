system_host_env = "QRADAR_HOST"
system_user_env = "QRADAR_USER"
system_password_env = "QRADAR_PASSWORD"
system_token_env = "QRADAR_TOKEN"
system_verify_env = "QRADAR_VERIFY"

import os
import argparse
try:
    # For all python < 3.2
    import backports.configparser as configparser
except ImportError:
    import configparser


class ToolCommand(object):
    help_string_base = "Use environment variables {}/{}/{} to "
    help_string = None
    system_host = None
    system_user = None
    system_password = None
    system_token = None
    system_verify = False

    def __init__(self, help_string):
        import os
        if system_host_env in os.environ:
            self.system_host = os.environ[system_host_env]
        else:
            print("Environment variable " + system_host_env + " is missing.")

        if system_user_env in os.environ:
            self.system_user = os.environ[system_user_env]
        else:
            print("Environment variable " + system_user_env + " is missing")

        if system_password_env in os.environ:
            self.system_password = os.environ[system_password_env]
        elif system_token_env in os.environ:
            self.system_token = os.environ[system_token_env]
        else:
            print("Environment variable " + system_password_env + " is missing")

        if system_verify_env in os.environ and os.environ[system_verify_env] == "True":
            self.system_verify = True

        self.help_string = help_string

        self.opts_dict = {}
        self.config = {}

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



