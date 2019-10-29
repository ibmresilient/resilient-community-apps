#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""
    RES-ML
    ------
    A command line tool to build machine learning model. It supports:
        build_nlp: This will download the existing incidents from the Resilient
            server specified in app.config. It then extracts the name, description,
            artifact description. These texts are used to build a NLP model
        view:       View the summary of a saved model

"""

import argparse
import logging
import os, os.path
import resilient
import sys

from fn_resilient_ml.lib import file_manage
from fn_resilient_ml.lib.res_utils import ResUtils
from fn_resilient_ml.lib.nlp.nlp_settings import NLPSettings
from fn_resilient_ml.lib.nlp.res_nlp import ResNLP

import configparser

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

RESILIENT_SECTION = "resilient"
MACHINE_LEARNING_SECTION = "fn_resilient_ml"
SAMPLE_CSV_FILE = "resilient_incidents.csv"
LOG_FILE = "res-ml.log"

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

def main():
    """
    Main function. We hanlde building NLP now.
        1. build_nlp:   Build a NLP model
            -i:         [Optional] CSV file for sample data. Download directly if not specified
            -o:         [Optional] Name used for output files. Use default if not specified
        2. view:        Show summary of a saved model/SIF file
            -i:         Required flag, input file to view
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Print debug output", action="store_true")

    subparsers = parser.add_subparsers(title="subcommands",
                                       help="one of these options must be provided",
                                       description="valid subcommands",
                                       dest="cmd")
    subparsers.required = True

    nlp_parser = subparsers.add_parser("build_nlp",
                                        help="Build a NLP model")

    view_parser = subparsers.add_parser("view",
                                        help="View summary of a saved model")

    # 1. build_nlp
    #   -i (Optional) Specify a CSV file with data samples
    nlp_parser.add_argument("-i", "--input",
                            help="CSV file with data samples",
                            default=None)
    #   -o (Optional) Name used for output files
    nlp_parser.add_argument("-o", "--output",
                            help="Name used for output files. Don't include extension.",
                            default=None)

    # 2. view
    #   -i Input file for viewing summary
    view_parser.add_argument("-i", "--input",
                             help="Input file for viewing summary",
                             default=None,
                             required=True)

    args, unknown_args = parser.parse_known_args()

    #
    #   Use res-ml -v sub-command.....
    #   to get debug level log
    #
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.INFO)
    if args.verbose:
        fh.setLevel(logging.DEBUG)
        LOG.info("Verbose Logging Enabled")
        LOG.setLevel(logging.DEBUG)
    LOG.addHandler(fh)

    opt_parser = OptParser(config_file=None)
    if args.cmd == "view":
        view_summary(args)
    elif args.cmd == "build_nlp":
        build_nlp(args, opt_parser)


def view_summary(args):
    """
    Show the summary of a saved file
    :param args: Command line arguments
    :return:
    """
    file_name = args.input
    fs = file_manage.FileManage(file_name)

    summary = fs.get_summary()
    for s in summary:
        print(s)


def build_nlp(args, opt_parser):
    """

    :param args: command lie argument
    :return:
    """
    # Update nlp setting from app.config if necessary
    nlp_settings = NLPSettings.get_instance()
    opt = opt_parser.opts.get(MACHINE_LEARNING_SECTION)
    nlp_settings.update_settings(opt)

    inc_file = args.input if args.input else file_manage.FileManage.DEFAULT_INCIDENT_FILE
    art_file = file_manage.FileManage.DEFAULT_ARTIFACT_FILE
    #
    #   1. Download incidents and artifacts. To be used as training data
    #
    res_utils = ResUtils()
    res_utils.connect(opt_parser)
    res_utils.download_incidents(inc_file)
    res_utils.download_artifacts(art_file)
    #
    #   2. Build NLP model
    #
    res_nlp = ResNLP(inc_file=inc_file,
                     art_file=art_file)

    res_nlp.build_model()
    #
    #   3. Save the model
    #
    res_nlp.save_model()

    return