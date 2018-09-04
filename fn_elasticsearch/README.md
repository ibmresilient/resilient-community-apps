# Fn_ElasticSearch_Query
The ElasticSearch integration allows users of the Resilient Platform to connect to and query an ElasticSearch Database.

Users can specify the location of a remote ElasticSearch instance and query this instance for data which is then returned to Resilient for display or use by other functions.

The function takes 3 inputs :

+ Index (Optional) --> An index to search for data. Default is searching all indices
+ Doc_Type (Optional) --> An type of document to search. Default is searching all doc_types
+ Query (Required) --> The query we will be submitting

Queries provided to the function must be properly formed to work.
Please review the [ElasticSearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/6.3/search-request-body.html) for examples on how to form your query.
A number of example queries are available when setting up the function in a workflow.

Two options are available for connection:
HTTP connection to localhost or remote 
HTTPS connection with username:password authentication

If you wish to connect to a resource with a self signed cert can provide a cafile as one of the config options.

### Installation
#### Set the following values in the config file (`~/.resilient/app.config`) under the `[fn_elasticsearch]` section:

```
es_datastore_url = <YOUR_URL>
es_datastore_scheme = <https OR http>
es_auth_username = <YOUR_USERNAME>
es_auth_password = <YOUR_PASSWORD>
es_cafile = <PATH_TO_CERT_FILE>
```

To install in "development mode"

    pip install -e fn_elasticsearch/

To package for distribution,

    python fn_elasticsearch/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install dist/<filename>.tar.gz

To uninstall,

    pip uninstall fn_elasticsearch

## How to use the function

1. Import the necessary customization data into the Resilient platform after pip installing the function:

    resilient-circuits customize

This creates the following customization components:

* Function inputs: `es_doc_type`, `es_index`, `es_query`
* Message Destinations:`fn_elasticsearch`
* Functions:`fn_elasticsearch_query`
* Workflows:`example_elasticsearch_query_from_artifact`, `example_elasticsearch_query_from_incident`
* Rules:`Example: ElasticSearch Query from Artifact`, `Example: ElasticSearch Query from Incident`

2. Update and edit `app.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits:
    ```
    resilient-circuits run
    ```

4. Trigger the rule.