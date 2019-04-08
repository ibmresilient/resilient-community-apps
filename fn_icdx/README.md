# Fn_ICDX

This integration is built for use with the Symantec Integrated Cyber Defense Exchange

There are two parts to the integration.  
The first is a number of functions which provide access to the ICDx Search API.
The second is a component which attempts to connect to a set-up ICDx forwarder. The forwarder then sends filtered events to the IBM Resilient Platform.

### Search API Function
The ICDx Search API provides a request/response model for gathering information about events in the ICDx Platform. 
There are 2 methods for interfacing with the API
+ A HTTP REST API
+ AMQP 

This integration uses AMQP to create a asynchronous request/response model. A request is sent to the `dx.archives.search` exchange and responses are sent to an exclusive queue which is set up by the caller.

The AMQP API returns a status code of 200 for requests which returned a non-empty response and 204 for empty ones.

There are 3 available API operations at the time of writing. Each one is denoted by its `id` value whereby:
+ 0 -- Represents the Get Event API Operation
+ 1 -- Represents the Find Events API Operation
+ 12 -- Represents the Get Archive List API Operation

#### Get Event
This function takes in an input of a Event UUID and if a matching Event is found in the ICDx platform, this Event is returned to the IBM Resilient Platform for use by other functions.

+ True/False -- Whether or not the query was successful. An empty response is consider unsuccessful
+ The event itself

#### Find Events
The Find Events function is used to search through all the events in the ICDx Platform or from a particular archive of events.
Requests can limit the maximum number of results returned by setting a `limit` attribute on the request payload. 


Results from the Find Events function include:
+ True/False -- Whether or not the query was successful. An empty response is consider unsuccessful
+ A list of results which were returned from the Find Events request
+ The number of events that were gathered from the event

#### Get Archive List 
Events in the ICDx platform, go to a Default Archive. ICDx allows users to setup a number of dedicated archives for certain events. 
Additionally a System archive is available for events specific to the ICDx platform. 

The Get Archive List function allows users to query which archives are available. 
Results include:
+ The name of archive
+ The UUID of the archive
+ The archive path relative to `$SYMC_DATA/archives` directory.

### Forwarder 
The ICDx Platform provides a way to forward filtered events through a number of means such as over AMQP. 
The icdx_forwarder_observer attempts to connect to a forwarder exchange that a user has setup on the ICDx platform. 
Once connected events are forwarded to this observer which will then create incidents in the IBM Resilient Platform. 

### Installation
#### Set the following values in the config file (`app.config`) under the `[fn_icdx]` section:

```
icdx_amqp_host = <YOUR_ICDX_URL>
icdx_amqp_port = <YOUR_ICDX_PORT>
icdx_amqp_vhost = <YOUR_ICDX_VHOST>
icdx_amqp_username = <YOUR_ICDX_USERNAME>
icdx_amqp_password = <YOUR_ICDX_PASSWORD>
```


To install in "development mode"

    pip install -e ./fn_icdx/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_icdx


To package for distribution,

    python ./fn_icdx/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install fn_icdx-1.0.0.tar.gz

## How to use the function

1. Import the necessary customization data into the IBM Resilient platform after pip installing the function:

    resilient-circuits customize

    This creates the following customization components:

    * Function inputs: `icdx_search_request`, `icdx_uuid`
    * Message Destinations:`fn_icdx`
    * Functions:`icdx_utilities_find_events`, `icdx_utilities_get_archive_list`, `icdx_utilities_get_event`
    * Workflows:`example_icdx_utilities_find_events`, `example_icdx_utilities_get_archive_list`, `example_icdx_utilities_get_event`
    * Rules:`Example: ICDx Utilities: Find Events`, `Example: ICDx Utilities: Get Event`, `Example: ICDx Utilities: Get Archive List`

2. Update and edit `app.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits:
    ```
    resilient-circuits run
    ```

4. Trigger the rule.

