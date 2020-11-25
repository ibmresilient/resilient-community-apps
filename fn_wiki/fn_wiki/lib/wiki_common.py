# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from cachetools import cached, TTLCache

WIKI_URL = "/wikis"

class WikiHelper():
    def __init__(self, res_client):
        self.res_client = res_client

    def get_wiki_id_by_title(self, title_or_id, parent_title_or_id):
        # get the wikis for the org
        all_wikis = self.get_wikis()

        id_type, wiki_title  = self.is_wiki_id(title_or_id)
        parent_type = parent_wiki_title = None
        if parent_title_or_id:
            parent_type, parent_wiki_title = self.is_wiki_id(parent_title_or_id)

        # match wiki defined by workflow to get id
        for wiki in all_wikis['entities']:
            if wiki[id_type] == wiki_title and parent_title_or_id is None:
                return wiki['id'], None

            if parent_title_or_id is None or wiki[parent_type] == parent_wiki_title:
                # look for child pages
                for child in wiki['children']:
                    if child[id_type] == wiki_title:
                        return child['id'], wiki['id']

        return None, None

    @cached(cache=TTLCache(maxsize=30, ttl=60))
    def get_wikis(self):
        # get the wikis for the org
        return self.res_client.get(WIKI_URL)

    def get_wiki_contents(self, wiki_title_or_id, wiki_parent_title_or_id):
        # grab the wiki content
        wiki_id, wiki_parent_id = self.get_wiki_id_by_title(wiki_title_or_id, wiki_parent_title_or_id)
        if not wiki_id:
            return None

        return self.res_client.get('{}/{}'.format(WIKI_URL, wiki_id))

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
