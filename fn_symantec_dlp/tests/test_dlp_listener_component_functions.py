# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
from fn_symantec_dlp.util.dlp_listener_component import DLPListener
import requests_mock
from resilient_circuits import ResilientComponent
import resilient
import pytest


class TestDLPListener():

    @classmethod
    def setup_class(self):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """

        parser = resilient.ArgumentParser(
            config_file=resilient.get_config_file())

        opts = parser.parse_args(args="")
        print(opts)

    @pytest.mark.parametrize("dlp_host", [
        ("my-soc-instance.acme.com"),
        ("dlp-installation.soc.company.com")
    ])
    def test_build_dlp_url(self, dlp_host):
        function_params = {
            "dlp_host": dlp_host
        }

        url = DLPListener.build_dlp_url(incidentid=111, host=dlp_host)
        assert url is not None
        assert "ProtectManager" in url
        assert dlp_host in url
