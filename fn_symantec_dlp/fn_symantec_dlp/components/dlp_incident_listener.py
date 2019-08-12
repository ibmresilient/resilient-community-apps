# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

import logging
import sys
from resilient_circuits import ResilientComponent
import threading
from fn_symantec_dlp.util.dlp_listener_component import DLPListener
from resilient_lib import str_to_bool


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that sets up a Listener to Poll DLP for Incidents, which are then added to Resilient"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_symantec_dlp", {})
        self.dlp_listener = DLPListener(opts)
        
        if "pytest" in sys.modules:
            """
            Reaching here indicates that the component is invoked from within a testing session.
            In this case, don't start the Poller
            """
            log.info("Running within a test environment. Not starting listener")
        else:
            # The dlp_listener_toggle will determine whether the Poller will run
            if str_to_bool(self.options.get("sdlp_listener_toggle", None)):
                self.setup_listener()



    def setup_listener(self):
        # Init the consumer class with needed app.config values
        log.debug("Now spawning a new daemon thread that DLP Listener will run inside of")
        """
        Start our consumer, which will attempt a connection to DLP
        """
        try:
            # Create a thread which targets the observers run function
            # N.B note the lack of parentheses on the target function
            self.res_daemon_thread = threading.Thread(
                target=self.dlp_listener.start_poller)
            # Make the thread a daemon (background)
            self.res_daemon_thread.daemon = True
            # Start daemon thread in bg so rest of resilient-circuits is not blocked
            self.res_daemon_thread.start()

        except Exception as e:
            log.error(
                u"Encountered an issue when starting the thread: {}".format(str(e)))


