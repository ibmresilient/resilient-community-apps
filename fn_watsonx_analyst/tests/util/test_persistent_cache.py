# Assisted by watsonx Code Assistant 
import time
import unittest
import os
from unittest.mock import patch
from resilient import SimpleClient

from fn_watsonx_analyst.util.persistent_org_cache import PersistentCache, ACCESS_TOKEN_ENDPOINT
from tests.helper import FakeResponse

get_lock = False
def mocked_client_get(_self, url, timeout):
    global get_lock
    if get_lock:
        raise Exception("Should have hit cache")
    if url == "":
        get_lock = True
        return {"test": 1}

post_lock = False # when True, disallow api key fetches, it should be a cache hit
def mocked_client_post(url, data=None, _json=None, **kwargs):
    global post_lock
    if post_lock and os.path.exists("/tmp/org.json"):
        raise Exception("Should have hit cache")
    if url == ACCESS_TOKEN_ENDPOINT:
        post_lock = True
        return FakeResponse(200, {"access_token": data["apikey"]})

@patch("requests.post", mocked_client_post)
@patch("resilient.SimpleClient.get", mocked_client_get)
class TestPersistentCache(unittest.TestCase):
    def setUp(self):
        global post_lock
        post_lock = False
        self.watsonx_cache = PersistentCache("watsonx_key")
        self.org_cache = PersistentCache("org")
        try:
            os.remove("/tmp/watsonx.json")
        except Exception as e:
            print("warn: failed to delete watsonx.json")
            print(e)
        finally:
            try:
                os.remove("/tmp/org.json")
            except Exception as e:
                print("warn: failed to delete org.json")
                print(e)

    def test_fetch_data_watsonx(self):
        res_client = SimpleClient()
        data = self.watsonx_cache.get_data(res_client, cache_obj="watsonx", watsonx_api_key="test_key1")
        data = self.watsonx_cache.get_data(res_client, cache_obj="watsonx", watsonx_api_key="test_key1")
        assert data["access_token"] == "test_key1"

    def test_get_data_org(self):
        res_client = SimpleClient()
        data = self.org_cache.get_data(res_client, cache_obj="org")
        data = self.org_cache.get_data(res_client, cache_obj="org")
        self.assertIsInstance(data, dict)

    def test_save_to_cache(self):
        data = {"test": "data"}
        self.org_cache._save_to_cache(data, cache_obj="org")
        self.assertTrue(os.path.exists(self.org_cache.cache_file))
