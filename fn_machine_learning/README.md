# Resilient Function for Machine Learning

## Description

This function package provides the following feature to be used in a workflow:

Make a prediction of one field of a given incident, using pre-built machine model

In addition, this package contains a web component used to build a machine model

## System Requirements
- Resilient Server version 30 or later
- Ability to connect to Resilient server with HTTPS on port 443 and 65001

## Package Dependences
- sklearn 0.19.2
- pandas 0.23.3
- numpy 1.12.1
- scipy 1.1.0
- resilient_circuits version 30 or later

## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -c`.

The app.config needs the following configuration values, in addition to those in the appropriate [resilient] section for
connecting to your Resilient platform:

```
[resilient]
# (Optional) Maximum number of samples to process
# max_samples = 10000
[machine_learning_predict]
# saved model to be used for prediction
active_model=file_path

[machine_learning]
# field  to predict
prediction=severity_code
# example: features=confirmed, incident_type_ids, negative_pr_likely
features=list_of_fields_for_features_separated_by_comma
# algorithm for building model
algorithm=Logistic Regression
# ensemble method
method=None
# split samples
split=0.5


```

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Start
Start this function app with: `resilient-circuits run`


## Uninstall,

    pip uninstall fn_machine_learning
