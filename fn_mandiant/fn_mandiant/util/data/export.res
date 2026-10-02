{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1697480045444,
  "export_format_version": 2,
  "export_type": null,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/mandiant_artifact_type",
      "hide_notification": false,
      "id": 299,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mandiant_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mandiant_artifact_type",
      "tooltip": "Artifact data type",
      "type_id": 11,
      "uuid": "e8aa4b21-3b13-4b68-9253-949bf261dc71",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/mandiant_artifact_data",
      "hide_notification": false,
      "id": 300,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mandiant_artifact_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mandiant_artifact_data",
      "tooltip": "Data from the artifact",
      "type_id": 11,
      "uuid": "61553bb8-4a9e-4ced-8c5b-ebd3de6865e3",
      "values": []
    },
    {
      "export_key": "incident/internal_customizations_field",
      "id": 0,
      "input_type": "text",
      "internal": true,
      "name": "internal_customizations_field",
      "read_only": true,
      "text": "Customizations Field (internal)",
      "type_id": 0,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa1"
    }
  ],
  "functions": [
    {
      "created_date": 1697188952723,
      "description": {
        "content": "Investigate publicly known threats with insights from Mandiant. Upon artifact creation scans Mandiant for any related information.",
        "format": "text"
      },
      "destination_handle": "fn_mandiant",
      "display_name": "Mandiant: Threat Intelligence",
      "export_key": "mandiant_threat_intelligence",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1697479955219,
      "name": "mandiant_threat_intelligence",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"url--30347ecb-ecc0-5d63-a422-2f0aa046d48c\", \"mscore\": 99, \"type\": \"url\", \"value\": \"http://achren.org\", \"is_publishable\": true, \"sources\": [{\"first_seen\": \"2020-07-31T00:15:02.614+0000\", \"last_seen\": \"2020-07-31T00:15:02.614+0000\", \"osint\": true, \"category\": [], \"source_name\": \"malwaredomainlist\"}], \"verdict\": {\"analystVerdict\": {\"timestamp\": null, \"verdict\": null, \"confidenceScore\": 0}, \"authoritativeVerdict\": \"mlVerdict\", \"mlVerdict\": {\"confidenceScore\": 0.9888736570875306, \"verdict\": \"malicious\", \"timestamp\": \"2022-02-17T22:00:35.914+0000\", \"modelVersion\": \"6.1.0\", \"reasoning\": {\"malicious_count\": 4, \"source_count\": 185, \"neighbor_influence\": null, \"mandiant\": {\"bp_hosting\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Bulletproof Hosting\", \"response_count\": 0, \"source_count\": 1}, \"fqdn_analysis\": {\"benign_count\": 1, \"confidence\": \"low\", \"malicious_count\": 0, \"name\": \"FQDN Analysis\", \"response_count\": 1, \"source_count\": 2}, \"knowledge_graph\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Knowledge Graph\", \"response_count\": 0, \"source_count\": 1}, \"malware_analysis\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Malware Analysis\", \"response_count\": 0, \"source_count\": 3}, \"name\": \"Mandiant\", \"spam\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Spam Monitoring\", \"response_count\": 0, \"source_count\": 1}, \"url_analysis\": {\"benign_count\": 1, \"confidence\": \"low\", \"malicious_count\": 0, \"name\": \"URL Analysis\", \"response_count\": 1, \"source_count\": 4}}, \"response_count\": 6, \"confidence_count\": {\"benign\": {\"high\": 0, \"low\": 2, \"med\": 0}, \"malicious\": {\"high\": 0, \"low\": 0, \"med\": 4}}, \"tp\": {\"crowdsource\": {\"benign_count\": 0, \"confidence\": \"med\", \"malicious_count\": 3, \"name\": \"Crowdsourced Threat Analysis\", \"response_count\": 3, \"source_count\": 91}, \"misp\": {\"dch\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Dynamic Cloud Hosting (DCH) Provider\", \"response_count\": 0, \"source_count\": 9}, \"edu\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Educational Institution\", \"response_count\": 0, \"source_count\": 1}, \"name\": \"MISP\", \"other\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Other\", \"response_count\": 0, \"source_count\": 14}, \"popular_infra\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Popular Internet Infrastructure\", \"response_count\": 0, \"source_count\": 18}, \"popular_web\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Popular Website\", \"response_count\": 0, \"source_count\": 8}, \"sinkhole\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Internet Sinkhole\", \"response_count\": 0, \"source_count\": 1}, \"vpn\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Known VPN Hosting Provider\", \"response_count\": 0, \"source_count\": 1}}, \"name\": \"Third Party\", \"tif\": {\"aa419\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Aa419\", \"response_count\": 0, \"source_count\": 1}, \"azorult-tracker\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Azorult-tracker\", \"response_count\": 0, \"source_count\": 1}, \"benkow\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Benkow\", \"response_count\": 0, \"source_count\": 1}, \"botvrij_urls\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Botvrij Urls\", \"response_count\": 0, \"source_count\": 1}, \"cryptolaemus\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Cryptolaemus\", \"response_count\": 0, \"source_count\": 1}, \"cybercrimetracker\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Cybercrimetracker\", \"response_count\": 0, \"source_count\": 1}, \"davidonzo_hashes\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Davidonzo Hashes\", \"response_count\": 0, \"source_count\": 1}, \"dev\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Dev\", \"response_count\": 0, \"source_count\": 1}, \"digitalside_it_hashes\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Digitalside It Hashes\", \"response_count\": 0, \"source_count\": 1}, \"digitalside_it_urls\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Digitalside It Urls\", \"response_count\": 0, \"source_count\": 1}, \"dyndns_ponmocup\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Dyndns Ponmocup\", \"response_count\": 0, \"source_count\": 1}, \"feodo\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Feodo\", \"response_count\": 0, \"source_count\": 1}, \"feodo_ids\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Feodo Ids\", \"response_count\": 0, \"source_count\": 1}, \"fumik0\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Fumik0\", \"response_count\": 0, \"source_count\": 1}, \"futex.re\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Futex.re\", \"response_count\": 0, \"source_count\": 1}, \"h3x_1day\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"H3x 1day\", \"response_count\": 0, \"source_count\": 1}, \"malc0de\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Malc0de\", \"response_count\": 0, \"source_count\": 1}, \"malshare\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Malshare\", \"response_count\": 0, \"source_count\": 1}, \"malwared\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Malwared\", \"response_count\": 0, \"source_count\": 1}, \"malwaredomainlist\": {\"benign_count\": 0, \"confidence\": \"med\", \"malicious_count\": 1, \"name\": \"Malwaredomainlist\", \"response_count\": 1, \"source_count\": 1}, \"malwaremustdie\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Malwaremustdie\", \"response_count\": 0, \"source_count\": 1}, \"name\": \"Threat Intelligence Feeds\", \"openphish\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Openphish\", \"response_count\": 0, \"source_count\": 1}, \"phishing_database\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Phishing Database\", \"response_count\": 0, \"source_count\": 1}, \"phishstats\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Phishstats\", \"response_count\": 0, \"source_count\": 1}, \"phishtank\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Phishtank\", \"response_count\": 0, \"source_count\": 1}, \"phishtank_valid_online\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Phishtank Valid Online\", \"response_count\": 0, \"source_count\": 1}, \"urlhaus\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Urlhaus\", \"response_count\": 0, \"source_count\": 1}, \"urlscan_phishing\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Urlscan Phishing\", \"response_count\": 0, \"source_count\": 1}, \"viriback\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Viriback\", \"response_count\": 0, \"source_count\": 1}, \"vxvault_virilist\": {\"benign_count\": 0, \"confidence\": null, \"malicious_count\": 0, \"name\": \"Vxvault Virilist\", \"response_count\": 0, \"source_count\": 1}}}, \"benign_count\": 2, \"version\": \"1.0.1\"}}}, \"misp\": {\"akamai\": false, \"alexa_1M\": false, \"apple\": false, \"bank-website\": false, \"cisco_1M\": false, \"cisco_top1000\": false, \"cisco_top20k\": false, \"common-contact-emails\": false, \"covid-19-cyber-threat-coalition-whitelist\": false, \"covid-19-krassi-whitelist\": false, \"dax30\": false, \"empty-hashes\": false, \"google-gcp\": false, \"google-gmail-sending-ips\": false, \"googlebot\": false, \"majestic_million_1M\": false, \"microsoft\": false, \"microsoft-attack-simulator\": false, \"microsoft-azure\": false, \"microsoft-azure-china\": false, \"microsoft-azure-germany\": false, \"microsoft-azure-us-gov\": false, \"microsoft-win10-connection-endpoints\": false, \"mozilla-IntermediateCA\": false, \"multicast\": false, \"nioc-filehash\": false, \"ovh-cluster\": false, \"public-dns-v4\": false, \"public-dns-v6\": false, \"sinkholes\": false, \"smtp-receiving-ips\": false, \"smtp-sending-ips\": false, \"university_domains\": false, \"url-shortener\": false, \"vpn-ipv4\": false, \"vpn-ipv6\": false, \"whats-my-ip\": false, \"wikimedia\": false}, \"last_updated\": \"2022-02-17T22:00:36.968Z\", \"first_seen\": \"2020-07-31T00:15:02.000Z\", \"last_seen\": \"2020-07-31T00:15:02.000Z\"}, \"raw\": null, \"inputs\": {\"mandiant_artifact_data\": \"http://achren.org\", \"mandiant_artifact_type\": \"URL\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mandiant\", \"package_version\": \"1.0.0\", \"host\": \"App Host\", \"execution_time_ms\": 223, \"timestamp\": \"2023-10-03 13:20:15\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"mscore\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}, \"is_publishable\": {\"type\": \"boolean\"}, \"sources\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"first_seen\": {\"type\": \"string\"}, \"last_seen\": {\"type\": \"string\"}, \"osint\": {\"type\": \"boolean\"}, \"category\": {\"type\": \"array\"}, \"source_name\": {\"type\": \"string\"}}}}, \"verdict\": {\"type\": \"object\", \"properties\": {\"analystVerdict\": {\"type\": \"object\", \"properties\": {\"timestamp\": {}, \"verdict\": {}, \"confidenceScore\": {\"type\": \"integer\"}}}, \"authoritativeVerdict\": {\"type\": \"string\"}, \"mlVerdict\": {\"type\": \"object\", \"properties\": {\"confidenceScore\": {\"type\": \"number\"}, \"verdict\": {\"type\": \"string\"}, \"timestamp\": {\"type\": \"string\"}, \"modelVersion\": {\"type\": \"string\"}, \"reasoning\": {\"type\": \"object\", \"properties\": {\"malicious_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}, \"neighbor_influence\": {}, \"mandiant\": {\"type\": \"object\", \"properties\": {\"bp_hosting\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"fqdn_analysis\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {\"type\": \"string\"}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"knowledge_graph\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"malware_analysis\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"name\": {\"type\": \"string\"}, \"spam\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"url_analysis\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {\"type\": \"string\"}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}}}, \"response_count\": {\"type\": \"integer\"}, \"confidence_count\": {\"type\": \"object\", \"properties\": {\"benign\": {\"type\": \"object\", \"properties\": {\"high\": {\"type\": \"integer\"}, \"low\": {\"type\": \"integer\"}, \"med\": {\"type\": \"integer\"}}}, \"malicious\": {\"type\": \"object\", \"properties\": {\"high\": {\"type\": \"integer\"}, \"low\": {\"type\": \"integer\"}, \"med\": {\"type\": \"integer\"}}}}}, \"tp\": {\"type\": \"object\", \"properties\": {\"crowdsource\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {\"type\": \"string\"}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"misp\": {\"type\": \"object\", \"properties\": {\"dch\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"edu\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"name\": {\"type\": \"string\"}, \"other\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"popular_infra\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"popular_web\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"sinkhole\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"vpn\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}}}, \"name\": {\"type\": \"string\"}, \"tif\": {\"type\": \"object\", \"properties\": {\"aa419\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"azorult-tracker\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"benkow\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"botvrij_urls\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"cryptolaemus\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"cybercrimetracker\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"davidonzo_hashes\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"dev\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"digitalside_it_hashes\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"digitalside_it_urls\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"dyndns_ponmocup\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"feodo\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"feodo_ids\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"fumik0\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"futex.re\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"h3x_1day\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"malc0de\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"malshare\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"malwared\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"malwaredomainlist\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {\"type\": \"string\"}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"malwaremustdie\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"name\": {\"type\": \"string\"}, \"openphish\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"phishing_database\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"phishstats\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"phishtank\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"phishtank_valid_online\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"urlhaus\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"urlscan_phishing\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"viriback\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}, \"vxvault_virilist\": {\"type\": \"object\", \"properties\": {\"benign_count\": {\"type\": \"integer\"}, \"confidence\": {}, \"malicious_count\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"response_count\": {\"type\": \"integer\"}, \"source_count\": {\"type\": \"integer\"}}}}}}}, \"benign_count\": {\"type\": \"integer\"}, \"version\": {\"type\": \"string\"}}}}}}}, \"misp\": {\"type\": \"object\", \"properties\": {\"akamai\": {\"type\": \"boolean\"}, \"alexa_1M\": {\"type\": \"boolean\"}, \"apple\": {\"type\": \"boolean\"}, \"bank-website\": {\"type\": \"boolean\"}, \"cisco_1M\": {\"type\": \"boolean\"}, \"cisco_top1000\": {\"type\": \"boolean\"}, \"cisco_top20k\": {\"type\": \"boolean\"}, \"common-contact-emails\": {\"type\": \"boolean\"}, \"covid-19-cyber-threat-coalition-whitelist\": {\"type\": \"boolean\"}, \"covid-19-krassi-whitelist\": {\"type\": \"boolean\"}, \"dax30\": {\"type\": \"boolean\"}, \"empty-hashes\": {\"type\": \"boolean\"}, \"google-gcp\": {\"type\": \"boolean\"}, \"google-gmail-sending-ips\": {\"type\": \"boolean\"}, \"googlebot\": {\"type\": \"boolean\"}, \"majestic_million_1M\": {\"type\": \"boolean\"}, \"microsoft\": {\"type\": \"boolean\"}, \"microsoft-attack-simulator\": {\"type\": \"boolean\"}, \"microsoft-azure\": {\"type\": \"boolean\"}, \"microsoft-azure-china\": {\"type\": \"boolean\"}, \"microsoft-azure-germany\": {\"type\": \"boolean\"}, \"microsoft-azure-us-gov\": {\"type\": \"boolean\"}, \"microsoft-win10-connection-endpoints\": {\"type\": \"boolean\"}, \"mozilla-IntermediateCA\": {\"type\": \"boolean\"}, \"multicast\": {\"type\": \"boolean\"}, \"nioc-filehash\": {\"type\": \"boolean\"}, \"ovh-cluster\": {\"type\": \"boolean\"}, \"public-dns-v4\": {\"type\": \"boolean\"}, \"public-dns-v6\": {\"type\": \"boolean\"}, \"sinkholes\": {\"type\": \"boolean\"}, \"smtp-receiving-ips\": {\"type\": \"boolean\"}, \"smtp-sending-ips\": {\"type\": \"boolean\"}, \"university_domains\": {\"type\": \"boolean\"}, \"url-shortener\": {\"type\": \"boolean\"}, \"vpn-ipv4\": {\"type\": \"boolean\"}, \"vpn-ipv6\": {\"type\": \"boolean\"}, \"whats-my-ip\": {\"type\": \"boolean\"}, \"wikimedia\": {\"type\": \"boolean\"}}}, \"last_updated\": {\"type\": \"string\"}, \"first_seen\": {\"type\": \"string\"}, \"last_seen\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mandiant_artifact_data\": {\"type\": \"string\"}, \"mandiant_artifact_type\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "4512cffd-9ea6-4246-ae93-e4d4c13f436b",
      "version": 2,
      "view_items": [
        {
          "content": "61553bb8-4a9e-4ced-8c5b-ebd3de6865e3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e8aa4b21-3b13-4b68-9253-949bf261dc71",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": []
    }
  ],
  "geos": null,
  "groups": null,
  "id": 3,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1697480042832,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1697480042832,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "26d6dc0a-f920-4abe-8f06-a815b9ca1416",
        "9516160d-d01e-490b-becb-04233ac9a81a"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_mandiant",
      "name": "fn_mandiant",
      "programmatic_name": "fn_mandiant",
      "tags": [],
      "users": [],
      "uuid": "88c3ce4e-571b-404b-a2c0-6fc6c00a7307"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": 2,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "IP Address"
            },
            {
              "evaluation_id": 3,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "URL"
            },
            {
              "evaluation_id": 4,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Malware MD5 Hash"
            },
            {
              "evaluation_id": 5,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "DNS Name"
            },
            {
              "evaluation_id": 1,
              "field_name": null,
              "method": "object_added",
              "type": null,
              "value": null
            }
          ],
          "custom_condition": "1 AND (2 OR 3 OR 4 OR 5)",
          "logic_type": "advanced"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34\" isExecutable=\"true\" name=\"playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1tkd9qq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Mandiant: Threat Intelligence\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4512cffd-9ea6-4246-ae93-e4d4c13f436b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.mandiant_artifact_data = artifact.value\\ninputs.mandiant_artifact_type = artifact.type\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"mandiant_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1tkd9qq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1dhtg4b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1tkd9qq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0vp4mzt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1dhtg4b\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Add search results to HITS\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"9804bc3f-ba90-478d-8bdc-c0a87a27b917\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1dhtg4b\u003c/incoming\u003e\u003coutgoing\u003eFlow_0vp4mzt\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0vp4mzt\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vp4mzt\" id=\"Flow_0vp4mzt_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"532\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"674\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1dhtg4b\" id=\"Flow_1dhtg4b_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"448\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1tkd9qq\" id=\"Flow_1tkd9qq_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"76\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"619\" y=\"24\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"644\" y=\"674\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"448\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1697188952990,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Mandiant: Scan artifact",
      "export_key": "mandiant_scan_artifact",
      "field_type_handle": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
      "fields_type": {
        "actions": [],
        "display_name": "Mandiant: Scan artifact",
        "export_key": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
        "uuid": "199c20c0-78f3-4a71-9ef2-6eda376007ee"
      },
      "has_logical_errors": false,
      "id": 1,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1697480031324,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1697188953055,
          "description": "",
          "enabled": false,
          "export_key": "Add search results to HITS",
          "id": 2,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1697479955662,
          "name": "Add search results to HITS",
          "object_type": "artifact",
          "playbook_handle": "mandiant_scan_artifact",
          "programmatic_name": "mandiant_scan_artifact_add_search_results_to_hits",
          "script_text": "\ndef compile_section_by_dtype(value, name):\n    \"\"\"\n    Complies received information into HIT Cards. The information can have varied datatype. This function\n    automatically detects the data type and formats the information suitable for a SOAR artifact. The result\n    is returned as a dictionary representing the subsection with its name, data type, and converted\n    value (if applicable).\n\n    Args:\n    ----\n        value (str): The value to be categorized into a specific data type.\n        name  (str): The name or identifier for the subsection.\n\n    Returns:\n    -------\n        dict: A dictionary representing the subsection with the following keys:\n            - \"name\"  : The name or identifier passed as the \u0027name\u0027 parameter.\n            - \"type\"  : The determined data type of the \u0027value\u0027 (either \"string,\" \"uri,\" or \"number\").\n            - \"value\" : The \u0027value\u0027 converted to the appropriate data type (int for numbers).\n    \"\"\"\n    info_type = \"string\"\n\n    # if \"http\" found, the string is classified as an URL\n    if \"http\" in value:\n        info_type = \"uri\"\n\n    # detects if the given string is a number\n    elif value.isdigit():\n        info_type = \"number\"\n        value = int(value)\n\n    # format required for a HIT card to compile within an artifact\n    subsection = {\n        \"name\"  : name,\n        \"type\"  : info_type,\n        \"value\" : value\n    }\n    return subsection\n\n\ndef dedup_section(section):\n    \"\"\"\n    An HIT card exclusively accommodates distinct entries and cannot exhibit information in a nested\n    structure. Consequently, data is condensed and organized within the HIT card. To prevent \n    redundancies, this function is employed to attach an index number to the names of recurring\n    entries, ensuring their uniqueness\n\n    Args:\n    ----\n        section (dict): The section to be de-duplicated\n\n    Returns:\n    -------\n        dict : Similar dictionary with de-duplicated \"name\" value\n    \"\"\"\n    unique_keys = {}\n    for idx, each_item in enumerate(section):\n        if each_item[\"name\"] not in unique_keys:\n            unique_keys[each_item[\"name\"]] = 0\n        else:\n            unique_keys[each_item[\"name\"]] += 1\n            section[idx][\"name\"] = section[idx][\"name\"] + str(unique_keys[each_item[\"name\"]])\n    return section\n\n\ndef dedup_verdict_section(section, verdict_name=\"\"):\n    \"\"\"\n    Verdict is a special section that contains the result of multiple analysis. Each analysis has\n    its own \"name\", \"response_count\", \"source_count\", \"benign_count\", \"confidence\", and \"malicious_count\".\n    As these values are being repeated, this function finds the appropriate analysis being performed using\n    the name parameter, and appends that to the appropriate fields, there by eliminating duplicates.\n    \n    Example:\n    -------\n        Input : Bulletproof Hosting, response_count, source_count, benign_count, malicious_count\n        Output: Bulletproof Hosting response_count, Bulletproof Hosting source_count, Bulletproof\n                Hosting benign_count, Bulletproof Hosting malicious_count\n\n    Args:\n    ----\n        section (dict): Verdict section of the response\n\n    Returns:\n        dict :  Similar dictionary with \"name\" values modified with their appropriate analysis type.\n    \"\"\"\n   \n\n    for each_item in section:\n        # Saving the analysis name for subsequent fields\n        if each_item[\"name\"] == \"name\":\n            verdict_name = each_item[\"value\"]\n\n        # Appending analysis name to fields that belong to the analysis\n        if verdict_name:\n            each_item[\"name\"] = f\"{verdict_name} {each_item[\u0027name\u0027]}\"\n    return section\n\n\ndef compile_hits_section(gathered_info, compiled_section:list, section_name:str=None) -\u003e list:\n    \"\"\" \n    The purpose of this function is to flatten and organize data from the `gathered_info`\n    dictionary and append it to the `compiled_section` list. The function can also handle\n    recursive calls when it encounters nested dictionaries or lists.\n\n    Here\u0027s a breakdown of its functionality:\n        1. It iterates through the keys of the `gathered_info` dictionary.\n        2. If a key corresponds to a dictionary, it recursively calls itself with the nested\n            dictionary, aiming to flatten it, and appends the results to the `compiled_section`.\n        3. If the `gathered_info` is not a list and the value associated with the current key\n            is a dictionary, it also recursively calls itself to flatten the nested dictionary.\n        4. If the current key is not a list, and the value is a list, it iterates through the\n            list and checks if the elements are dictionaries or lists. If so, it recursively\n            calls itself on each element and appends the results to the `compiled_section`.\n        5. If neither of the above conditions is met (i.e., the key or value is not a list or\n            dictionary), it formats the key and value into a subsection using a function called\n            `compile_section_by_dtype`. It then appends this subsection to the `compiled_section`.\n        6. Finally, it returns the `compiled_section` containing the flattened and organized data.\n\n    Args:\n    ----\n        gathered_info   (dict or list) : Could either be a dictionary or a list that requires\n                                            flattening.\n        compiled_section        (list) : Final flattened result. Contains a list of dictionaries.\n                                            The function starts of with an empty list.\n\n    Returns:\n    -------\n        list: compiled_section\n    \"\"\"\n    for each_key in gathered_info:\n    \n        if section_name:\n            _new_section_name = f\"{section_name} {each_key}\"\n        else:\n            _new_section_name = each_key\n\n        # This function has been designed with recursion in mind. This means that\n        # gathered_info can be a dict and at times even a list. And therefore \n\n        # If gathered_info is a list and each_key is a dict is found within the section,\n        # this function is recursively called with the newly found dict while passing\n        # the previous output list. This is done to flatten the newly found dict and\n        # append its contents to the existing section.\n        if isinstance(each_key, dict):\n            compile_hits_section(each_key, compiled_section, _new_section_name)\n\n        # If gathered_info is not a list and the current value of the gathered_info is a dict\n        # the function is called recursively to flatten the newly found dict.\n        elif not isinstance(gathered_info, list) and isinstance(gathered_info[each_key], dict):\n            compile_hits_section(gathered_info[each_key], compiled_section, _new_section_name)\n\n        # Similarly if a list is found for the current value or key, it is then iterated further\n        # and flattened out.\n        elif not isinstance(each_key, list) and isinstance(gathered_info[each_key], list):\n            for each_entity in gathered_info[each_key]:\n                if isinstance(each_entity, dict) or isinstance(each_entity, list):\n                    subsection = compile_hits_section(each_entity, compiled_section, _new_section_name)\n\n        # Finally, if the key or value is not a list or dict, then it\u0027s classified based on\n        # it\u0027s datatype and formatted into a section.\n        else:\n            subsection = compile_section_by_dtype(str(gathered_info[each_key]), _new_section_name)\n            compiled_section.append(subsection)\n\n    return compiled_section\n\n\ndef add_response_as_hits(response):\n    \"\"\"\n    Here the HIT cards are created for artifacts. Depending on the response, 2 or more cards can\n    be created. The primary/top level of the response is created into a HIT card by itself. Every\n    other nested item within the response is created into a standalone section.\n\n    Args:\n    ----\n        response (dict): response from the function that contains information that is to be displayed\n                            as HITS.\n    Returns:\n    -------\n        None\n    \"\"\"\n    # Extract information found in the top level of the response and create a standalone HIT card\n    # for those values. This usually has information related to MScore. Other sections are created\n    # into separate HIT cards.\n    main_section , other_sections, verdict_section = {}, {}, {}\n    for section in response:\n        if section.lower().strip() == \"verdict\":\n            verdict_section =  response[section]\n        elif isinstance(response[section], list) or isinstance(response[section], dict):\n            other_sections[section] = response[section]\n        else:\n            main_section[section] = response[section]\n\n    # Three primary sections are created MScore, Verdict and Additional Information\n    # Each of these sections are create into separate HIT cards.\n    # Special processing done for Verdict to accommodate various analysis results.\n    # Each section is then deduplicated to avoid any conflicts.\n\n    _othr_section = compile_hits_section(other_sections, [], None)\n    _othr_section = dedup_verdict_section(_othr_section)\n    _othr_section = dedup_section(_othr_section)\n    artifact.addHit(f\"Mandiant Threat Intelligence: Additional Information\", _othr_section)\n    \n    _main_section = compile_hits_section(main_section, [], None)\n    _main_section = dedup_section(_main_section)\n    artifact.addHit(\"Mandiant Threat Intelligence: MScore\", _main_section)\n\n    _verd_section = compile_hits_section(verdict_section, [], None)\n    _verd_section = dedup_verdict_section(_verd_section)\n    _verd_section = dedup_section(_verd_section)\n    artifact.addHit(f\"Mandiant Threat Intelligence: Verdict \", _verd_section)\n\n\n\nresult = playbook.functions.results.mandiant_results\nif not result.success:\n    incident.addNote(helper.createRichText(result.reason))\nelif \"Not Found\" in result.content:\n    # Insert code here to modify behavior when no results are found\n    incident.addNote(f\"No enrichment data found for artifact {artifact.value} from Mandiant\")\nelse:\n    add_response_as_hits(result.content)",
          "tags": [],
          "uuid": "9804bc3f-ba90-478d-8bdc-c0a87a27b917"
        }
      ],
      "name": "mandiant_scan_artifact",
      "object_type": "artifact",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_a87ae009-da8b-4a6b-b5ff-ff205216ed34",
        "id": 2,
        "name": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
        "type": "playbook",
        "uuid": "98374d47-0f1b-43cc-aafe-76f312650454"
      },
      "tags": [],
      "type": "default",
      "uuid": "a87ae009-da8b-4a6b-b5ff-ff205216ed34",
      "version": 13
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 16,
    "major": 48,
    "minor": 2,
    "version": "48.2.16"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
