# Resilient Integration with Elasticsearch

**The ElasticSearch integration allows users of the Resilient Platform to connect to and query an ElasticSearch Database.**

Users can specify the location of a remote Elasticsearch instance and query this instance for data which is then returned to Resilient for display or use by other functions.


Queries provided to the function must be properly formed to work.
Please review the [ElasticSearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/6.3/search-request-body.html) for examples on how to form your query.
A number of example queries are available when setting up the function in a workflow.

Two options are available for connection:
HTTP connection to localhost or remote 
HTTPS connection with username:password authentication

If you wish to connect to a resource with a self signed cert can provide a cafile as one of the config options.

  - [app.config settings:](#appconfig-settings)
  - [Function Inputs: Elasticsearch Query:](#function-inputs-elasticsearch-query)
  - [Pre-Processing Scripts](#pre-processing-scripts)
  - [Post-Processing Script](#post-processing-script)
  - [ElasticSearch Query Function Output:](#elasticsearch-query-function-output)
  - [Rules](#rules)# Resilient Integration with Elasticsearch

## app.config settings

```python
[fn_elasticsearch]
es_datastore_url = <YOUR_URL>
es_datastore_scheme = <https OR http>
es_auth_username = <YOUR_USERNAME>
es_auth_password = <YOUR_PASSWORD>
es_cafile = <PATH_TO_CERT_FILE>
```

## Function Inputs: Elasticsearch Query

| Function Name | Type | Required | Example |
| ------------- | :--: | :-------:| ------- |
| `es_doc_type ` | `String` | No | `'logs'` | 
| `es_index ` | `String` | No | `'logs'` | 
| `es_query ` | `String` | Yes | `'logs'` |  


## Pre-Processing Scripts

The workflow `Example: ElasticSearch Query from Artifact` includes a pre-processing script which gathers the input `es_query` from the artifact value and uses that as the query.

The workflow `Example: ElasticSearch Query from Incident` does not use a pre-processing script. With this in mind, to improve the usability of this workflow, 3 example query's are provided for `es_query` to help get up to speed. 

## Post-Processing Script

```python

"""
# An Example of the result object 
    results = {
        "inputs": {
          "es_query": { "query": { "match_all": {} } },
          "es_doc_type": logs,
          "es_index" : my_logstore
        },
        "query_results": [
          <elasticsearch-record>,
        "success": True / False,
        "matched_records": 1000,
        "returned_records": 100
    }
# Note: The schema of elasticsearch-record; outlined above, will reflect the structure of your data in Elastic itself
"""

if results.matched_records:
  noteText = """<b>ElasticSearch Query status</b>
                <br> Query supplied: <b>{0}</b>
                <br> Total matched records :<b>{1}</b>""".format(results.inputs["es_query"], results.matched_records)
  
  if results.returned_records != 0:
    noteText += """<br> Total returned records : <b>{0}</b>""".format(results.returned_records)
  incident.addNote(helper.createRichText(noteText))
```

## ElasticSearch Query Function Output

The function returns the results as a Python Dictionary. Here is an example ouput:

```python
  results = {
    "inputs": {
        "es_query": { "query": { "match_all": {} } },
        "es_doc_type": logs,
        "es_index" : my_logstore
    },
    "query_results": [
      <your_elasticsearch_record_schema>
    ],
    "success": True,
    "matched_records": 11000,
    "returned_records": 1000
  }
```

## Rules

| Rule Name | Object Type | Workflow Triggered |
| --------- | :---------: | ------------------ |
| 	Example: ElasticSearch Query from Artifact | `Artifact` | `Example: ElasticSearch Query from Artifact` |
| 	Example: ElasticSearch Query from Incident | `Incident` | `Example: ElasticSearch Query from Incident` |