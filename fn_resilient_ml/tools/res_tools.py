#!/usr/bin/env python
# -*- coding: utf-8 -*-

import resilient
import argparse
import logging
import json
import subprocess
import requests

import tempfile
import os
from fn_resilient_ml.lib import res_utils
import sys

class OptParser(resilient.ArgumentParser):
    """
    This is a subclass of resilient.ArgumentParser. resilient.ArgumentParser takes care of both
        1. Reading app.config
        2. Validating required command line arguments.
    Here we just want app.config, we are parsing/validating commandline arguments in our main function.
    """
    def __init__(self, config_file=None):
        self.config_file = config_file or resilient.get_config_file()
        super(OptParser, self).__init__(config_file=self.config_file)
        #
        #   Note this is a trick used by resilient-circuits. resilient.ArgumentParser will
        #   validate the arguments of the command line. Since we use command line
        #   argument of input/output files, we don't want that validation, so we
        #   erase them before we call parse_args(). Then parse_args() only
        #   reads from app.config
        #
        sys.argv = sys.argv[0:1]
        self.opts = self.parse_args()

        if self.config:
            for section in self.config.sections():
                #
                # Handle sections other than [resilient] in app.config
                #
                items = dict((item.lower(), self.config.get(section, item)) for item in self.config.options(section))
                self.opts.update({section: items})

            resilient.parse_parameters(self.opts)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "help":
        print("""This is a tool for executing/debugging res lib of this package. It supports three subcommands:\n
        \t 1. help: print out this
        \t 2. incidents: Download incidents
        \t 3. artifacts: Download artifacts""")
    else:
        opt_parser = OptParser(config_file=None)
        res_utils = res_utils.ResUtils()
        res_utils.connect(opt_parser)

        if cmd == "incidents":
            res_utils.download_incidents("resilient_incidents.csv")
        elif cmd == "artifacts":
            res_utils.download_artifacts("resilient_artifacts.json")

