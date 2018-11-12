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
# A possible persons response returns possible persons in descending order based on their match rate 
# (whether you can see the match rate or not). 
# The most probable person will always appear as the first possible person at the top of the results 
# and the least probable person will appear at the bottom of the list.
pipl_max_no_possible_per_matches=10

# Optional
# Value between 0 and 1 (float value) The minimum required match score for possible persons to be returned.
# minimum_match 1 will return the information for the chosen person only - the definite match.
# A definite match is best when you need someone’s contact information or for identity verification.
# Values other than 1 will return a possible persons list.
#pipl_minimum_match=1

# Optional
# Value between 0 and 1 (float value) The minimum acceptable probability for inferred data
# Minimum probability lets you decide if your matches should only include source-validated data 
# (data found in one of pipl data sources) or can include inferred data (data pipl infers based on statistical analysis).
# Setting your minimum probability to 1 means no inferred data will be used to determine a match or be included in matches.
# Setting your minimum probability to 0.7 will include inferred data that has a 70% confidence level or higher.
#pipl_minimum_probability=0.7

# Optional
# True or False, default value is False
# whether the API should return persons made up solely from data inferred by statistical analysis from your search query.
#pipl_infer_persons=True
    """
    return config_data