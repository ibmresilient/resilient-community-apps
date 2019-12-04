# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import json
import os
import jinja2
from resilient_lib import RequestsCommon, validate_fields
from resilient_lib.components.integration_errors import IntegrationError
from requests.auth import HTTPBasicAuth
from pkg_resources import Requirement, resource_filename
from fn_proofpoint_tap.util.proofpoint_common import custom_response_err_msg, PROOFPOINT_TAP_404_ERROR
from resilient_circuits import ResilientComponent, function, handler, template_functions, StatusMessage, FunctionResult, FunctionError
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_pp_forensics"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        self.opts = opts
        self.options = opts.get("fn_proofpoint_tap", {})
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.default_path = os.path.join(current_path, os.path.pardir, "data/templates/pp_threat_forensics.jinja")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_proofpoint_tap", {})

    @function("fn_pp_forensics")
    def _fn_pp_forensics_function(self, event, *args, **kwargs):
        """Function: Function to retrieve Forensics data from the ProofPoint API by Campaign or Threat ID"""

        try:
            # Get the function parameters:
            campaign_id = kwargs.get('proofpoint_campaign_id')
            threat_id = kwargs.get('proofpoint_threat_id')
            aggregate_flag = kwargs.get('proofpoint_aggregate_flag')
            malicious_flag = kwargs.get('proofpoint_malicious_flag')

            log.info('proofpoint_campaign_id: {}'.format(campaign_id))
            log.info('proofpoint_threat_id: {}'.format(threat_id))
            log.info('proofpoint_aggregate_flag: {}'.format(aggregate_flag))
            log.info('proofpoint_malicious_flag: {}'.format(malicious_flag))

            yield StatusMessage("Starting...")

            inputs = {
                'campaign_id': campaign_id,
                'threat_id': threat_id,
                'aggregate_flag': aggregate_flag,
                'malicious_flag': malicious_flag,
            }

            results = {
                'inputs': inputs,
                'success': False,
            }

            if campaign_id is None:
                if threat_id is None:
                    raise FunctionError(u"either campaign_id or threat_id is required")

                params = 'threatId={0}'.format(threat_id)
                if aggregate_flag:
                    params += '&includeCampaignForensics=true'
            else:
                if threat_id is not None:
                    raise FunctionError(u"only one of campaign_id or threat_id is allowed")

                params = 'campaignId={0}'.format(campaign_id)

            yield StatusMessage("Function inputs OK")

            # Get configuration values
            validate_fields(['base_url', 'username', 'password'], self.options)

            base_url = self.options.get('base_url')
            username = self.options.get('username')
            password = self.options.get('password')
            cafile = self.options.get('cafile')
            bundle = os.path.expanduser(cafile) if cafile else False

            yield StatusMessage("Configuration values OK")
            yield StatusMessage("Certificate verify {0}".format(bundle))

            basic_auth = HTTPBasicAuth(username, password)
            url = '{0}/forensics?{1}'.format(base_url, params)  # /v2/forensics Fetch forensic information for a given threat or campaign.
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            try:
                yield StatusMessage('Sending GET request to {0}'.format(url))
                forensics_response = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies(),
                                                        callback=custom_response_err_msg)
                aggregate_forensics = forensics_response.json()
                log.debug('Get Forensics Response content: {}'.format(aggregate_forensics))

                malicious_reports = []
                reports = aggregate_forensics.get('reports', [])
                for report in reports:

                    malicious_evidence = []  # array of malicious Evidence rendered with jinja template
                    for forensic in report.get('forensics', []):

                        if not forensic:
                            # no object
                            continue
                        if malicious_flag is True and forensic.get('malicious') is False:
                            # we're only interested in malicious ones
                            continue

                        log.debug('Malicious forensic evidence found {}'.format(json.dumps(forensic, indent=2)))
                        try:
                            # load the forensics jinja template
                            self._open_template()
                            # render it and add malicious forensics to malicious_evidence list
                            malicious_evidence.append(template_functions.render(self.forensics_template, forensic))
                        except jinja2.exceptions.TemplateSyntaxError:
                            log.info('forensics template is not set correctly in config file')

                    if malicious_evidence:
                        # add report_generated date to report Dict
                        report['report_generated'] = aggregate_forensics.get('generated')
                        # add malicious forensics
                        report['malicious_forensic_report'] = malicious_evidence

                        malicious_reports.append(report)

                if malicious_reports:
                    num_reports = len(malicious_reports)
                    yield StatusMessage('Found {} {} with malicious forensics'.format(num_reports, "report" if
                                        num_reports == 1 else "reports"))
                else:
                    yield StatusMessage('No report with malicious forensics found')

                results['success'] = True
                results['reports'] = malicious_reports

                yield StatusMessage("Done...")
                # Produce a FunctionResult with the results
                yield FunctionResult(results)

            except IntegrationError as err:
                msg = err.value
                # If endpoint returns 404 workflow is not terminated - a Note with error msg is created instead
                if PROOFPOINT_TAP_404_ERROR in msg:
                    # clean the error value, remove \' and \\n
                    msg = msg.split("\'")[1].strip("\\n")
                    results['note_err_text'] = msg
                    results['success'] = False

                    yield StatusMessage("404 Client Error...")
                    # Produce a FunctionResult with the results
                    yield FunctionResult(results)
                else:
                    raise FunctionError(err)

        except Exception as err:
            yield FunctionError(err)

    def _open_template(self):
        """
        Open jinja template file.
        :return:
        """
        forensics_path = self.options.get("forensics_template", self.default_path)
        if forensics_path and not os.path.exists(forensics_path):
            log.warn(u"Template file '%s' not found.", forensics_path)
            forensics_path = None
        if not forensics_path:
            # Use the template file installed by this package
            forensics_path = resource_filename(Requirement("fn-proofpoint_tap"),
                                               "fn_proofpoint_tap/data/templates/pp_threat_forensics.jinja")
        if not os.path.exists(forensics_path):
            raise Exception(u"Template file '{}' not found".format(forensics_path))

        log.info(u"Template file: %s", forensics_path)
        with open(forensics_path, "r") as forensics_file:
            self.forensics_template = forensics_file.read()
