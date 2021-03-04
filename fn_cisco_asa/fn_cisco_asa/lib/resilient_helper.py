# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# 

from resilient_lib import IntegrationError
    
def init_select_list_choices(rest_client, field_name, field_value=None):
    """
    Update the rule activity select field choices at run time.  
    We do not know the firewall and network object group lists till run time as 
    these are defined by the user in the app.config.  
    """
    try: 
        # Get the current firewall rule activity select list.
        uri = "/types/actioninvocation/fields/{0}".format(field_name)
        get_response = rest_client.get(uri)

        values = []

        # Add each firewall as a select list entry.
        for label in field_value:
            entry = {'label': label,
                     'enabled': True,
                     'hidden': False}
            values.append(entry)

        # Put the new values into the select list to replace the current values there.
        get_response['values'] = values
        put_response = rest_client.put(uri, payload=get_response)

        return put_response

    except Exception as err:
        raise IntegrationError(err)    