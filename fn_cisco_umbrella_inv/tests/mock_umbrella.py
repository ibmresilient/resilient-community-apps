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
                ],
                umbrella_classifiers_classifiers = {u'securityCategories': [u'Malware'],
                                                    u'attacks': [u'Neutrino'],
                                                    u'threatTypes': [u'Exploit Kit']
                },
                umbrella_classifiers_info = {
                    u'firstQueried': 1479496560000
                },
                umbrella_related_domains = {u'tb1': [[u'www.domain.com', 8],
                                            [u'secure.statcounter.com', 4],
                                            [u'static.addtoany.com', 4],
                                            [u'image.tmdb.org', 3],
                                            [u'0.gravatar.com', 3],
                                            [u'1.gravatar.com', 3],
                                            [u'2.gravatar.com', 3],
                                            [u'api.bltd.ovh', 3],
                                            [u'static.vnpt.vn', 3]],
                                  u'found': True
                },
                umbrella_domain_volume = {u'dates': [1524589200000, 1524679200000],
                                          u'queries': [2610011, 2576588, 2518676, 2361999, 2161170, 1992158, 1835777, 1847458, 1809848,
                                                       1791200, 1784312, 1776649, 1830100, 1939211, 2023009, 2075916, 2042269, 2065889,
                                                       2137081, 2442077, 2618018, 2690130, 2726822, 2650116, 0, 0]
                },
                umbrella_domain_whois_info_domain = {u'registrantFaxExt': None, u'administrativeContactPostalCode': u'95134',
                          u'zoneContactCity': None, u'addresses': [u'170 w. tasman drive', u'170 west tasman drive'],
                          u'billingContactState': None, u'technicalContactStreet': [u'170 w. tasman drive'],
                          u'auditUpdatedDate': u'2018-04-22 20:55:22.000 UTC', u'administrativeContactCity': u'San Jose',
                          u'administrativeContactEmail': u'infosec@cisco.com', u'technicalContactFax': u'14085267373',
                          u'technicalContactTelephone': u'14085279223', u'billingContactEmail': None,
                          u'technicalContactPostalCode': u'95134', u'registrantOrganization': u'Cisco Technology Inc.',
                          u'zoneContactPostalCode': None, u'registrantState': u'CA',
                          u'administrativeContactName': u'Info Sec', u'billingContactFaxExt': None,
                          u'billingContactCity': None, u'technicalContactEmail': u'dns-info@CISCO.COM',
                          u'registrantCountry': u'UNITED STATES', u'technicalContactFaxExt': None,
                          u'registrantName': u'Info Sec', u'registrantEmail': u'infosec@cisco.com',
                          u'billingContactCountry': None, u'billingContactName': None,
                          u'registrarName': u'CSC CORPORATE DOMAINS, INC.', u'technicalContactTelephoneExt': None,
                          u'administrativeContactFax': None, u'zoneContactFax': None, u'zoneContactFaxExt': None,
                          u'registrantCity': u'San Jose', u'administrativeContactTelephoneExt': None,
                          u'status': [u'clientTransferProhibited serverDeleteProhibited serverTransferProhibited serverUpdateProhibited'],
                          u'updated': u'2017-05-11', u'expires': u'2018-05-15', u'whoisServers': u'whois.corporatedomains.com',
                          u'zoneContactEmail': None, u'technicalContactState': u'CA',
                          u'nameServers': [u'ns1.cisco.com', u'ns2.cisco.com', u'ns3.cisco.com'], u'timestamp': None,
                          u'recordExpired': False, u'registrantFax': u'14085264575',
                          u'administrativeContactStreet': [u'170 west tasman drive'],
                          u'registrantTelephoneExt': None, u'billingContactFax': None,
                          u'technicalContactOrganization': u'Cisco Technology Inc.',
                          u'administrativeContactState': u'CA', u'zoneContactOrganization': None,
                          u'billingContactPostalCode': None, u'zoneContactStreet': [],
                          u'zoneContactName': None, u'registrantPostalCode': u'95134',
                          u'billingContactTelephone': None, u'emails': [u'dns-info@cisco.com', u'infosec@cisco.com'],
                          u'registrantTelephone': u'14085273842', u'administrativeContactCountry': u'UNITED STATES',
                          u'technicalContactCity': u'San Jose', u'administrativeContactTelephone': u'14085273842',
                          u'created': u'1987-05-14', u'registrantStreet': [u'170 west tasman drive'],
                          u'domainName': u'cisco.com', u'technicalContactCountry': u'UNITED STATES',
                          u'billingContactStreet': [], u'timeOfLatestRealtimeCheck': 1524501072693, u'zoneContactState': None,
                          u'administrativeContactOrganization': u'Cisco Technology Inc.', u'administrativeContactFaxExt': None,
                          u'billingContactTelephoneExt': None, u'zoneContactTelephone': None, u'technicalContactName':
                          u'Network Services', u'zoneContactTelephoneExt': None, u'billingContactOrganization': None,
                          u'registrarIANAID': u'299', u'zoneContactCountry': None, u'hasRawText': True
                },
                umbrella_domain_whois_info_emails = {u'test@example.com': {u'sortField': u'created',
                                                                       u'limit': 2, u'moreDataAvailable': True,
                                                                       u'offset': 0, u'domains': [{u'current': True, u'domain': u'ev-dragon.com'}],
                                                     u'totalResults': 1
                                                    }
                },
                umbrella_domain_whois_info_ns = {u'ns1.google.com': {u'sortField': u'created',
                                                                         u'limit': 2,
                                                                         u'moreDataAvailable': True,
                                                                         u'offset': 0,
                                                                         u'domains': [{u'current': True,
                                                                                       u'domain': u'blogspot.jp'}],
                                                                         u'totalResults': 1
                                                                         }
                },
                umbrella_ip_as_info_ip_address = [{u'description': u'EDGECAST - MCI Communications Services, Inc. d/b/a Verizon Business, US 86400',
                                                   u'cidr': u'93.184.216.0/24',
                                                   u'ir': 3,
                                                   u'asn': 15133,
                                                   u'creation_date': u'2007-03-19'}
                ],
                umbrella_ip_as_info_asn = [{u'cidr': u'212.47.32.0/19',
                                            u'geo': {u'country_name': u'Italy',
                                                     u'country_code': u'IT'
                                                    }
                                           }
                ],
                umbrella_threat_grid_sample_basic = { u'magicType': u'PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows',
                                                      u'behaviors': [{u'category': [u'file'],
                                                                u'hits': 1,
                                                                u'severity': 90,
                                                                u'title': u'Process Modified a File in a System Directory',
                                                                u'tags': [u'executable', u'file', u'process'],
                                                                u'confidence': 100,
                                                                u'threat': 90,
                                                                u'name': u'modified-file-in-system-dir'}
                                                            ],
                                                      u'sha1': u'00bf659061121200c1e5469fbe31d100418b149e',
                                                      u'size': 228864,
                                                      u'threatScore': 100,
                                                      u'connections': {u'connections': [{  u'threatTypes': [],
                                                                                        u'popularity1Month': None,
                                                                                        u'name': u'195.22.28.198',
                                                                                        u'attacks': [],
                                                                                        u'popularity3Month': None,
                                                                                        u'popularity': None,
                                                                                        u'firstQueried': None,
                                                                                        u'popularityWeek': None,
                                                                                        u'securityCategories': [],
                                                                                        u'ips': [],
                                                                                        u'lastCommit': None,
                                                                                        u'urls': [], u'type': u'IP',
                                                                                        u'firstSeen': 1460762759000,
                                                                                        u'lastSeen': 1460762759000
                                                                                     }
                                                                                    ],
                                                                       u'totalResults': 5,
                                                                       u'limit': 5,
                                                                       u'moreDataAvailable': True,
                                                                       u'offset': 0
                                                                      },
                                                                      u'visible': True,
                                                                      u'lastSeen': 1460762759000,
                                                                      u'samples': {u'totalResults': 0,
                                                                                   u'limit': 5,
                                                                                   u'moreDataAvailable': False,
                                                                                   u'samples': [], u'offset': 0
                                                                                  },
                                                      u'sha256': u'414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c',
                                                      u'avresults': [],
                                                      u'firstSeen': 1460762759000,
                                                      u'md5': u'6d8b70d20b1182546bc58ce7f90549d7'
                 },
                 umbrella_threat_grid_sample_samples = {  u'totalResults': 2,
                                                          u'limit': 2,
                                                          u'moreDataAvailable': True,
                                                          u'samples': [{u'magicType': u'PE32 executable (GUI) Intel 80386, for MS Windows',
                                                                        u'behaviors': [],
                                                                        u'direction': u'IN',
                                                                        u'sha1': u'6d33e9091193b24cef05a6f1b4d7a8ae92dd530a',
                                                                        u'size': 103424,
                                                                        u'threatScore': 90,
                                                                        u'visible': True,
                                                                        u'lastSeen': 1461433810000,
                                                                        u'sha256': u'f73322d64517785b6ce41523882e3b03ff8c77704302a6282a90f2bfc14abbef',
                                                                        u'avresults': [],
                                                                        u'firstSeen': 1461433810000,
                                                                        u'md5': u'be036d05dd75e65561d961b84ca42253'
                                                                        },
                                                                       {
                                                                        u'magicType': u'PE32 executable (GUI) Intel 80386, for MS Windows',
                                                                        u'behaviors': [],
                                                                        u'direction': u'IN',
                                                                        u'sha1': u'2daa7d45e9ff11c830dc33df002648f6afbcd6e3',
                                                                        u'size': 534308,
                                                                        u'threatScore': 24,
                                                                        u'visible': True,
                                                                        u'lastSeen': 1462230655000,
                                                                        u'sha256': u'bb36f5fa0519bcfc82bb180187b9d47621634c71a19796831c87148ceb3b364c',
                                                                        u'avresults': [],
                                                                        u'firstSeen': 1462230655000,
                                                                        u'md5': u'af3d619e1419b293c499e671a3da5b8e'
                                                                       }
                                                                      ],
                                                          u'offset': 0
                 },
                 umbrella_threat_grid_sample_behaviors = [{u'category': [u'persistence'],
                                                          u'hits': 1,
                                                          u'severity': 80,
                                                          u'title': u'Process Modified Autorun Registry Key Value',
                                                          u'tags': [u'process', u'autorun', u'registry'],
                                                          u'confidence': 60,
                                                          u'threat': 48,
                                                          u'name': u'registry-autorun-key-modified'
                                                         },
                                                         {u'category': [u'forensics'],
                                                           u'hits': 200,
                                                           u'severity': 80,
                                                           u'title': u'Artifact Flagged by Antivirus',
                                                           u'tags': [u'file'],
                                                           u'confidence': 90,
                                                           u'threat': 72,
                                                           u'name': u'antivirus-flagged-artifact'
                                                         }
                 ],
                 umbrella_threat_grid_sample_connections = {u'connections': [{u'threatTypes': [],
                                                                              u'popularity1Month': None,
                                                                              u'name': u'16.126.17.103',
                                                                              u'attacks': [],
                                                                              u'popularity3Month': None,
                                                                              u'popularity': None,
                                                                              u'firstQueried': None,
                                                                              u'popularityWeek': None,
                                                                              u'securityCategories': [],
                                                                              u'ips': [],
                                                                              u'lastCommit': None,
                                                                              u'urls': [],
                                                                              u'type': u'IP',
                                                                              u'firstSeen': 1503550227000,
                                                                              u'lastSeen': 1503550227000
                                                                             },
                                                                             {u'threatTypes': [],
                                                                              u'popularity1Month': None,
                                                                              u'name': u'207.71.100.129',
                                                                              u'attacks': [],
                                                                              u'popularity3Month': None,
                                                                              u'popularity': None,
                                                                              u'firstQueried': None,
                                                                              u'popularityWeek': None,
                                                                              u'securityCategories': [],
                                                                              u'ips': [],
                                                                              u'lastCommit': None,
                                                                              u'urls': [],
                                                                              u'type': u'IP',
                                                                              u'firstSeen': 1503550227000,
                                                                              u'lastSeen': 1503550227000
                                                                             }
                                                                            ],
                                                            u'totalResults': 2,
                                                            u'limit': 2,
                                                            u'moreDataAvailable': True,
                                                            u'offset': 0
                 },

                 umbrella_threat_grid_samples = {u'limit': 2,
                                                u'moreDataAvailable': True,
                                                u'samples': [{u'magicType': u'PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed',
                                                                u'behaviors': [],
                                                                u'sha1': u'ccdeb2319d6b924e359f563527404a0af3d1ac54',
                                                                u'size': 22020, u'threatScore': 100,
                                                                u'visible': False, u'lastSeen': 1518410873000,
                                                                u'sha256': u'65f33f9e6d16918ba72bc20bcd85ebd75bc735df5666a843cab9c6dec9c0b1c1',
                                                                u'avresults': [{u'product': u'ClamAV', u'signature': u'Win.Worm.Mydoom'}],
                                                                u'firstSeen': 1518410872000, u'md5': u'0c340a220817e157346bef7976a0d0b6'},
                                                            ],
                                                u'offset': 0,
                                                u'query': u'cisco.com', u'totalResults': 2
                 }
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
    elif re.search("^url\/.+\/classifiers", args[0]):
        return MockResponse(RESPONSES["umbrella_classifiers_classifiers"], 200)
    elif re.search("^url\/.+\/info", args[0]):
        return MockResponse(RESPONSES["umbrella_classifiers_info"], 200)
    elif re.search("^links\/name\/.+\.json", args[0]):
        return MockResponse(RESPONSES["umbrella_related_domains"], 200)
    elif re.search("^domains\/volume\/", args[0]):
        return MockResponse(RESPONSES["umbrella_domain_volume"], 200)
    elif re.search("^whois\/emails\/", args[0]):
        return MockResponse(RESPONSES["umbrella_domain_whois_info_emails"], 200)
    elif re.search("^whois\/nameservers\/", args[0]):
        return MockResponse(RESPONSES["umbrella_domain_whois_info_ns"], 200)
    elif re.search("^whois\/", args[0]):
        return MockResponse(RESPONSES["umbrella_domain_whois_info_domain"], 200)
    elif re.search("^bgp_routes\/ip\/.+\/.+\.json", args[0]):
        return MockResponse(RESPONSES["umbrella_ip_as_info_ip_address"], 200)
    elif re.search("^bgp_routes\/asn\/.+\/.+\.json", args[0]):
        return MockResponse(RESPONSES["umbrella_ip_as_info_asn"], 200)
    elif re.search("^sample\/.+\/samples", args[0]):
        return MockResponse(RESPONSES["umbrella_threat_grid_sample_samples"], 200)
    elif re.search("^sample\/.+\/behaviors", args[0]):
        return MockResponse(RESPONSES["umbrella_threat_grid_sample_behaviors"], 200)
    elif re.search("^sample\/.+\/connections", args[0]):
        return MockResponse(RESPONSES["umbrella_threat_grid_sample_connections"], 200)
    elif re.search("^sample\/", args[0]):
        return MockResponse(RESPONSES["umbrella_threat_grid_sample_basic"], 200)
    elif re.search("^samples\/", args[0]):
        return MockResponse(RESPONSES["umbrella_threat_grid_samples"], 200)
    return MockResponse(None, 404)
