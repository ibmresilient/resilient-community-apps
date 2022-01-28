# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[postgres_feed]
class=ODBCFeed
odbc_connect=Driver={PostgreSQL};Server=127.0.0.1;DB=<db>;Port=5432;connectTimeout=0
sql_dialect=PostgreSQL96Dialect
uid=<acct>
pwd=<pwd>

#[oracle_feed]
#class=ODBCFeed
#odbc_connect=<service_name> or (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<host>)(PORT=<port>))(CONNECT_DATA=(SID=<sid>)))
#sql_dialect=OracleDialect
#uid=<acct>
#pwd=<pwd>

#[sqlserver_feed]
#class=ODBCFeed
#odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;PORT=1443;DATABASE=<db>
#sql_dialect=SQLServerDialect
#uid=<acct>
#pwd=<pwd>

#[mysql_feed]
#class=ODBCFeed
#odbc_connect=Driver={MariaDB ODBC 3.0 Driver};Server=127.0.0.1;DB=<db>;Port=3306;connectTimeout=0
#sql_dialect=MariaDBDialect
#uid=<acct>
#pwd=<pwd>

#[my_sqlite_feed]
#class=SQLiteFeed
#file_name=/tmp/feed.sqlite3
"""

    return config_data

def apphost_config_section_data():
    return u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=<change to feed section above>
reload=False
# set to true if ElasticSearch errors occur during reload=True
reload_query_api_method=False
# feed_data is the default message destination that will be listened to
queue=feed_data
# change setting to true to capture contents of an attachment
include_attachment_data = false
# use reload_types to limit the types of objects when reload=true.
# Ex: incident,task,note,artifact,attachment,<data_table_api_name>
reload_types=
# if necessary, specify the supported workspace (by label, case sensitive) and the list of feeds associated with it
# ex: 'Default Workspace': ['sqlserver_feed'], 'workspace A': ['kafka_feed', 'resilient_feed']
workspaces=
"""
