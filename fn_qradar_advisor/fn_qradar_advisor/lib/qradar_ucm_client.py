# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import requests
import json
from .qradar_http_info import HttpInfo

class QRadarUCMClient(object):
    """
    QRadar Use Case Manager Client
    """
    def __init__(self, qradar_host, advisor_app_id, qradar_token, cafile, log, opts=None, function_opts=None):
        self.http_info = HttpInfo(qradar_host=qradar_host,
                                  advisor_app_id=advisor_app_id,
                                  qradar_token=qradar_token,
                                  cafile=cafile, log=log,
                                  opts=opts, function_opts=function_opts)
        self.log = log

    def test_connectivity(self):
        """test_connectivity - determine if the Use Case Manager UCM app is installed and running.
           UCM is used to map a QRadar rule to a MITRE tactic.  Use QRadar app framework 
           endpoint to see which extensions are installed on the server and then check if UCM is 
           in the RUNNING state.
        """
        url = self.http_info.get_qradar_apps_url()

        session = self.http_info.get_session()
        response = session.get(url=url, 
                               data=None,
                               verify=self.http_info.get_cafile())
        status_code = response.status_code
        ucm_running = False
        if status_code > 200:
            return status_code, ucm_running

        response_json = response.json()
        ucm_uuid = self.http_info.get_UCM_UUID()

        # Loop through the installed extensions and look for the UCM uuid and it's state.
        if response_json:
            for app in response_json:
                manifest = app.get("manifest")
                if manifest:
                    uuid = manifest.get("uuid")
                    if uuid == ucm_uuid:
                        application_state = app.get("application_state")
                        if application_state.get("status") == 'RUNNING':
                            ucm_running = True
                        break
        return status_code, ucm_running

    def find_tactic_mapping(self, rule_name):
        """
        Find the MITRE Tactic that maps to a given QRadar rule
        :param rule_name: QRadar rule
        :return:
        """
        # Get the Qradar UUID of the rule name
        rule_id = self.get_qradar_rule_id(rule_name)

        if rule_id:
            tactics = self.get_tactics_of_rule(rule_name, rule_id)
        else:
            # Log that there is no tactic mapping and return empty mapping 
            self.log.info("Map rule: QRadar ID not found for rule: %s", rule_name)
            tactics = {'mapping': {}}

        return tactics

    def get_qradar_rule_id(self, rule_name):
        """
        Get the UUID for the rule given the the rule name
        """
        session = self.http_info.get_session()
        url = self.http_info.get_qradar_get_rule_url(rule_name)

        response = session.get(url=url,
                               data=None,
                               verify=self.http_info.get_cafile())
        response.raise_for_status()

        response_json = response.json()
        if not response_json:
            rule_id = None
        else:
            rule_id = response_json[0].get("identifier")
        return rule_id

    def get_tactics_of_rule(self, rule_name, rule_id):
        """
        Return the MITRE rule tactics given the Qradar rule name and ID (UUID).
        """
        url = self.http_info.get_qradar_ucm_get_mitre_mitre_coverage_url(rule_id=rule_id)
        mitre_results = self.http_info.session.get(url=url,
                                                   verify=self.http_info.get_cafile(),
                                                   headers=self.http_info.session.headers)
        mitre_results.raise_for_status()
        mitre_tactics = json.loads(mitre_results.text)
        tactics = mitre_tactics.get(rule_name)
        return tactics    