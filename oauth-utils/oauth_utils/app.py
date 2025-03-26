# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""App builder for oauth-utils package"""
import argparse
import logging
from click import Abort
from oauth_utils.bin.oauth2_generate_refresh_token import main as oauth2_generate_refresh_token

# Setup logging
LOGGER_NAME = "oauth_utils"
FORMATTER_CLASS = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=35, width=80)
LOG = logging.getLogger(LOGGER_NAME)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def get_parent_parser():
    """
    Create the parent parser for oauth-utils.

    :return : Parent Parser
    """

    parser = argparse.ArgumentParser(prog='oauth-utils', formatter_class=FORMATTER_CLASS,
                                 description='Tools to manage OAuth for IBM SOAR apps',
                                     epilog="For support, please visit ibm.biz/soarcommunity")

    parser.usage = """
    $ oauth-utils <subcommand> ...
    $ oauth-utils -v <subcommand> ...
    $ oauth-utils oauth2_generate_refresh_token
    $ oauth-utils oauth2_generate_refresh_token -b
    $ oauth-utils oauth2_generate_refresh_token -c <path_to_config_file>/app.config -a <app_name>
    $ oauth-utils -h
    """

    # Add --verbose argument
    parser.add_argument("-v", "--verbose",
                        help="Set the log level to DEBUG",
                        action="store_true")

    return parser

def get_sub_parser(parent_parser):
    """
    Create a sub_parser to parent_parser.
    Returns the sub_parser

    :param parent_parser: Parent parser to add the sub_parser to
    :return: Sub Parser
    """
    # Define sub_parser object, its dest is cmd
    sub_parser = parent_parser.add_subparsers(
        title="subcommands",
        description="One of these subcommands must be provided",
        dest="cmd"
    )

    return sub_parser

def main():

    parent_parser = get_parent_parser()
    subparsers = get_sub_parser(parent_parser)

    parser_oauth2_gen_refresh_token = subparsers.add_parser(
        'oauth2_generate_refresh_token', description="A utility to generate a refresh token for an OAuth 2.0 service"
                                                     " (to be used with an IBM SOAR app).\nThe parameters used for "
                                                     "the OAuth 2.0 service can be taken either from an app.config file or "
                                                     "manually from the command line.\n(For further information please "
                                                     "refer to the auth_utils documentation.)",
        help="Generate a refresh token for an OAuth 2.0 service\n(to be used with an IBM SOAR app)",
        formatter_class=FORMATTER_CLASS)
    parser_oauth2_gen_refresh_token.add_argument("-c", "--config_file", help="Location of app.config file")
    parser_oauth2_gen_refresh_token.add_argument('-t', '--timeout', help="Timeout callback listener after "
                                                                         "timeout (seconds)")
    parser_oauth2_gen_refresh_token.add_argument('-b', '--browser', action='store_true', help="Use browser "
                                                                                              "and listener")
    parser_oauth2_gen_refresh_token.add_argument('-a', '--app_name', help="Specify the app name")
    parser_oauth2_gen_refresh_token.add_argument('-p', '--port', help="Specify port for callback url and "
                                                                      "listener")
    parser_oauth2_gen_refresh_token.add_argument('-ci', '--client_id', help="Specify OAuth 2.0 application "
                                                                            "client ID")
    parser_oauth2_gen_refresh_token.add_argument('-cs', '--client_secret', help="Specify OAuth 2.0 application "
                                                                                "client secret")
    parser_oauth2_gen_refresh_token.add_argument('-sc', '--scope', help="Specify OAuth 2.0 application scope")
    parser_oauth2_gen_refresh_token.add_argument('-tu', '--token_url', help="Specify OAuth 2.0 application "
                                                                            "token url")
    parser_oauth2_gen_refresh_token.add_argument('-au', '--auth_url', help="Specify OAuth 2.0 application "
                                                                           "authorization url")
    parser_oauth2_gen_refresh_token.set_defaults(function=oauth2_generate_refresh_token)

    args = parent_parser.parse_args()

    # If -v was specified, set the log level to DEBUG
    if args.verbose:
        LOG.setLevel(logging.DEBUG)
        LOG.debug("Logging set to DEBUG mode")
    # Execute the subcommand
    try:
        args.function(args)
    except AttributeError as ae:
        parent_parser.print_help()
    except (KeyboardInterrupt, Abort):
        print('')

if __name__ == "__main__":
    main()