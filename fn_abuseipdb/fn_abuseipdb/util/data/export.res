{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        }
      ],
      "enabled": true,
      "export_key": "AbuseIPDB Check IP Address Blocklist",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "AbuseIPDB Check IP Address Blocklist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "f6f43731-35c7-45bc-8331-29a173ed70fc",
      "view_items": [],
      "workflows": [
        "abuseipdb_check_ip_address_blocklist"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1647460346086,
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
      "export_key": "__function/abuseipdb_artifact_value",
      "hide_notification": false,
      "id": 271,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "abuseipdb_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "templates": [],
      "text": "abuseipdb_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d7001b29-3bca-495f-abbb-39ee068b9356",
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
      "export_key": "__function/abuseipdb_range_of_days",
      "hide_notification": false,
      "id": 282,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "abuseipdb_range_of_days",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "templates": [],
      "text": "abuseipdb_range_of_days",
      "tooltip": "Range of days from current time to get reports. Default is 30",
      "type_id": 11,
      "uuid": "f1463eae-adc0-4c3b-be0e-ea2f8f54e502",
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
      "export_key": "__function/abuseipdb_artifact_type",
      "hide_notification": false,
      "id": 272,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "abuseipdb_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "templates": [],
      "text": "abuseipdb_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "156070d3-a12a-4429-8084-5f7d98e027b7",
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
      "created_date": 1643921317640,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted. Needs an AbuseIPDB account and an v2 api key to work.",
        "format": "text"
      },
      "destination_handle": "abuseipdb",
      "display_name": "AbuseIPDB",
      "export_key": "fn_abuseipdb",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1646160939122,
      "name": "fn_abuseipdb",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"data\": {\"ipAddress\": \"110.77.136.226\", \"isPublic\": true, \"ipVersion\": 4, \"isWhitelisted\": false, \"abuseConfidenceScore\": 100, \"countryCode\": \"TH\", \"usageType\": null, \"isp\": \"CAT Telecom Public Company Ltd\", \"domain\": \"cattelecom.com\", \"hostnames\": [], \"countryName\": \"Thailand\", \"totalReports\": 93, \"numDistinctUsers\": 32, \"lastReportedAt\": \"2022-02-08T17:10:55+00:00\", \"reports\": [{\"reportedAt\": \"2022-02-08T17:10:55+00:00\", \"comment\": \"Attempted Brute Force (dovecot)\", \"categories\": [18], \"reporterId\": 34703, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-06T19:27:40+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-06T06:05:38+00:00\", \"comment\": \"5 Login Attempts\", \"categories\": [14, 18], \"reporterId\": 5371, \"reporterCountryCode\": \"CA\", \"reporterCountryName\": \"Canada\"}, {\"reportedAt\": \"2022-02-06T04:13:11+00:00\", \"comment\": \"Feb  6 05:13:10 soli-gate postfix/smtpd[19017]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-02-06T00:17:05+00:00\", \"comment\": \"Distributed brute force attack\", \"categories\": [18], \"reporterId\": 5688, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-02-05T21:32:31+00:00\", \"comment\": \"Multiple bruteforce attempts\", \"categories\": [18], \"reporterId\": 48314, \"reporterCountryCode\": \"RU\", \"reporterCountryName\": \"Russian Federation\"}, {\"reportedAt\": \"2022-02-05T19:24:27+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-05T08:05:32+00:00\", \"comment\": \"6 Login Attempts\", \"categories\": [14, 18], \"reporterId\": 5371, \"reporterCountryCode\": \"CA\", \"reporterCountryName\": \"Canada\"}, {\"reportedAt\": \"2022-02-05T00:47:10+00:00\", \"comment\": \"Attempted Brute Force (dovecot)\", \"categories\": [18], \"reporterId\": 34703, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-04T22:14:33+00:00\", \"comment\": \"Feb  4 23:14:31 soli-gate postfix/smtpd[3749]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-02-04T19:22:53+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-04T16:40:48+00:00\", \"comment\": \"failed_logins\", \"categories\": [18], \"reporterId\": 23948, \"reporterCountryCode\": \"NL\", \"reporterCountryName\": \"Netherlands\"}, {\"reportedAt\": \"2022-02-04T08:47:03+00:00\", \"comment\": \"2022-02-04T09:45:50+01:00 \u003cmasked\u003e exim[798150]: fixed_login authenticator failed for ([127.0.0.1]) [110.77.136.226]: 535 Incorrect authentication data (set_id=heger.csaba@sma.hu)\", \"categories\": [18], \"reporterId\": 35002, \"reporterCountryCode\": \"HU\", \"reporterCountryName\": \"Hungary\"}, {\"reportedAt\": \"2022-02-03T23:52:03+00:00\", \"comment\": \"SMTP auth failures (1)\", \"categories\": [18], \"reporterId\": 18150, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-03T20:34:35+00:00\", \"comment\": \"Feb  3 14:34:32 mailman postfix/smtpd[20987]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\", \"categories\": [18], \"reporterId\": 10374, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-02-03T19:19:03+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [risda.net@risda.net] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-02-03T18:36:23+00:00\", \"comment\": \"Feb  3 19:36:22 soli-gate postfix/smtpd[974]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-02-03T03:05:33+00:00\", \"comment\": \"6 Login Attempts\", \"categories\": [14, 18], \"reporterId\": 5371, \"reporterCountryCode\": \"CA\", \"reporterCountryName\": \"Canada\"}, {\"reportedAt\": \"2022-02-03T02:22:01+00:00\", \"comment\": \"Feb  3 03:22:01 soli-gate postfix/smtpd[9393]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-02-03T02:18:00+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [silent] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-02-02T20:54:32+00:00\", \"comment\": \"Multiple bruteforce attempts\", \"categories\": [18], \"reporterId\": 48314, \"reporterCountryCode\": \"RU\", \"reporterCountryName\": \"Russian Federation\"}, {\"reportedAt\": \"2022-02-02T06:39:16+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-02-02T03:05:29+00:00\", \"comment\": \"6 Login Attempts\", \"categories\": [14, 18], \"reporterId\": 5371, \"reporterCountryCode\": \"CA\", \"reporterCountryName\": \"Canada\"}, {\"reportedAt\": \"2022-02-01T23:56:08+00:00\", \"comment\": \"SMTP AUTH LOGIN\", \"categories\": [18], \"reporterId\": 15073, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-02-01T22:29:41+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [silent] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-02-01T06:52:54+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [risda.net] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-02-01T02:20:23+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [phid] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-31T22:09:04+00:00\", \"comment\": \"$f2bV_matches\", \"categories\": [18], \"reporterId\": 19154, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-31T19:21:39+00:00\", \"comment\": \"Brute force attempt\", \"categories\": [18, 20], \"reporterId\": 25085, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-31T18:07:33+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-31T17:29:04+00:00\", \"comment\": \"2022-01-31T18:28:19+01:00 \u003cmasked\u003e exim[408831]: fixed_login authenticator failed for ([127.0.0.1]) [110.77.136.226]: 535 Incorrect authentication data (set_id=zsolt.makovsky@makovsky.hu)\", \"categories\": [18], \"reporterId\": 35002, \"reporterCountryCode\": \"HU\", \"reporterCountryName\": \"Hungary\"}, {\"reportedAt\": \"2022-01-30T22:00:04+00:00\", \"comment\": \"SMTP-SASL bruteforce attempt\", \"categories\": [18], \"reporterId\": 14854, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-30T18:07:22+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-30T15:45:00+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [hadirah@dzoul.net] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-30T15:17:03+00:00\", \"comment\": \"Jan 30 16:17:02 config dovecot: auth-worker(23532): sql(andreas.rauterberg@aknds.de,110.77.136.226,\u003c1fPzKM7W76JuTYji\u003e): unknown user\\n...\", \"categories\": [11, 18], \"reporterId\": 73069, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-30T09:55:26+00:00\", \"comment\": \"(PERMBLOCK) 110.77.136.226 (TH/Thailand/-) has had more than 2 temp blocks in the last 86400 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-29T22:28:46+00:00\", \"comment\": \"Unauthorized connection attempt/Brute force attempt\", \"categories\": [18, 20], \"reporterId\": 75374, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-01-29T14:04:59+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [postoffice@syok.org] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-29T12:59:00+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [postoffice] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-29T00:50:40+00:00\", \"comment\": \"Attempted Brute Force (dovecot)\", \"categories\": [18], \"reporterId\": 34703, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-28T14:16:04+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 5 distributed smtpauth attacks on account [mail] in the last 3600 secs\", \"categories\": [15], \"reporterId\": 32379, \"reporterCountryCode\": \"CA\", \"reporterCountryName\": \"Canada\"}, {\"reportedAt\": \"2022-01-28T04:14:53+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-27T13:58:25+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [accounts] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-27T10:32:05+00:00\", \"comment\": \"Jan 27 04:32:03 mailman postfix/smtpd[12384]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\", \"categories\": [18], \"reporterId\": 10374, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-01-27T10:15:40+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [webmail@dzoul.net] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-26T18:13:25+00:00\", \"comment\": \"Brute force attempt\", \"categories\": [18, 20], \"reporterId\": 25085, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-26T09:06:45+00:00\", \"comment\": \"$f2bV_matches\", \"categories\": [18], \"reporterId\": 19154, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-26T08:50:52+00:00\", \"comment\": \"Jan 26 03:20:51 posta postfix/smtps/smtpd[1297084]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: UGFzc3dvcmQ6\\nJan 26 09:50:52 posta postfix/smtps/smtpd[1494620]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: UGFzc3dvcmQ6\\n...\", \"categories\": [11, 18, 20], \"reporterId\": 62692, \"reporterCountryCode\": \"CZ\", \"reporterCountryName\": \"Czechia\"}, {\"reportedAt\": \"2022-01-26T04:21:55+00:00\", \"comment\": \"Jan 26 05:21:55 soli-gate postfix/smtpd[25533]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-26T04:02:53+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-25T08:45:39+00:00\", \"comment\": \"$f2bV_matches\", \"categories\": [18], \"reporterId\": 19154, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-25T05:43:23+00:00\", \"comment\": \"(PERMBLOCK) 110.77.136.226 (TH/Thailand/-) has had more than 2 temp blocks in the last 86400 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-24T23:05:20+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [bounce] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-24T14:34:04+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [marketing] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-24T10:30:15+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [domains@coffeeclassic.com.my] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-24T06:17:48+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-24T03:51:17+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-23T21:15:33+00:00\", \"comment\": \"Jan 23 22:15:31 fiha postfix/smtpd[75155]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: UGFzc3dvcmQ6\\n...\", \"categories\": [11, 18], \"reporterId\": 54731, \"reporterCountryCode\": \"PL\", \"reporterCountryName\": \"Poland\"}, {\"reportedAt\": \"2022-01-23T15:33:18+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [auto@syok.org] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-23T07:51:23+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [order@bicoms.com.my] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-22T20:54:56+00:00\", \"comment\": \"Jan 22 21:54:55 soli-gate postfix/smtpd[30628]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-22T19:50:21+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [system] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-22T18:16:12+00:00\", \"comment\": \"Distributed brute force attack\", \"categories\": [18], \"reporterId\": 5688, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-01-22T09:08:40+00:00\", \"comment\": \"failed_logins\", \"categories\": [18], \"reporterId\": 23948, \"reporterCountryCode\": \"NL\", \"reporterCountryName\": \"Netherlands\"}, {\"reportedAt\": \"2022-01-21T23:34:31+00:00\", \"comment\": \"Repeated SMTP failures\", \"categories\": [18], \"reporterId\": 50845, \"reporterCountryCode\": \"US\", \"reporterCountryName\": \"United States of America\"}, {\"reportedAt\": \"2022-01-21T09:58:06+00:00\", \"comment\": \"Jan 21 10:58:06 soli-gate postfix/smtpd[1308]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [18], \"reporterId\": 74775, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-20T23:31:28+00:00\", \"comment\": \"Jan 20 04:19:34 posta postfix/smtps/smtpd[2600602]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: UGFzc3dvcmQ6\\nJan 21 00:31:28 posta postfix/smtps/smtpd[3051688]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: UGFzc3dvcmQ6\\n...\", \"categories\": [11, 18, 20], \"reporterId\": 62692, \"reporterCountryCode\": \"CZ\", \"reporterCountryName\": \"Czechia\"}, {\"reportedAt\": \"2022-01-20T06:34:43+00:00\", \"comment\": \"SMTP-25/465/587 BRUTE FORCE ATTEMPT\", \"categories\": [11, 18], \"reporterId\": 53276, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-20T04:40:55+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [ticket@gemini.com.my] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-19T12:52:11+00:00\", \"comment\": \"Attempted Brute Force (dovecot)\", \"categories\": [18], \"reporterId\": 34703, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-18T16:27:44+00:00\", \"comment\": \"Attempts to login to mail server with wrong username and/or password\", \"categories\": [18], \"reporterId\": 51787, \"reporterCountryCode\": \"NL\", \"reporterCountryName\": \"Netherlands\"}, {\"reportedAt\": \"2022-01-18T03:35:28+00:00\", \"comment\": \"2022-01-18T04:35:25.199554 X postfix/smtps/smtpd[438363]: warning: unknown[110.77.136.226]: SASL CRAM-MD5 authentication failed: PDAxMTE2NTc1MTE3NDg3ODUuMTY0MjQ3NjkyMUBkZWRpNC5taWNsZWQubmV0Pg==\\n2022-01-18T04:35:26.656970 X postfix/smtps/smtpd[438363]: lost connection after AUTH from unknown[110.77.136.226]\\n2022-01-18T04:35:26.657258 X postfix/smtps/smtpd[438363]: disconnect from unknown[110.77.136.226] ehlo=1 auth=0/1 commands=1/2\", \"categories\": [18], \"reporterId\": 28604, \"reporterCountryCode\": \"NL\", \"reporterCountryName\": \"Netherlands\"}, {\"reportedAt\": \"2022-01-17T20:43:33+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-17T16:49:37+00:00\", \"comment\": \"Jan  9 14:42:50 mail postfix/smtpd[21172]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\nJan 13 05:53:06 mail postfix/smtpd[15834]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\nJan 17 17:49:37 mail postfix/smtpd[20898]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\n...\", \"categories\": [15, 18], \"reporterId\": 53366, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-17T05:48:46+00:00\", \"comment\": \"Attempted Brute Force (dovecot)\", \"categories\": [18], \"reporterId\": 34703, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-17T04:15:32+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-17T02:03:46+00:00\", \"comment\": \"Jan 17 03:03:45 ns postfix/smtps/smtpd[1685565]: warning: unknown[110.77.136.226]: SASL CRAM-MD5 authentication failed: authentication failure\\n...\", \"categories\": [10, 11, 14, 18], \"reporterId\": 27823, \"reporterCountryCode\": \"ES\", \"reporterCountryName\": \"Spain\"}, {\"reportedAt\": \"2022-01-16T20:41:25+00:00\", \"comment\": \"Email Auth Brute force attack 1/1 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-16T14:21:43+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [richard] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-16T04:09:14+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-16T03:45:30+00:00\", \"comment\": \"SMTP AUTH 110.77.136.226 (SMTP_LOGIN_ATTEMPT)\", \"categories\": [18], \"reporterId\": 12605, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-15T23:59:45+00:00\", \"comment\": \"Suspicious access to SMTP/POP/IMAP services.\", \"categories\": [15], \"reporterId\": 23367, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-15T21:43:42+00:00\", \"comment\": \"Attempted Brute Force (dovecot)\", \"categories\": [18], \"reporterId\": 34703, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-15T13:17:26+00:00\", \"comment\": \"110.77.136.226 (TH/Thailand/-), 2 distributed smtpauth attacks on account [kirei] in the last 3600 secs\", \"categories\": [18], \"reporterId\": 55388, \"reporterCountryCode\": \"MY\", \"reporterCountryName\": \"Malaysia\"}, {\"reportedAt\": \"2022-01-15T04:02:08+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-15T03:55:45+00:00\", \"comment\": \"SMTP SASL brute-force attempt\", \"categories\": [18, 20], \"reporterId\": 36200, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-15T03:16:48+00:00\", \"comment\": \"SMTP AUTH 110.77.136.226 (SMTP_LOGIN_ATTEMPT)\", \"categories\": [18], \"reporterId\": 12605, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-14T21:47:02+00:00\", \"comment\": \"Jan 14 22:47:00 lince postfix/smtpd[27858]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\nJan 14 22:47:01 lince postfix/smtpd[27858]: lost connection after AUTH from unknown[110.77.136.226]\", \"categories\": [18], \"reporterId\": 52343, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}, {\"reportedAt\": \"2022-01-14T03:57:57+00:00\", \"comment\": \"SMTP auth dictionary attack\", \"categories\": [18], \"reporterId\": 52437, \"reporterCountryCode\": \"IT\", \"reporterCountryName\": \"Italy\"}, {\"reportedAt\": \"2022-01-13T23:10:03+00:00\", \"comment\": \"Unauthorized SMTP/IMAP/POP3 connection attempt\", \"categories\": [18], \"reporterId\": 25736, \"reporterCountryCode\": \"NL\", \"reporterCountryName\": \"Netherlands\"}, {\"reportedAt\": \"2022-01-13T13:21:04+00:00\", \"comment\": \"Suspicious access to SMTP/POP/IMAP services.\", \"categories\": [15], \"reporterId\": 23367, \"reporterCountryCode\": \"FR\", \"reporterCountryName\": \"France\"}, {\"reportedAt\": \"2022-01-13T09:28:57+00:00\", \"comment\": \"Email Auth Brute force attack 2/2 in last day\", \"categories\": [18], \"reporterId\": 49881, \"reporterCountryCode\": \"GB\", \"reporterCountryName\": \"United Kingdom of Great Britain and Northern Ireland\"}, {\"reportedAt\": \"2022-01-12T21:09:54+00:00\", \"comment\": \"Jan 12 22:09:52 lince postfix/smtpd[16240]: warning: unknown[110.77.136.226]: SASL LOGIN authentication failed: authentication failure\\nJan 12 22:09:53 lince postfix/smtpd[16240]: lost connection after AUTH from unknown[110.77.136.226]\", \"categories\": [18], \"reporterId\": 52343, \"reporterCountryCode\": \"DE\", \"reporterCountryName\": \"Germany\"}]}}, \"raw\": null, \"inputs\": {\"abuseipdb_artifact_type\": \"IP Address\", \"abuseipdb_artifact_value\": \"110.77.136.226\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-abuseipdb\", \"package_version\": \"1.0.0\", \"host\": \"Christophers-MacBook-Pro.local\", \"execution_time_ms\": 298, \"timestamp\": \"2022-02-11 14:18:53\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"data\": {\"type\": \"object\", \"properties\": {\"ipAddress\": {\"type\": \"string\"}, \"isPublic\": {\"type\": \"boolean\"}, \"ipVersion\": {\"type\": \"integer\"}, \"isWhitelisted\": {\"type\": \"boolean\"}, \"abuseConfidenceScore\": {\"type\": \"integer\"}, \"countryCode\": {\"type\": \"string\"}, \"usageType\": {}, \"isp\": {\"type\": \"string\"}, \"domain\": {\"type\": \"string\"}, \"hostnames\": {\"type\": \"array\"}, \"countryName\": {\"type\": \"string\"}, \"totalReports\": {\"type\": \"integer\"}, \"numDistinctUsers\": {\"type\": \"integer\"}, \"lastReportedAt\": {\"type\": \"string\"}, \"reports\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"reportedAt\": {\"type\": \"string\"}, \"comment\": {\"type\": \"string\"}, \"categories\": {\"type\": \"array\", \"items\": {\"type\": \"integer\"}}, \"reporterId\": {\"type\": \"integer\"}, \"reporterCountryCode\": {\"type\": \"string\"}, \"reporterCountryName\": {\"type\": \"string\"}}}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"abuseipdb_artifact_type\": {\"type\": \"string\"}, \"abuseipdb_artifact_value\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "uuid": "f26776eb-acf7-4df7-b827-fd71a8d986a0",
      "version": 6,
      "view_items": [
        {
          "content": "156070d3-a12a-4429-8084-5f7d98e027b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f1463eae-adc0-4c3b-be0e-ea2f8f54e502",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d7001b29-3bca-495f-abbb-39ee068b9356",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "AbuseIPDB Check IP Address Blocklist",
          "object_type": "artifact",
          "programmatic_name": "abuseipdb_check_ip_address_blocklist",
          "tags": [
            {
              "tag_handle": "fn_abuseipdb",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 58,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1647460344715,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1647460344715,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea",
        "09dcb865-3269-45e8-a887-5c5f3f0bb5e1"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "abuseipdb",
      "name": "AbuseIPDB",
      "programmatic_name": "abuseipdb",
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "users": [],
      "uuid": "2359b60c-9076-435b-8c9d-194076dd59bb"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 61,
        "workflow_id": "abuseipdb_check_ip_address_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"abuseipdb_check_ip_address_blocklist\" isExecutable=\"true\" name=\"AbuseIPDB Check IP Address Blocklist\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted. Needs an AbuseIPDB account and an v2 api key to work. Default is reports from the last 30 days, but can be changed to as many as the last 365 days\u0027 reports.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_146m5zt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_166ubax\"\u003e\u003cincoming\u003eSequenceFlow_1qgcmf3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_146m5zt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1itvc92\"/\u003e\u003cserviceTask id=\"ServiceTask_1itvc92\" name=\"AbuseIPDB\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f26776eb-acf7-4df7-b827-fd71a8d986a0\"\u003e{\"inputs\":{\"f1463eae-adc0-4c3b-be0e-ea2f8f54e502\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":30}}},\"post_processing_script\":\"CATEGORIES= {\\n  3: \\\"Fraud Orders\\\",\\n  4: \\\"DDoS Attack\\\",\\n  5: \\\"FTP Brute-Force\\\",\\n  6: \\\"Ping of Death\\\",\\n  7: \\\"Phishing\\\",\\n  8: \\\"Fraud VoIP\\\",\\n  9: \\\"Open Proxy\\\",\\n  10: \\\"Web Spam\\\",\\n  11: \\\"Email Spam\\\",\\n  12: \\\"Blog Spam\\\",\\n  13: \\\"VPN IP\\\",\\n  14: \\\"Port Scan\\\",\\n  15: \\\"Hacking\\\",\\n  16: \\\"SQL Injection\\\",\\n  17: \\\"Spoofing\\\",\\n  18: \\\"Brute-Force\\\",\\n  19: \\\"Bad Web Bot\\\",\\n  20: \\\"Exploited Host\\\",\\n  21: \\\"Web App Attack\\\",\\n  22: \\\"SSH\\\",\\n  23: \\\"IoT Targeted\\\",\\n}\\n\\nif results.success:\\n  if results.content:\\n    resp_data = results.content[\u0027data\u0027]\\n    number_of_reports = resp_data[\u0027totalReports\u0027]\\n    country_name = resp_data[\u0027countryName\u0027]\\n    most_recent_report = resp_data[\u0027lastReportedAt\u0027]\\n    confidence_score = resp_data.get(\\\"abuseConfidenceScore\\\", 0)\\n    \\n    hit = []\\n    \\n    # get clean list of de-duped categories\\n    categories_names = \\\"\\\"\\n    if resp_data.get(\u0027reports\u0027):\\n        categories_list = []\\n        for report in resp_data[\u0027reports\u0027]:\\n            categories_list.extend(report[\\\"categories\\\"])\\n        categories_set = set(categories_list)  # dedup list\\n        categories_names = u\u0027, \u0027.join(CATEGORIES.get(item, \u0027unknown\u0027) for item in categories_set)\\n  \\n    \\n    # only return data if there\u0027s anything useful\\n    if number_of_reports or confidence_score:\\n      hit = [\\n        {\\n          \\\"name\\\": \\\"Confidence Score\\\",\\n          \\\"type\\\": \\\"number\\\",\\n          \\\"value\\\": \\\"{}\\\".format(confidence_score)\\n        }, \\n        {\\n          \\\"name\\\": \\\"Number of Reports\\\",\\n          \\\"type\\\": \\\"number\\\",\\n          \\\"value\\\": \\\"{}\\\".format(number_of_reports)\\n        }, \\n        {\\n          \\\"name\\\": \\\"Country\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(country_name)\\n        },\\n        {\\n          \\\"name\\\": \\\"Most Recent Report\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(most_recent_report)\\n        },\\n        {\\n          \\\"name\\\": \\\"Categories\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(categories_names)\\n        }\\n        ]\\n      artifact.addHit(\\\"AbuseIPDB Function hits added\\\", hit)\\n    else:\\n      incident.addNote(\\\"No reports or confidence score to return.\\\")\\nelse:\\n  incident.addNote(\\\"AbuseIPDB Check IP Address Blocklist failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.abuseipdb_artifact_type = artifact.type\\ninputs.abuseipdb_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_146m5zt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qgcmf3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qgcmf3\" sourceRef=\"ServiceTask_1itvc92\" targetRef=\"EndEvent_166ubax\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00ulpkw\"\u003e\u003ctext\u003eResults are returned as a hit in the artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1f6opjk\" sourceRef=\"ServiceTask_1itvc92\" targetRef=\"TextAnnotation_00ulpkw\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_166ubax\" id=\"EndEvent_166ubax_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"520\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"493\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_146m5zt\" id=\"SequenceFlow_146m5zt_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"302\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"250\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1itvc92\" id=\"ServiceTask_1itvc92_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"302\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qgcmf3\" id=\"SequenceFlow_1qgcmf3_di\"\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"520\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"416\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00ulpkw\" id=\"TextAnnotation_00ulpkw_di\"\u003e\u003comgdc:Bounds height=\"49\" width=\"100\" x=\"414\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1f6opjk\" id=\"Association_1f6opjk_di\"\u003e\u003comgdi:waypoint x=\"392\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 61,
      "creator_id": "admin@example.com",
      "description": "Pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted. Needs an AbuseIPDB account and an v2 api key to work. Default is reports from the last 30 days, but can be changed to as many as the last 365 days\u0027 reports.",
      "export_key": "abuseipdb_check_ip_address_blocklist",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647460308612,
      "name": "AbuseIPDB Check IP Address Blocklist",
      "object_type": "artifact",
      "programmatic_name": "abuseipdb_check_ip_address_blocklist",
      "tags": [
        {
          "tag_handle": "fn_abuseipdb",
          "value": null
        }
      ],
      "uuid": "a4d1ce0e-7fe0-4896-9296-0cc9d4f352d9",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
