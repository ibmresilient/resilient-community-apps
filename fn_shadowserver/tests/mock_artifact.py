class MockedResponse:
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = '0E53C14A3E48D94FF596A2824307B492 {"application_type":"Graphic/Drawing","mfg_name":"Corel Corporation","os_mfg":"Microsoft","filename":"00br2026.gif","md5":"0E53C14A3E48D94FF596A2824307B492","os_name":"Windows NT","sha1":"0000004DA6391F7F5D2F7FCCF36CEBDA60C6EA02","filesize":"2226","os_version":"Generic","product_name":"Gallery","crc32":"AA6A7B16","product_version":"750,000","source_version":"$version","source":"NIST","language":"English"}\n'

    def json(self):
        mock_successful_result = {
        'version': 2.0,
        'success': True,
        'reason': None,
        'content':
            {'application_type': 'Graphic/Drawing',
            'mfg_name': 'Corel Corporation',
            'os_mfg': 'Microsoft',
            'filename': '00br2026.gif',
            'md5': '0E53C14A3E48D94FF596A2824307B492',
            'os_name': 'Windows NT',
            'sha1': '0000004DA6391F7F5D2F7FCCF36CEBDA60C6EA02',
            'filesize': '2226',
            'os_version': 'Generic',
            'product_name': 'Gallery',
            'crc32': 'AA6A7B16',
            'product_version': '750,000',
            'source_version': '$version',
            'source': 'NIST',
            'language': 'English'},
        'raw': None,
        'inputs': 
            {'shadowserver_artifact_type': 'Malware MD5 Hash',
            'shadowserver_artifact_value': '0E53C14A3E48D94FF596A2824307B492'},
        'metrics': 
            {'version': '1.0',
            'package': 'fn-shadowserver',
            'package_version': '1.0.0',
            'host': 'My Host',
            'execution_time_ms': 220,
            'timestamp': '2022-03-22 16:40:55'}}
        return mock_successful_result