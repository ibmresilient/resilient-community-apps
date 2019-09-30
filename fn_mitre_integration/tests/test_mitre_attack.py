# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""
Note that the mitre_attack class encapsulates the
MITRE ATTACK STIX TAXII server. Since that sever is
available to public, this file is a system level test
"""

from fn_mitre_integration.lib.mitre_attack import MitreAttackConnection, MitreAttackTactic, MitreAttackTechnique, \
    MitreAttackMitigation, MitreAttackSoftware
from fn_mitre_integration.lib.mitre_attack_utils import get_tactics_and_techniques
import requests
import pytest
import mock
from .mock_stix import MitreQueryMocker
from mock import patch
import re


def url_get(url):
    ret = False
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ret = True
    except:
        ret = False
    return ret


class TestMitreTactic(object):
    mitre_attack = MitreAttackConnection()

    @pytest.fixture(autouse=True)
    def set_up_mock_for_query(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            yield

    def test_get_by_id_works(self):
        assert MitreAttackTactic.get_by_id(self.mitre_attack, "TA0007") is not None
        assert MitreAttackTactic.get_by_id(self.mitre_attack, "TA00007") is None

    def test_get_by_name_works(self):
        assert MitreAttackTactic.get_by_name(self.mitre_attack, "Collection") is not None
        assert MitreAttackTactic.get_by_name(self.mitre_attack, "Absurd Search") is None

    def test_extra_spaces_doent_fail_search(self):
        assert MitreAttackTactic.get_by_id(self.mitre_attack, " TA0007") is not None
        assert MitreAttackTactic.get_by_name(self.mitre_attack, " Collection  ") is not None

    def test_get_all(self):
        assert len(MitreAttackTactic.get_all(self.mitre_attack)) == len(MitreQueryMocker.TACTICS[0])+len(MitreQueryMocker.TACTICS[1])+len(MitreQueryMocker.TACTICS[2])

    def test_collection_name_included(self):
        tactics = MitreAttackTactic.get_by_name(self.mitre_attack, "Impact")
        assert len(tactics) == 2
        assert tactics[0].collection is not None and tactics[1].collection is not None
        assert tactics[0].collection != tactics[1].collection

    def test_mutiple_of_same_name_returns_list(self):
        tactics = MitreAttackTactic.get_by_name(self.mitre_attack, "Impact")
        assert isinstance(tactics, list)

    def test_tactic_representation_doesnt_have_unsupported_tags(self):
        """
        Mocked Impact has code tags added on purpose
        """
        tactics = MitreAttackTactic.get_by_name(self.mitre_attack, "Impact")
        dict_reps = [tactic.dict_form() for tactic in tactics]
        # check for every tactic that every field of their representation doesn't container the tag.
        assert all([("<code>" not in tactic_repr[key] for key in tactic_repr) for tactic_repr in dict_reps])

    def test_deprecated_tactic_states_so_in_description(self):
        """
        Gets tactics with name Impact, and checks that deprecation message was added.
        Deprecation flag was added to one of the mocked tactics.
        """
        tactics = MitreAttackTactic.get_by_name(self.mitre_attack, "Impact")
        assert any(x.description.startswith("Deprecated") for x in tactics)


class TestMitreTechnique(object):
    mitre_attack = MitreAttackConnection()

    @pytest.fixture(autouse=True)
    def set_up_mock_for_query(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            yield

    def test_tech_of_tactic(self):
        collection_tech = MitreAttackTechnique.get_by_tactic(self.mitre_attack,
                                                             MitreAttackTactic.get_by_name(self.mitre_attack,
                                                                                           "Collection")[0])
        assert collection_tech is not None
        assert len(collection_tech) > 1

        assert MitreAttackTactic.get_by_name(self.mitre_attack, "Command and Control")[0]\
                   .get_techniques(self.mitre_attack) is not None

    def test_all_searches_returns_list(self):
        techniques = MitreAttackTechnique.get_by_name(self.mitre_attack, "Port Knocking")
        assert isinstance(techniques, list)
        assert len(techniques) > 1
        techniques = MitreAttackTechnique.get_by_name(self.mitre_attack, "Domain Generation Algorithms")
        assert isinstance(techniques, list)
        assert len(techniques) == 1

    def test_by_id_works(self):
        tech = MitreAttackTechnique.get_by_id(self.mitre_attack,"T1205")
        assert tech is not None
        tech = MitreAttackTechnique.get_by_id(self.mitre_attack,"Made up id")
        assert tech is None

    def test_by_name_works(self):
        tech = MitreAttackTechnique.get_by_name(self.mitre_attack, "Port Knocking")
        assert tech is not None
        tech = MitreAttackTechnique.get_by_name(self.mitre_attack, "Absolutely made up name")
        assert tech is None

    def test_tech_get_all(self):
        assert len(MitreAttackTechnique.get_all(self.mitre_attack)) == len(MitreQueryMocker.TECHNIQUES[0]) + len(
            MitreQueryMocker.TECHNIQUES[1]) + len(MitreQueryMocker.TECHNIQUES[2])

    def test_collection_name_included(self):
        techniques = MitreAttackTechnique.get_by_name(self.mitre_attack, "Port Knocking")
        assert len(techniques) == 2
        assert techniques[0].collection is not None and techniques[1].collection is not None
        assert techniques[0].collection != techniques[1].collection

    def test_technique_representation_doesnt_have_unsupported_tags(self):
        """
        Mocked Domain Generation Algorithms on purpose has added code tags to where they could appear.
        """
        techniques = MitreAttackTechnique.get_by_name(self.mitre_attack, "Domain Generation Algorithms")
        dict_reps = [technique.dict_form() for technique in techniques]
        # check for every technique's representation that all the field don't have the tag
        assert all([("<code>" not in technique_repr[key] for key in technique_repr) for technique_repr in dict_reps])

    def test_deprecated_technique_states_so_in_description(self):
        """
        Gets tactics with name Impact, and checks that deprecation message was added.
        Deprecation flag was added to one of the mocked techniques.
        """
        techniques = MitreAttackTechnique.get_by_name(self.mitre_attack, "Domain Generation Algorithms")
        assert any(x.description.startswith("Deprecated") for x in techniques)

class TestMitreMitigation(object):
    mitre_attack = MitreAttackConnection()

    def test_mitigation_of_tech(self):
        """
        This one isn't mocked, because it would require mocking relationships
        :return:
        """
        mitigations = MitreAttackTechnique.get_by_name(self.mitre_attack, "Port Knocking")[0]\
            .get_mitigations(self.mitre_attack)
        assert mitigations is not None
        assert len(mitigations)

    def test_mitigation_get_all(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            assert len(MitreAttackMitigation.get_all(self.mitre_attack)) == len(MitreQueryMocker.MITIGATIONS[0]) + len(
                MitreQueryMocker.MITIGATIONS[1]) + len(MitreQueryMocker.MITIGATIONS[2])

    def test_mitigation_representation_doesnt_have_unsupported_tags(self):
        """
        Mocked Domain Generation Algorithms on purpose has added code tags to where they could appear.
        """
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            mitigations = MitreAttackMitigation.get_all(self.mitre_attack)
            dict_reps = [mitigation.dict_form() for mitigation in mitigations]
            # check for every technique's representation that all the field don't have the tag
            assert all([("<code>" not in mitigation_repr[key] for key in mitigation_repr) for mitigation_repr in dict_reps])

    def test_mitigation_doesnt_have_mardown_links(self):
        """
        Mocked Domain Generation Algorithms on purpose has added code tags to where they could appear.
        """
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            mitigation = MitreAttackMitigation.get_all(self.mitre_attack)
            dict_reps = [s.dict_form() for s in mitigation]
            # check for every technique's representation that all the field don't have the tag
            assert all([(re.search("\[(.*?)\]\((.*?)\)", s_repr["description"]) is None) for s_repr in dict_reps])

    def test_deprecated_mitigation_states_so_in_description(self):
        """
        Gets tactics with name Impact, and checks that deprecation message was added.
        Deprecation flag was added to one of the mocked mitigations.
        """
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            mitigations = MitreAttackMitigation.get_all(self.mitre_attack)
            assert any(x.description.startswith("Deprecated") for x in mitigations)


class TestMitreSoftware(object):
    mitre_attack = MitreAttackConnection()

    def test_software_doesnt_have_mardown_links(self):
        """
        Mocked Domain Generation Algorithms on purpose has added code tags to where they could appear.
        """
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            software = MitreAttackSoftware.get_all(self.mitre_attack)
            dict_reps = [s.dict_form() for s in software]
            # check for every technique's representation that all the field don't have the tag
            assert all([(re.search("\[(.*?)\]\((.*?)\)", s_repr["description"]) is None) for s_repr in dict_reps])

    def test_get_all(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            assert len(MitreAttackSoftware.get_all(self.mitre_attack)) == len(MitreQueryMocker.SOFTWARE[0]) + len(
                MitreQueryMocker.SOFTWARE[1]) + len(MitreQueryMocker.SOFTWARE[2])


class TestMitreGroup(object):
    class MockGroupID(object):
        def __init__(self, group_id):
            self.id = group_id

    mitre_attack = MitreAttackConnection()

    def test_groups_done_have_mardown_links(self):
        """
        Test that links are sanitized.
        """
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            groups = MitreAttackGroup.get_all(self.mitre_attack)
            dict_reps = [g.dict_form() for g in groups]
            # check for every technique's representation that all the field don't have the tag
            assert all([(re.search("\[(.*?)\]\((.*?)\)", group["description"]) is None) for group in dict_reps])

    def test_groups_dont_have_mardown_links(self):
        """
        Mocked Domain Generation Algorithms on purpose has added code tags to where they could appear.
        """
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            software = MitreAttackSoftware.get_all(self.mitre_attack)
            dict_reps = [s.dict_form() for s in software]
            # check for every technique's representation that all the field don't have the tag
            assert all([(re.search("\[(.*?)\]\((.*?)\)", s_repr["description"]) is None) for s_repr in dict_reps])

    def test_group_single_intersection_exists(self):
        """
        test_list is a list of lists.
        Each sublist is the groups that use a technique.
        Group with id 42 is in every sublist.
        """
        GROUP = self.MockGroupID
        test_list = [[GROUP(42), GROUP(1), GROUP(2), GROUP(3)],
                     [GROUP(10), GROUP(11), GROUP(12), GROUP(42)],
                     [GROUP(20), GROUP(21), GROUP(22), GROUP(23), GROUP(42)],
                     [GROUP(30), GROUP(31), GROUP(32), GROUP(42)]]
        intersection = MitreAttackGroup.get_intersection_of_groups(test_list)
        assert len(intersection) == 1
        assert 42 in intersection

    def test_group_multiple_intersection_exists(self):
        """
        test_list is a list of lists.
        Each sublist is the groups that use a technique.
        Groupswith id 42 and 123 are in every sublist.
        """
        GROUP = self.MockGroupID
        test_list = [[GROUP(42), GROUP(1), GROUP(2), GROUP(3), GROUP(123), GROUP(122)],
                     [GROUP(10), GROUP(11), GROUP(123), GROUP(122), GROUP(12), GROUP(42)],
                     [GROUP(20), GROUP(21), GROUP(22), GROUP(23), GROUP(42), GROUP(123), GROUP(122)],
                     [GROUP(123), GROUP(30), GROUP(31), GROUP(32), GROUP(42)]]
        intersection = MitreAttackGroup.get_intersection_of_groups(test_list)
        assert len(intersection) == 2
        assert 42 in intersection
        assert 123 in intersection

    def test_group_no_intersection_exists(self):
        """
        test_list is a list of lists.
        Each sublist is the groups that use a technique.
        There aren't any groups in each of the subsets.
        """
        GROUP = self.MockGroupID
        test_list = [[GROUP(42), GROUP(1), GROUP(2), GROUP(3), GROUP(123), GROUP(122)],
                     [GROUP(10), GROUP(11), GROUP(123), GROUP(122), GROUP(12), GROUP(42)],
                     [GROUP(20), GROUP(21), GROUP(22), GROUP(23), GROUP(42), GROUP(122)],
                     [GROUP(123), GROUP(30), GROUP(31), GROUP(32)]]
        intersection = MitreAttackGroup.get_intersection_of_groups(test_list)
        assert len(intersection) == 0


class TestMitre(object):
    mitre_conn = MitreAttackConnection()

    @pytest.mark.livetest
    def test_get_all_tactics_from_all_frameworks(self):
        tactics = MitreAttackTactic.get_all(self.mitre_conn)
        # As 8/5/19 there are 40 tactics
        assert len(tactics) >= 40

    @pytest.mark.livetest
    def test_get_tactic_url(self):
        tactics = MitreAttackTactic.get_all(self.mitre_conn)

        for tactic in tactics[:1]:
            url = tactic.get_url()
            assert url_get(url)

    @pytest.mark.livetest
    def test_get_tech_mitigation(self):
        techs = MitreAttackTechnique.get_all(self.mitre_conn)
        assert len(techs)
        try:
            #
            #   There are more than 200 techs. Try first 5 only
            #
            count = 0
            for tech in techs:
                id = tech.id
                assert(id)
                mitigation = tech.get_mitigations(self.mitre_conn)
                assert mitigation
                count += 1
                if count > 2:
                    break
                # Test getting mitigation using name
                mitigation = tech.get_mitigations(self.mitre_conn)
                assert mitigation
        except Exception as e:
            assert(False)

    def test_mitre_attack_util(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            tactics = "Impact, Collection"
            techs = get_tactics_and_techniques(tactic_names=tactics)
            assert len(techs) == 3

            tactics = "TA0040, TA0007, TA0009"
            techs = get_tactics_and_techniques(tactic_ids=tactics)
            assert(len(techs) > 0)

    def test_get_tech_info(self):
        data_mocker = MitreQueryMocker()
        with patch("fn_mitre_integration.lib.mitre_attack.TAXIICollectionSource.query", data_mocker.query):
            tech = MitreAttackTechnique.get_by_name(self.mitre_conn, "Port Knocking")
            assert(tech[0].name == "Port Knocking")

            tech = MitreAttackTechnique.get_by_id(self.mitre_conn, "T1205")
            assert(tech[0].id == "T1205")
