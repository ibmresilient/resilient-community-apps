# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest

from fn_docker.util.docker_utils import DockerUtils


class TestDockerInterface:

    @pytest.mark.parametrize("options", [
        {"docker_extra_volumes": "volume"},
        {"docker_extra_volumes": "volume", "docker_extra_host": "host", "not_a_docker_var": 123, "extra_var": 123},
        {"docker_extrbadformatting": 123, "docker_extra_volumes": 123, "bad_docker_extraformat": "Test"}
    ])
    def test_parsing_extra_kwargs(self, options):

        docker_interface = DockerUtils()
        docker_options = docker_interface.parse_extra_kwargs(options=options)
        assert(docker_options) # Asset docker_options has values and is truthy
        assert(len(docker_options.keys()))

    @pytest.mark.parametrize("options", [
        {"docker_etra_volumes": "volume"},
        {"not_a_docker_var": 123, "extra_var": 123},
        {"docker_extrbadformatting": 123, "bad_docker_extraformat": "Test"},
        {"unrelated option ": "Test"}
    ])
    def test_parsing_extra_kwargs_failure(self, options):
        docker_interface = DockerUtils()
        docker_options = docker_interface.parse_extra_kwargs(options=options)
        assert (not docker_options) # Asset docker_options has no values and is falsey
        assert (not len(docker_options.keys()))

    @pytest.mark.parametrize("options", [
        {"docker_extra_volumes": "volume"}
    ])
    def test_parsing_extra_kwargs_removal(self, options):
        """A test to ensure the 'docker_extra' options are not returned as part of the dict.
        They should be renamed when returned by the function to remove 'docker_extra_'"""
        docker_interface = DockerUtils()
        docker_options = docker_interface.parse_extra_kwargs(options=options)
        assert ('docker_extra' not in docker_options.keys())


