Post to Twitter from Resilient
===================================


Use Case: Given a twitter account defined in the config file and a message
specified when executing a manual action, post the message to twitter. This
would be useful if one is managing the social media accounts of a company.


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.

Copy the .py file into your `components` directory, where it will be
loaded automatically when your application starts.

Copy the configuration file fragment into your application's configuration
file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:


## Message Destination

Create a Queue message destination with programmatic name `twitterpost`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Manual Action

Create an manual action named 'Post to Twitter', associated with object type
"Incident". Choose `twitterpost` as the message 
destination. 


## Twitter Configuration

This incident assumes you have a working twitter account with valid login
credentials. To get your keys for authenticating to twitter and interacting
with twitter's API, follow the instructions for the Python twitter API
as detailed at [https://github.com/sixohsix](https://github.com/sixohsix).

Once you have followed those instructions and gotten your login credentials,
put them in the associated places in the app.config.fragment file. 
