# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

# Constant values
DEFAULT_HTTPS_PORT = 8443

# Interpreted values
HTTPS_BASE_URL = lambda host, port: "https://{0}:{1}/api".format(host, str(port))