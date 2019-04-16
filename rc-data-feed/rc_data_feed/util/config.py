# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=<your feeds>
reload=True
# feed_data is the default message destination that will be listened to
queue=feed_data

#[postgres_feed]
#class=ODBCFeed
#odbc_connect=Driver={PostresSQL Driver};Server=127.0.0.1;DB=<db>;Port=5432;connectTimeout=0
#sql_dialect=PostgreSQL96Dialect
#uid=<acct>
#pwd=<pwd>

#[oracle_feed]
#class=ODBCFeed
#odbc_connect=Driver={Oracle 12c ODBC driver};DBQ=ORCLCDB
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

#[elastic_feed]
#class=ElasticFeed
#url=https://your_org.com
#port=9200
# if using multiple organizations, consider indexes such as resilient_<org_ID>
# each document type will append to this index as elastic 6.0 onlyl supports one document type per index
#index_prefix=resilient_
#auth_user=
#auth_password=
#cafile=false

#[splunk_hec_feed]
#class=SplunkHECFeed
#token=<token>
#host=<host>
#port=8088
#index=data_feeder
# only use source_type if using one type. otherwise, the resilient object type (incident, note, artifact, etc.) is used
#event_source_type=txt
#event_host=
#event_source=resilient
#use_ssl=true

#[my_sqlite_feed]
#class=SQLiteFeed
#file_name=/tmp/feed.sqlite3

"""
    return config_data
