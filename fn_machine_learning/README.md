# Resilient Function for Machine Learning

## Description

This function package provides the following feature to be used in a workflow:

Make a prediction of a selected field of a given incident, using a pre-built machine learning model.

In addition, this package contains a command line tool used to build a machine learning model.
Please refer to the User Guide for instructions on building the model and running predictions.

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

The app.config file needs the following configuration values, in addition to those in the appropriate [resilient] section for
connecting to your Resilient platform:

```
[resilient]

[machine_learning_predict]
#   The folder for saved models
model_dir=path to the folder of saved machine learning models you built

[machine_learning]
#
#   Field  to predict
#
prediction=severity_code
#
#   Features to use
#       example: features=confirmed, incident_type_ids, negative_pr_likely
features=list_of_fields_for_features_separated_by_comma
#
#   Algorithms supported:
#       Logistic Regression, Decision Tree, Random Forest, Dummy Classifier
#       SVM, SVM with Gaussian kernel, GaussianNB, BernoulliNB, K-Nearest Neighbors
algorithm=Logistic Regression
#
#   Ensemble method is optional, it can be Bagging or Adaptive Boosting (Optional)
#
method=None
#
#   Split samples for testing. 0.5 means 50% of the samples will be used for testing
#
split=0.5

#
# Advanced options
#-----------------
#
#   1. Imbalance Class
#
#   Predicted data could be imbalanced. Uncomment one of the following option
#   to handle it
#
class_weight=balanced
#imbalance_upsampling=true
#
#   2. Data Preparation
#
#   Some prediction values could be misleading for the machine learning model
#   Put those values below. Samples with those values will be removed
#
unwanted_values=None
#
#   3. Filter (Optional)
#
#       * Time filter: format YYYY-mm-dd
#
#time_start=2018-10-01
#time_end=2018-10-08
#
#       * Count: Maximum number of samples to process
#
#max_count = 10000

```

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Start
Start this function app with: `resilient-circuits run`

## Build a mechine learning model
Use the command line tool
```
res-ml
```
to build a machine learning model

### Download incidents
Enter desired values into app.config, and download incidents and save them into a CSV file.
```
res-ml download -o resilient_incidents.csv
```

### Build a model
Using the setings in app.config to build a machine model
```
res-ml build -c resilient_incidents.csv -o incident_prediction.ml
```
Note that the sample workflow ml_predict included in this package uses incident_prediction.ml in
the folder specified in the app.config as model_dir. You can modify the name of model to be used in
the input tab of the workflow if you want.

### View a saved model
Use the view command to view a summary of a saved model
```
res-ml view -i incident_prediction.ml
```

### Rebuild a saved model
If you have newly added incidents, and you want to retrain a saved model, you can rebuild it
```
res-ml rebuild -i incident_prediction.ml
```
As a rule, it is recommended that customers rebuild their model once a week.

There are more advanced options. Please refer to the User Guide.
## Uninstall,

    pip uninstall fn_machine_learning
