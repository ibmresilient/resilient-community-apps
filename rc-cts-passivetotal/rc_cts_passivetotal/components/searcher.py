#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import json
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp

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
        if "passivetotal_api_key" in self.options:
            self.passivetotal_api_key = self.options["passivetotal_api_key"]
        else:
            self._raise_mandatory_setting_error("passivetotal_api_key")

        if "passivetotal_username" in self.options:
            self.passivetotal_username = self.options["passivetotal_username"]
        else:
            self._raise_mandatory_setting_error("passivetotal_username")

        if "passivetotal_base_url" in self.options:
            self.passivetotal_base_url = self.options["passivetotal_base_url"]
        else:
            self._raise_mandatory_setting_error("passivetotal_base_url")

        if "passivetotal_account_api_url" in self.options:
            self.passivetotal_account_api_url = self.options["passivetotal_account_api_url"]
        else:
            self._raise_mandatory_setting_error("passivetotal_account_api_url")

        if "passivetotal_actions_tags_api_url" in self.options:
            self.passivetotal_actions_tags_api_url = self.options["passivetotal_actions_tags_api_url"]
        else:
            self._raise_mandatory_setting_error("passivetotal_actions_tags_api_url")

        if "passivetotal_tags" in self.options:
            self.passivetotal_tags = self.options["passivetotal_tags"]
        else:
            self._raise_mandatory_setting_error("passivetotal_tags")

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.info("_lookup started for Artifact Type {0} - Artifact Value {1}".format(
            artifact_type, artifact_value))

        hits = self._query_passivetotal_find(artifact_value)
        yield hits

    @staticmethod
    def _raise_mandatory_setting_error(app_config_setting_name):
        """
        Raise ValueError for the mandatory config setting.
        """
        error_msg = "Mandatory config setting '{}' not set.".format(app_config_setting_name)
        LOG.error(error_msg)
        raise ValueError(error_msg)

    def _query_passivetotal_find(self, artifact_value):
        hits = []

        # checks if user account API call quota has exceeded
        account_metadata_response = self._passivetotal_get_resoponse(self.passivetotal_account_api_url, '')
        if account_metadata_response.status_code == 200:
            account = account_metadata_response.json()
        else:
            LOG.info("No Account information found for username: {0}".format(self.passivetotal_username))
            LOG.debug(account_metadata_response.text)
            return hits

        account_quota_exceeded = account.get("searchApiQuotaExceeded", None)
        if account_quota_exceeded:
            LOG.info("Your PassiveTotal Account has no API queries left.")
            LOG.debug(account_metadata_response)
            return hits

        # compares your definition of a hit with the tags in PassiveTotal
        tags_results_response = self._passivetotal_get_resoponse(self.passivetotal_actions_tags_api_url, artifact_value)
        if tags_results_response.status_code == 200:
            tags = tags_results_response.json()

        tags_hits = tags.get('tags', None)

        # FIXME - continue here!
        LOG.info("Comparing tags " + str(tags_hits) + " and " + self.passivetotal_tags)

        # Tests the site has tags you have flagged
        if set(tags_hits) & self.passive_tag_set:
            LOG.info("Positive Threat Intel for %s", artifact_value)

            # Passive DNS Results
            pdns_results = passivetotal_get('/v2/dns/passive', artifact_value)
            pdns_hit = pdns_results["totalRecords"]
            LOG.debug(pdns_results)
            LOG.info(pdns_hit)

            # URL Classification
            classification_results = passivetotal_get('/v2/actions/classification', artifact_value)
            classification_hit = classification_results['classification']
            LOG.debug(classification_results)
            LOG.info(classification_hit)

            # Count of subdomains
            subdomain_results = passivetotal_get('/v2/enrichment/subdomains', artifact_value)
            subdomain_hits = len(subdomain_results['subdomains'])
            LOG.debug(subdomain_results)
            LOG.info(subdomain_hits)

            # Construct simple link to PT
            report_url = "https://community.riskiq.com/search/" + artifact_value

            # Create the hits array to sent back to Resilient
            hits.append(Hit(
                StringProp(name="Passive DNS Hits", value=str(pdns_hit)),
                StringProp(name="Number of subdomains", value=str(subdomain_hits)),
                StringProp(name="Tags", value=str(tags_hits)),
                StringProp(name="Classification", value=str(classification_hit)),
                UriProp(name="Report Link", value=report_url)
            ))
        else:
            # failure condition if the site doesn't match your definition
            LOG.info("The site isn't currently listed as compromised according to your definition")
        return hits

    def _passivetotal_get_resoponse(self, path, query):
        """
        Get response from the given API for the given query.
        """
        url = self.passivetotal_base_url + path
        data = {'query': query}
        auth = (self.passivetotal_username, self.passivetotal_api_key)

        response = requests.get(url, auth=auth, json=data)
        return response
