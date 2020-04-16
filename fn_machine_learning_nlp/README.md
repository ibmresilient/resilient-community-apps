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
num_top_similar_incidents=5

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
If `build_nlp` fails due to SSL certifications errors caused by NLTK, you can run the following in a separate file and
download everything for NLTK:
```buildoutcfg
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download()
```