# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
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
from resilient import get_config_file
from resilient_circuits import helpers
from fn_outbound_email.lib.oauth2 import OAuth2
from fn_outbound_email.lib.flask_app import FlaskApp

# Global variables
FN_NAME = "fn_outbound_email"
FLASK_TIMEOUT = 60 # Timeout Flask server after 60 secs, can be over-ridden by command line arg -t
# Generate csrf state token
CSRF_TOKEN = hashlib.sha256(os.urandom(64)).hexdigest()

urllib3.disable_warnings()


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
    print("Flask thread timeout limit reached.")
    # Ensure app is stopped
    flask_app.stop()
    sys.exit(0)
    # Use the command-line

def cli_authorize(oauth2, auth_url):
    """
    Use a command-line to authorize the app and retrieve a refresh token.
    """
    print('To authorize a token, visit this url and follow the directions:')
    print("{}".format(auth_url))
    if sys.version_info[0] == 3:
        auth_code = input("Enter redirected URL: ") # nosec - Will fail bandit for python2 which uses raw_input.
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
    # Parse config_file argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config_file", help="(Optional) Location of app.config file")
    parser.add_argument('-t', '--timeout', help="(Optional) Timeout Flask after timeout (seconds)")
    parser.add_argument('-b', '--browser', action='store_true', help="(Optional) Use browser")
    script_args = parser.parse_args()

    if script_args.config_file:
        print("Using config file {}.".format(script_args.config_file))
    if script_args.timeout:
        print("Timeout Flask app after {} seconds.".format(script_args.timeout))
    if script_args.browser:
        print("Running with flask and web browser.")
    else:
        print("Running with from command line.")
    # Get the app.config section for the app.
    opts = helpers.get_configs(path_config_file=get_config_file(script_args.config_file),
                                     ALLOW_UNRECOGNIZED=True)
    fn_opts = opts[FN_NAME]
    # Setup OAuth2 helper object
    oauth2 = OAuth2(opts, CSRF_TOKEN)
    # Validate settings
    oauth2.validate_settings(fn_opts)
    # Get the authorization url.
    auth_url = oauth2.get_authorization_url()
    try:
        if script_args.browser:
            # Create stop event object
            stop_event = Event()
            # Setup Flask object
            flask_app = FlaskApp(CSRF_TOKEN, stop_event)
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

main()
