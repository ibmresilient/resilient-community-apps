# Resilient Functions for Microsoft Security Graph
<br/>
## Installation

To install in "development mode":

    pip install -e ./fn_microsoft_security_graph/

After installation, the package is loaded by `resilient-circuits run`.


To uninstall:

    pip uninstall fn_microsoft_security_graph


To package for distribution:

    python ./fn_microsoft_security_graph/setup.py sdist

The resulting .tar.gz file can be installed using:

    pip install <filename>.tar.gz

<br/>
## Configuration

1. Import the package's customization data into the Resilient platform using the command:

		resilient-circuits customize

2. Update the `app.config` file by first running:

		resilient-circuits configure -c, to start a new configuration file or
		resilient-circuits configure -u, to update an existing configuration

3.	Edit the `app.config` file:

		[fn_microsoft_security_graph]
		# Graph URL with version number
		microsoft_graph_url=https://graph.microsoft.com/v1.0/
		tenant_id=<Tenant directory id>
		client_id=<App client id>
		client_secret=<App client secret>
		
		## Polling options
		# How often polling should happen. Value is in seconds. To disable polling, set this to zero.
		msg_polling_interval=0
		#incident_template=<location_of_template_file>  # If not set uses default template.
		
		# String query to apply to the alert polling component. This will be added to the end of the url
		# when searching for alerts. The example shown below would make the whole search url equal to
		# https://graph.microsoft.com/v1.0/security/alerts/?$filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'
		# This query string is full OData so alert query can start with 'top=', 'skip=', 'filter=', etc. Do not add a '$' at the start
        # of the value as that character is reserved for environment variables
		#alert_query=filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'
		
		# Alert Time range sec - Optional value in seconds to set the start dateTime values for the createdDateTime field when filtering alerts.
		# This is calculated by adding to the filter 'createdDateTime ge (current_dateTime - alert_time_range_sec)
		#alert_time_range_sec=3600

## Customization
For each workflow, verify the inputs and the post-process scripts to ensure that they are accurate and appropriate.

## Run Functions
1. Start Resilient Circuits with:

		resilient-circuits run

2. Trigger one of the rules that will return information on alerts from the Microsoft Graph.

## Run alert poller:
Based on configurations under the `## Polling options` section in the `app.config`, you can customize the polling interval, which alerts to find, and other settings.

1. Start Resilient Circuits with:

		resilient-circuits run

2. When an alert that does not have a corresponding open incident in the Resilient platform and would be returned by the search query, is generated in the Microsoft Security Graph, a new incident is created.