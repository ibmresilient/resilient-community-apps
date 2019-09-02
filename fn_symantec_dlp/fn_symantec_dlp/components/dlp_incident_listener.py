# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

import logging
import sys
import threading

from circuits import Event, Timer, handler
from resilient_circuits import ResilientComponent
from resilient_lib import str_to_bool

from fn_symantec_dlp.util.dlp_listener_component import DLPListener


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that sets up a Listener to Poll DLP for Incidents, which are then added to Resilient"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_symantec_dlp", {})
        self.dlp_listener = DLPListener(opts)

        
        if "pytest" in sys.modules:
            # Reaching here indicates that the component is invoked from within a testing session.
            # In this case, don't start the Poller

            log.info("Running within a test environment. Not starting listener")
        else:
            # The dlp_listener_toggle will determine whether the Poller will run
            if str_to_bool(self.options.get("sdlp_listener_toggle", None)):
                if self.dlp_listener.soap_client.is_connected:
                    self.setup_listener()

                    # Use a circuits timer to fire off an event every N seconds.
                    #     When the event is fired, a function with the decorator @handler(name_of_event)
                    #     will be used to handle the event and perform some task
                    log.debug(u"DLP Polling interval will be %s seconds", self.options.get("sdlp_listener_timer", 600))
                    Timer(interval=int(self.options.get("sdlp_listener_timer", 600)),
                        event=Event.create("DLPListenerPollingEvent"),
                        persist=True).register(self)

    def setup_listener(self):
        """setup_listener Start our consumer, which will attempt a connection to DLP
        """
        log.debug("Now spawning a new daemon thread that DLP Listener will run inside of")

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
            log.error(
                u"Encountered an issue when starting the thread: %s", e)

    @handler("DLPListenerPollingEvent")
    def dlp_thread_start(self):
        """dlp_thread_start function which checks if the current thread is still running.
        If not setup and new one and Poll DLP for Incidents
        """
        log.info("DLP Listener initiated.!")

        # If the poller is not already running
        if self.res_daemon_thread.is_alive():
            log.debug(
                "dlp_threat_start: poller_thread is still alive, not creating a new thread.")
        else:
            log.debug(
                "dlp_thread_start: Creating a thread to poll DLP")
            self.setup_listener()
