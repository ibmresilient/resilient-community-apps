Task Tracker
=============


Use Case: This is a circuits module to be used to track tasks in Resilient. 
Every time a task is closed or re-opened in Resilient, this script posts
the task name, init_date, closed_date, task ID, and how long it took to close
said task in a data table. This enables the user to quickly see which tasks
were closed and how long it took to close each one.


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.
* A script to automatically set up the rule, data table, and message destination
* A configuration file for the setup script

Copy the .py file into your 'components' directory, where it will be
loaded automatically when your application starts.

Copy the configuration file fragment into your application's configuration
file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
To do this, there are two options. If you would like to set everything up
automatically, you can:
* Fill out the setup.config file with login credentials
* Run the setup.py script to automatically create an automatic rule, data table, 
and message destination
* Manually add the integration user to the tasktrackerqueue users list
* Add the Task History table to an incident tab to make it visible
OR you can set everything up manually by carrying out the following 
instructions. 


## Message Destination

Create a Queue message destination with programmatic name 'tasktrackerqueue'.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

Note: 'tasktrackerqueue' must match the queue field in the app.config file.

## Rule

Create an automatic rule named 'Task Tracker', associated with  
object type "Task".  Choose 'tasktrackerqueue' as the message destination.  
Add condition "Active is changed".

## Data Table

Create a data table with the title "Task History," the text value "task name",
the text value "task notes", the datetimepicker "init date", the 
datetimepicker "closed date", the text field "time to close, and the text field
"task id". Make sure all those tasks are in order. Place the names of the
fields you just created in the app.config file under the appropriate column.

