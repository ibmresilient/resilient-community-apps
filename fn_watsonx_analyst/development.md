# Development

## Requirements
- Python 3.12
  - packages will be pulled in through `setup.py`

## Setup

1. Create a virtual environment.

```sh
python -m venv venv
```

2. Install the app package (from the base of the repository.)

```sh
pip install -e .
```
> (This should grab all of your dependencies)

3. Grab the SOAR API Key ID and secret

Administrator Settings > Users > API Keys > Create API Key (on right) 

4. Update (`$HOME/.resilient/app.config`)

```
[resilient]
host=<IP address or Domain name of SOAR>
org=<Name of org; can include spaces>
api_key_id=<API KEY ID>
api_key_secret=<API Key Secret>
cafile=false
port=443

[fn_watsonx_analyst]
watsonx_api_key=$WATSONX_API_KEY
watsonx_project_id=$WATSONX_PROJECT_ID
watsonx_endpoint=https://us-south.ml.cloud.ibm.com

[watsonx_property_labels]
# below this line, you can include incident_property_name="New property label"
```
> Get the project ID on slack from Walter

5. Package the app
```
resilient-sdk package -p .
```

6. Install the App on SOAR

- Go to Administrator Settings -> Apps -> Install
- Upload the .zip file under the `dist/` directory in this repository.

## What happens when the SOAR customizations are updated 

If the function definitions are updated, you'll need to perform steps 2, (4 if config/app name changed), 5, and 6.

