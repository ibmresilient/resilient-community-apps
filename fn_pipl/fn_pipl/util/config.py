# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_pipl"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_pipl]
pipl_api_key=xxxxx

# Number of possible person matches to include in the results.
pipl_max_no_possible_per_matches=10

# Optional
# Value between 0 and 1 (float value) The minimum required match score for possible persons to be returned.
#pipl_minimum_match=1

# Optional
# Value between 0 and 1 (float value) The minimum acceptable probability for inferred data
#pipl_minimum_probability=0.7

# Optional
# True if the API should return persons made up solely from data inferred by statistical analysis from your search query.
#pipl_infer_persons=True
    """
    return config_data