#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if sys.version_info[0] <= 2:
    from pyclamd import __version__
    from pyclamd import *
elif sys.version_info[0] >= 3:
    from .pyclamd import __version__
    from .pyclamd import *



