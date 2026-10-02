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
        'content': {
            'data': {
                'ipAddress': '110.77.136.226',
                'isPublic': True,
                'ipVersion': 4,
                'isWhitelisted': False,
                'abuseConfidenceScore': 100,
                'countryCode': 'TH',
                'usageType': None,
                'isp': 'CAT Telecom Public Company Ltd',
                'domain': 'cattelecom.com',
                'hostnames': [],
                'countryName': 'Thailand',
                'totalReports': 105,
                'numDistinctUsers': 35,
                'lastReportedAt': '2022-02-08T17:10:55+00:00',
                'reports': [{
                    'reportedAt': '2022-02-08T17:10:55+00:00',
                    'comment': 'Attempted Brute Force (dovecot)',
                    'categories': [18],
                    'reporterId': 34703,
                    'reporterCountryCode': 'GB',
                    'reporterCountryName': 'United Kingdom of Great Britain and Northern Ireland'
                }]
            }
        },
        'raw': None,
        'inputs': {
            'abuseipdb_artifact_type': 'IP Address',
            'abuseipdb_artifact_value': '110.77.136.226'
            },
        'metrics': {
            'version': '1.0',
            'package': 'fn-abuseipdb',
            'package_version': '1.0.0',
            'host': '',
            'execution_time_ms': 4498,
            'timestamp': '2022-02-09 13:29:46'
            }
        }
        return mock_successful_result
