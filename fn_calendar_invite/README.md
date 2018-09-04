# Resilient Function Calendar Invite

This Resilient Function package provides a function fn_calendar_invite
which will send an email with a calendar invitation in ICS format to the members
and owner of an incident. (ICS file can be used by several email and
calendar programs including Microsoft Outlook, Google Calendar and
Apple Calendar.)

Also included in the package:

An example workflow which calls the fn_calendar_invite function:

	example_calendar_invite

An example rule:

	Example: Calendar Invite

And a message queue:

	fn_calendar_invite



## fn_calendar_invite Package Dependences
- Resilient V31 or later 
- Python V2.7.10 or later
- Python email package, for Python version less than 3.0

## Installation

1) Install fn_calendar_invite in "development mode":
    ```
	$ pip install -e  ./fn_calendar_invite/
    ```
   or the distribution file can be installed using:
   
    ```
	$ pip install fn_calendar-<version>.tar.gz
	```

## Setup

To configure the fn_calendar_invite parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the [fn_calendar_invite] section to define the input
parameters for account from which email will be sent:

```
[fn_calendar_invite]
# Setup the email information for the sender of the calendar_invite email 
email_username=jimmy@example.com
email_password=l33t
email_nickname=Resilient Meeting Organizer
email_host=mail.example.com
email_port=25
```
## Customize
To install function definition, message destination, sample workflow to the Resilient server:

	$ resilient-circuits customize
	
This package includes the followings:

	Functions:
		- fn_calendar_invite

	Sample Workflows that demostrate how to use fn_calendar_invite:
		- Example: Calendar Invite

## Start
To start this function: 

	$ resilient-circuits run


## Uninstall
To uninstall this function:

	$ pip uninstall fn_calendar_invite
  
