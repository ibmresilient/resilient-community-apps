# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_risk_fabric"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_risk_fabric]
# Risk Fabric server ip or fully qualified hostname	
server=https://www.riskfabric.com
username=<username>
password=<password>
# bypass https certificate validation (only set to False for testing purposes)
verifyFlag=True
"""
    return config_data
