class MockedResponse:
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = "mock data"

    def __len__(self):
        return len(self.text)

    def observable_search(self, **kwargs):
        mock_successful_result = {
            "version": 2.0,
            "success": True,
            "reason": None,
            "content": [
                {
                "context": [],
                "created": "2022-04-04T18:52:23.699000",
                "description": None,
                "human_url": "http://localhost:8080/observable/624b3e67f533f89c2f700992",
                "id": "624b3e67f533f89c2f700992",
                "last_analyses": {},
                "sources": [],
                "tags": [
                    {
                    "first_seen": "2022-04-04T18:52:23.751000",
                    "fresh": True,
                    "last_seen": "2022-04-04T18:52:23.751000",
                    "name": "dridex"
                    }
                ],
                "type": "Path",
                "url": "http://localhost:8080/api/observable/624b3e67f533f89c2f700992",
                "value": "C:\\Users\\admin\\AppData\\Roaming\\Adada\\stolen.dat"
                }
            ],
            "raw": None,
            "inputs": {
                "yeti_artifact_type": "File Path",
                "yeti_artifact_value": "C:\\Users\\admin\\AppData\\Roaming\\Adada\\stolen.dat"
            },
            "metrics": {
                "version": "1.0",
                "package": "fn-yeti",
                "package_version": "1.0.0",
                "host": "My Host",
                "execution_time_ms": 37,
                "timestamp": "2022-04-04 16:50:55"
            }
            }
        return mock_successful_result
