# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2023, 2025. All Rights Reserved.

"""Function implementation"""

import logging
import os
import tempfile
import datetime
from resilient_lib import RequestsCommon, validate_fields
from resilient_lib.components.integration_errors import IntegrationError
from requests.auth import HTTPBasicAuth
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_proofpoint_tap.util.proofpoint_common import custom_response_err_msg, PROOFPOINT_TAP_404_ERROR, filter_reports, create_attachment
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_pp_forensics"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)

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
            incident_id = kwargs.get('incident_id')  # number
            campaign_id = kwargs.get('proofpoint_campaign_id')
            threat_id = kwargs.get('proofpoint_threat_id')
            aggregate_flag = kwargs.get('proofpoint_aggregate_flag')
            malicious_flag = kwargs.get('proofpoint_malicious_flag')

            log.info(f"incident_id: {incident_id}")
            log.info(f"proofpoint_campaign_id: {campaign_id}")
            log.info(f"proofpoint_threat_id: {threat_id}")
            log.info(f"proofpoint_aggregate_flag: {aggregate_flag}")
            log.info(f"proofpoint_malicious_flag: {malicious_flag}")

            yield StatusMessage("Starting...")

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
                    raise FunctionError("either campaign_id or threat_id is required")

                params = f"threatId={threat_id}"
                if aggregate_flag:
                    params += '&includeCampaignForensics=true'
            else:
                if threat_id:
                    raise FunctionError("only one of campaign_id or threat_id is allowed")

                params = f"campaignId={campaign_id}"

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
            url = f"{base_url}/forensics?{params}"  # /v2/forensics Fetch forensic information for a given threat or campaign.
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            try:
                yield StatusMessage('Sending GET request to {0}'.format(url))
                forensics_response = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies(),
                                                        callback=custom_response_err_msg)
                aggregate_forensics = forensics_response.json()
                log.debug(f"Get Forensics Response content: {aggregate_forensics}")

                with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_file:
                    # "w+b" Binary mode is used so that it behaves consistently on all platforms without
                    # regard for the data that is stored.
                    try:
                        # Write title in a temp file
                        report_title = "Proofpoint TAP - Aggregate Forensics Report"
                        temp_file.write(report_title.encode('utf-8'))

                        # Filter results
                        filtered_reports = filter_reports(aggregate_forensics, malicious_flag, temp_file, self.options,
                                                          self.default_path)

                        # Close temp_file before creating an Attachment
                        temp_file.close()

                        # Create an Attachment only if Reports were found
                        if filtered_reports:
                            num_reports = len(filtered_reports)
                            results['num_reports'] = num_reports

                            yield StatusMessage('Found {} {} with forensics evidence'.format(num_reports, "report" if
                                                num_reports == 1 else "reports"))

                            # Initialize Resilient API object
                            res_client = self.rest_client()

                            # Create an Attachment
                            file_name = "Aggregate Forensics Report - {}.txt".format(str(datetime.datetime.now()))

                            new_attachment = create_attachment(res_client, file_name, temp_file, incident_id, 'text/plain')
                            if new_attachment:
                                yield StatusMessage("Report with forensic evidence uploaded as an Attachment: {}".format(file_name))
                            else:
                                raise FunctionError(
                                    "Failed creating an Attachment with forensic evidence report")
                        else:
                            yield StatusMessage('No report with forensics evidence found')

                        results['success'] = True

                    except ValueError as err:
                        raise err
                    finally:
                        os.unlink(temp_file.name)

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
                    raise FunctionError(err) from err

        except Exception as err:
            yield FunctionError(err)
