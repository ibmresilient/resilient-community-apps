# Resilient Functions Integration to Slack

This function creates a Slack message based on a Resilient incident and it's notes. Threaded replies are possible based on a retained Slack thread_id.
Many of the features of posting a Slack message are under customer control including:
- Creating private or public channels
- Inviting users to conversations
- Preserving embedded links
- Slack markdown capability
- Posting messages from Incidents, Notes, Artifacts and Tasks displaying authorship
- Uploading Incident, Task or Artifact attachment
- Slack user ID <@U345GHIJKL> and channel ID <#C012ABCDE> references
- Exporting conversation history to a text file, saving it as an attachment in Resilient and archiving Slack channel

## Installation

Prerequisites:

    resilient-circuits >=v30.0.0

To install in "development mode"

    pip install -e ./fn_slack/

After installation, the package will be accessible to 
    
    resilient-circuits run

To uninstall,

    pip uninstall fn_slack

To package for distribution,

    python ./fn_slack/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install fn_slack-<version>.tar.gz
    
To uninstall

    pip uninstall fn_slack
    
See the accompanying documentation for how to install to Resilient and configure the function.
    
## Configuration

1. Import the package's customization data into the Resilient Platform through the command:

    resilient-circuits customize

	This will create the following custom components:
	* Message Destinations: `slack`
	* Functions: 
	* Custom Fields: 
	* Custom datatables: 
	* Workflows: 
	* Rules: 

2. Update and edit `app.config` by first running:

		resilient-circuits config [-u | -c]. 
		
Then edit the [fn_slack]:

```
    [fn_slack]
    api_token=Your_OAuth_Access_Token
    
    # Set your bot's name that will appear as the author of the message. 
    # Must be used in conjunction with slack_as_user set to false, otherwise ignored.
    username=Resilient
```

## Use

1. Start Resilient Circuits with: `resilient-circuits run`

See the accompanying documentation for how to customize and use the function.