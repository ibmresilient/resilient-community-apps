# Introduction
This package contains the odbcfeed Plugin to the Data Feed extension.  This Data Feed extension allows one to maintain "replica" data for Resilient incidents, artifacts, tasks, notes, etc.  The updates are performed in near real-time.

This plugin allows this replica data to be maintained in a sql-based database.

Refer to the documentation on the Data Feed extension for uses cases support and configuration options. Also refer to the other Data Feed plugins which can be used in combination.
  
# License

Unless otherwise specified, contents of this repository are published under the MIT open-source
[LICENSE](LICENSE).

# Installation
  The integration package contains Python components that are called by the Resilient platform. These components run in the Resilient Circuits integration framework. The package also includes Resilient customizations that will be imported into the platform later.
  You perform these installation procedures at the Resilient integration server.
  
## Install the Python components
  Complete the following steps to install the Python components:
* Ensure that the environment is up-to-date, as follows:
```
  sudo pip install --upgrade pip
  sudo pip install --upgrade setuptools
  sudo pip install --upgrade resilient-circuits
```  
* | Run the following commands to install the package:
```
  unzip rc_data_feed-plugin-odbcfeed-<version>.zip
  [sudo] pip install --upgrade rc_data_feed-plugin-odbcfeed-<version>.tar.gz
```  
* | Configure Resilient-circuits

  The Resilient Circuits process runs as an unprivileged user, typically named integration. If you do not already have an integration user configured on your appliance, create it now. 
  Complete the following steps to configure and run the integration:
* Using sudo, switch to the integration user, as follows:

`  sudo su - integration`
* Use one of the following commands to create or update the resilient-circuits configuration file. Use –c for new environments or –u for existing environments.
```
  resilient-circuits config -c
  or
  resilient-circuits config –u [-l rc-data-feed-plugin-odbcfeed]
```
* Edit the resilient-circuits configuration file, as follows:
    
     - In the [resilient] section, ensure that you provide all the information required to connect to the Resilient platform.
     - In the [postgres_feed] or similar sections, configure the settings for your database environment.
     - In the [feeds] section, define the feed(s) you intend to use and create separate sections for each feed. For example:
```
  
  [feeds]
  feed_names=postgres_feed
  reload=True
  # feed_data is the default queue that will be listened to
  queue=feed_data
  
  [postgres_feed]
  class=ODBCFeed
  odbc_connect=Driver={PostresSQL Driver};Server=127.0.0.1;DB=<db>;Port=5432;connectTimeout=0
  sql_dialect=PostgreSQL96Dialect
  uid=<acct>
  pwd=<pwd>

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

  #[my_sqlite_feed]
  #class=SQLiteFeed
  #file_name=/tmp/feed.sqlite3
```

# ODBCFeed Class
The ODBCFeed class is probably the most flexible and useful of the feeds. It allows you to write all the incoming data to an ODBC database. 
The following configuration items are supported:

| Key | Values | Description |
| :-- | :----- | :---------- |
| class | ODBCFeed | Indicates that the section is for an ODBCFeed. |
| odbc_connect | ODBC connect string | Example for PostgreSQL:  Driver={PostgreSQL};Server=localhost;Port=5432;Database=feed |
| sql_dialect | PostgreSQL96Dialect, MariaDBDialect, SQLServerDialect, OracleDialect | Name of the SQL dialect. |
| uid | DB user name | Specify the database user name in this property and not in the connect string. Most DBs support the uid in the connect string but you should specify in this property instead. |
| pwd | DB password | Specify the database user's password in this property and not in the connect string. Most DBs support the pwd in the connect string but you should specify it in this property instead.  You can use the standard Resilient Circuits mechanism for secure password storage. |

When using a data feed database, IBM Resilient strongly recommends that you create and maintain the database on system separate from the Resilient platform, where queries cannot impact your running Resilient instance. Allowing access to the Resilient platform for a database instance can also compromise security of the platform itself. 

## Additional connection strings
The following table lists additional database connection strings for the other supported databases. 

| Database | Connection Strings |
| :------- | :----------------- |
MariaDB | Driver={MariaDB ODBC 3.0 Driver};Server=127.0.0.1;Port=3306; DB=<yourDB>;connectTimeout=0 |
| Oracle | Driver={Oracle 12c ODBC driver};DBQ=ORCLCDB |
| SQLServer | DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;PORT=1443;DATABASE=<yourDB>; |

Your naming of the database drivers (Ex. `MariaDB ODBC 3.0 Driver`) may vary and is specified in your `odbcinst.ini` file. 

Oracle has the further requirement of specifying the connection string references in a TNSNAMES.ORA file. Setting up the Oracle client environment will include the following environment variables (and may include others):

```
export LD_LIBRARY_PATH=/path/to/oracle/libraries/
export TNS_ADMIN=/path/to/tnsnames/
```

## Database Field Length Considerations
Each database type has limits to the size of data stored. The following table describes the limits for each database.

| Database | Field | Limit |
| :------- | :---- | :---- |
| Postgres | text | 1GB |
| MySQL/MariaDB | text | 4GB |
| MS SQLServer | varchar(max) | 2GB |
| MS SQLServer | varchar(xx) | 4000 |
| Oracle | nvarchar2(xx) | 2000 |

Some databases support blobs which can be supported specific cases. Blobs are presently unsupported.

## Additional considerations
* Some databases have reserve words which cannot be used in tables (such as date and size). If a Resilient custom field is found to be in a database reserve list, the name (for example, the column name) is altered to include a trailing '_'.

## Integration Server Requirements
All SQL database datastores are accessible via a python library (pyodbc) which further references a system library (unixodbc). Due to the complexity of the pyodbc, you will either need an environment with the `gcc compiler` to install it or, for RHEL environments, you can use a .whl file packaged by IBM and available on the public github (https://github.com/ibmresilient/resilient-community-apps/tree/master/fn_odbc_query/lib). 

Information about pyodbc and installing unixodbc can be found here: https://github.com/mkleehammer/pyodbc/wiki/Install.


# SQLiteFeed Class
The SQLiteFeed class allows you to write all the incoming data to a SQLite DB file. SQLite is very useful for testing and in cases where you want to have the data stored in a single file that you can easily share. Some tools may natively support SQLite as well.

SQLite supports CSV formatting, so you can easily export the data from the SQLite file into a CSV file, which can then be imported into another tool, such as Excel, for further analysis.

The following configuration items are supported:
| Key | Values | Description |
| :-- | :----- | :---------- |
| class | SQLiteFeed | Indicates that the section is for an SQLite.
| file_name | Path for a local file on the system where the SQLite DB resides. | This is created if it does not exist. If it does exist, it must be an SQLite database. |
