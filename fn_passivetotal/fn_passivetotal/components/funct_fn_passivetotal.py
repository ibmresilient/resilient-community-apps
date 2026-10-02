# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_passivetotal"
FN_NAME = "fn_passivetotal"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_passivetotal'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _lookup(self, fn_inputs):
        """
        Validate user account if API call quota has exceeded, verify if tags are match, and query RiskIQ PassiveTotal API
         for the given domain name artifact or IP address.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        artifact_type = fn_inputs.passivetotal_artifact_type
        artifact_value = fn_inputs.passivetotal_artifact_value

        accepted_types = ["IP Address", "DNS Name"]

        if artifact_type not in accepted_types:
            yield self.status_message("Artifact type not one of the expected values")
        else:
            # Example validating app_configs
            validate_fields([
                {"name": "passivetotal_api_key"},
                {"name": "passivetotal_username"},
                {"name": "passivetotal_base_url"},
                {"name": "passivetotal_account_api_url"},
                {"name": "passivetotal_actions_tags_api_url"},
                {"name": "passivetotal_passive_dns_api_url"},
                {"name": "passivetotal_actions_class_api_url"},
                {"name": "passivetotal_enrich_subdom_api_url"},
                {"name": "passivetotal_community_url"},
                {"name": "passivetotal_tags"}],
                self.app_configs)

            LOG.info("_lookup started for Artifact Type {0} - Artifact Value {1}".format(artifact_type, artifact_value))

            results = self._query_passivetotal_api(artifact_value)
            
            yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

            yield FunctionResult(results)


    def _query_passivetotal_api(self, artifact_value):
        """
        Validate user account if API call quota has exceeded, verify if tags are match, query RiskIQ PassiveTotal API
         for the given domain name artifact, or IP address and gather info needed to create hits.
        :param artifact_value
        """
        results = []

        # If the api quota has been exceeded or there is no account found, return empty list and log a warning
        if self._validate_user_account_exceeded():
            return results

        validate_tags_match, tags_hits = self._validate_tag_match(artifact_value)
        if not validate_tags_match:
            # failure condition if the site doesn't match your definition
            LOG.info("The site isn't currently listed as compromised according to your definition.")
            return results

        LOG.info("Positive Threat Intel for %s", artifact_value)

        pdns_results_response = self._passivetotal_get_response(self.app_configs.passivetotal_passive_dns_api_url,
                                                                artifact_value)
        if pdns_results_response.status_code == 200:
            pdns_results = pdns_results_response.json()
        else:
            LOG.info("No Passive DNS information found for artifact value: {0}".format(artifact_value))
            LOG.debug(pdns_results_response.text)

        # URL Classification - suspicious, malicious etc
        classification_results_response = self._passivetotal_get_response(self.app_configs.passivetotal_actions_class_api_url,
                                                                          artifact_value)
        if classification_results_response.status_code == 200:
            classification_results = classification_results_response.json()
        else:
            LOG.info("No URL classification found for artifact value: {0}".format(artifact_value))
            LOG.debug(classification_results_response.text)

        # Count of subdomains
        subdomain_results_response = self._passivetotal_get_response(self.app_configs.passivetotal_enrich_subdom_api_url,
                                                                     artifact_value)
        if subdomain_results_response.status_code == 200:
            subdomain_results = subdomain_results_response.json()
        else:
            LOG.info("No subdomain information found for artifact value: {0}".format(artifact_value))
            LOG.debug(subdomain_results_response.text)

        # Convert tags hits list to str
        tags_hits_str = ", ".join(tags_hits) if tags_hits else None

        # Construct url back to PassiveThreat
        report_url = self.app_configs.passivetotal_community_url + artifact_value

        results = [
            pdns_results,
            classification_results,
            subdomain_results,
            {"tags_hits_str": tags_hits_str},
            {"report_url": report_url}
            ]

        results_dict = {}

        # Change results from a list of dicitonaries into results_dict which is a dictionary of dictionaries 
        # to be easily handled by the workflow post-processing script
        for dicitonary in results:
            results_dict.update(dicitonary)

        return results_dict

    def _validate_user_account_exceeded(self):
        """
        Validate if user's API call quota has exceeded.
        Return True if user may not proceed.
        """

        account_metadata_response = self._passivetotal_get_response(self.app_configs.passivetotal_account_api_url, '')
        if account_metadata_response.status_code == 200:
            account = account_metadata_response.json()
        else:
            LOG.warning("No Account information found for username: {0}".format(self.app_configs.passivetotal_username))
            LOG.debug(account_metadata_response.text)
            return True

        account_quota_exceeded = account.get("searchApiQuotaExceeded", None)
        if account_quota_exceeded:
            LOG.warning("Your PassiveTotal Account has no API queries left.")
            LOG.debug(account_metadata_response)
            return True

        return False

    def _validate_tag_match(self, artifact_value):
        """
        Validate if returned PassiveTotal tag hits for given artifact_value include user's flagged tags from app.config file.
        Return True if tags intersect, there is a match. PT returns tags users has flagged.
        :param artifact_value
        """

        tags_response = self._passivetotal_get_response(self.app_configs.passivetotal_actions_tags_api_url, artifact_value)
        if tags_response.status_code == 200:
            tags = tags_response.json()
        else:
            LOG.info("No Tag information found for artifact value: {0}".format(artifact_value))
            LOG.debug(tags_response.text)
            return False, None

        tags_hits = tags.get('tags', None)

        LOG.info("Comparing tags that result with a hit " + str(tags_hits)
                 + " with flagged tags in app.config file " + self.app_configs.passivetotal_tags)

        # Tests the site has tags you have flagged
        passive_tag_set = set(item.lower().strip() for item in self.app_configs.passivetotal_tags.split(","))
        tags_hit_set = set(item.lower() for item in tags_hits)

        return bool(passive_tag_set.intersection(tags_hit_set)), tags_hits

    def _passivetotal_get_response(self, path, query):
        """
        Get response from the given API for the given query.
        :param path PT API url
        :param query the domain or IP being queried
        """
        url = self.app_configs.passivetotal_base_url + path
        data = {'query': query}
        auth = (self.app_configs.passivetotal_username, self.app_configs.passivetotal_api_key)

        response = self.rc.execute("get", url, auth=auth, json=data)
        return response
