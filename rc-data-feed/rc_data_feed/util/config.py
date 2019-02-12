# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[feeds]
feed_names=sqlserver_feed
reload=True
# feed_data is the default message destination that will be listened to
queue=feed_data

#[sqlserver_feed]
#class=ODBCFeed
#odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;PORT=1443;DATABASE=res_test;UID=sa;PWD=Passw0rd
#sql_dialect=SQLServerDialect
#uid=sa
#pwd=sa
"""
    return config_data
