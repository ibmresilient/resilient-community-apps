# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Generate Mock responses to simulate Cisco Umbrella Investigate for Unix tests """

PACKAGE_NAME = "fn_cisco_umbrella_inv"
whois_history_return = [
    {
        "administrativeContactFax": "",
        "whoisServers": "",
        "addresses": [
            "1600 amphitheatre parkway",
            "please contact contact-admin@google.com, 1600 amphitheatre parkway",
            "2400 e. bayshore pkwy"
        ],
        "administrativeContactName": "DNS Admin",
        "zoneContactEmail": "",
        "billingContactFax": "",
        "administrativeContactTelephoneExt": "",
        "administrativeContactEmail": "dns-admin@google.com",
        "technicalContactEmail": "dns-admin@google.com",
        "technicalContactFax": "16506181499",
        "nameServers": [
            "ns1.google.com",
            "ns2.google.com",
            "ns3.google.com",
            "ns4.google.com"
        ],
        "zoneContactName": "",
        "billingContactPostalCode": "",
        "zoneContactFax": "",
        "registrantTelephoneExt": "",
        "zoneContactFaxExt": "",
        "technicalContactTelephoneExt": "",
        "billingContactCity": "",
        "zoneContactStreet": [],
        "created": "",
        "administrativeContactCity": "Mountain View",
        "registrantName": "Dns Admin",
        "zoneContactCity": "",
        "domainName": "google.com",
        "zoneContactPostalCode": "",
        "administrativeContactFaxExt": "",
        "technicalContactCountry": "UNITED STATES",
        "registrarIANAID": "292",
        "updated": "2011-07-20 00:00:00 UTC",
        "administrativeContactStreet": [
            "1600 amphitheatre parkway"
        ],
        "billingContactEmail": "",
        "status": [
            "clientDeleteProhibited",
            "clientTransferProhibited",
            "clientUpdateProhibited",
            "serverDeleteProhibited",
            "serverTransferProhibited",
            "serverUpdateProhibited"
        ],
        "registrantCity": "Mountain View",
        "billingContactCountry": "",
        "expires": "2020-09-14 00:00:00 UTC",
        "technicalContactStreet": [ "2400 e. bayshore pkwy" ],
        "registrantOrganization": "Google Inc.",
        "billingContactStreet": [],
        "registrarName": "MARKMONITOR INC.",
        "registrantPostalCode": "94043",
        "zoneContactTelephone": "",
        "registrantEmail": "dns-admin@google.com",
        "technicalContactFaxExt": "",
        "technicalContactOrganization": "Google Inc.",
        "emails": [ "dns-admin@google.com" ],
        "registrantStreet": [
            "please contact contact-admin@google.com",
            "1600 amphitheatre parkway"
        ],
        "technicalContactTelephone": "16503300100",
        "technicalContactState": "CA",
        "technicalContactCity": "Mountain View",
        "registrantFax": "16506188571",
        "registrantCountry": "UNITED STATES",
        "billingContactFaxExt": "",
        "timestamp": 0,
        "zoneContactOrganization": "",
        "administrativeContactCountry": "UNITED STATES",
        "billingContactName": "",
        "registrantState": "CA",
        "registrantTelephone": "16502530000",
        "administrativeContactState": "CA",
        "registrantFaxExt": "",
        "technicalContactPostalCode": "94043",
        "rawBase64": "",
        "zoneContctTelephoneExt": "",
        "administrativeContactOrganization": "Google Inc.",
        "billingContactTelephone": "",
        "billingContactTelephoneExt": "",
        "zoneContactState": "",
        "administrativeContactTelephone": "16506234000",
        "billingContactOrganization": "",
        "technicalContactName": "DNS Admin",
        "administrativeContactPostalCode": "94043",
        "zoneContactCountry": "",
        "billingContactState": ""
    }
]
categorization_return = {
    "amazon.com": {
        "status": 1,
        "security_categories": [ "150" ],
        "content_categories": [ "8" ]
    }
}
cooccurrences_return = {
    "pfs2": [
        "download.example.com",
        "query.example.com"
    ],
    "found": True
}
related_return = {
    "tb1": [
        {
            "domain": "www.example1.com",
            "score": 10
        },
        {
            "domain": "info.example2.com",
            "score": 9
        },
        {
            "domain": "support.example.com",
            "score": 3
        }
    ],
    "found": True
}
security_return = {
    "dga_score": 38.301771886101335,
    "perplexity": 0.4540313302593146,
    "entropy": 2.5216406363433186,
    "securerank2": -1.3135141095601992,
    "pagerank": 0.0262532,
    "asn_score": -29.75810625887133,
    "prefix_score": -64.9070502788884,
    "rip_score": -75.64720536038982,
    "popularity": 25.335450495507196,
    "geodiversity": [ 0.24074075, 0.018518519 ],
    "geodiversity_normalized": [
        0.3761535390278368,
        0.0005015965168831449
    ],
    "tld_geodiversity": [ 0 ],
    "geoscore": 0,
    "ks_test": 0,
    "attack": "",
    "threat_type": "",
    "found": True
}
whois_email_return = {
    "totalResults": 500,
    "moreDataAvailable": True,
    "limit": 500,
    "sortField": "updated",
    "domains": [
        {
            "domain": "0emm.com",
            "current": True
        },
        {
            "domain": "10tothe100.net",
            "current": True
        },
        {
            "domain": "youtubube.com",
            "current": True
        },
        {
            "domain": "zagat.net",
            "current": True
        },
        {
            "domain": "zagatnyc.com",
            "current": True
        },
        {
            "domain": "zavers.com",
            "current": True
        }
    ]
}
whois_nameserver_return = {
    "totalResults": 500,
    "moreDataAvailable": True,
    "limit": 500,
    "sortField": "updated",
    "domains": [
        {
            "domain": "46645.biz",
            "current": True
        },
        {
            "domain": "800google411.net",
            "current": True
        },
        {
            "domain": "zagatnyc.com",
            "current": True
        },
        {
            "domain": "zavers.com",
            "current": True
        }
    ]
}
search_return = {
    "expression": "exa[a-z]ple.com",
    "totalResults": 1,
    "moreDataAvailable": False,
    "limit": 1000,
    "matches": [
        {
            "name": "example",
            "firstSeen": 1432330927421,
            "firstSeenISO": "2015-05-22T21:42:07.421Z",
            "securityCategories": [ "Botnet" ]
        }
    ]
}
samples_return = {
    "query": "google.com",
    "totalResults": 10,
    "moreDataAvailable": True,
    "limit": 10,
    "offset": 0,
    "samples": [
        {
            "sha256": "e9d3470c37dada28d5a32fb53a243c5b20def35bb01abf8f5403182cc2b91fdd",
            "sha1": "de182fdcc3c0d473b90a0df0ad14c2074d1e7c50",
            "md5": "282f80e8a2cf9e0e0dd72093787d99c6",
            "magicType": "PE32 executable (GUI) Intel 80386, for MS Windows",
            "threatScore": 100,
            "size": 192512,
            "firstSeen": 1460108539000,
            "lastSeen": 1460108539000,
            "visible": True,
            "avresults": [
                {
                    "signature": "Win.Trojan.Ramnit",
                    "product": "ClamAV"
                },
                {
                    "signature": "Win.Trojan.Parite",
                    "product": "ClamAV"
                }
            ]
        }
    ]
}
sample_artifact_return = {
    "totalResults": 10,
    "moreDataAvailable": True,
    "limit": 100,
    "offset": 0,
    "artifacts": [
        {
            "sha256": "fd6c69c345f1e32924f0a5bb7393e191b393a78d58e2c6413b03ced7482f2320",
            "sha1": "b4fa74a6f4dab3a7ba702b6c8c129f889db32ca6",
            "md5": "ff5e1f27193ce51eec318714ef038bef",
            "magicType": "PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed",
            "size": 56320,
            "firstSeen": 1460108539000,
            "lastSeen": 1460108539000,
            "visible": False,
            "avresults": [
                {
                    "signature": "Win.Trojan.Ramnit",
                    "product": "ClamAV"
                },
                {
                    "signature": "Win.Trojan.Parite",
                    "product": "ClamAV"
                }
            ]
        }
    ],
    "samples": []
}
sample_connections_return = {
    "totalResults": 2,
    "moreDataAvailable": True,
    "limit": 2,
    "offset": 0,
    "connections": [
        {
            "name": "google.com",
            "firstSeen": 1456268452000,
            "lastSeen": 1456268452000,
            "securityCategories": [ "Botnet", "Malware" ],
            "attacks": [],
            "threatTypes": [],
            "type": "HOST",
            "ips": [ "172.217.1.78" ],
            "urls": [
                "http://goo.gl/PDIfV"
            ]
        },
        {
            "name": "rtvwerjyuver.com",
            "firstSeen": 1456268452000,
            "lastSeen": 1456268452000,
            "securityCategories": [ "Botnet", "Malware" ],
            "attacks": [],
            "threatTypes": [],
            "type": "HOST",
            "ips": [],
            "urls": []
        }
    ]
}
sample_return = {
    "sha256": "e9d3470c37dada28d5a32fb53a243c5b20def35bb01abf8f5403182cc2b91fdd",
    "sha1": "de182fdcc3c0d473b90a0df0ad14c2074d1e7c50",
    "md5": "282f80e8a2cf9e0e0dd72093787d99c6",
    "magicType": "PE32 executable (GUI) Intel 80386, for MS Windows",
    "threatScore": 100,
    "size": 192512,
    "firstSeen": 1460108539000,
    "lastSeen": 1460108539000,
    "visible": True,
    "avresults": [
        {
            "signature": "Win.Trojan.Ramnit",
            "product": "ClamAV"
        },
        {
            "signature": "Win.Trojan.Parite",
            "product": "ClamAV"
        }
    ]
}
bgp_routes_ip_return = {
    "creation_date": "2002-08-01",
    "ir": 2,
    "description": "CHINANET-BACKBONE No.31,Jin-rong Street,CN 86400",
    "asn": "4134",
    "cidr": "123.172.0.0/15"
}
bgp_routes_asn_return = {
    "cidr": [ "98.143.32.0/20" ],
    "geo": {
        "name": "United States",
        "id": 10
    }
}
timeline_return = [
    {
        "categories": [ "Malware" ],
        "attacks": [ "Trojan" ],
        "threatTypes": [],
        "timestamp": 1561574807853
    },
    {
        "categories": [ "8", "150" ],
        "attacks": [ "Trojan" ],
        "threatTypes": [],
        "timestamp": 1559545774604
    }
]
domains_volume_return = {
    "dates": [
        "1510873200000",
        "1510959600000"
    ],
    "queries": [
        "1378426",
        "1361934",
        "1308188",
        "1238823",
        "1245126",
        "1215994",
        "1256917",
        "1200190",
        "1245963",
        "1355719",
        "1332685",
        "1319825",
        "1362464",
        "1457174",
        "1695448"
    ]
}
sample_behaviors_return = {
    "totalResults": 2,
    "moreDataAvailable": True,
    "limit": 2,
    "offset": 0,
    "behaviors": [
        {
            "name": "pe-packed-upx",
            "title": "Executable Packed with UPX",
            "hits": 2,
            "confidence": 30,
            "severity": 30,
            "tags": [
                "packer",
                "crypter",
                "encoding",
                "PE"
            ],
            "threat": 9,
            "category": [ "attribute" ]
        },
        {
            "name": "pe-header-timestamp-null",
            "title": "PE COFF Header Timestamp is Not Set",
            "hits": 2,
            "confidence": 60,
            "severity": 5,
            "tags": [
                "file",
                "attributes",
                "anomaly",
                "PE"
            ],
            "threat": 3,
            "category": [ "attribute" ]
        }
    ]
}

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
                domain_status_and_category_cat =  {"133": u'Safe for Kids',
                               "132": u'SaaS and B2B',
                               "131": u'Real Estate',
                               "130": u'Professional Networking',
                               "137": u'Society and Culture',
                               "141": u'Organisation Email'
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
                timeline = [{u'threatTypes': [],
                             u'timestamp_converted': u'2017-06-14 23:21:34',
                             u'attacks': [],
                             u'timestamp': 1497478894605,
                             u'source': u'googlevideo.com',
                             u'categories': []}
                ],
                umbrella_classifiers_classifiers = {u'securityCategories': [u'Malware'],
                                                    u'attacks': [u'Neutrino'],
                                                    u'threatTypes': [u'Exploit Kit']
                },
                umbrella_classifiers_info = {
                    u'firstQueried': 1479496560000
                },
)

def mock_client():
    class MockClient(object):
        """ Create mock connection """

        def __init__(self, options=None, rc=None) -> None:
            """ Mock """
            pass

        def make_api_call(self, method: str=None, uri: str=None, params: dict=None, data: dict=None):
            """ Mock make API call """
            if "domains/categorization" in uri:
                return categorization_return
            elif "recommendations/name/" in uri:
                return cooccurrences_return
            elif "dnsdb/name/" in uri:
                return RESPONSES.get("dns_rr_hist_domain")
            elif "dnsdb/ip/" in uri:
                return RESPONSES.get("dns_rr_hist_ip")
            elif "/latest_domains" in uri:
                return RESPONSES.get("ip_latest_malicious_domains")
            elif "links/name/" in uri:
                return related_return
            elif "security/name/" in uri:
                return security_return
            elif "whois/emails/" in uri:
                return whois_email_return
            elif "whois/nameservers/" in uri:
                return whois_nameserver_return
            elif "/history" in uri:
                return whois_history_return
            elif "search/" in uri:
                return search_return
            elif "samples/" in uri:
                return samples_return
            elif "/artifacts" in uri:
                return sample_artifact_return
            elif "/connections" in uri:
                return sample_connections_return
            elif "/behaviors" in uri:
                return sample_behaviors_return
            elif "sample/" in uri:
                return sample_return
            elif "bgp_routes/ip/" in uri:
                return bgp_routes_ip_return
            elif "bgp_routes/asn/" in uri:
                return bgp_routes_asn_return
            elif "timeline/" in uri:
                return timeline_return
            elif "domains/volume/" in uri:
                return domains_volume_return
            elif "domains/categories/" in uri:
                return RESPONSES.get("domain_status_and_category_cat")
            elif "/classifiers" in uri:
                return RESPONSES.get("umbrella_classifiers_classifiers")
            elif "/info" in uri:
                return RESPONSES.get("umbrella_classifiers_info")
            else:
                return {}

    return MockClient()
