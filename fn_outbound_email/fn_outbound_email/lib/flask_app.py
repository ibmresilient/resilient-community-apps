# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Flask support classes for OAuth2 utility for the Outbound email app"""
import os
import hashlib
from threading import Thread
from datetime import timedelta
from flask import Flask, request, render_template, session
from werkzeug.serving import make_server

# Global variables
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')

class FlaskThread(Thread):
    """
    Thread Class to run Flask app.

    The Flask app is being run in a thread instead of stand alone to make it
    easier to shutdown.
    """
    def __init__(self, app, s_event):
        super(FlaskThread, self).__init__(args=(s_event,))
        # Run app with self-signed cert, server visible only on local host.
        self.server = make_server("127.0.0.1", 8080, app, ssl_context="adhoc")
        self.ctx = app.app_context()
        self.ctx.push()
        self._stop_event = s_event

    def run(self):
        # Start Flask.
        print("Starting Flask server.")
        self.server.serve_forever()

    def set_stop(self):
        # Set stop event
        self._stop_event.set()

    def shutdown(self):
        # Shutdown thread
        self._stop_event.set()
        self.server.shutdown()

class FlaskApp():
    """
    Class to run Flask app.

    The Flask app is being run in a thread instead of stand alone to make it
    easier to shutdown.
    """
    def __init__(self, csrf_token, s_event):
        self.csrf_token = csrf_token
        self.app = Flask("OAuth2 App", template_folder=TEMPLATE_PATH)
        self.thread = FlaskThread(self.app, s_event)
        self.stop_event = s_event

    def start(self, oauth2, s_event):
        """ Function to run Flask app in a thread.

        :param oauth2: An OAuth2 object.
        :param s_event: An event object to allow thread to be stopped.
        """
        app = self.app

        @app.route("/callback")
        def authorize():
            if not request.args.get("state") or request.args.get("state") != self.csrf_token:
                print("Flask ERROR: State value doesn't match, shutting down.")
                # For safety do a hard exit if the correct "state" not received in the request
                # or doesn't match the original value.
                os._exit(0)
            if request.args.get("code"):
                # For safety do a hard exit if a "code" not received in the request."
                # Set response values in shared dict
                auth_code = request.args.get("code")
                refresh_token = oauth2.authenticate(auth_code)
                return render_template('refresh_token.html', refresh_token=refresh_token)
            else:
                print("Flask ERROR: Code not received, shutting down...")
                os._exit(0)

            @app.before_request
            def make_session_permanent():
                session.permanent = True
                app.permanent_session_lifetime = timedelta(seconds=10)

        self.thread.setDaemon(True)
        self.thread.start()

    def stop(self):
        # Stop the Flask thread by setting the event.
        print("Sending stop event to Flask thread...")
        self.thread.set_stop()
        if self.thread.is_alive():
            print("Flask thread hasn't stopped, forcing shutdown...")
            self.thread.shutdown()
