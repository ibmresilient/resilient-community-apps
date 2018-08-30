# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

import logging
import json
import requests
import time
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, UriProp, NumberProp, ThreatLookupIncompleteException


LOG = logging.getLogger(__name__)


class HaveIBeenPwnedSearcher(BaseComponent):
    """
    Have I been Pwned custom threat searcher component

    Test using 'curl':
        curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/have_i_been_pwned_threat_service'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"email.header",
        "value":"test@example.com"}' 'http://127.0.0.1:9000/cts/have_i_been_pwned_threat_service'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"email.header.to",
        "value":"safe@email2.com"}' 'http://127.0.0.1:9000/cts/have_i_been_pwned_threat_service'

    """

    HAVE_I_BEEN_PWNED_URL = "https://haveibeenpwned.com/api/v2"

    def __init__(self, opts):
        super(HaveIBeenPwnedSearcher, self).__init__(opts)
        LOG.debug(opts)

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("have_i_been_pwned_threat_service")

    # Handle lookups for artifacts of type 'email sender' and 'email receiver
    @handler("email.header", "email.header.to")
    def _lookup_email_sender(self, event, *args, **kwargs):
        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.debug("_lookup_email_sender started for Artifact Type {0} - Artifact Value {1}".format(
            artifact_type, artifact_value))

        hits = self._query_hibp_api(artifact_value)

        yield hits

    def _query_hibp_api(self, artifact_value):
        hits = []
        retry = True
        while(retry):
            try:
                # Return zero or more hits.  Here's one example.
                breach_url = "{0}/breachedaccount/{1}".format(self.HAVE_I_BEEN_PWNED_URL, artifact_value)
                breaches_response = requests.get(breach_url, headers={'User-Agent': 'Resilient HIBP CTS'})

                paste_url = "{0}/pasteaccount/{1}".format(self.HAVE_I_BEEN_PWNED_URL, artifact_value)
                pastes_response = requests.get(paste_url, headers={'User-Agent': 'Resilient HIBP CTS'})

                if breaches_response.status_code == 200 and pastes_response.status_code == 200:
                    b_content = breaches_response.json()
                    if b_content is None:
                       b_content = []
                    p_content = pastes_response.json()
                    if p_content is None:
                        p_content = []

                    hits.append(
                        Hit(
                            NumberProp(name="Breached Sites", value=len(b_content)),
                            NumberProp(name="Pastes", value=len(p_content))
                        )
                    )
                    retry = False

                # 404 is returned when an email was not found
                elif breaches_response.status_code == 404 or pastes_response.status_code == 404:
                    LOG.info("No hit information found on email address: {0}".format(artifact_value))
                    retry = False
                elif breaches_response.status_code == 429 or pastes_response.status_code == 429:
                    # Rate limit was hit, wait 2 seconds and try again
                    time.sleep(2)
                else:
                    LOG.warn("Have I Been pwned returned expected status code")
                    retry = False
                    raise ThreatLookupIncompleteException()
            except BaseException as e:
                LOG.exception(e.message)
            return hits
