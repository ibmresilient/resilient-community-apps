class MockResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    def json(self):
        return self.data


class AuthenticationMock:
    
    def get_token(self):
        pass

    def get_headers(self):
        return {"Authorization": "Bearer token"}


def give_response(status_code, data):
    return MockResponse(status_code, data)


GUIDS_MOCK = {
    "resources": [
        {
            "entity": {
                "name": "test1",
                "space_guid": "space",
                "state": "STARTED"
            },
            "metadata": {
                "guid": "guid",
                "updated_at": "2012-01-01T13:00:00Z"
            }
        },

        {
            "entity": {
                "name": "test2",
                "space_guid": "space",
                "state": "STOPPED"
            },
            "metadata": {
                "guid": "guid",
                "updated_at": "2012-01-01T13:00:00Z"
            }
        }
    ]
}