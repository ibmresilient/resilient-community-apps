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
LOG = logging.getLogger(LOGGER_NAME)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def get_parent_parser():
    """
    Create the parent parser for oauth-utils.

    :return : Parent Parser
    """

    parser = argparse.ArgumentParser(prog='oauth-utils', formatter_class=argparse.RawTextHelpFormatter,
                                 description='Tools to manage oauth for IBM SOAR apps',
                                     epilog="For support, please visit ibm.biz/soarcommunity")

    parser.usage = """
    $ oauth-utils <subcommand> ...
    $ oauth-utils -v <subcommand> ...
    $ oauth-utils oauth2_generate_refresh_token
    $ oauth-utils oauth2_generate_refresh_token -c <path_to_config_file>/app.config
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
        description="one of these subcommands must be provided",
        metavar="",
        dest="cmd"
    )

    return sub_parser

def main():

    parent_parser = get_parent_parser()
    subparsers = get_sub_parser(parent_parser)

    parser_oauth2_gen_refresh_token = subparsers.add_parser(
        'oauth2_generate_refresh_token', help="Generate a refresh token for an OAuth2 service to be used with an IBM "
                                              "SOAR app", formatter_class=argparse.RawTextHelpFormatter)
    parser_oauth2_gen_refresh_token.add_argument("-c", "--config_file", help="(Optional) Location of app.config file")
    parser_oauth2_gen_refresh_token.add_argument('-t', '--timeout', help="(Optional) Timeout callback listener after "
                                                                         "timeout (seconds)")
    parser_oauth2_gen_refresh_token.add_argument('-b', '--browser', action='store_true', help="(Optional) Use browser "
                                                                                              "and listener")
    parser_oauth2_gen_refresh_token.add_argument('-a', '--app_name', help="(Optional) Specify the app name")
    parser_oauth2_gen_refresh_token.add_argument('-p', '--port', help="(Optional) Specify port for callback url and "
                                                                      "listener")
    parser_oauth2_gen_refresh_token.add_argument('-ci', '--client_id', help="(Optional) Specify oauth2 application "
                                                                            "client ID")
    parser_oauth2_gen_refresh_token.add_argument('-cs', '--client_secret', help="(Optional) Specify oauth2 application "
                                                                                "client secret")
    parser_oauth2_gen_refresh_token.add_argument('-sc', '--scope', help="(Optional) Specify oauth2 application scope")
    parser_oauth2_gen_refresh_token.add_argument('-tu', '--token_url', help="(Optional) Specify oauth2 application "
                                                                            "token url")
    parser_oauth2_gen_refresh_token.add_argument('-au', '--auth_url', help="(Optional) Specify oauth2 application "
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