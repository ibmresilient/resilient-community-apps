# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_passivetotal"""


"""Generate a default configuration-file section for fn_passivetotal"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_passivetotal when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_passivetotal]
    passivetotal_api_key=
    passivetotal_username=
    passivetotal_base_url=https://api.passivetotal.org
    passivetotal_account_api_url=/v2/account
    passivetotal_actions_tags_api_url=/v2/actions/tags
    passivetotal_passive_dns_api_url=/v2/dns/passive
    passivetotal_actions_class_api_url=/v2/actions/classification
    passivetotal_enrich_subdom_api_url=/v2/enrichment/subdomains
    passivetotal_community_url=https://community.riskiq.com/search/
    passivetotal_tags=
    """
    return config_data
