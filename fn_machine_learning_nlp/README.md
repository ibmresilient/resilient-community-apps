# Resilient Function for NLP Search

## Description

This function package provides the following feature to be used in a workflow:

* Search existing incidents and find the top similar ones.

In addition, this package contains a command line tool used to build a Natural Language Process (NLP) model.
Please refer to the User Guide for instructions on building the model and running predictions.

## System Requirements
- Resilient platform version 32 or later
- Ability to connect to a Resilient platform with HTTPS on port 443 and 65001
- The minimum set of Resilient API permissions if using an API key account:
    - Incidents.Read
    - Edit Org Data
    - Functions.Read

## Package Dependencies
- sklearn 0.19.2
- pandas 0.23.3
- numpy 1.12.1
- scipy 1.1.0
- Resilient Circuits version 32 or later

## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -c` or update app.config with `resilient-circuits config -u`.

The app.config file needs the following configuration values, in addition to those in the appropriate [resilient]
section for connecting to your Resilient platform:

```
[fn_machine_learning_nlp]
#
# Required. The (absolute) path to the folder of the saved NLP model
#
model_path=path_of_the_saved_models

#
#   Advanced configuration
#-------------------------
# Use the followings to optimize the performance of a NLP model
#
# Number of features for NLP word2vec model.
num_features=50
```

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient platform.

## Start
Start this function with: `resilient-circuits run`

## Build a new NLP model
Use the command line tool:
```
res-ml build_nlp
```
to build a machine learning model

### Rebuild the NLP model
Same as building a new model.

As a rule, it is recommended that customers rebuild their model once a week.

There are more advanced options. Please refer to the User Guide.
## Uninstall

    pip uninstall fn-machine-learning-nlp

## Troubleshooting
If `res-ml build_nlp` fails due to a LookupError caused by SSL errors and NLTK Downloader unable to obtain specific resources,
you can run the file `bin/nltkdownload.py` and download everything for NLTK. This will resolve any future SSL errors when trying to access NLTK resources.