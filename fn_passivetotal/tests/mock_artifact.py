class MockedResponse:
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = "mock data"

    def json(self):
        mock_successful_result = {
            'version': 2.0,
            'success': True,
            'reason': None,
            # Added so funct_fn_passivetotal.py can reach "tags_hits_str"
            'tags': 'ransomeware, compromised',
            'content': [
                {'pdns_hit_number': 0},
                {'pdns_first_seen': None},
                {'pdns_last_seen': None},
                {'subdomain_hits_number': None},
                {'first_ten_subdomains': None},
                {'tags_hits_str': 'ransomeware, compromised'},
                {'classification_hit': None},
                {'report_url': 'https://community.riskiq.com/search/45.146.165.37'}
                ],
                'raw': None,
                'inputs': {
                    'passivetotal_artifact_type': 'IP Address',
                    'passivetotal_artifact_value': '45.146.165.37'
                },
                'metrics': {
                    'version': '1.0',
                    'package': 'fn-passivetotal',
                    'package_version': '1.0.0',
                    'host': 'My Host',
                    'execution_time_ms': 2392,
                    'timestamp': '2022-03-10 14:21:43'
                    }
                }
        return mock_successful_result