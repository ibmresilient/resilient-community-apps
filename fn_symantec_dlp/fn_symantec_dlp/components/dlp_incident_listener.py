# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
""" DLP_Incident_Listener is a Component used to poll DLP for Incidents on an recurring interval
Incidents are queried through the Incident and Reporting API and that is handled by the DLPSoapClient class through delagation

Every N seconds, an event is fired which causes a thread to be created, starting the poller
If the poller is still active when the next polling event is fired, the original thread is kept alive.
"""
import logging
import sys
import threading

from circuits import Event, Timer, handler
from resilient_circuits import ResilientComponent
from resilient_lib import str_to_bool

from fn_symantec_dlp.util.dlp_listener_component import DLPListener
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient



LOG = logging.getLogger(__name__)
DEFAULT_POLLING_INTERVAL = 600
class FunctionComponent(ResilientComponent):
    """Component that sets up a Listener to Poll DLP for Incidents, which are then added to Resilient"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_symantec_dlp", {})
        self.dlp_listener = DLPListener(opts)

        if "pytest" in sys.modules:
            # Reaching here indicates that the component is invoked from within a testing session.
            # In this case, don't start the Poller

            LOG.info("Running within a test environment. Not starting listener")
        else:
            # The dlp_listener_toggle will determine whether the Poller will run
            if str_to_bool(self.options.get("sdlp_should_poller_run", None)):
                if self.dlp_listener.soap_client.is_connected:
                    self.setup_listener()

                    # Use a circuits timer to fire off an event every N seconds.
                    #     When the event is fired, a function with the decorator @handler(name_of_event)
                    #     will be used to handle the event and perform some task
                    polling_interval = int(self.options.get("sdlp_listener_timer", DEFAULT_POLLING_INTERVAL))
                    LOG.debug(u"DLP Polling interval will be %s seconds", polling_interval)
                    
                    Timer(interval=polling_interval,
                          event=Event.create("DLPListenerPollingEvent"),
                          persist=True).register(self)
    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        # Compare the existing options with what we just pulled, has ANY value changed?
        LOG.debug("Reloading event triggered, comparing app.config values")
        if self.options != opts.get("fn_symantec_dlp", {}):
            self.options = opts.get("fn_symantec_dlp", {})
            # Toggle the shared class_vars_loaded so the init of DLPSoapClient isin't skipped
            self.dlp_listener.soap_client.class_vars_loaded = False 
            # Reinit the DLPSoapClient class
            DLPSoapClient.__init__(self.dlp_listener.soap_client, app_configs=self.options)
            # Once here, the SoapClient should be reloaded and the Timer component on the next iteration will make calls with the new details


    def setup_listener(self):
        """setup_listener Start our consumer, which will attempt a connection to DLP
        """
        LOG.info("Now spawning a new daemon thread that DLP Listener will run inside of")

        try:
            # Create a thread which targets the observers run function
            # N.B note the lack of parentheses on the target function
            self.res_daemon_thread = threading.Thread(
                target=self.dlp_listener.start_poller,
                name="Symantec DLP Listener Component")
            # Make the thread a daemon (background)
            self.res_daemon_thread.daemon = True
            # Start daemon thread in bg so rest of resilient-circuits is not blocked
            self.res_daemon_thread.start()
        except Exception as e:
            LOG.error(
                u"Encountered an issue when starting the thread: %s", e)

    @handler("DLPListenerPollingEvent")
    def dlp_thread_start(self):
        """dlp_thread_start function which checks if the current thread is still running.
        If not setup and new one and Poll DLP for Incidents
        """
        LOG.info("DLP Listener Polling Event received. Checking if any previous thread is still alive")

        # If the poller is not already running
        if self.res_daemon_thread.is_alive():
            LOG.debug(
                "dlp_threat_start: poller_thread is still alive, not creating a new thread.")
        else:
            LOG.debug(
                "dlp_thread_start: Creating a thread to poll DLP")
            self.setup_listener()
