# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_anomali_staxx.lib.staxx_lib import StaxxClient
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

STAXX_SECTION = "fn_anomali_staxx"
RESILIENT_TAG = "resilient"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(STAXX_SECTION, {})
        self.staxx_ip = self.options.get('staxx_ip')
        self.staxx_port = self.options.get('staxx_port')
        self.staxx_user = self.options.get('staxx_user')
        self.staxx_password = self.options.get('staxx_password')

        validate_fields(['staxx_ip', 'staxx_port', 'staxx_user', 'staxx_password'], self.options)

    @function("staxx_import")
    def _send_to_staxx_function(self, event, *args, **kwargs):
        """Function: """
        try:
            rc = ResultPayload(STAXX_SECTION, **kwargs)
            # Get the function parameters:
            staxx_confidence = kwargs.get("staxx_confidence_lvl")  # num: 0-100
            staxx_tlp = self.get_select_param(kwargs.get("staxx_tlp"))  # multiselect, values: "RED", "AMBER", "GREEN", "WHITE"
            staxx_auto_approve = self.get_select_param(kwargs.get("staxx_auto_approve"))  # select, values: "yes", "no"
            staxx_severity = self.get_select_param(kwargs.get("staxx_severity"))  # select, values: "low", "medium", "high", "very-high"
            staxx_indicator_type = self.get_select_param(kwargs.get("staxx_indicator_type"))  # select, values: "apt_md5", "apt_subject", "apt_ua", "apt_url", "bot_ip", "brute_ip", "c2_domain", "c2_ip", "compromised_ domain", "compromised_email", "compromised_ip", "compromised_url", "ddos_ip", "dyn_dns", "exfil_domain", "exfil_ip", "exfil_url", "exploit_domain", "exploit_ip", "exploit_url", "geolocation_url", "hack_tool", "ipcheck_url", "mal_domain", "mal_email", "mal_ip", "mal_md5", "mal_ua", "mal_url", "p2pcnc", "parked_ip", "pastesite_url", "phish_domain", "phish_email", "phish_url", "proxy_ip", "scan_ip", "sinkhole_domain", "sinkhole_ip", "spam_domain", "spam_email", "spam_ip", "spam_url", "speedtest_url", "ssh_ip", "suppress", "suspicious_domain", "tor_ip", "torrent_tracker_url", "vpn_domain", "vps_ip"
            staxx_indicator = kwargs.get("staxx_indicator")  # text

            log = logging.getLogger(__name__)

            # test the value of confidence as values 0-100
            try:
                if staxx_confidence < 0 or staxx_confidence > 100:
                    raise ValueError("Specify the confidence value between 0-100")
            except ValueError:
                raise ValueError("Specify the confidence value between 0-100")

            tlp = "TLP:{}".format(staxx_tlp)

            yield StatusMessage(u"Creating indicator {} with the following {},{},{},{},{}".format(staxx_indicator,
                                                                                                 staxx_confidence,
                                                                                                 staxx_severity,
                                                                                                 staxx_auto_approve,
                                                                                                 staxx_tlp,
                                                                                                 staxx_indicator_type)
                                )

            staxx = StaxxClient("https://{}:{}".format(self.staxx_ip,self.staxx_port),
                                self.staxx_user,
                                self.staxx_password,
                                RequestsCommon(self.opts, self.options)
                                )

            try:
                staxx_response = staxx.import_staxx_intel(tlp=tlp,
                                                          severity=staxx_severity,
                                                          threat_type=staxx_indicator_type,
                                                          auto_approve=staxx_auto_approve,
                                                          confidence=staxx_confidence,
                                                          tags=RESILIENT_TAG,
                                                          intel_str=staxx_indicator
                                                          )
                yield StatusMessage("Posted Staxx Object Successfully: {}".format(staxx_response))
                status = True
                reason = None
            except Exception as err:
                err = "Error Staxx query: {}".format(str(err))
                raise FunctionError(err)

            results = rc.done(status, staxx_response, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
