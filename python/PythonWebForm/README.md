# Example Python/Flask Web Form for incident creation

This directory contains an example flask application that creates a web form for creating incidents in the Resilient Platform
without using the Resilient UI 

## Installation
There is not any specific installation.  Pre-Requsites are contain in the file requirements.txt and can be installed with pip with:
```
pip install -r requirements.txt
```
Note, the Resilient API is not available via public python repositories and will have to be manually installed.


## Authentication
Authentication handled by a simple SQLite database for the user.  Passwords are stored in the DB as SHA256 hash values.  Prior to running the web server, you must run the db_create.py which will create the database.  If run from the top level directory of the project, it will create the database in app/db/webform.db. 
```
python db_create.py
```
Then add a user by running the db_adduser.py script
```
python db_adduser.py --user=<username> --password=<password>
```

this will add the user to the tool.  By default the database contains the user *admin* with the password *admin*.  To remove this use 
```
sqlite3 ./WebForm/db/webform.db
sqlite> select * from user;
sqlite> delete from user where username='admin'
```

Run the server with
```
python runserver.py
```


This will run on the localhost interface a test server instance.


## Configuration
There are 2 levels of configuration.  First being the FLASK environment.  This is in the top level config.py file.  The important values are the "RES*" variables.  These are the pieces
```
RES_ID - id of the resilient user to run the creation 
RES_PW - Password of the above resilient user
RES_PORT - port for accessing the Resilient server (usually 443)
RES_ORG - text name of the organization within the Resilient system
RES_PROXY -  Proxy for connecting to Resilient
RES_CA - path to CA file, or False if Certificate verificaiton is not to be used.
```
The rest are internal to the applicaiton.

### form_layout.json
this file located in the app/config directory is the layout of the form and the mapping to the Resilient API.    The following data types are supported
```
Text - single row Text box
TextArea - Text box defined by the number of rows and columns specified
Boolean - True/False
Select - single select item
MultiSelect - Multiple item select
Date - Date picker
DateTime - Date and Time stamp picker
Number - Integer value
```
Note, there is no validation of inputs in this example code. 

The fields within a specification are
```
fieldlabel - text displayed to the left of the field
fieldname   - internal name of the field 
fieldtype - type of field (see above)
choosefrom - what resilient system api field will the selections come from
resapi - what resilient api the input value will be mapped to.
row - number of rows (height) to display in a text area
cols - number of columns (width) to make the text area
```

## Usage

To print usage information:

```
python scripts/runserver.py --help
```
This creates a local test/development web server which can be accessed from your local host to exercise the example client create


## Limitations
### Authentication
Authentication is a very simple SHA256 hashed password stored in a SQLite database.  As such it is not a production ready implementaiton, nor does it allow for authentication against other sources.  It utilizes the FLASK LoginManager extension which provides an abstraction for different authentication technologies

### Authorization
There is no authorization or limitation once authenticated.  This simply creates a web form that then creates an incident in the Resilient platform.

### Required Fields
The application does not differentiate required fields for incident creation from optional fields.  

### Forms
The forms are dynamically created based on the configuration.  Different browsers render the form elements differently.  Specifically, in FireFox, the DateTime picker does not allow for entering the time portion of the data.  Other form elements may be affected by the browser.  Most of the testing of this has been done against Google Chrome. 

There are two forms within this example.  A simple login form which authenticates using the SQLite database.  The second form is created based on the form_layout.json file.  As this is dynamically created (fields are created based on the order which they are found in the file) this is a critical component of the example.  This is hung off the index route.  And is set up to require login before the form will be displayed.

The "test" form which is an example used to test various types of fields to implement the application.

# Running under Apache
As this is an example, this has not been tested running under WSGI with Apache.  It is up to the user to understand how to configure WSGI with Apache and running under Apache.


## Apache2 mod-wsgi
Example configurations for running under apache2 with mod-wsgi are provide.  The file *apache2.config* is an example virtual host configuration (non-ssl) which assumes that the code is installed in /var/www/WebForm directory.  Logging of the application under mod-wsgi is done to */tmp/webform.log*.  This can be changed in the *WebForm.wsgi* file.

