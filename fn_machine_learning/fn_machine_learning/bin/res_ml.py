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
        1. config.      Generate a sample ml.config
        2. download.    Download incidents and save in CSV format.
        3. build.       Build machine model and save it into a file
        4. count-value. Value count for a given field. Useful for discovering imbalanced dataset
        5. view.        View the summary of a saved model.
        6. rebuild.     Rebuild a saved model with latest data

    Note the recommended steps to use our res-ml package are:
        1. Use this command line tool to generate a sample ml.config
        2. Use this command line tool to
            a. download incidents
            b. build and save a machine learning model
        3. Use our function component to do prediction, by pointing to the saved model file
        4. Rebuild the saved model periodically with updated incidents/samples.
"""

from __future__ import absolute_import

import argparse
import logging
import os, os.path
import resilient
import sys
from fn_machine_learning.lib.ml_model_common import MlModelCommon
from fn_machine_learning.lib.ml_config import MlConfig
import fn_machine_learning.lib.resilient_utils as resilient_utils
import fn_machine_learning.lib.model_utils as model_utils
from fn_machine_learning.lib.incident_time_filter import IncidentTimeFilter
import fn_machine_learning.lib.res_ml_config as res_ml_config
import requests

try:
    # For all python < 3.2
    import backports.configparser as configparser
except ImportError:
    import configparser

if sys.version_info.major == 2:
    from io import open
else:
    unicode = str


LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


RESILIENT_SECTION = "resilient"
MACHINE_LEARNING_SECTION = "machine_learning"
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
        #   erase them before we call parse_args(). So parse_args() only
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
    We support 6 sub-commands: config, build, rebuild, view, download, and count_value.
        1. config: create a smaple config file
        2. build: build a new model
            -o  Required flag, pointing to a file we can save the model to
            -c  Optional flag, pointing to a CSV file with samples. If this is absent, we will
                download incidents and use them as samples.
            Example: res-ml build -o logReg_adaboost.ml
        3. rebuild: Rebuild a saved model
            -i  Required flag, file of saved model to rebuild
            -c  Optional falg, same as -c of build above
        4. view: show summary of a saved model
            -i  Required flag, pointing to a saved model file
        5. download: Download incidents and save as CSV file
            -o  Required flag, file of saved incidents in CSV
        6. count_value: show value count for a given field. Normally this is the field to be predict.
                        This can help to determine whether the dataset is imbalance regarding this field
            -i  Required flag, pointing to a CSV file with samples
            -f  Required flag, the field to check value count
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Print debug output", action="store_true")

    subparsers = parser.add_subparsers(title="subcommands",
                                       help="one of these options must be provided",
                                       description="valid subcommands",
                                       dest="cmd")
    subparsers.required = True

    config_parser = subparsers.add_parser("config",
                                          help="Generate a sample config file")

    build_parser = subparsers.add_parser("build",
                                         help="Build a machine model")
    rebuild_parser = subparsers.add_parser("rebuild",
                                           help="Rebuild an saved machine learning model")
    view_parser = subparsers.add_parser("view",
                                        help="View the summary of a saved machine learning model")
    download_parser = subparsers.add_parser("download",
                                            help="Download incidents and save into a CSV file")
    count_value_parser = subparsers.add_parser("count_value",
                                               help="Count value of a field")

    # 1. config
    #   -o (Optional) name of sample config file. If not specified, ml.config will be used
    #
    config_parser.add_argument("-o", "--output",
                               help="Create sample config file as",
                               default=None)

    # 2. build process
    #
    #   -c (Optional) Specify a CSV file with samples. Otherwise download incidents

    build_parser.add_argument("-c", "--csv",
                              help="Use samples from CSV file",
                              default=None)

    #
    #   -f (Optional) Specify a config file for ml. Otherwise use ml.config
    #
    build_parser.add_argument("-f", "--file_config",
                              help="Use config file",
                              default=None)

    #
    #   -o Save model as
    #
    build_parser.add_argument("-o", "--output",
                              help="Save model as",
                              required=True,
                              default=None)

    # 3. rebuild process
    #
    #   -c Specify a CSV file with samples. Otherwise download incidents
    #
    rebuild_parser.add_argument("-c", "--csv",
                                help="Use samples from CSV file",
                                default=None)
    #
    #   -i Model file to rebuild
    #
    rebuild_parser.add_argument("-i", "--input",
                                help="Model file to rebuild",
                                required=True,
                                default=None)

    #
    #   -f (Optional) Specify a config file for ml. Otherwise use ml.config
    #
    rebuild_parser.add_argument("-f", "--file_config",
                                help="Use config file",
                                default=None)

    # 4. View
    #
    #   -i Model file to view
    #
    view_parser.add_argument("-i", "--input",
                             help="Model file to rebuild",
                             required=True,
                             default=None)

    # 5. Download
    #
    #   -o file to save
    #
    download_parser.add_argument("-o", "--output",
                                 help="CSV file to save samples",
                                 required=True,
                                 default=None)
    #
    #   -f (Optional) Specify a config file for ml. Otherwise use ml.config
    #
    download_parser.add_argument("-f", "--file_config",
                                 help="Use config file",
                                 default=None)
    # 6. Value count
    #
    #   -i  input CSV file with samples
    #   -f  field to check
    #
    count_value_parser.add_argument("-i", "--input",
                                    help="CSV file with samples",
                                    required=True,
                                    default=None)
    count_value_parser.add_argument("-f", "--field",
                                    help="value of which field to count",
                                    required=True,
                                    default=None)

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

    #
    #   Get config file
    #
    config_file = None
    if args.cmd in ("download", "build", "rebuild"):
        #
        # For these three subcommands,
        # uer can use -f to specify config file for machine learning
        #
        config_file = args.file_config
        if config_file is None and os.path.isfile("./ml.config"):
            #
            # If ./ml.config exits and user doesn't specify what to use, use ./ml.config
            #
            config_file = "./ml.config"

    opt_parser = OptParser(config_file=config_file)
    if args.cmd == "config":
        create_sample_config(args)
    elif args.cmd == "build":
        build_new_model(args, opt_parser)
    elif args.cmd == "rebuild":
        rebuild_model(args, opt_parser)
    elif args.cmd == "view":
        view_model(args)
    elif args.cmd == "download":
        csv_file = args.output
        download_incidents_csv(opt_parser, csv_file)
    elif args.cmd == "count_value":
        count_value(args)
    else:
        LOG.error("Unknown command: " + args.cmd)


def create_sample_config(args):
    """
    Create a sample config
    :param args:
    :param opt_parser:
    :return:
    """
    config_data = res_ml_config.get_config_data()
    config_file = "ml.config"

    #
    # Check if config_file specified
    #
    if args.output is not None:
        config_file = args.output

    #
    # Check if file already exists. If so, print out error message and quit
    #
    if os.path.isfile(config_file):
        LOG.info("{} already exists. Please use another file name.".format(config_file))
        return

    with open(config_file, "w") as outfile:
        outfile.write(config_data)


def count_value(args):
    """
    Count values
    :param args:
    :return:
    """
    csv_file = args.input
    field = args.field

    value_counts = model_utils.count_values(csv_file, field)
    LOG.info("------------")
    LOG.info("Value Counts")
    LOG.info("------------")
    LOG.info("Value counts for {} in {}:".format(field, csv_file))
    LOG.info("{}".format(value_counts))


def download_incidents_csv(opt_parser, csv_file):
    """
    Download incidents and convert json into CSV. Save the result to the csv_file.

    :param opt_parser:  Options/configurations and command line parameters
    :param csv_file:    CSV file to save samples/incidents to
    :return:            Number of incidents saved to the CSV file
    """
    res_opt = opt_parser.opts.get(RESILIENT_SECTION)
    host = res_opt.get("host", None)
    email = res_opt.get("email", None)
    password = res_opt.get("password", None)
    org = res_opt.get("org", None)

    num_inc = 0
    if host and org and email and password:
        url = "https://{}:443".format(host)
        verify = True
        try:
            cafile = opt_parser.getopt(RESILIENT_SECTION, "cafile")
            if cafile == "false" or cafile == "False":
                #
                #   This is a security related feature. The user has to explicitly enter false or False to
                #   turn it off. We don't accept anything else.
                #
                LOG.debug("HTTPS certificate validation has been turned off.")

                requests.packages.urllib3.disable_warnings()
                verify = False
            elif os.path.isfile(cafile):
                #
                #   User specified a cafile for trusted certificate
                #
                verify = cafile
        except:
            verify = True

        args = {"base_url": url,
                "verify": verify,
                "org_name": org}

        resilient_client = resilient.SimpleClient(**args)
        session = resilient_client.connect(email, password)
        max_count = None
        if opt_parser.getopt(MACHINE_LEARNING_SECTION, "max_count"):
            max_count = int(opt_parser.getopt(MACHINE_LEARNING_SECTION, "max_count"))

        time_start = opt_parser.getopt(MACHINE_LEARNING_SECTION, "time_start")
        time_end = opt_parser.getopt(MACHINE_LEARNING_SECTION, "time_end")
        res_filter = IncidentTimeFilter(time_start=time_start,
                                        time_end=time_end,
                                        in_log=LOG)

        # get_incidents is going to download all the incidents using this resilient_client
        # The optional max_count controls how many samples to process. The conversion from
        # json to CSV will stop once reaches this limit.
        num_inc = resilient_utils.get_incidents(res_client=resilient_client,
                                                filename=csv_file,
                                                filter=res_filter,
                                                max_count=max_count,
                                                in_log=LOG)

    LOG.info("Saved {} samples into {}".format(num_inc, csv_file))

    return num_inc


def build_model(model_file, opt_parser, csv_file=None, rebuilding=False):
    """
    Build a model
    :param model_file: Save built model to this file
    :param opt_parser: information from app.config
    :param csv_file: CSV file with samples
    :param rebuilding: True if rebuilding saved model
    :return:
    """
    res_opt = opt_parser.opts.get(RESILIENT_SECTION)
    ml_opt = opt_parser.opts.get(MACHINE_LEARNING_SECTION)

    mlconfig = MlConfig()

    if not csv_file:
        #
        #   Users did not specify a CSV file with samples. So we
        #   need to download incidents first.
        #   Save them to SAMPLE_CSV_FLLE
        #
        num_inc = download_incidents_csv(opt_parser, SAMPLE_CSV_FILE)
        LOG.info("Download and save samples to " + SAMPLE_CSV_FILE)
        mlconfig.number_samples = num_inc
        csv_file = SAMPLE_CSV_FILE

    if rebuilding:
        model_utils.update_config_from_saved_model(model_file, mlconfig)
    else:
        model_utils.update_config_from_app_config(ml_opt, mlconfig)

    model = resilient_utils.get_model(name=mlconfig.model_name,
                                      imbalance_upsampling=mlconfig.imbalance_upsampling,
                                      class_weight=mlconfig.class_weight,
                                      method=mlconfig.addition_method)
    model.log = LOG
    model.config.number_samples = mlconfig.number_samples

    if model is not None:
        model.build(csv_file=csv_file,
                    features=mlconfig.selected_features,
                    prediction=mlconfig.predict_field,
                    test_prediction=mlconfig.split_percentage,
                    unwanted_values=mlconfig.unwanted_values)
        # Output summary of build

        show_model_summary(model, os.path.abspath(model_file))
        # save the model
        model.save_to_file(os.path.abspath(model_file))


def build_new_model(args, opt_parser):
    """
    Build a model.
    This method is called when user uses the command line util to build a model

    :param args:
    :param opt_parser:
    :return:
    """
    LOG.debug("Building a new model: " + str(args))
    file_name = args.output
    csv_file = args.csv

    build_model(file_name, opt_parser, csv_file)


def rebuild_model(args, opt_parser):
    """
    This method is called when user uses the command line util to rebuild
    a model, based on a saved model file

    :param args:            command line tools arguments
    :param opt_parser:      app.config information
    :return:
    """
    LOG.debug("Rebuilding a model: " + str(args))
    model_file = args.input
    csv_file = args.csv
    build_model(model_file, opt_parser, csv_file, True)


def show_model_summary(model, model_file):
    """
    Output summary of a given model

    :param model:           saved model re-constructed frome saved model
    :param model_file:      model file name
    :return:
    """
    try:
        method_name = model.config.addition_method
    except Exception:
        method_name = "None"

    LOG.info("--------")
    LOG.info("Summary:")
    LOG.info("--------")
    LOG.info("File:            {}".format(model_file))
    LOG.info("Build time:      {}".format(model.config.build_time))
    LOG.info("Num_samples:     {}".format(model.config.number_samples))
    LOG.info("Algorithm:       {}".format(model.get_name()))
    LOG.info("Method:          {}".format(method_name))
    LOG.info("Prediction:      {}".format(model.config.predict_field))
    LOG.info("Features:        {}".format(", ".join(model.config.selected_features)))
    LOG.info("Class weight:    {}".format(str(model.config.class_weight)))
    LOG.info("Upsampling:      {}".format(str(model.config.imbalance_upsampling)))
    if model.config.unwanted_values is not None:
        LOG.info("Unwanted Values: {}".format(", ".join(model.config.unwanted_values)))
    LOG.info("Accuracy:        {}".format(model.config.accuracy))
    #
    #@TODO: Does customer care about precision and recall? F1 is enough?
    #
    # if model.config.precision is not None:
    #     LOG.info("Precision:       {}".format(model.config.precision))
    # if model.config.recall is not None:
    #     LOG.info("Recall:           }".format(model.config.recall))
    if model.config.f1 is not None:
        LOG.info("F1:              {}".format(model.config.f1))

    if model.config.analysis:
        LOG.info("  Accuracy for {} value:".format(model.config.predict_field))
        for key, value in model.config.analysis.iteritems():
            LOG.info("    %-*s %s" % (12, key + ":", value))


def view_model(args):
    """
    Show the summary of a saved model file.
    This method is call when user use command line util to view summary of
    a saved model file.

    :param args:        Command line arguments
    :return:
    """
    file_name = args.input

    file_exits = os.path.exists(file_name)

    if file_exits:
        #
        # Deserialize model
        #
        model = MlModelCommon.load_from_file(file_name)
        #
        # Output the information of this model
        #
        show_model_summary(model, os.path.abspath(file_name))
    else:
        LOG.error("Model file {} does not exist.".format(file_name))

if __name__ == "__main__":
    LOG.debug("Calling main")
    main()
