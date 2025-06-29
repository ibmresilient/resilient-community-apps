# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=pointless-string-statement, line-too-long, wrong-import-order

"""Function implementation"""

import logging
from urllib.parse import urlsplit
from fn_network_utilities.util.distance import damerau_levenshtein_distance
from fn_network_utilities.util.confusable import Confusable
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError
from resilient import ensure_unicode


class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'domain_distance"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_network_utilities", {})
        # Load the confusable-characters table
        self.confusable = Confusable()

    def normalize_name(self, domain):
        """Produce a normalized version for comparison"""
        # Strip leading and trailing spaces
        domain = domain.strip()
        # First, decode IDNA to unicode
        try:
            domain = domain.encode("utf-8").decode("idna")
        except (UnicodeError, UnicodeDecodeError):
            domain = ensure_unicode(domain)
        # Normalize unicode strings
        # domain = unicodedata.normalize("NFKD", domain)
        domain = self.confusable.skeleton(domain)

        # strip off any aspect of a URL name
        parsed = urlsplit(domain)
        if parsed.scheme:
            return parsed.hostname

        return parsed.path

    @function("network_utilities_domain_distance")
    def _domain_distance_function(self, event, *args, **kwargs):
        """Function: Identifies similarity between domain names.
        """
        try:
            # Get the function parameters:
            domain_name = kwargs.get("network_utilities_domain_name")  # text
            domain_list = kwargs.get("network_utilities_domain_list")  # text

            log = logging.getLogger(__name__)
            log.info("domain_name: %s", domain_name)
            log.debug("domain_list: %s", domain_list)   # may be very long

            compare_domains = domain_list.split(",")
            results = {
                "domain_name": domain_name,
                "distances": {},
                "closest": {}
            }

            min_distance = None
            comp1 = self.normalize_name(domain_name)
            log.debug("normalized domain: %s", comp1)

            for compare in compare_domains:
                compp = compare.strip()
                comp2 = self.normalize_name(compare)
                dist = damerau_levenshtein_distance(comp1, comp2)
                results["distances"][compp] = dist

                if min_distance is None or dist < min_distance:
                    min_distance = dist
                    results["closest"] = {"name": compp, "distance": dist}

            log.info("closest: %s, distance %s", results["closest"]["name"], results["closest"]["distance"])

            # Produce a FunctionResult with the return value
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
