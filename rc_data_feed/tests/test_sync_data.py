# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
from rc_data_feed.components.feed_ingest import PluginPool

WORKSPACE_MAP = {
    "Default Workspace": ["elastic_feed"],
    "WorkspaceA": [],
    "WorkspaceB": ["elastic_feed", "resilient_feed"]
}

WORKSPACE_MAP_B = {
    "Default Workspace": "elastic_feed"
}

def test_is_workspace_valid_success():

    pool1 = PluginPool(None, 
                      None, 
                      ["elastic_feed"],
                      WORKSPACE_MAP,
                      False)

    assert pool1._is_workspace_valid("Default Workspace", "elastic_feed")
    assert pool1._is_workspace_valid("WorkspaceB", "elastic_feed")

    pool2 = PluginPool(None, 
                      None, 
                      [],
                      None,
                      False)

    assert pool2._is_workspace_valid("Default Workspace", "elastic_feed")
    assert pool2._is_workspace_valid("WorkspaceX", "elastic_feed")

    pool3 = PluginPool(None, 
                      None, 
                      ["elastic_feed"],
                      WORKSPACE_MAP_B,
                      False)

    assert pool3._is_workspace_valid("Default Workspace", "elastic_feed")


def test_is_workspace_valid_fail():

    pool1 = PluginPool(None, 
                      None, 
                      ["elastic_feed"],
                      WORKSPACE_MAP,
                      False)

    assert not pool1._is_workspace_valid("workspace_not_found", "elastic_feed")
    assert not pool1._is_workspace_valid("WorkspaceA", "feed_not_found")
    assert not pool1._is_workspace_valid("WorkspaceB", "feed_not_found")

    pool1 = PluginPool(None, 
                      None, 
                      ["elastic_feed"],
                      WORKSPACE_MAP_B,
                      False)

    assert not pool1._is_workspace_valid("Default Workspace", "feed_not_found")
