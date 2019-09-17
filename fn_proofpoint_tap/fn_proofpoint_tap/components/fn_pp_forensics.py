# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import jinja2
import json
import os
import requests
from requests.auth import HTTPBasicAuth
from resilient_circuits import ResilientComponent, function, handler, template_functions, StatusMessage, FunctionResult, FunctionError
from fn_proofpoint_tap.util.helpers import get_config_option
from pkg_resources import Requirement, resource_filename
import fn_proofpoint_tap.util.selftest as selftest
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

        self.options = opts.get("fn_proofpoint_tap", {})
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.default_path = os.path.join(current_path, os.path.pardir, "data/templates/pp_threat_forensics.jinja")
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_proofpoint_tap", {})

    @function("fn_pp_forensics")
    def _fn_pp_forensics_function(self, event, *args, **kwargs):
        """Function: Function to retrieve Forensics data from the ProofPoint API by Campaign or Threat ID"""
        # Get the function parameters:
        incident_id = kwargs.get('incident_id')
        campaign_id = kwargs.get('proofpoint_campaign_id')
        threat_id = kwargs.get('proofpoint_threat_id')
        aggregate_flag = kwargs.get('proofpoint_aggregate_flag')
        malicious_flag = kwargs.get('proofpoint_malicious_flag')

        log.info('incident_id: {}'.format(incident_id))
        log.info('proofpoint_campaign_id: {}'.format(campaign_id))
        log.info('proofpoint_threat_id: {}'.format(threat_id))
        log.info('proofpoint_aggregate_flag: {}'.format(aggregate_flag))
        log.info('proofpoint_malicious_flag: {}'.format(malicious_flag))

        yield StatusMessage("starting...")

        inputs = {
            'incident_id': incident_id,
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

        yield StatusMessage("function inputs OK")

        # get configuration values
        base_url = get_config_option(self.options, 'base_url')
        username = get_config_option(self.options, 'username')
        password = get_config_option(self.options, 'password')
        cafile = self.options.get('cafile')
        bundle = os.path.expanduser(cafile) if cafile else False

        yield StatusMessage("configuration values OK")
        yield StatusMessage("Certificate verify {0}".format(bundle))

        basic_auth = HTTPBasicAuth(username, password)
        url = '{0}/forensics?{1}'.format(base_url, params)  # /v2/forensics Fetch forensic information for a given threat or campaign.

        try:
            yield StatusMessage('Sending GET request to {0}'.format(url))

            res = requests.get(url, auth=basic_auth, verify=bundle)

            # Debug logging
            log.debug("Response status_code: {}".format(res.status_code))
            log.debug("Response content: {}".format(res.content))

            res.raise_for_status()

            if res.status_code == 200:
                data = []
                forensics = json.loads(res.text)
                log.debug('got {}'.format(json.dumps(forensics, indent=2)))
                for report in forensics['reports']:
                    for forensic in report['forensics']:
                        if not forensic:
                            # no object?
                            yield StatusMessage('no forensic')
                            continue
                        if malicious_flag and not forensic.get('malicious'):
                            # non-malicious result and we're only interested in malicious ones
                            yield StatusMessage('not malicious')
                            continue
                        try:
                            yield StatusMessage('forensic data {}'.format(json.dumps(forensic, indent=2)))
                            # load the forensics jinja template
                            self._parse_opts()
                            # render it
                            data.append(template_functions.render(self.forensics_template, forensic))
                            yield StatusMessage('now data {}'.format(data))

                        except jinja2.exceptions.TemplateSyntaxError:
                            log.info('forensics template is not set correctly in config file')
                            continue

                yield StatusMessage('final data {}'.format(data))

                results['success'] = True
                results['data'] = data
            else:
                yield StatusMessage('status code {}'.format(res.status_code))
                raise ValueError('request to {0} failed with code {1}'.format(url, res.status_code))

        except requests.exceptions.Timeout:
            yield StatusMessage('timeout')
            raise ValueError('request to {0} timed out'.format(url))

        except requests.exceptions.TooManyRedirects:
            yield StatusMessage('too many redirects')
            raise ValueError('URL redirection loop?', url)

        except requests.exceptions.HTTPError as err:
            yield StatusMessage('HTTP error {}'.format(err))
            if err.response.content is not None:
                try:
                    custom_error_content = json.loads(err.response.content)
                except JSONDecodeError:
                    raise ValueError(err)
                # raise ValueError(custom_error_content)
                yield FunctionResult(custom_error_content)
            raise ValueError(err)

        except requests.exceptions.RequestException as ex:
            yield StatusMessage('exception {}'.format(ex))
            raise ValueError(ex)

        yield StatusMessage("done...")
        # Produce a FunctionResult with the results
        yield FunctionResult(results)

    def _parse_opts(self):
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

