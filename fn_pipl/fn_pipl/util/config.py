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

# Optional
# 0 – 1 (float value) The minimum required match score for possible persons to be returned.
# minimum_match 1 will return the information for the chosen person only - the definite match
# other values will return a possible persons list
#pipl_minimum_match=1

# Optional
# 0 – 1 (float value) The minimum acceptable probability for inferred data
# Minimum probability lets you decide if your matches should only include source-validated data 
(data found in one of our data sources) or can include inferred data (data we infer based on statistical analysis).
# Setting your minimum probability to 1 means no inferred data will be used to determine a match or be included in matches.
#pipl_minimum_probability=1

# Optional
# True or False, default value is False
# whether the API should return persons made up solely from data inferred by statistical analysis from your search query.
#pipl_infer_persons=True
    """
    return config_data