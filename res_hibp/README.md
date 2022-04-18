# SOAR Content Package for Have I Been Pwned

## Description

This content package contains a single resource file with the following rule and workflow:

1. Have I Been Pwned Hits (Rule)
- Automatic rule invoked by an artifact of type Email Recipient or Email Sender 
- Associated with the Have I Been Pwned Hits Workflow
2. Have I Been Pwned Hits (Workflow)
- Queries Have I Been Pwned for Breaches and Pastes given an email address.
- Uses the Functions Have I Been Pwned Get Breaches and Have I Been Pwned Get Pastes


## Package Dependences
The workflows in this package depend on the following
- SOAR Version 43
- fn_hibp Version 2.0.2


## Import
Ensure that the above packages have been installed.
Download the res_hibp package. Unzip it if necessary(tar -xvf res_qraw_mitre.tar). 
In SOAR server, go to Administrator Settings->Organization->Import->Import Settings 
and select the hibp.res file downloaded above.

## Usage
Once the resource file is successfully imported, the workflows included in the file are ready for use.


### Example of QRadar Advisor Offense Analysis with MITRE
This workflow invokes two functions from two integration packages.
![Workflow1](./screenshots/workflow1.png)
The "QRadar Advisor Offense Analysis" is a function from the QRadar Advisor integration, 
and "MITRE Tactic Information"
is a function from the MITRE integration. The data flow is shown below
![Dataflow1](./screenshots/dataflow1.png)
Here, a user starts from an incident with a QRadar offense id. In the following example, 
the incident is escalated from QRadar offense 23. 
![Offense Analysis](./screenshots/offense_analysis.png)
Note for convenience, a tab was created to hold all the related information here. To do analysis for the related offense, select 
Actions->"QRadar Advisor Offense Analysis with MITRE", to start this workflow. The first function, "QRadar 
Advisor Offense Analysis", is called to get 
the analysis and insights of the offense from QRadar Advisor. The insights contains MITRE ATT&CK 
tactic information, shown in the "MITRE ATT&CK of Incident" data table. In this example, 
QRadar Advisor returns a tactic called "Command and Control", together with a confidence value 
of 60 (over 100). 

With this information, the second function "MITRE Tactic Information" is called. This function 
retrieves the following information from the MITRE STIX TAXII server: 
- Tactic ID
- Reference link to tactic
- Techniques related to this tactic
The information is populated into the "MITRE ATT&CK Techniques" data table.
 
Note that from the "MITRE ATT&CK Techniques" data table, the user can easily create a task for 
a selected technique, by clicking a data table menu item.
![Create task](./screenshots/create_task.png)
A new task is created with description, detection, and mitigation for the selected technique.
![New task](./screenshots/new_task.png)

tasks for selected techniques.

## Uninstall
Manually delete the followings:
1. Rules
- "Have I Been Pwned Hits"
2. Workflows
- Have I Been Pwned Hits




