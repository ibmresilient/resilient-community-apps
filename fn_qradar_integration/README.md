# Resilient Function for QRadar integration

## Description

This function package provides the following features which can be used in workflows:

1. Perform an ariel search. The returned data can be used in the post-process script of a workflow to update a datatable
2. Find an item in a given reference set. This function can be used to check if an artifact is in a reference set
3. Add an item to a given reference set
4. delete an item from a given reference set

## System Requirements
- Resilient Server version 30 or later
- QRadar 7.2.8 or later
- Ability to connect to Resilient server with HTTPS on port 443 and 65001
- Ability to connect to QRadar with HTTPS on port 443

## Package Dependences
- resilient_circuits version 30 or later
- python version 2.7.10 or later
## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -u`.

The app.config needs the following configuration values, in addition to the appropriate [resilient] section for connecting to your Resilient platform:  

```
[fn_qradar_integration]  
host = qradar-server-hostname-or-ip-address    
username = qradar-login-user-name 
splunkpassword = qradar-password-keyring-recommended
verify_cert = False-to-skip-qradar-cert-validation
```
## Customize
Run with: `resilient-circuits customize` to install function definitions, message destinations, sample workflows, datatable, and rules to the Resilient server. 

This package includes the followings:

Functions:
- QRadar Add Reference Set Item
- QRadar Delete Reference Set Item
- QRadar Find Reference Set Item
- QRadar Search

Sample Workflows that demostrate how to use the functions above:
- Example of adding an item to QRadar reference set
- Example of deleting QRadar Reference set item
- Example of finding an item from a QRadar reference set
- Example of searching QRadar events using offense_id

Sample rules that call the sample workflow above
- Add to QRadar Reference Set. A menu item added to artifact.
- Delete from QRadar Reference Set. A menu item added to artifact
- Find in QRadar Reference Set. A menu item added to artifact
- QRadar Move from suspet to blocked. A menu item added to artifact
- Search QRadar for offense id


## Start
Start this function app with: `resilient-circuits run`

## Samples
Please refer to the installation doc for more details about sample searches and workflows included in this package.

## Uninstall
Run with `pip uninstall fn_qradar_integration`

