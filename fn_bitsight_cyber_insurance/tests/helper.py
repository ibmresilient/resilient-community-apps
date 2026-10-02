# -*- coding: utf-8 -*-
"""Helper for tests"""

PACKAGE_NAME = "fn_bitsight_cyber_insurance"


config = """[fn_bitsight_cyber_insurance]
bitsight_url = https://api.bitsighttech.com/ratings/
bitsight_api_token = 12345abcde """
get_alerts_results = [
    {
      "guid": 617110381,
      "alert_type": "FINDINGS_FILTER",
      "alert_date": "2025-04-01",
      "start_date": "2025-04-01",
      "company_name": "Saperix Corporate",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483413_virtual_folder",
      "severity": None,
      "trigger": "FINDINGS_FILTER",
      "alert_set_name": "New findings",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "guid": 617110382,
      "alert_type": "FINDINGS_FILTER",
      "alert_date": "2025-04-01",
      "start_date": "2025-04-01",
      "company_name": "Saperix Corporate - US West",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483413_virtual_folder",
      "severity": None,
      "trigger": "FINDINGS_FILTER",
      "alert_set_name": "New findings",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "guid": 617110383,
      "alert_type": "FINDINGS_FILTER",
      "alert_date": "2025-04-01",
      "start_date": "2025-04-01",
      "company_name": "Saperix, Inc - Wifi testing",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483413_virtual_folder",
      "severity": None,
      "trigger": "FINDINGS_FILTER",
      "alert_set_name": "New findings",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "guid": 617110380,
      "alert_type": "FINDINGS_FILTER",
      "alert_date": "2025-04-01",
      "start_date": "2025-04-01",
      "company_name": "Saperix, Inc.",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483413_virtual_folder",
      "severity": None,
      "trigger": "FINDINGS_FILTER",
      "alert_set_name": "New findings",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "guid": 617110384,
      "alert_type": "RISK_GRADE_CHANGE",
      "alert_date": "2025-04-01",
      "start_date": "2025-03-31",
      "company_name": "Saperix, Inc.",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483431_virtual_folder",
      "severity": None,
      "trigger": "RISK_GRADE_CHANGE",
      "alert_set_name": "Risk Vector Grades",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  ]

get_company_details_results = {
    "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "custom_id": None,
    "name": "Saperix, Inc.",
    "description": "Saperix Technologies LLC develops risk analysis software solutions.",
    "ipv4_count": 15082,
    "people_count": 700,
    "shortname": "Saperix",
    "industry": "Technology",
    "industry_slug": "technology",
    "sub_industry": "Computer & Network Security",
    "sub_industry_slug": "computer_network_security",
    "homepage": "http://www.saperix.com",
    "primary_domain": "saperix.com",
    "type": "CURATED",
    "display_url": "https://service.bitsighttech.com/app/spm/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/overview/",
    "rating_details": {
      "botnet_infections": {
        "name": "Botnet Infections",
        "rating": 600,
        "grade": "D",
        "percentile": 25,
        "grade_color": "#E17141",
        "category": "Compromised Systems",
        "category_order": 0,
        "beta": False,
        "order": 0,
        "display_url": "https://service.bitsighttech.com/app/spm/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/findings/?affects_rating=True&risk_vector=botnet_infections"
      },
      "spam_propagation": {
        "name": "Spam Propagation",
        "rating": 790,
        "grade": "A",
        "percentile": 90,
        "grade_color": "#239563",
        "category": "Compromised Systems",
        "category_order": 0,
        "beta": False,
        "order": 1,
        "display_url": "https://service.bitsighttech.com/app/spm/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/findings/?affects_rating=True&risk_vector=spam_propagation"
      }
    }
}

get_company_search_results = [
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "Saperix Corporate",
      "industry": "Technology",
      "industry_slug": "technology",
      "primary_domain": "saperix.com",
      "description": "Saperix Technologies LLC develops risk analysis software solutions.",
      "website": "http://saperix.com/corporate"
    },
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "Saperix, Inc.",
      "industry": "Technology",
      "industry_slug": "technology",
      "primary_domain": "saperix.com",
      "description": "Saperix Technologies LLC develops risk analysis software solutions.",
      "website": "http://www.saperix.com"
    },
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "Saperix, LAB AWS",
      "industry": "Technology",
      "industry_slug": "technology",
      "primary_domain": "saperix.com",
      "description": "This is a self-published break-out entity, which is used for grouping a portion of a company's internet assets together into a rating report.",
      "website": "http://saperix.com"
    },
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "Saperix Corporate - US West",
      "industry": "Technology",
      "industry_slug": "technology",
      "primary_domain": "saperix.com",
      "description": "Saperix Technologies LLC develops risk analysis software solutions.",
      "website": "http://saperix.com/corpwest"
    },
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "Saperix Corporate - US East",
      "industry": "Technology",
      "industry_slug": "technology",
      "primary_domain": "saperix.com",
      "description": "Saperix Technologies LLC develops risk analysis software solutions.",
      "website": "http://saperix.com/corpeast"
    }
  ]

get_finding_details_results = [
    {
      "temporary_id": "A9Jq47BBje5203d5b107bb1ef688e5290e3021685f4786023f325d86ef3884fe15d76c14a5",
      "affects_rating": True,
      "assets": [
        {
          "asset": "saperix.com",
          "identifier": None,
          "category": "low",
          "importance": 0.0,
          "is_ip": False,
          "asset_type": "Domain",
          "is_monitored": False
        }
      ],
      "details": {
        "cvss": {
          "base": []
        },
        "check_pass": "***",
        "diligence_annotations": {
          "message": "DNSSEC is not configured on this domain",
          "annotation_tokens": [
            {
              "***": "dns.no_dnssec_on_domain",
              "values": []
            }
          ],
          "security outcome": "Provably Insecure",
          "dnskeys": [],
          "***": [],
          "reason": "{{saperix.com./DNSKEY}} does not have a validated chain of trust",
          "dses": [],
          "nsecs": [
            {
              "recordType": "NSEC3",
              "algorithm": "SHA1",
              "flags": "Opt-out",
              "iterations": 0,
              "nextHash": "7tljso37jdfmo5go4kctqtc3sg8ikan6",
              "prevHash": "7TLJF311GL3UM2MIM44C9QB4L1MJRTO3",
              "salt": "-",
              "recordHash": "7tljqejgqkadoviqpav2ttv4k40ver77",
              "types": "NS DS RRSIG"
            }
          ]
        },
        "grade": "NEUTRAL",
        "remediations": [
          {
            "message": "DNSSEC is not configured on this domain",
            "help_text": "This domain is missing a DNSKEY record and therefore cannot be authenticated using DNSSEC.",
            "remediation_tip": "You will need to set up DNSSEC for your domain, including generating necessary keys and updating DNS zone records accordingly. See this <a target=\"new\" href=\"https://www.digitalocean.com/community/tutorials/how-to-setup-dnssec-on-an-authoritative-bind-dns-server--2\">DigitalOcean guide</a> for instructions which may be applicable to your server configuration, as well as <a target=\"new\" href=\"http://www.dnssec.net/practical-documents\">dnssec.net</a> for practical documents related to DNSSEC setup."
          }
        ],
        "sample_timestamp": "2025-04-13T12:02:51Z",
        "vulnerabilities": [],
        "rollup_end_date": "2025-04-13",
        "rollup_start_date": "2024-01-20",
        "searchable_details": "DNSSEC is not configured on this domain"
      },
      "evidence_key": "***",
      "first_seen": "2024-01-20",
      "last_seen": "2025-04-13",
      "related_findings": [],
      "risk_category": "Diligence",
      "risk_vector": "dnssec",
      "risk_vector_label": "DNSSEC",
      "rolledup_observation_id": "rPFFNU9KxWPvS55FgjhbEQ==",
      "severity": 1.0,
      "severity_category": "minor",
      "tags": [],
      "remediation_history": {
        "last_requested_refresh_date": None,
        "last_refresh_status_date": None,
        "last_refresh_status_label": None,
        "last_refresh_status_reason": None,
        "last_refresh_reason_code": None,
        "last_refresh_requester": None,
        "result_finding_date": None
      },
      "duration": None,
      "comments": None,
      "remaining_decay": 59,
      "remediated": None,
      "impacts_risk_vector_details": "AFFECTS_RATING",
      "grace_period_end_date": None
    },
    {
      "temporary_id": "A9Jq47BBjeb903751c1ff8a4aaa0329e0ded23d87e940c27bfe5f4b56e0749e18b27f30bee",
      "affects_rating": True,
      "assets": [
        {
          "asset": "saperix.com",
          "identifier": None,
          "category": "low",
          "importance": 0.0,
          "is_ip": False,
          "asset_type": "Domain",
          "is_monitored": False
        }
      ],
      "details": {
        "cvss": {
          "base": []
        },
        "check_pass": "***",
        "diligence_annotations": {
          "message": "Record does not exist",
          "annotation_tokens": [
            {
              "***": "dmarc.no_record",
              "values": []
            }
          ],
          "record": [
            []
          ],
          "percentage": 0,
          "policy": "NOT_SET",
          "ruaReportEmail": [],
          "rufReportEmail": []
        },
        "grade": "BAD",
        "remediations": [
          {
            "message": "Record does not exist",
            "help_text": "The domain does not have a DMARC record in place.",
            "remediation_tip": "See <a href=\"https://help.bitsight.com/hc/en-us/articles/23007682932247-Setting-a-DMARC-Policy\">how to set a DMARC policy</a> and implement a DMARC policy for this domain."
          }
        ],
        "sample_timestamp": "2025-04-12T21:29:39Z",
        "vulnerabilities": [],
        "rollup_end_date": "2025-04-12",
        "rollup_start_date": "2024-03-31"
      },
      "evidence_key": "***",
      "first_seen": "2024-03-31",
      "last_seen": "2025-04-12",
      "related_findings": [],
      "risk_category": "Diligence",
      "risk_vector": "dmarc",
      "risk_vector_label": "DMARC",
      "rolledup_observation_id": "mwiQBQcVjbtfZ7f95I95Xw==",
      "severity": 8.0,
      "severity_category": "material",
      "tags": [],
      "remediation_history": {
        "last_requested_refresh_date": None,
        "last_refresh_status_date": None,
        "last_refresh_status_label": None,
        "last_refresh_status_reason": None,
        "last_refresh_reason_code": None,
        "last_refresh_requester": None,
        "result_finding_date": None
      },
      "duration": None,
      "comments": None,
      "remaining_decay": 58,
      "remediated": None,
      "impacts_risk_vector_details": "AFFECTS_RATING",
      "grace_period_end_date": None
    }
  ]

get_latest_alerts_results = [
    {
      "guid": 624802211,
      "alert_type": "RISK_GRADE_CHANGE",
      "alert_date": "2025-04-12",
      "start_date": "2025-04-11",
      "company_name": "Saperix, Inc - Wifi testing",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483431_virtual_folder",
      "severity": None,
      "trigger": "RISK_GRADE_CHANGE",
      "alert_set_name": "Risk Vector Grades",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "guid": 624802210,
      "alert_type": "FINDINGS_FILTER",
      "alert_date": "2025-04-12",
      "start_date": "2025-04-12",
      "company_name": "Saperix, Inc.",
      "company_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "company_url": "/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/",
      "folder_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "folder_name": "alertset_483413_virtual_folder",
      "severity": None,
      "trigger": "FINDINGS_FILTER",
      "alert_set_name": "New findings",
      "alert_set_guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  ]

get_portfolio_details_results = [
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "custom_id": None,
      "name": "Actors Films",
      "shortname": "Actors Films",
      "network_size_v4": 512,
      "rating": 650,
      "rating_date": "2025-04-13",
      "added_date": "2024-04-19",
      "industry": {
        "name": "Media/Entertainment",
        "slug": "mediaentertainment"
      },
      "sub_industry": {
        "name": "Motion Pictures and Film",
        "slug": "motion_pictures_and_film"
      },
      "type": [
        "CURATED",
        "PRIVATE"
      ],
      "logo": "https://api.bitsighttech.com/ratings/v1/companies/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/logo-image",
      "sparkline": "https://api.bitsighttech.com/ratings/v1/companies/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/sparkline?size=small",
      "subscription_type": {
        "name": "Total Risk Monitoring",
        "slug": "continuous_monitoring"
      },
      "primary_domain": "actorsfilms.us",
      "display_url": "https://service.bitsighttech.com/app/tprm/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/overview/",
      "tier": None,
      "tier_name": None,
      "life_cycle": None,
      "relationship": None,
      "details": {
        "confidence": "HIGH",
        "is_primary": False,
        "primary_company": None
      }
    },
    {
      "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "custom_id": None,
      "name": "Bitsight Labs",
      "shortname": "AnubisNetworks - Labs",
      "network_size_v4": 438,
      "rating": 560,
      "rating_date": "2025-04-13",
      "added_date": "2024-04-19",
      "industry": {
        "name": "Technology",
        "slug": "technology"
      },
      "sub_industry": {
        "name": "Computer Software",
        "slug": "computer_software"
      },
      "type": [
        "CURATED",
        "SELF-PUBLISHED"
      ],
      "logo": "https://api.bitsighttech.com/ratings/v1/companies/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/logo-image",
      "sparkline": "https://api.bitsighttech.com/ratings/v1/companies/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/sparkline?size=small",
      "subscription_type": {
        "name": "Total Risk Monitoring",
        "slug": "continuous_monitoring"
      },
      "primary_domain": "bitsight.io",
      "display_url": "https://service.bitsighttech.com/app/tprm/company/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/overview/",
      "tier": None,
      "tier_name": None,
      "life_cycle": None,
      "relationship": None,
      "details": {
        "confidence": "HIGH",
        "is_primary": False,
        "primary_company": None
      }
    }
  ]

def mock_init():
    class MockClient(object):
        """ Add Mock connection data """

        def __init__(self):
            """ Mock """
            pass

        def get_alerts(self, limit: int=100, offset: int=0, alert_date: str=None, alert_date_gt: str=None, alert_date_gte: str=None,
                   alert_date_lt: str=None, alert_date_lte: str=None, alert_type: str=None, company_guid: str=None,
                   expand: str=None, folder_guid: str=None, severity: str=None):
            return {"results": get_alerts_results}

        def get_latest_alerts(self, limit: int=100, offset: int=0, alert_type: str=None, company_guid: str=None,
                          expand: str=None, folder_guid: str=None, severity: str=None):
            return {"results": get_latest_alerts_results}

        def get_company_search(self, limit: int=100, offset: int=0, domain: str=None, expand: str=None, guids: str=None, industry: str=None,
                           industry_slug: str=None, in_portfolio: bool=None, name: str=None, scope: str=None):
            return {"results": get_company_search_results}

        def get_company_details(self, company_guid: str=None, fields: str=None):
            return get_company_details_results

        def get_company_finding_details(self, limit: int=100, offset: int=0, company_guid: str=None, affects_rating: bool=None, affects_rating_details: str=None,
                                    assets_asset: str=None, assets_category: str=None, assets_combined_importance: str=None, assets_hosted_by: str=None, attributed_companies_guid: list=None,
                                    attributed_companies_name: list=None, cvss_base_gte: float=None, cvss_base_lte: float=None, details_grade: str=None,
                                    details_grade_gt: str=None, details_grade_lt: str=None, details_infection_family: str=None, details_observed_ips_contains: str=None,
                                    details_vulnerabilities_severity: str=None, evidence_key: str=None, expand: str=None, first_seen: str=None, first_seen_gt: str=None,
                                    first_seen_gte: str=None, first_seen_lt: str=None, first_seen_lte: str=None, last_remediation_status_date: str=None,
                                    last_remediation_status_date_gt: str=None, last_remediation_status_date_gte: str=None, last_remediation_status_date_lt: str=None,
                                    last_remediation_status_date_lte: str=None, last_remediation_status_label: str=None, last_seen: str=None, last_seen_gt: str=None,
                                    last_seen_gte: str=None, last_seen_lt: str=None, last_seen_lte: str=None, remediation_assignments: str=None, risk_vector_label: str=None,
                                    severity: float=None, severity_gt: float=None, severity_gte: float=None, severity_lt: float=None, severity_lte: float=None,
                                    severity_category: float=None, tags_contains: str=None, unsampled: bool=None, vulnerabilities: str=None):
            return {"results": get_finding_details_results}

        def get_portfolio_details(self, limit: int=100, offset: int=0, countries: str=None, exclude_subscription_type_slug: list=None, filter_group: str=None,
                              risk_vectors_grade: str=None, risk_vectors_slug: str=None, software_category: str=None, software_name: str=None, folder: list=None,
                              industry_name: str=None, industry_slug: str=None, infections: list=None, life_cycle_slug: str=None, open_ports: list=None,
                              products: list=None, product_types: list=None, providers: str=None, rating: int=None, rating_gt: int=None, rating_gte: int=None,
                              rating_lt: int=None, rating_lte: int=None, relationship_slug: str=None, security_incident_categories: list=None,
                              subscription_type_slug: list=None, tier: str=None, type: str=None, vendor_action_plan: str=None, vulnerabilities: list=None):
            return {"results": get_portfolio_details_results}

    return MockClient()