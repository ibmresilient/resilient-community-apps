import requests
import pytest
import mock
from .mock_stix import MitreQueryMocker
from mock import patch
from fn_mitre_integration.lib import mitre_attack

class TestCache(object):
    """
    Simple test, that I learned needs to happen, because STIX cuts corners, by adding
    description of a mitigation to a technique using technique's id.
    So mitigation id == technique id, and cache is spoiled.
    """
    mitre_attack = mitre_attack.MitreAttackConnection()

    @pytest.fixture(autouse=True)
    def set_up_mock_for_query(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            yield

    def test_cache_not_shared_between_classes(self):
        print(mitre_attack.MitreAttackTechnique._cached_obj)
        mitre_attack.MitreAttackTechnique.get(self.mitre_attack, name="Port Knocking")
        mitre_attack.MitreAttackTactic.get(self.mitre_attack, name="Impact")
        print(mitre_attack.MitreAttackTechnique._cached_obj)
        print(mitre_attack.MitreAttackTactic._cached_obj)
        print(mitre_attack.MitreAttackBase._cached_obj)
        assert "Port Knocking" in mitre_attack.MitreAttackTechnique._cached_obj["name"]
        assert not "Port Knocking" in mitre_attack.MitreAttackTactic._cached_obj["name"]

        assert not "Impact" in mitre_attack.MitreAttackTechnique._cached_obj["name"]
        assert "Impact" in mitre_attack.MitreAttackTactic._cached_obj["name"]

    def test_cache_not_shared_between_classes_module_import(self):
        print(mitre_attack.MitreAttackTechnique._cached_obj)
        tech = mitre_attack.MitreAttackTechnique.get(self.mitre_attack, name="Port Knocking")
        tact = mitre_attack.MitreAttackTactic.get(self.mitre_attack, name="Impact")
        print(mitre_attack.MitreAttackTechnique._cached_obj)
        print(mitre_attack.MitreAttackTactic._cached_obj)
        print(mitre_attack.MitreAttackBase._cached_obj)
        assert "Port Knocking" in tech[0]._cached_obj["name"] and not "Port Knocking" in tact[0]._cached_obj["name"]
        assert not "Impact" in tech[0]._cached_obj["name"] and "Impact" in tact[0]._cached_obj["name"]

        assert "Port Knocking" in mitre_attack.MitreAttackTechnique._cached_obj["name"]
        assert not "Port Knocking" in mitre_attack.MitreAttackTactic._cached_obj["name"]

        assert not "Impact" in mitre_attack.MitreAttackTechnique._cached_obj["name"]
        assert "Impact" in mitre_attack.MitreAttackTactic._cached_obj["name"]
