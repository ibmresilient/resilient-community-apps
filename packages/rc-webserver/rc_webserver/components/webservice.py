"""The main web server"""

import os
import logging
import traceback
import pkg_resources
from circuits.web import Server

LOG = logging.getLogger(__name__)

CONFIG_SECTION = "webserver"
CONFIG_SERVER = "server"
CONFIG_PORT = "port"
CONFIG_SECURE = "secure"
CONFIG_CERTFILE = "certfile"


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = pkg_resources.resource_filename("rc_webserver", "data/app.config")
    with open(section_config_fn, 'r') as section_config_file:
        section_config = section_config_file.read()
        return section_config


def _make_loc(opts):
    options = opts.get(CONFIG_SECTION, {})
    server = options.get(CONFIG_SERVER, "localhost")
    port = int(options.get(CONFIG_PORT, 9000))
    return (server, port)


def _make_args(opts):
    options = opts.get(CONFIG_SECTION, {})
    is_https = options.get(CONFIG_SECURE, "0")[:1].lower() in ["1", "y", "t"]
    certfile = options.get(CONFIG_CERTFILE, None)
    if certfile:
        certfile = os.path.expanduser(certfile)
    kwargs = {
        "encoding": "utf-8",
        "display_banner": False,
        "secure": is_https,
        "certfile": certfile
    }
    return kwargs


class WebService(Server):
    """A Circuits-based web server."""

    def __init__(self, opts):
        try:
            super(WebService, self).__init__(_make_loc(opts), **_make_args(opts))
            self.options = opts.get(CONFIG_SECTION, {})
            LOG.info("WebService listen address: %s", self.http.base)
        except:
            LOG.error(traceback.format_exc())
            raise
