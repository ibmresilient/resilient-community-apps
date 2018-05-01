# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import datetime

def validateFields(fieldList, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param fieldList:
    :param kwargs:
    :return: no return
    """
    for field in fieldList:
        if field not in kwargs or kwargs.get(field) == '':
            raise ValueError('Required field is missing or empty: '+field)

def readableDateTime(timestamp, milliseconds=True):
    if milliseconds:
        ts = timestamp/1000
    else:
        ts = timestamp

    return datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
