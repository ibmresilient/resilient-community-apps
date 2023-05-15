import os, json
import pytest, logging
from resilient_lib import RequestsCommon

APP_CONFIG = {
    "directory_id"   : "1d8a5928-8678-408e-ab06-50ca7e01766a",
    "application_id" : "18d10049-72e3-4652-ac9f-d9b13f24303c",
    "secret_value"   : "oCN8Q~1I0dFCI_x1kI6EseRxeTmNazVJboA0ZaMF"}

PATH_TEST_DATA = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
PATH_MS_USERS = os.path.join(PATH_TEST_DATA, "find_all_users.json")
PATH_MS_GROUP = os.path.join(PATH_TEST_DATA, "find_group.json")
PATH_WRITE_GROUPS_JSON = os.path.join(PATH_TEST_DATA, "write_group.json")
PATH_RESILIENT_USERS = os.path.join(PATH_TEST_DATA, "resilient_users.json")
PATH_RESILIENT_GROUP = os.path.join(PATH_TEST_DATA, "resilient_groups.json")

@pytest.fixture(scope="function")
def required_parameters():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    header = {
        'Authorization': 'Bearer ID123',
        'Content-type': 'application/json'}
    yield {
        "rc" : RequestsCommon(),
        "logger" : log,
        "header" : header,
        "resclient" : None}

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


def check_request_parameters(**kwargs):
    assert "url" in kwargs
    assert "method" in kwargs and kwargs["method"].lower() in ["put", "post", "get", "delete"]
    assert "headers" in kwargs
    assert "callback" in kwargs
    if "body" in kwargs and kwargs.get("body"):

        print(kwargs["body"])
        try :
            return json.loads(kwargs["body"])
        except Exception as err:
            raise TypeError("Request Error: Improper body format") from err


def json_read(path):
    with open(path) as open_file:
        data = json.loads(open_file.read())
    return data
