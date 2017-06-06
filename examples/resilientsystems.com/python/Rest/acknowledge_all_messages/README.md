Acknowledge All Messages
===============

Command line tool that allows you to subscribe to subscribe to all of 
an org's messages destinations and acknowledge all outstanding 
action messages.  The Resilient user specified must have permission
to subscribe to all destinations that you want cleared.  This is useful
for clearing out accumulated action messages during testing.


## Environment and Installation

This integration is provided as
* A command line tool

This tool requres the co3 and stomp packages to be installed.
pip install stomp.py


## Sample Usage

./ack_all_actions.py --email user@example.com --password Pass4Admin --host app.resilientsystems.com --org TestOrg --cafile false


Once all messages have been acknowledged, you can end it with Ctrl+C
