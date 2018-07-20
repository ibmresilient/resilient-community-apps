# Resilient Function - ODBC Query Function

The ODBC Query Function establishes an OBDC connection to the desired SQL database server and executes SELECT, INSERT, UPDATE or DELETE SQL statements.

Prerequisites
```
resilient-circuits >=v30.0.0
```

## Environment
To install in "development mode"
    `pip install -e ./fn_odbc_query/`
    
The distribution file can be installed using
    `pip install fn_odbc_query-<version>.tar.gz`
    
Import the package into Resilient by running `resilient-circuits customize`

To configure the ODBC Query function parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the `[fn_odbc_query]` template with the connection string and other optional settings.

After installation, the package will be loaded by: `resilient-circuits run`.

To uninstall,
    `pip uninstall fn_odbc_query`

## Resilient Configuration
Follow the steps to add a fn_odbc_query section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

```
[fn_odbc_query]
# Define your connection string
sql_connection_string=Driver={PostgreSQL};Server=IPAddress;Port=5432;Database=myDataBase;Uid=myUserName;Pwd=myPassword;

# Optional settings:

# Define restricted SQL statements as a list, separated by a comma, using square brackets.
# Example: ["delete", "update", "insert"].
# Comment out this line if there are no restrictions.
sql_restricted_sql_statements=["delete", "insert", "update"]

# Executes commits automatically after every SQL statement.
# Comment out this line to use false - the default.
sql_autocommit=true

# Define a query timeout in seconds.
# Comment out this line to use the default 0, which means "no timeout".
# Might not be supported for all database drivers.
sql_query_timeout=10

# Unicode encoding and decoding settings needed for your SQL database.
# Currently MariaDB, PostgreSQL and MySQL encoding/decoding settings are supported out of the box.
# Recent SQLServer drivers match the specification, no additional Unicode configuration is necessary.
# Define which supported setting to use by using one of the keywords:
# MariaDB, PostgreSQL, MySQL, SQLServer
# Comment out this line to not configure any supported encoding/decoding settings, or to use your own.
sql_database_type=MariaDB

# Define number of rows to fetch.
# Comment out this line to fetch all.
sql_number_of_records_returned=10

# Some ODBC drivers might throw an error while setting db_connection.timeout.
# Psqlodbc driver (PostgreSQL) throws a general error 'HY000'
# Override this SQLSTATE if your odbc driver is throwing a different error.
sql_pyodbc_timeout_error_state=HY000
```

For more information on how to configure database connection, please refer to Resilient Integrations ODBC Query Function Guide.

Example workflows have been provided. They include: 
* ODBC SELECT Workflow
* ODBC UPDATE Workflow
* ODBC INSERT Workflow
* ODBC DELETE Workflow

