# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
import logging
from cachetools import cached, TTLCache

LOG = logging.getLogger(__name__)
WIKI_URL = "/wikis"

class WikiHelper():
    def __init__(self, res_client):
        self.res_client = res_client

    def get_wiki_contents(self, wiki_title, wiki_parent_path):
        # grab the wiki content
        wiki_id, _ = self.get_wiki_by_title(wiki_title, wiki_parent_path)
        if not wiki_id:
            return None

        return self.res_client.get('{}/{}'.format(WIKI_URL, wiki_id))

    def get_wiki_by_title(self, title, parent_path_list):
        # get the wikis for the org
        wikis = self.get_wikis()

        for parent_name in parent_path_list:
            if parent_name in wikis:
                wikis = wikis[parent_name]['children']
            else:
                LOG.error(wikis)
                raise ValueError(u"Unable to find parent page: %s", parent_name)

        if title in wikis:
            return wikis[title]['id'], wikis[title]['parent']

        return None, None

    @cached(cache=TTLCache(maxsize=30, ttl=60))
    def get_wikis(self):
        # get the wikis for the org
        wikis = self.res_client.get(WIKI_URL)

        # build index of ids and titles
        return self._index_wikis(wikis['entities'])

    def _index_wikis(self, entities):
        index = {}
        for entity in entities:
            index[entity["title"]] = {
                "id": entity["id"],
                "parent": entity["parent"],
                "children": self._index_wikis(entity["children"])
            }

        return index

    def create_wiki(self, wiki_title, wiki_parent_id, content):
        payload = {
            "title": wiki_title,
            "text": {
                "format": "text",
                "content": content
            }
        }

        if wiki_parent_id:
            payload['parent'] = wiki_parent_id

        return self.res_client.post(WIKI_URL, payload)

    def update_wiki(self, wiki_id, wiki_title, wiki_parent_id, content):
        payload = {
            "id": wiki_id,
            "title": wiki_title,
            "text": {
                "format": "text",
                "content": content
            }
        }

        if wiki_parent_id:
            payload['parent'] = wiki_parent_id

        wiki_url = '{}/{}'.format(WIKI_URL, wiki_id)
        return self.res_client.put(wiki_url, payload)

    def is_wiki_id(self, title_or_id):
        """[Determine if this is a title or id]

        Args:
            title_or_id ([str]): [string encoded id or title]
        Return:
            numeric id or string version
        """
        try:
            return "id", int(title_or_id)
        except ValueError:
            return "title", title_or_id
