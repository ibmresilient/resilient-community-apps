import json
import time
import os
from typing import Literal

from resilient import SimpleClient

from fn_watsonx_analyst.util.logging_helper import create_logger

CacheObj = Literal["org"]

log = create_logger(__name__)

class PersistentCache:
    def __init__(self, cache_obj: CacheObj = "org"):
        if cache_obj == "org":
            self.expiry_time = 1200
            self.cache_file = "/tmp/org.json"
        else:
            self.expiry_time = 3000  # less than access_token expiry
            self.cache_file = "/tmp/watsonx.json"

    def fetch_data(
        self,
        res_client: SimpleClient,
        cache_obj: CacheObj = "org",
    ) -> dict:
        """
        Fetches Org JSON data from SOAR API

        Parameters:
            res_client (resilient.SimpleClient): The REST API Client

        Returns:
            org_data (dict): Org JSON data in a Python dictionary
        """
        if cache_obj == "org":
            try:
                return res_client.get("", timeout=120)
            except Exception as e:
                log.exception(e)

    def get_data(
        self, res_client: SimpleClient, cache_obj: CacheObj
    ) -> dict:
        """
        Attempts to fetch Org data from cache, otherwise fetches it from SOAR API

        Parameters:
                res_client (resilient.SimpleClient): The Resilient REST API client

        Returns:
                org_data (dict): Org JSON data in a Python dictionary
        """
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r", encoding="utf-8") as f:
                try:
                    cache = json.load(f)
                    cache_timestamp = cache.get("timestamp", 0)

                    if time.time() - cache_timestamp < self.expiry_time:
                        if cache.get("data"):
                            return cache.get("data")
                except:
                    log.debug("Invalid cache for %s", cache_obj)

        data = self.fetch_data(res_client, cache_obj)
        self._save_to_cache(data, cache_obj)
        return data

    def _save_to_cache(self, data: dict, cache_obj: CacheObj):
        """
        Save the fetched data and timestamp to the cache file

        Parameters:
            data (dict): Data to persist in cache
        """
        try:
            cache = {"data": data, "timestamp": time.time()}
            with open(self.cache_file, "w") as f:
                json.dump(cache, f)
        except Exception:
            log.error("Warning: unable to cache data...")
