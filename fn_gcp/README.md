## app.config settings:
```python
[fn_gcp]
gcp_region = <GCP_REGION_ID>
gcp_project_id = <GCP_PROJECT_ID>
gcp_function_name = <NAME_OF_CLOUD_FUNCTION>
# Optional Config values
gcp_http_proxy = None
gcp_https_proxy = None

```

## Function Inputs:
**gcp_url:**
* The URL to send to the GCP Cloud Function
* E.g. https://www.ibm.com

## Function Output:
* The function returns the results as a Python Dictionary. Here is an example ouput:
```
{
    "success": True/False,
    "base64Screenshot": <base64 string>
    "input_url": <string>
}
```

To install in "development mode"

    pip install -e ./fn_gcp/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_gcp


To package for distribution,

    python ./fn_gcp/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
