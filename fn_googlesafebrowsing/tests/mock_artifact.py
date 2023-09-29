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
                'matches': [{
                    'threatType': 'MALWARE',
                    'platformType': 'ANY_PLATFORM',
                    'threat': {
                        'url': 'http://malware.testing.google.test/testing/malware/*'
                    },
                    'cacheDuration': '300s',
                    'threatEntryType': 'URL'
                }]
            },
            'raw': None,
            'inputs': {
                'googlesafebrowsing_artifact_value': 'http://malware.testing.google.test/testing/malware/*',
                'googlesafebrowsing_artifact_type': 'URL'
            },
            'metrics': {
                'version': '1.0',
                'package': 'fn-googlesafebrowsing',
                'package_version': '1.0.0',
                'host': 'My Host',
                'execution_time_ms': 30134,
                'timestamp': '2022-02-17 15:58:26'
            }
        }
        return mock_successful_result
        