# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2021. All Rights Reserved.

# Constant values
DEFAULT_HTTP_PORT = 8008
DEFAULT_HTTPS_PORT = 8443

# Interpreted values
HTTP_BASE_URL = lambda host, port: "http://{0}:{1}/api".format(host, str(port))
HTTPS_BASE_URL = lambda host, port: "https://{0}:{1}/api".format(host, str(port))