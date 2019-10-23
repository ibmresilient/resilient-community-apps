# Resilient Function for NLP Search

## Description

This function package provides the following feature to be used in a workflow:

Search existing incidents and find the top similar ones.

In addition, this package contains a command line tool used to build a Natural Language Process (NLP) model.
Please refer to the User Guide for instructions on building the model and running predictions.

## System Requirements
- Resilient Server version 33 or later
- Ability to connect to Resilient server with HTTPS on port 443 and 65001

## Package Dependences
- sklearn 0.19.2
- pandas 0.23.3
- numpy 1.12.1
- scipy 1.1.0
- resilient_circuits version 33 or later

## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -c`.

The app.config file needs the following configuration values, in addition to those in the appropriate [resilient] section for
connecting to your Resilient platform:

```
[resilient]

[resilient_ml]

```

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Start
Start this function app with: `resilient-circuits run`

## Build a new NLP model
Use the command line tool
```
res-ml build_nlp
```
to build a machine learning model
```

### Rebuild the NLP model
Same as building a new model.

As a rule, it is recommended that customers rebuild their model once a week.

There are more advanced options. Please refer to the User Guide.
## Uninstall,

    pip uninstall fn_resilient_nlp
