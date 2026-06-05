# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2025. All Rights Reserved.
#pragma pylint: disable=line-too-long
"""Utility to retrieve OAuth 2.0 refresh token in order to configure the Outbound email app"""
import os
import sys
import argparse
import hashlib
import webbrowser
from threading import Event
from textwrap import dedent
from urllib.parse import urlparse, parse_qs
import urllib3
from oauth_utils.lib.helpers import get_config_file, get_configs, set_configs
from oauth_utils.lib.oauth2flow import OAuth2Flow
from oauth_utils.bin.flask_app import FlaskApp


# Global variables
FLASK_TIMEOUT = 60 # Timeout Flask server after 60 secs, can be over-ridden by command line arg -t
CMD_DESCRIPTION = "A utility to generate a refresh token for an OAuth 2.0 service to be used with an IBM SOAR app."
# Generate csrf state token
CSRF_TOKEN = hashlib.sha256(os.urandom(64)).hexdigest()

urllib3.disable_warnings()

def get_cmd_usage():
    cmd_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))
    cmd_usage = dedent(f"""
    $ {cmd_name}
    $ {cmd_name} -b --port 4000 -t 90
    $ {cmd_name} --app_name fn_test_app
    $ {cmd_name} -c <path_to_config_file>/app.config
    $ {cmd_name} -ci 1234567a-abc8-90d1-2efa3-123456789abcd -cs ABCDEF-123456789abcd123456789a_aWX4 -sc
    https://mail.myservice.com/ -tu https://myservice.com/o/oauth2/token -au https://myservice.com/o/oauth2/auth
    """)
    return cmd_usage

def parse_args(args=None):
    """
    Parse the command-line arguments.
    """
    if args is None:
        parser = argparse.ArgumentParser()
        parser.usage = get_cmd_usage()
        parser.description = CMD_DESCRIPTION
        parser.add_argument("-c", "--config_file", help="Location of app.config file")
        parser.add_argument('-t', '--timeout', help="Timeout callback listener after timeout (seconds)")
        parser.add_argument('-b', '--browser', action='store_true', help="Use browser and listener")
        parser.add_argument('-a', '--app_name', help="Specify the app name")
        parser.add_argument('-p', '--port', help="Specify port for callback url and listener")
        parser.add_argument('-ci', '--client_id', help="Specify OAuth 2.0 application client ID")
        parser.add_argument('-cs', '--client_secret', help="Specify OAuth 2.0 application client secret")
        parser.add_argument('-sc', '--scope', help="Specify OAuth 2.0 application scope")
        parser.add_argument('-tu', '--token_url', help="Specify OAuth 2.0 application token url")
        parser.add_argument('-au', '--auth_url', help="Specify OAuth 2.0 application authorization url")
        args = parser.parse_args()

    if args.config_file:
        print(f"Using config file {args.config_file}.")
    if args.app_name:
        print(f"Using app name {args.app_name}.")
    if args.timeout:
        print(f"Timeout callback listener app after {args.timeout} seconds.")
    if args.port:
        print(f"Using port {args.port}.")
    if args.browser:
        print("Running with callback listener and web browser.")
    else:
        print("Running from command line.")

    return args

def browser_authorize(script_args, flask_app, oauth2, auth_url, stop_event):
    """
    Use a browser/Flask combination to authorize the app and retrieve a refresh token.
    The refresh token will be displayed in the browser.
    """
    # Run utility using Flask and web browser
    timeout = int(script_args.timeout) if script_args.timeout else FLASK_TIMEOUT
    # Start Flask app
    flask_app.start(oauth2, stop_event)
    # Open Oauth2 url in web browser. The web session should eventually send re-direct to the flask callback.
    print("Starting browser.")
    webbrowser.open(auth_url)
    # Wait "timeout" seconds for the Flask thread to finish its work
    stop_event.wait(timeout=timeout)
    print("Listener thread timeout limit reached.")
    # Ensure app is stopped
    flask_app.stop()
    sys.exit(0)
    # Use the command-line

def cli_authorize(oauth2, auth_url):
    """
    Use a command-line to authorize the app and retrieve a refresh token.
    """
    print('\nTo authorize a token, copy the following URL into a browser and follow the directions then enter the '
          'generated callback URL below:\n')
    print(f"{auth_url}\n")
    auth_code = input("Enter callback URL: ") # nosec - Will fail bandit for python2 which uses raw_input.
    params = parse_qs(urlparse(auth_code).query)
    if params.get("code"):
        auth_code = params['code'][0]
        refresh_token = oauth2.authenticate(auth_code)
        print("\n\nrefresh_token=" + refresh_token + "\n")
    else:
        print("ERROR: Code not available in redirected URL.")

def main(args=None):
    """
    The main() function is the starting entry point function for utility.
    """
    script_args=parse_args(args)
    use_app_config=True

    if any(a is not None for a in [script_args.scope, script_args.client_id, script_args.client_secret,
                                       script_args.token_url, script_args.auth_url]):
        use_app_config = False
        # Use discrete values from command-line.
        print("Using OAuth 2.0 discrete settings from command line arguments.")
        fn_opts = set_configs(script_args)
        if script_args.config_file:
            print("ERROR: Using arguments for an app.config file and OAuth 2.0 service settings are not allowed at the "
                  "same time.")
            os._exit(0)
    else:
        # Use values from an app.config file.
        path_config_file = get_config_file(script_args.config_file)
        print(f"Reading OAuth 2.0 settings from app.config file {path_config_file}.")
        # Get the app.config section for the app.
        fn_opts = get_configs(path_config_file=path_config_file, app_name=script_args.app_name)

    oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, script_args.port)
    # Validate settings
    oauth2.validate_settings(fn_opts, use_app_config)
    oauth2.validate_urls(fn_opts)
    # Get the authorization url.
    auth_url = oauth2.get_authorization_url()
    try:
        if script_args.browser:
            # Create stop event object
            stop_event = Event()
            # Setup Flask object
            flask_app = FlaskApp(CSRF_TOKEN, stop_event, script_args.port)
            # If -b or --browser option is set use Flask app and process callback.
            browser_authorize(script_args, flask_app, oauth2, auth_url, stop_event)
        else:
            # Use the command-line mode
            cli_authorize(oauth2, auth_url)

    except KeyboardInterrupt:
        print("Exiting...")
        if script_args.browser:
            flask_app.stop()
        sys.exit(0)

if __name__ == "__main__":
    main()
