def get_mock_config_data():
    return u"""[fn_spamhaus_query]
# The API endpoint URL to query Spamhaus Web Query Service
spamhaus_wqs_url = https://apibl.spamhaus.net/lookup/v1/{}/{}
spamhaus_dqs_key = gkoga24t6zag5tpj6rsbxz722e
# Proxy Configuration if any by default will be None
http_proxy=
https_proxy=
"""


def get_mock_input_data_dict():
    return {'spamhaus_query_string': '127.0.0.2', 'spamhaus_search_resource': 'SBL'}


def get_mock_output_data_dict():
    return {'inputs': {'spamhaus_search_resource': 'SBL', 'spamhaus_query_string': '127.0.0.2'},
            'metrics': {'package': 'fn-spamhaus-query', 'timestamp': '2019-05-14 18:22:12', 'package_version': '1.0.0',
                        'host': 'oc3777881733.ibm.com', 'version': '1.0', 'execution_time_ms': 1289}, 'success': True,
            'content': {u'status': 200, u'resp': [1002], 'is_in_blocklist': True,
                        1002: {'URL': 'https://www.spamhaus.org/sbl/',
                               'explanation': 'IP addresses are listed on the SBL because they appear to Spamhaus to be under the control of, used by, or made available for use by spammers and abusers in unsolicited bulk email or other types of Internet-based abuse that threatens networks or users.',
                               'dataset': 'SBL'}},
            'raw': '{"status": 200, "resp": [1002], "is_in_blocklist": true, "1002": {"URL": "https://www.spamhaus.org/sbl/", "explanation": "IP addresses are listed on the SBL because they appear to Spamhaus to be under the control of, used by, or made available for use by spammers and abusers in unsolicited bulk email or other types of Internet-based abuse that threatens networks or users.", "dataset": "SBL"}}',
            'reason': None, 'version': '1.0'}

