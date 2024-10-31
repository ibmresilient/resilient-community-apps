# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
from rc_data_feed.components.threadpool import PluginPool

WORKSPACE_MAP = {
    "Default Workspace": ["elastic_feed"],
    "WorkspaceA": [],
    "WorkspaceB": ["elastic_feed", "resilient_feed"]
}

WORKSPACE_MAP_B = {
    "Default Workspace": "elastic_feed"
}

WORKSPACE_VERIZON = {
    "TMC workspace": ["postgres_feed:label1"],
    "RMC VCG workspace": ["postgres_feed:label2"],
    "RED workspace": ["postgres_feed:label3"],
    "Legal workspace": ["postgres_feed:label4"],
    "GSOC workspace": ["postgres_feed:label5"],
    "EVM workspace": ["postgres_feed:label6"],
    "ASIRT workspace": ["postgres_feed:label7"],
    "ITO workspace": ["postgres_feed:label8"],
    "TF Workspace": ["postgres_feed:label9"],
    "NCC workspace": ["postgres_feed:label10"],
    "DF Workspace": ["postgres_feed:label11"]
}

VERIZON_FEEDS = ','.join(['postgres_feed:label1', 'postgres_feed:label2', 'postgres_feed:label3', 'postgres_feed:label4', 'postgres_feed:label5', 'postgres_feed:label6', 'postgres_feed:label7', 'postgres_feed:label8', 'postgres_feed:label9', 'postgres_feed:label10', 'postgres_feed:label11'])

OPTIONS = {
    "feed_names": "",
    "timeseries": "",
    "timeseries_fields": ""
}

def test_is_workspace_valid_success():

    pool1 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_MAP,
                      False)

    assert pool1._is_workspace_valid("Default Workspace", "elastic_feed")
    assert pool1._is_workspace_valid("WorkspaceB", "elastic_feed")

    pool2 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      None,
                      False)

    assert pool2._is_workspace_valid("Default Workspace", "elastic_feed")
    assert pool2._is_workspace_valid("WorkspaceX", "elastic_feed")

    pool3 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_MAP_B,
                      False)

    assert pool3._is_workspace_valid("Default Workspace", "elastic_feed")


def test_is_workspace_valid_fail():

    pool1 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_MAP,
                      False)

    assert not pool1._is_workspace_valid("workspace_not_found", "elastic_feed")
    assert not pool1._is_workspace_valid("WorkspaceA", "feed_not_found")
    assert not pool1._is_workspace_valid("WorkspaceB", "feed_not_found")

    pool1 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_MAP_B,
                      False)

    assert not pool1._is_workspace_valid("Default Workspace", "feed_not_found")

def test_is_verizon_valid_success():

    pool1 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_VERIZON,
                      False)

    assert pool1._is_workspace_valid("TMC workspace", "postgres_feed:label1")
    assert pool1._is_workspace_valid("DF Workspace", "postgres_feed:label11")

    pool2 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      None,
                      False)

    assert pool2._is_workspace_valid("Default Workspace", "postgres_feed:label1")
    assert pool2._is_workspace_valid("WorkspaceX", "postgres_feed:label2")


def test_is_verizon_valid_fail():

    pool1 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_VERIZON,
                      False)

    assert not pool1._is_workspace_valid("workspace_not_found", "postgres_feed:label1")
    assert not pool1._is_workspace_valid("RMC VCG workspace", "postgres_feed:label1")
    assert not pool1._is_workspace_valid("DF Workspace", "feed_not_found")

    pool1 = PluginPool(None,
                      None,
                      OPTIONS,
                      {},
                      WORKSPACE_VERIZON,
                      False)

    assert not pool1._is_workspace_valid("Default Workspace", "postgres_feed:label1")
    assert not pool1._is_workspace_valid(None, "postgres_feed:label1")
    assert not pool1._is_workspace_valid("DF Workspace", None)
    assert not pool1._is_workspace_valid(None, None)
