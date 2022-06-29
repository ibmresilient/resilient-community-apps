# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Utility to retrieve OAuth2 refresh token in order to configure the Outbound email app"""
import os
import sys
import webbrowser
import argparse
import hashlib
from threading import Event
import urllib3
if sys.version_info[0] == 3:
    from urllib.parse import urlparse, parse_qs
else:
    from urlparse import urlparse, parse_qs

from oauth_utils.lib.helpers import get_config_file, get_configs, set_configs
from oauth_utils.lib.oauth2flow import OAuth2Flow
from oauth_utils.bin.flask_app import FlaskApp

# Global variables
FLASK_TIMEOUT = 60 # Timeout Flask server after 60 secs, can be over-ridden by command line arg -t
# Generate csrf state token
CSRF_TOKEN = hashlib.sha256(os.urandom(64)).hexdigest()

urllib3.disable_warnings()

def parse_args():
    """
    Parse the command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_file", help="(Optional) Location of app.config file")
    parser.add_argument('-t', '--timeout', help="(Optional) Timeout callback listener after timeout (seconds)")
    parser.add_argument('-b', '--browser', action='store_true', help="(Optional) Use browser and listener")
    parser.add_argument('-a', '--app_name', help="(Optional) Specify the app name")
    parser.add_argument('-p', '--port', help="(Optional) Specify port for callback url and listener")
    parser.add_argument('-ci', '--client_id', help="(Optional) Specify oauth2 application client ID")
    parser.add_argument('-cs', '--client_secret', help="(Optional) Specify oauth2 application client secret")
    parser.add_argument('-sc', '--scope', help="(Optional) Specify oauth2 application scope")
    parser.add_argument('-tu', '--token_url', help="(Optional) Specify oauth2 application token url")
    parser.add_argument('-au', '--auth_url', help="(Optional) Specify oauth2 application authorization url")
    args = parser.parse_args()

    if args.config_file:
        print("Using config file {}.".format(args.config_file))
    if args.app_name:
        print("Using app name {}.".format(args.app_name))
    if args.timeout:
        print("Timeout callback listener app after {} seconds.".format(args.timeout))
    if args.port:
        print("Using port {}.".format(args.port))
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
    print("{}\n".format(auth_url))
    if sys.version_info[0] == 3:
        auth_code = input("Enter callback URL: ") # nosec - Will fail bandit for python2 which uses raw_input.
    else:
        auth_code = raw_input("Enter redirected URL: ")
    params = parse_qs(urlparse(auth_code).query)
    auth_code = params['code'][0]
    refresh_token = oauth2.authenticate(auth_code)
    print("\n\nrefresh_token=" + refresh_token + "\n")

def main():
    """
    The main() function is the starting entry point function for utility.
    """
    script_args = parse_args()

    if any(a is not None for a in [script_args.scope, script_args.client_id, script_args.client_secret,
                                       script_args.token_url, script_args.auth_url]):
        # Use discrete values from command-line.
        print("Using OAuth2 discrete settings from command-line arguments.")
        fn_opts = set_configs(script_args)
        if script_args.config_file:
            print("ERROR: Using arguments for an app.config file and OAuth2 service settings are not allowed at the "
                  "same time.")
            os._exit(0)
    else:
        # Use values from an app.config file.
        path_config_file = get_config_file(script_args.config_file)
        print("Reading OAuth2 settings from app.config file {}.".format(path_config_file))
        # Get the app.config section for the app.
        fn_opts = get_configs(path_config_file=path_config_file, app_name=script_args.app_name)

    oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, script_args.port)
    # Validate settings
    oauth2.validate_settings(fn_opts)
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

