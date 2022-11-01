import os
import json


class MockRestClient:
    def __init__(self):
        self.get_db  = {}
        self.post_db = {}
    
    def add_get_request(self, url, response):
        self.get_db[url] = response

    def add_post_request(self, url, response):
        self.post_db[url] = response

    def get(self, url):
        return self.get_db.get(url)

    def post(self, url, payload):
        return self.post_db.get(url)


class MockResponse:
    def __init__(self, status_code, message): 
        self.status_code = status_code
        self.message = message


def check_request_parameters(method, url, body, headers, callback):
    assert url
    assert method.lower() in ["post", "get"]
    assert headers
    assert callback
    try :
        return json.loads(body)
    except TypeError as err:
        raise "Request Error: Improper body format"


def json_read(path):
    with open(path) as open_file:
        data = json.loads(open_file.read())
    return data