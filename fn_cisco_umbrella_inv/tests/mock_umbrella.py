# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate Mock responses to simulate Cisco Umbrella Investigate fro Unix tests """
import re

RESPONSES = dict(dns_rr_hist_ip={u'rrs': [{u'ttl': 3600, u'type': u'A', u'class': u'IN', u'rr': u'dual46.gp1.wac.v2cdn.net.', u'name': u'93.184.216.119'},
                                          {u'ttl': 86400, u'type': u'A', u'class': u'IN', u'rr': u'mail.funken-flug.com.', u'name': u'93.184.216.119'}],
                                 u'features': {u'div_ld2_2': 0.7619047619047619, u'div_ld2_1': 0.3333333333333333, u'div_ld3': 0.7619047619047619,
                                            u'div_ld2': 0.3333333333333333, u'ld2_1_count': 7, u'ld2_count': 7, u'rr_count': 21, u'ld3_count': 16,
                                            u'ld2_2_count': 16}
                },
                dns_rr_hist_domain={u'features': {u'geo_distance_mean': 0.0, u'locations': [{u'lat': 42.15080261230469, u'lon': -70.82279968261719}],
                                          u'rips': 1, u'is_subdomain': False, u'prefixes': [u'93.184.216.0'], u'non_routable': False,
                                          u'ff_candidate': False, u'base_domain': u'example.com', u'ttls_min': 86400, u'country_codes': [u'US'],
                                          u'rips_stability': 1.0, u'ttls_max': 86400, u'ttls_stddev': 0.0, u'prefixes_count': 1, u'mail_exchanger': False,
                                          u'geo_distance_sum': 0.0, u'asns_count': 1, u'country_count': 1, u'ttls_median': 86400.0, u'age': 92,
                                          u'asns': [15133], u'div_rips': 1.0, u'cname': False, u'ttls_mean': 86400.0, u'locations_count': 1},
                                    u'rrs_tf': [{u'first_seen': u'2018-01-04', u'rrs': [{u'ttl': 86400, u'type': u'A', u'class': u'IN', u'rr': u'93.184.216.34',
                                                 u'name': u'example.com.'}], u'last_seen': u'2018-04-05'}]
                },
                domain_co_occurrences={ u'found': True, u'domain_name': u'googlevideo.com',
                                        u'pfs2': [[u'gowatchfreemovies.to', 0.14300200812663327],
                                                  [u'www.mc-skv.com', 0.12482579576302438],
                                                  [u'r5---sn-n4v7sn7l.googlevideo.com', 0.0064511764392265955],
                                                  [u'sage200.co.uk', 0.006262067692875829],
                                                  [u'demon.co.uk', 0.005126508408778887]]
                },
                domain_security_info = {u'geodiversity_normalized': [[u'??', 0.5554201725159715], [u'DZ', 0.00018227600641865165]],
                           u'geodiversity': [[u'US', 0.4624],[u'LK', 0.0001]],
                           u'dga_score': 0.0, u'rip_score': 0.0, u'asn_score': -0.03238785566453197, u'securerank2': 100.0,
                           u'popularity': 100.0, u'geoscore': 0.0, u'ks_test': 0.0, u'attack': u'', u'pagerank': 40.09394,
                           u'entropy': 2.521640636343318, u'prefix_score': 0.0, u'perplexity': 0.2327827581680193,
                           u'found': True, u'fastflux': False, u'threat_type': u'', u'tld_geodiversity': []
                },
                domain_status_and_category_cat =  {"133": u'Safe for Kids',
                               "132": u'SaaS and B2B',
                               "131": u'Real Estate',
                               "130": u'Professional Networking',
                               "137": u'Society and Culture',
                               "141": u'Organisation Email'
                },
                domain_status_and_category_dom = {u'amazon.com': {u'status': 1,
                                                                  u'content_categories': [u'Ecommerce/Shopping'],
                                                                  u'security_categories': []
                                                                 }
                },
                ip_latest_malicious_domains = [
                    {
                        u'id': 22842894,
                        u'name': u'www.cxhyly.com',
                    },
                    {
                        u'id': 22958747,
                        u'name': u'cxhyly.com'
                    }
                ],
                umbrella_pattern_search = {u'matches': [{u'securityCategories': [], u'firstSeen': 1521407460000, u'name': u'paypal.com-webcsr.me',
                                                         u'firstSeenISO': u'2018-03-18T21:11:00.000Z'}, {u'securityCategories': [],
                                                         u'firstSeen': 1521167520000, u'name': u'paypalz.co.uk.userwww.bbmno2i54b0.hartleyformz.com',
                                                         u'firstSeenISO': u'2018-03-16T02:32:00.000Z'}],
                                                         u'limit': 10, u'totalResults': 10, u'expression': u'paypal.*', u'moreDataAvailable': True
                },
                timeline = [{u'threatTypes': [],
                             u'timestamp_converted': u'2017-06-14 23:21:34',
                             u'attacks': [],
                             u'timestamp': 1497478894605,
                             u'source': u'googlevideo.com',
                             u'categories': []}
                ]
)

def mocked_response(*args, **kwargs):

    """Function will be used by the mock to replace investigate.Investigate.get"""

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            pass

    if re.search("^dnsdb\/ip\/.+\/.+\.json", args[0]):
        return MockResponse(RESPONSES["dns_rr_hist_ip"], 200)
    elif re.search("^dnsdb\/name\/.+\/.+\.json", args[0]):
        return MockResponse(RESPONSES["dns_rr_hist_domain"], 200)
    elif re.search("^recommendations\/name\/.+\.json", args[0]):
        return MockResponse(RESPONSES["domain_co_occurrences"], 200)
    elif re.search("^security\/name\/.+\.json", args[0]):
        return MockResponse(RESPONSES["domain_security_info"], 200)
    elif re.search("^domains\/categories\/", args[0]):
        return MockResponse(RESPONSES["domain_status_and_category_cat"], 200)
    elif re.search("^domains\/categorization\/", args[0]):
        return MockResponse(RESPONSES["domain_status_and_category_dom"], 200)
    elif re.search("^ips\/.+\/latest_domains", args[0]):
        return MockResponse(RESPONSES["ip_latest_malicious_domains"], 200)
    elif re.search("^search\/", args[0]):
        return MockResponse(RESPONSES["umbrella_pattern_search"], 200)
    elif re.search("^timeline/", args[0]):
        return MockResponse(RESPONSES["timeline"], 200)
    return MockResponse(None, 404)