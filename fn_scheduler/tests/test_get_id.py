# -*- coding: utf-8 -*-
"""
Unit tests for get_id().
Verifies case-insensitive lookup by display_name.

Note: the incident REST endpoint only returns 'playbook_handle' and
'display_name' per playbook entry. The export key (name field) is not
present in the incident response, so export key matching is not supported.
Users must enter the Playbook display name (any casing is accepted).
"""
import pytest
from fn_scheduler.components.create_a_scheduled_rule import get_id

PLAYBOOKS = [
    {
        "display_name": "Demo Scheduled Playbook",
        "playbook_handle": 102
    }
]

ACTIONS = [
    {"id": 24, "name": "Test Rule", "enabled": True},
    {"id": 25, "name": "Disabled Rule", "enabled": False}
]


@pytest.mark.parametrize("rule_name, expected", [
    # Playbook: exact display_name
    ("Demo Scheduled Playbook",   102),
    # Playbook: lowercase display_name — case-insensitive match
    ("demo scheduled playbook",   102),
    # Playbook: uppercase display_name — case-insensitive match
    ("DEMO SCHEDULED PLAYBOOK",   102),
    # Rule: exact name
    ("Test Rule",                  24),
    # Rule: lowercase name — case-insensitive match
    ("test rule",                  24),
    # Disabled rule: must not match
    ("Disabled Rule",            None),
    # Unknown: must return None
    ("nonexistent",              None),
])
def test_get_id(rule_name, expected):
    assert get_id(ACTIONS, PLAYBOOKS, rule_name) == expected
