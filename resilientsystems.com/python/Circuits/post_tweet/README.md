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

This uses the "twitter" package for python. 
[http://mike.verdone.ca/twitter](http://mike.verdone.ca/twitter)
Install with:
`pip install twitter`

## Twitter Configuration

This integration requires you to have a working twitter account with valid login
credentials. To get your keys for authenticating to twitter and interacting
with twitter's API, follow the instructions for the Python twitter API
as detailed at [https://github.com/sixohsix/twitter](https://github.com/sixohsix/twitter).

Once you have followed those instructions and gotten your login credentials,
put them in the associated places in the app.config.fragment file. 


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Customization Settings menu, then:


## Message Destination
Click the Message Destinations tab.
Create a Queue message destination with programmatic name `twitterpost`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Rule
Click the Rules tab.
Create a Menu Item named `Post to Twitter`, associated with object type
"Incident". Choose `twitterpost` as the message destination. 
