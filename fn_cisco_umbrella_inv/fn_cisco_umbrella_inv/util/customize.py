# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_cisco_umbrella_inv"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_cisco_umbrella_inv package
    """
    return {
        "package": u"fn_cisco_umbrella_inv",
        "message_destinations": [
            u"umbrella_investigate"
        ],
        "functions": [
            u"umbrella_classifiers",
            u"umbrella_dns_rr_hist",
            u"umbrella_domain_co_occurrences",
            u"umbrella_domain_related_domains",
            u"umbrella_domain_security_info",
            u"umbrella_domain_status_and_category",
            u"umbrella_domain_volume",
            u"umbrella_domain_whois_info",
            u"umbrella_ip_as_info",
            u"umbrella_ip_latest_malicious_domains",
            u"umbrella_pattern_search",
            u"umbrella_threat_grid_sample",
            u"umbrella_threat_grid_samples",
            u"umbrella_timeline"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"umbinv_as_for_an_ip_or_asn",
            u"umbinv_categories_for_a_domain",
            u"umbinv_category_identifiers",
            u"umbinv_classifiers_for_a_domain",
            u"umbinv_dns_rr_history_domain",
            u"umbinv_dns_rr_history_ip",
            u"umbinv_domain_co_occurrences",
            u"umbinv_domain_security_info",
            u"umbinv_domain_volume",
            u"umbinv_domain_whois_info_domain",
            u"umbinv_latest_malicious_domains_for_an_ip",
            u"umbinv_pattern_search_start_epoch",
            u"umbinv_pattern_search_start_relative",
            u"umbinv_related_domains_for_a_domain",
            u"umbinv_thread_grid_sample_info_for_a_hash_basic",
            u"umbinv_thread_grid_samples_for_a_resource",
            u"umbinv_timeline_for_a_resource"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"cisco_umbrella_inv_as_information_for_an_ip_address_or_asn",
            u"cisco_umbrella_inv_categories_for_a_domain",
            u"cisco_umbrella_inv_cooccurrences_for_a_domain",
            u"cisco_umbrella_inv_domain_volume",
            u"cisco_umbrella_inv_domain_whois_information_for_a_domain",
            u"cisco_umbrella_inv_pattern_search_start_epoch",
            u"cisco_umbrella_inv_related_domains_for_a_domain",
            u"cisco_umbrella_inv_security_information_for_a_domain",
            u"cisco_umbrella_inv_threadgrid_sample_information_for_a_hash",
            u"cisco_umbrella_inv_threadgrid_samples_for_a_resource",
            u"cisco_umbrella_inv_timeline_for_a_resource"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - umbrella_investigate
    - Functions:
        - umbrella_classifiers
        - umbrella_dns_rr_hist
        - umbrella_domain_co_occurrences
        - umbrella_domain_related_domains
        - umbrella_domain_security_info
        - umbrella_domain_status_and_category
        - umbrella_domain_volume
        - umbrella_domain_whois_info
        - umbrella_ip_as_info
        - umbrella_ip_latest_malicious_domains
        - umbrella_pattern_search
        - umbrella_threat_grid_sample
        - umbrella_threat_grid_samples
        - umbrella_timeline
    - Playbooks:
        - cisco_umbrella_inv_as_information_for_an_ip_address_or_asn
        - cisco_umbrella_inv_categories_for_a_domain
        - cisco_umbrella_inv_cooccurrences_for_a_domain
        - cisco_umbrella_inv_domain_volume
        - cisco_umbrella_inv_domain_whois_information_for_a_domain
        - cisco_umbrella_inv_pattern_search_start_epoch
        - cisco_umbrella_inv_related_domains_for_a_domain
        - cisco_umbrella_inv_security_information_for_a_domain
        - cisco_umbrella_inv_threadgrid_sample_information_for_a_hash
        - cisco_umbrella_inv_threadgrid_samples_for_a_resource
        - cisco_umbrella_inv_timeline_for_a_resource
    - Data Tables:
        - umbinv_as_for_an_ip_or_asn
        - umbinv_categories_for_a_domain
        - umbinv_category_identifiers
        - umbinv_classifiers_for_a_domain
        - umbinv_dns_rr_history_domain
        - umbinv_dns_rr_history_ip
        - umbinv_domain_co_occurrences
        - umbinv_domain_security_info
        - umbinv_domain_volume
        - umbinv_domain_whois_info_domain
        - umbinv_latest_malicious_domains_for_an_ip
        - umbinv_pattern_search_start_epoch
        - umbinv_pattern_search_start_relative
        - umbinv_related_domains_for_a_domain
        - umbinv_thread_grid_sample_info_for_a_hash_basic
        - umbinv_thread_grid_samples_for_a_resource
        - umbinv_timeline_for_a_resource
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)