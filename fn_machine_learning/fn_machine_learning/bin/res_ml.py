#!/usr/bin/env python

""" Command line tool to manage and run resilient-circuits """
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
        4. download: Download incidents and save as CSV file
            -o  Required flag, file of saved incidents in CSV
        5. count_value: show value count for a given field. Normally this is the field to be predict.
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

    build_parser = subparsers.add_parser("build",
                                         help="Build a machine model")
    rebuild_parser = subparsers.add_parser("rebuild",
                                           help="Rebuild an saved machine model")
    view_parser = subparsers.add_parser("view",
                                        help="Manage Resilient Circuits as a service with Windows or Supervisord")
    download_parser = subparsers.add_parser("download",
                                            help="Download incidents and save into a CSV file")
    count_value_parser = subparsers.add_parser("count_value",
                                               help="Count value of a field")

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

    # 4. Download
    #
    #   -o file to save
    #
    download_parser.add_argument("-o", "--output",
                                 help="CSV file to save samples",
                                 default=None)

    # 5. Value count
    #
    #   -i  input CSV file with samples
    #   -f  field to check
    #
    count_value_parser.add_argument("-i", "--input",
                                    help="CSV file with samples",
                                    default=None)
    count_value_parser.add_argument("-f", "--field",
                                    help="value of which field to count",
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
    elif args.cmd == "download":
        csv_file = args.output
        download_incidents_csv(opt_parser, csv_file)
    elif args.cmd == "count_value":
        count_value(args)
    else:
        LOG.info("Unknown command")


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

    :param opt_parser:
    :return:
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
        if opt_parser.getopt(MACHINE_LEARNING_SECTION, "max_count"):
            max_count = int(opt_parser.getopt(MACHINE_LEARNING_SECTION, "max_count"))

        # get_incidents is going to download all the incidents using this resilient_client
        # The json result will be converted into CSV format, and then save into
        # SAMPLE_CSV_FILE.
        # The optional max_count controls how many samples to process. The conversion from
        # json to CSV will stop once reaches this limit.
        num_inc = resilient_utils.get_incidents(res_client=resilient_client,
                                                filename=csv_file,
                                                max_count=max_count)

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
        num_inc = download_incidents_csv(opt_parser, SAMPLE_CSV_FILE)
        mlconfig.number_samples = num_inc
        csv_file = SAMPLE_CSV_FILE
    elif not csv_file:
        LOG.error("You need to specify a CSV file for samples")
        return

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
    file_name = args.output
    csv_file = args.csv

    build_model(file_name, opt_parser, csv_file)


def rebuild_model(args, opt_parser):
    """
    This method is called when user uses the command line util to rebuild
    a model, based on a saved model file
    :param args:
    :param opt_parser:
    :return:
    """
    LOG.info("Rebuilding a  model: " + str(args))
    model_file = args.input
    csv_file = args.csv
    build_model(model_file, opt_parser, csv_file, True)


def show_model_summary(model, model_file):
    """
    Output summary of a given model
    :param model:
    :param model_file: model file read/write
    :return:
    """
    try:
        method_name = model.config.method_name
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
            LOG.info("    {}:        {}".format(key, value))


def view_model(args):
    """
    Show the summary of a saved model file.
    This method is call when user use command line util to view summary of
    a saved model file.
    :param args:
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
