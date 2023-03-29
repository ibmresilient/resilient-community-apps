""" Pull arguments from system keystore using keyring """

from __future__ import print_function

import sys
if sys.version_info.major < 3:
    from StringIO import StringIO
else:
    from io import StringIO

if sys.version_info[0] < 3:
    import ConfigParser as configparser
else:
    import configparser

import logging
import os
import json
import urllib
import csv
import collections
import keyring
import copy
import resilient_circuits.keyring_arguments as keyring_arguments

LOG = logging.getLogger(__name__)


def log(log_level):
    logging.getLogger().setLevel(log_level)


# The config file location should usually be set in the environment
APP_CONFIG_FILE = os.environ.get("APP_CONFIG_FILE", "app.config")

application = None


class OptArgumentParser(keyring_arguments.ArgumentParser):
    """Helper to parse command line arguments."""
    DEFAULT_LOG_LEVEL = 'WARN'

    def __init__(self):
        super(OptArgumentParser, self).__init__(config_file=APP_CONFIG_FILE)
        default_log_level = self.getopt("resilient", "loglevel") or self.DEFAULT_LOG_LEVEL

        self.add_argument("--loglevel",
                          type=str,
                          default=default_log_level,
                          help="Log level")

    def parse_args(self, args=None, namespace=None):
        """Parse commandline arguments and construct an opts dictionary"""
        opts = super(OptArgumentParser, self).parse_args(args, namespace)
        if self.config:
            for section in self.config.sections():
                items = dict((item.lower(), self.config.get(section, item)) for item in self.config.options(section))
                opts.update({section: items})
        return opts


# Main class for util script
class KeyringUtils(object):
    """Our main app class"""

    STDERR_LOG_FORMAT = '%(asctime)s %(levelname)s [%(module)s] %(message)s'

    def __init__(self):
        super(KeyringUtils, self).__init__()

        LOG.info("Configuration file is %s", APP_CONFIG_FILE)

        config_file = APP_CONFIG_FILE
        config_path = os.path.expanduser(config_file)
        self.config = configparser.SafeConfigParser()
        self.config.read(config_path)

    def run(self):
        opts = {}
        for section in self.config.sections():
            items = dict((item.lower(), self.config.get(section, item)) for item in self.config.options(section))
            opts.update({section: items})

        print("Secrets are stored with {}".format(type(keyring.get_keyring()).__module__))
        try:
            list_parameters(opts)
        except (KeyboardInterrupt, EOFError):
            print()
            pass
        pass


def list_parameters(options):
    names = ()
    return _list_parameters(names, options)


def _list_parameters(names, options):
    """Parse parameters, with a tuple of names for keyring context"""
    for key in options.keys():
        val = options[key]
        if isinstance(val, dict):
            val = _list_parameters(names + (key,), val)
        if isinstance(val, str) and len(val) > 1 and val[0] == "^":
            # This value is from the keyring
            tag = val
            val = val[1:]
            service = ".".join(names) or "_"
            LOG.debug("keyring get('%s', '%s')", service, val)
            value = keyring.get_password(service, val)

            if value is None:
                print("[{0}] {1}: <not set>".format(",".join(names), key))
            else:
                print("[{0}] {1}: {2}".format(",".join(names), key, tag))

            newvalue = None
            do_set = True
            while do_set:
                newvalue = raw_input("  Enter new value (or <ENTER> to leave unchanged): ")
                if len(newvalue) == 0:
                    do_set = False
                    break
                confirm = raw_input("  Confirm new value: ")
                if confirm == newvalue:
                    break
                print("Values do not match, try again.")

            if do_set:
                keyring.set_password(service, val, newvalue)
                print("Value set.")

        options[key] = val
    return options


if __name__ == "__main__":
    KeyringUtils().run()
