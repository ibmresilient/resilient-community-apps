# Resilient Function - ODBC Query Function

The ODBC Query Function establishes an OBDC connection to the desired SQL database server and executes SELECT, INSERT, UPDATE or DELETE SQL statements.

Before installing, verify that your environment meets the following prerequisites:
* Resilient platform is version 30 or later. 
* You have a Resilient account to use for the integrations. This can be any account that has the permission to view and modify administrator and customization settings, and read and update incidents. You need to know the account username and password.
* You have access to a Resilient integration server where you will deploy and run the functions code. If not, you need to install and configure the server as described in the [Integration Server Guide](https://github.com/ibmresilient/resilient-reference/blob/master/developer_guides/Integration%20Server%20Guide.pdf).
* Because of dependencies on other libraries, including GCC, the system hosting the integration server must allow additional components to be installed. Therefore, it cannot be installed on the default Resilient appliance.
* The ODBC function uses pyodbc, an open source Python module. For an integration server on Linux, you need to install additional packages to support compiling pyodbc, before installing the function. When installing pyodbc on Linux, the pip utility downloads and compiles the pyodbc source code. This requires that related components and source files are available for the compile to succeed. Got to [GitHub Pyodbc Wiki page](https://github.com/mkleehammer/pyodbc/wiki/Install) for the list of all needed packages and installation instructions.
* resilient-circuits >=v30.0.0

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

# Define number of rows to fetch.
# Comment out this line to fetch all.
sql_number_of_records_returned=10

# Executes commits automatically after every SQL statement.
# Comment out this line to use false - the default.
sql_autocommit=true

# Unicode encoding and decoding settings needed for your SQL database.
# MariaDB, PostgreSQL and MySQL encoding/decoding settings are supported out of the box.
# Recent SQLServer drivers match the specification, no additional Unicode configuration is necessary.
# Define which supported setting to use by using one of the keywords:
# MariaDB, PostgreSQL, MySQL, SQLServer
# If commented out, none of the supported encoding/decoding settings will be configured.
sql_database_type=PostgreSQL

# Define query timeout in seconds.
# If commented out, the default value 0 is used, which means "no timeout".
# Some ODBC drivers do not implement the connection timeout and will throw pyodbc.Error while trying to set it.
# The error will be logged as a warning and will not terminate the workflow.
#sql_query_timeout=10
```

For more information on how to configure database connection, please refer to Resilient Integrations ODBC Query Function Guide.

Example workflows have been provided. They include: 
* ODBC SELECT Workflow
* ODBC UPDATE Workflow
* ODBC INSERT Workflow
* ODBC DELETE Workflow