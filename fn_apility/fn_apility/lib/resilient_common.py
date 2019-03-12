# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.


def api_url(query_type):
    """
    Method Will return appropriate URL based on query type    
    """
    type_url_mapping = {'Email Sender': 'bademail', 'Email Recipient': 'bademail', 'Domain': 'baddomain', 'IP Address': 'v2.0/ip'}
    return type_url_mapping[query_type]


def validate_fields(fieldList, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param fieldList:
    :param kwargs:
    :return: no return
    """
    for field in fieldList:
        if field not in kwargs or kwargs.get(field) == '':
            raise ValueError('Required field is missing or empty: '+field)