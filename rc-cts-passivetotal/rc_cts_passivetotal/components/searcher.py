#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from __future__ import unicode_literals
import logging
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp

LOG = logging.getLogger(__name__)


class PassiveTotalSearcher(BaseComponent):
    """
    A custom threat service 'searcher' for Passive Total

    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/pst'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'

    """

    CONFIG_SECTION = "passivetotal"

    def __init__(self, opts):
        super(PassiveTotalSearcher, self).__init__(opts)
        LOG.debug(opts)
        self.options = opts.get(self.CONFIG_SECTION, {})

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("pst")

    @handler("net.name", "net.uri", "net.ip")
    def _lookup(self, event, *args, **kwargs):
        """
        Handle lookups for artifacts of type 'net.name' (domain name artifact), 'net.uri' (URL) or 'net.ip' (IP address)
        """

        # Read configuration settings:

        self.passivetotal_api_key = self._get_value_from_options("passivetotal_api_key")
        self.passivetotal_username = self._get_value_from_options("passivetotal_username")
        self.passivetotal_base_url = self._get_value_from_options("passivetotal_base_url")
        self.passivetotal_account_api_url = self._get_value_from_options("passivetotal_account_api_url")
        self.passivetotal_actions_tags_api_url = self._get_value_from_options("passivetotal_actions_tags_api_url")
        self.passivetotal_passive_dns_api_url = self._get_value_from_options("passivetotal_passive_dns_api_url")
        self.passivetotal_actions_class_api_url = self._get_value_from_options("passivetotal_actions_class_api_url")
        self.passivetotal_enrich_subdom_api_url = self._get_value_from_options("passivetotal_enrich_subdom_api_url")
        self.passivetotal_community_url = self._get_value_from_options("passivetotal_community_url")
        self.passivetotal_tags = self._get_value_from_options("passivetotal_tags")

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.info("_lookup started for Artifact Type {0} - Artifact Value {1}".format(artifact_type, artifact_value))

        hits = self._query_passivetotal_api(artifact_value)
        yield hits

    def _get_value_from_options(self, app_config_setting_key):
        """
        Get value from options dict or raise ValueError for the mandatory config setting.
        :param app_config_setting_key key
        """
        if app_config_setting_key in self.options:
            return self.options[app_config_setting_key]
        else:
            error_msg = "Mandatory config setting '{}' not set.".format(app_config_setting_key)
            LOG.error(error_msg)
            raise ValueError(error_msg)

    def _query_passivetotal_api(self, artifact_value):
        """
        Validate user account if API call quota has exceeded, verify if tags are match, query RiskIQ PassiveTotal API
         for the given 'net.name' (domain name artifact), 'net.uri' (URL) or 'net.ip' (IP address) and generate Hits.
        :param artifact_value
        """
        hits = []

        if self._validate_user_account_exceeded():
            return hits

        validate_tags_match, tags_hits = self._validate_tag_match(artifact_value)
        if not validate_tags_match:
            # failure condition if the site doesn't match your definition
            LOG.info("The site isn't currently listed as compromised according to your definition.")
            return hits

        LOG.info("Positive Threat Intel for %s", artifact_value)

        # Create the hits array to sent back to Resilient
        hits.append(self._generate_hit(artifact_value, tags_hits))

        return hits

    def _validate_user_account_exceeded(self):
        """
        Validate if user's API call quota has exceeded.
        Return True if user may not proceed.
        """

        account_metadata_response = self._passivetotal_get_response(self.passivetotal_account_api_url, '')
        if account_metadata_response.status_code == 200:
            account = account_metadata_response.json()
        else:
            LOG.info("No Account information found for username: {0}".format(self.passivetotal_username))
            LOG.debug(account_metadata_response.text)
            return True

        account_quota_exceeded = account.get("searchApiQuotaExceeded", None)
        if account_quota_exceeded:
            LOG.info("Your PassiveTotal Account has no API queries left.")
            LOG.debug(account_metadata_response)
            return True

        return False

    def _validate_tag_match(self, artifact_value):
        """
        Validate if returned PassiveTotal tag hits for given artifact_value include user's flagged tags from app.config file.
        Return True if tags intersect, there is a match. PT returns tags users has flagged.
        :param artifact_value
        """

        tags_response = self._passivetotal_get_response(self.passivetotal_actions_tags_api_url, artifact_value)
        if tags_response.status_code == 200:
            tags = tags_response.json()
        else:
            LOG.info("No Tag information found for artifact value: {0}".format(artifact_value))
            LOG.debug(tags_response.text)
            return False, None

        tags_hits = tags.get('tags', None)

        LOG.info("Comparing tags that result with a hit " + str(tags_hits)
                 + " with flagged tags in app.config file " + self.passivetotal_tags)

        # Tests the site has tags you have flagged
        passive_tag_set = set(item.lower().strip() for item in self.passivetotal_tags.split(","))
        tags_hit_set = set(item.lower() for item in tags_hits)

        return bool(passive_tag_set.intersection(tags_hit_set)), tags_hits

    def _passivetotal_get_response(self, path, query):
        """
        Get response from the given API for the given query.
        :param path PT API url
        :param query the domain or IP being queried
        """
        url = self.passivetotal_base_url + path
        data = {'query': query}
        auth = (self.passivetotal_username, self.passivetotal_api_key)

        response = requests.get(url, auth=auth, json=data)
        return response

    def _generate_hit(self, artifact_value, tags_hits_list):
        """
        Query RiskIQ PassiveTotal API for the given 'net.name' (domain name artifact), 'net.uri' (URL) or 'net.ip'
        (IP address) and generate a Hit.
        :param artifact_value
        :param tags_hits_list
        """
        # Passive DNS Results - Hits
        # We grab the totalRecords number and show the First Seen date to Last Seen date interval
        pdns_results_response = self._passivetotal_get_response(self.passivetotal_passive_dns_api_url,
                                                                artifact_value)
        pdns_hit_number, pdns_first_seen, pdns_last_seen = None, None, None
        if pdns_results_response.status_code == 200:
            pdns_results = pdns_results_response.json()
            pdns_hit_number = pdns_results.get("totalRecords", None)
            pdns_first_seen = pdns_results.get("firstSeen", None)
            pdns_last_seen = pdns_results.get("lastSeen", None)
            LOG.info(pdns_hit_number)
            LOG.info(pdns_first_seen)
            LOG.info(pdns_last_seen)
        else:
            LOG.info("No Passive DNS information found for artifact value: {0}".format(artifact_value))
            LOG.debug(pdns_results_response.text)

        # URL Classification - suspicious, malicious etc
        classification_results_response = self._passivetotal_get_response(self.passivetotal_actions_class_api_url,
                                                                          artifact_value)
        classification_hit = None
        if classification_results_response.status_code == 200:
            classification_results = classification_results_response.json()
            classification_hit = classification_results.get("classification", None)
            LOG.info(classification_hit)
        else:
            LOG.info("No URL classification found for artifact value: {0}".format(artifact_value))
            LOG.debug(classification_results_response.text)

        # Count of subdomains
        subdomain_results_response = self._passivetotal_get_response(self.passivetotal_enrich_subdom_api_url,
                                                                     artifact_value)
        subdomain_hits_number, first_ten_subdomains = None, None
        if subdomain_results_response.status_code == 200:
            subdomain_results = subdomain_results_response.json()
            subdomain_hits = subdomain_results.get("subdomains", None)
            subdomain_hits_number = len(subdomain_hits) if subdomain_hits else None
            first_ten_subdomains = ', '.join(subdomain_hits[:10]) if subdomain_hits else None
            LOG.info(subdomain_hits_number)
            LOG.info(first_ten_subdomains)
        else:
            LOG.info("No subdomain information found for artifact value: {0}".format(artifact_value))
            LOG.debug(subdomain_results_response.text)

        # Convert tags hits list to str
        tags_hits = ", ".join(tags_hits_list) if tags_hits_list else None

        # Construct url back to to PassiveThreat
        report_url = self.passivetotal_community_url + artifact_value

        return Hit(
            NumberProp(name="Number of Passive DNS Records", value=pdns_hit_number),
            StringProp(name="First Seen", value=pdns_first_seen),
            StringProp(name="Last Seen", value=pdns_last_seen),
            NumberProp(name="Subdomains - All", value=subdomain_hits_number),
            StringProp(name="Subdomains - First ten Hostnames", value=first_ten_subdomains),
            StringProp(name="Tags", value=tags_hits),
            StringProp(name="Classification", value=classification_hit),
            UriProp(name="Report Link", value=report_url)
            )
