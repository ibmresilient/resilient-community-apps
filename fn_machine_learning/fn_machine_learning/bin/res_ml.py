#!/usr/bin/env python

""" Command line tool to manage and run resilient-circuits """
from __future__ import absolute_import

import argparse
import logging
import os, os.path
import resilient
import sys
from fn_machine_learning.lib.ml_model_common import MlModelCommon
import fn_machine_learning.lib.resilient_utils as resilient_utils
import fn_machine_learning.lib.model_utils as model_utils


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


RESILIENT_SECTION="resilient"
MACHINE_LEARNING_SECTION="machine_learning"
SAMPLE_CSV_FILE="resilient_incidents.csv"


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
        #   validate the arguments of the command line. We don't want that, so we
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
    We support 3 subcommands: build, rebuild, view.
    1. build: build a new model
        -o  Required flag, pointing to a file we can save the model to
        -c  Optional flag, pointing to a CSV file with samples. If this is absent, we will
            download incidents and use them as samples.
        Example: res-ml build -o logReg_adaboost.ml
    2. rebuild: Rebuild a saved model
        -i  Required flag, file of saved model to rebuild
        -c  Optional falg, same as -c of build above
    3. view: show summary of a saved model
        -i  Required flag, pointing to a saved model file
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Print debug output", action="store_true")

    subparsers = parser.add_subparsers(title="subcommands",
                                       help="one of these options must be provided",
                                       description="valid subcommands",
                                       dest="cmd")
    subparsers.required = True

    build_parser = subparsers.add_parser("build",
                                         help="Build a machine model")
    rebuild_parser = subparsers.add_parser("rebuild",
                                           help="Rebuild an saved machine model")
    view_parser = subparsers.add_parser("view",
                                        help="Manage Resilient Circuits as a service with Windows or Supervisord")


    # 1. build process
    #
    #   -c Specifiy a CSV file with samples. Otherwise download incidents
    #
    build_parser.add_argument("-c", "--csv",
                              help="Use samples from CSV file",
                              default=None)
    #
    #  -o Save model as
    #
    build_parser.add_argument("-o", "--output",
                              help="Save model as",
                              default=None)


    # 2. rebuild process
    #
    #   -c Specifiy a CSV file with samples. Otherwise download incidents
    #
    rebuild_parser.add_argument("-c", "--csv",
                                help="Use samples from CSV file",
                                default=None)
    #
    #  -i Model file to rebuild
    #
    rebuild_parser.add_argument("-i", "--input",
                                help="Model file to rebuild",
                                default=None)

    # 3. View
    #
    #   -i Model file to view
    #
    view_parser.add_argument("-i", "--input",
                             help="Model file to rebuild",
                             default=None)

    args, unknown_args = parser.parse_known_args()
    fh = logging.FileHandler("res-ml.log")
    fh.setLevel(logging.INFO)
    if args.verbose:
        fh.setLevel(logging.DEBUG)
        LOG.info("Verbose Logging Enabled")
        LOG.setLevel(logging.DEBUG)
    LOG.addHandler(fh)

    opt_parser = OptParser()
    if args.cmd == "build":
        build_new_model(args, opt_parser)
    elif args.cmd == "rebuild":
        rebuild_model(args, opt_parser)
    elif args.cmd == "view":
        view_model(args)
    else:
        LOG.info("Unknown command")


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

    host = res_opt.get("host", None)
    email = res_opt.get("email", None)
    password = res_opt.get("password", None)
    org = res_opt.get("org", None)

    if host and org and email and password and not csv_file:
        url = "https://{}:443".format(host)
        verify = True
        try:
            cafile = opt_parser.getopt(RESILIENT_SECTION, "cafile")
            if cafile == "false":
                verify = False
        except:
            verify = True

        args = {"base_url": url,
                "verify": verify,
                "org_name": org}

        resilient_client = resilient.SimpleClient(**args)
        session = resilient_client.connect(email, password)
        max_count = None
        if opt_parser.getopt(RESILIENT_SECTION, "max_count"):
            max_count = int(opt_parser.getopt(RESILIENT_SECTION, "max_count"))

        resilient_utils.get_incidents(res_client=resilient_client,
                                      filename=SAMPLE_CSV_FILE,
                                      max_count=max_count)
        csv_file = SAMPLE_CSV_FILE
    elif not csv_file:
        LOG.error("You need to specify a CSV file for samples")
        return

    mlconfig = resilient_utils.MlConfig()

    if rebuilding:
        model_utils.update_config_from_saved_model(model_file, mlconfig)
    else:
        model_utils.update_config_from_app_config(ml_opt, mlconfig)

    model = resilient_utils.get_model(mlconfig.model_name, mlconfig.addition_method)

    if model:
        model.build(csv_file=csv_file,
                    features=mlconfig.selected_features,
                    prediction=mlconfig.predict_field,
                    test_prediction=mlconfig.split_percentage)
        # Output summary of build


        LOG.info("--------")
        LOG.info("Summary:")
        LOG.info("--------")
        LOG.info("File:        {}".format(os.path.abspath(model_file)))
        LOG.info("Algorithm:   {}".format(model.get_name()))
        LOG.info("Method:      {}".format(mlconfig.addition_method))
        LOG.info("Prediction:  {}".format(model.prediction))
        LOG.info("Features:    {}".format(", ".join(model.features)))
        LOG.info("Build time:  {}".format(model.build_time))
        LOG.info("Accuracy:    {}".format(model.accuracy))
        # save the model
        model.save_to_file(os.path.abspath(model_file))



def build_new_model(args, opt_parser):
    """
    Build a model
    :param args:
    :param opt_parser:
    :return:
    """
    file_name = args.output
    csv_file = args.csv

    build_model(file_name, opt_parser, csv_file)


def rebuild_model(args, opt_parser):
    LOG.info("Rebuilding a  model: " + str(args))
    model_file = args.input
    csv_file = args.csv
    build_model(model_file, opt_parser, csv_file, True)


def view_model(args):
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

        try:
            method_name = model.method_name
        except Exception:
            method_name = "None"
        LOG.info("--------")
        LOG.info("Summary:")
        LOG.info("--------")
        LOG.info("File:        {}".format(os.path.abspath(file_name)))
        LOG.info("Algorithm:   {}".format(model.get_name()))
        LOG.info("Method:      {}".format(method_name))
        LOG.info("Prediction:  {}".format(model.prediction))
        LOG.info("Features:    {}".format(", ".join(model.features)))
        LOG.info("Build time:  {}".format(model.build_time))
        LOG.info("Accuracy:    {}".format(model.accuracy))
    else:
        LOG.error("Model file {} does not exist.".format(file_name))

if __name__ == "__main__":
    LOG.debug("Calling main")
    main()