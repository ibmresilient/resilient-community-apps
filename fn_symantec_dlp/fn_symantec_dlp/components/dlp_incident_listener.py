# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

import logging
from resilient_circuits import ResilientComponent
from fn_symantec_dlp.util.dlp_listener_component import DLPListener


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that sets up a Listener to Poll DLP for Incidents, which are then added to Resilient"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_symantec_dlp", {})
        self.dlp_listener = DLPListener(opts)
        
