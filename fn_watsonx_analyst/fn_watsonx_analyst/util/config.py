# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""Generate a default configuration-file section for fn_watsonx_analyst"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_watsonx_analyst when called by `resilient-circuits config [-c|-u]`
    """
    config_data = """[fn_watsonx_analyst]
# Note: don't use quotes around values.
watsonx_api_key=$WATSONX_API_KEY
watsonx_project_id=$WATSONX_PROJECT_ID
watsonx_endpoint=$WATSONX_ENDPOINT

[watsonx_property_labels]
# Note: don't use quotes around values.
# Here you can add a replacement label for an Incident custom field/property, if the existing field name is misleading or unclear.
# e.g.
# fn_obscure_api_name=incident report
"""
    return config_data
