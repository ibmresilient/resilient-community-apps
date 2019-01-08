# Introduction #
This is the code for the Data Feed extension.  This extension allows you to maintain "replica" data for a Resilient system.  The updates are performed in near real-time.

The use case for this extension is for cases where you want to run business intelligence queries from other tools.  It hopefully eliminates the desire to query the Resilient database directly (since the Resilient DB schema is not documented and can change at any time).

The data can be written to any or all of the following destinations:

- ODBC databases (e.g. PostgreSQL)
- SQLite file/database
- Local directory (one file per object)

The architecture was written to allow other destinations to be created with relative ease.

The content is consistent with the Resilient type/field semantic model and will include custom fields.  For SQL destinations, the table name is the same as the type name (e.g. incident, task, artifact, etc.) and the column names are the same as the field "programmatic name".

Data tables are supported (the programmatic name will be the same as the DB table name).

Newly added fields and data tables are created in the destination database (for ODBC/SQLite destinations).

# Setup

Refer to each directory for any pre-requisites and specific install instructions.

Each application has a `setup.py` installer.  You can install in two ways:

## Installing in "developer mode"

To install a package in "developer mode", change to the directory that contains `setup.py` and install with:
```shell
pip install -e .
```

If you make any changes to the source files, they will apply next time the application is run.

## Creating a Distribution

To create a distribution package,
```shell
python setup.py sdist
```

Then in the `dist` subdirectory you will find a .tar.gz file that you can copy to another environment and
install using 'pip' (specifying the filename of the package that you built):

```shell
pip install app_name.tar.gz
```

If you make any changes to the source files, you'll need to rebuild and reinstall the distribution package.

# Configuration #
The configuration goes in the standard app.config file.  There is one "feeds" section that contains a "feed_names" key, which is a comma separated list of feeds that you want to enable.  The names you use here have to be unique, but they're otherwise unimportant...they are just the names of the sections that contain the actual feed configurations.  For example:

```
[feeds]
feed_names=my_postgresql_feed,my_file_feed,my_sqlite_feed
reload=True

[my_postgresql_feed]
class=ODBCFeed
odbc_connect=Driver={PostgreSQL};Server=localhost;Port=5432;Database=feed
sql_dialect=PostgreSQL96Dialect
uid=mypguser
pwd=mypassword

[my_file_feed]
class=FileFeed
directory=/tmp/feed_data

[my_sqlite_feed]
class=SQLiteFeed
file_name=/tmp/feed.sqlite3
```

Notice how the above configuration references my\_postgresql\_feed in the feed\_names key (feeds section), then puts the specific feed configuration in the "my\_postgresql\_feed" section.

This structure allows you to create as many feeds as you need, regardless of the "class" (meaning you can have, say, 3 different ODBC feeds so long as you give them all unique names).

The following sections will explain the configuration options for each of the feed classes.

## FileFeed class ##
The FileFeed class allows you to write all the incoming data to a directory on your file system (one file per object).  The structure of the file names is either:

incident\_{inc_id}.json (for incident objects)

or

incident\_{inc_id}\_{type}\_{obj\_id}.json (for all other types of objects).  In this context, "type" can be:

* task
* artifact
* milestone
* note
* _data table programmatic name_

The following configuration items are supported:

|Key|Values|Description|
|:--|:-----|:----------|
|class|FileFeed|This indicates that the section is for a FileFeed.|
|directory|Path for a directory on local system (must exist).|This is where the files will be written.|

## SQLiteFeed class ##
The SQLiteFeed class allows you to write all the incoming data to a SQLite DB file.  SQLite is very useful for testing and in cases where you want to have the data stored in a single file that you can ship around.  Some tools may natively support SQLite as well.

SQLite has pretty good CSV support also, so you can easily export the data from the SQLite file into a CSV, which can then be imported into something like Excel for further analysis.

The following configuration items are supported:

|Key|Values|Description|
|:--|:-----|:----------|
|class|SQLiteFeed|This indicates that the section is for a SQLiteFeed.|
|file_name|Path for a local file on the system where the SQLite DB will reside.|This will be created if it doesn't yet exist.  If it does exist, it must be a SQLite database.|

## ODBCFeed class ##
The ODBCFeed class is probably the most flexible and useful of the feeds.  It allows you to write all the incoming data to an ODBC database (currently we only support PostgreSQL 9.6 or higher, but other SQL dialects will be straightforward to add).

The following configuration items are supported:

|Key|Values|Description|
|:--|:-----|:----------|
|class|ODBCFeed|This indicates that the section is for an ODBCFeed.|
|odbc_connect|The ODBC connect string.|Example for PostgreSQL:  Driver={PostgreSQL};Server=localhost;Port=5432;Database=feed|
|sql_dialect|PostgreSQL96Dialect|The name of the SQL dialect.  As mentioned before, we only support PostgreSQL96Dialect right now...but others will eventually be added.|
|uid|DB user name|Specify the database user name in this property and not in the connect string (most DBs support the uid in the connect string but you should specify in this property instead).|
|pwd|DB password|Specify the database user's password in this property and not in the connect string (most DBs support the pwd in the connect string but you should specify it in this property instead).  You can use the standard Resilient Circuits mechanism for secure password storage.|

# Useful Tools
Most "business intelligence" tools allow you to query data from SQL databases.  Here are some tools that you can use to run queries/reports against this data:

* Tableau
* Microsoft Power BI
* IBM Cognos
* Grafana
* Interactive SQL, for example:

```
  -- Number of artifacts for each incident
  select i.id, i.name, count(*) num_artifacts
  from incident i join artifact a on i.id = a.inc_id
  group by i.id, i.name;
```
  
# License

Unless otherwise specified, contents of this repository are published under the MIT open-source license.
[LICENSE](LICENSE)

Files and subdirectories within this repository may contain specific licenses that apply individually to that item.

# FAQ #
## Resilient uses PostgreSQL.  Why can't I just open up access to the PostgreSQL and query the DB directly?##
The primary reason is because IBM Resilient doesn't support direct database access.  Why's that?  The DB schema is not documented and has a different semantic model than is exposed by the Resilient REST API.  It would be confusing to document two separate models.  It'd also slow down the Resilient team if we had to be conerned with breaking code that we didn't write.  

The DB schema changes for almost every release, which could mean breaking anything that is accessing the database directly.

## You support PostgreSQL, can I create a new database on my Resilient appliance and connect to that? ##
This is not recommended.  It would be better to maintain the database on another system where queries won't impact your running Resilient instance.

Allowing access to the Resilient appliance PostgreSQL instance can also compromise security of the appliance itself.  It is possible to do it securely, but it would be somewhat complicated to configure properly.  For example, the Resilient appliance today doesn't support TLS connections to the PostgreSQL port because it isn't needed (all communication happens over localhost/loopback).

## Is historical data maintained? ##
Not at this time.  The data written represents the current snapshot.  It would be possible to have the extension maintain historical data, but doing so would be non-trivial.  If you have a need for historical data queries, we'd love to hear from you.  Please log a GitHub issue that explains your use case in as much detail as you can.

## Why isn't X supported as a "feed destination"? ##
We have some ideas about other feed destinations that can be added:

* Splunk
* Microsoft SQL Server (new "dialect" for ODBCFeed)
* MySQL (new "dialect" for ODBC)

Do you need others?  If so, we'd love to see a pull request from you!  If you can't do that, then maybe file an issue in GitHub and perhaps someone else can add it.

## Where are the tests for this code?! ##
This is an excellent question!  They are coming.  The project started as a PoC and we have not yet added tests, although some manual testing has been performed.  This is one reason why we're not yet considering this a supported product, but we wanted to get this out into the community to get feedback and (hopefully) help.