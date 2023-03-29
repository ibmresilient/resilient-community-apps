# Contributing the Community Apps

We encourage the Resilient teams to contribute their integrations to the Community Apps repo. 
In order to submit your solutions, a number of steps need to be performed. 

In general the steps for submissions include:

* accessing the community apps repository
* creating a branch off community apps
* developing or copying in your code
* testing your submission
* submitting a pull request
* testing the submission by Engineering
* merging the code to the master branch
* packaging for app exchange

## Access to Community Apps
Both Professional Services and Sales Engineering teams have access to read from the Community Apps. If you cannot access this repo, you need to contact your manager who can add you to the approrpriate team list.

Once you have repository access, make sure you've taken the steps to access the repo by setting up your ssh key for git.
Here are the steps needed:


1) Create your ssh key

    $ ssh-keygen [don't enter passphrase]

2) Add the ssh key ( ~/.ssh/id_rsa.pub) to your profile on github.ibm.com. This is the URL to manage ssh keys on GitHub: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/. NOTE - need to copy the key carefully. See this if you get an "invalid key" error in git.

3) Create the repo clone 
    
    $ git clone git@github.ibm.com:Resilient/resilient-community-apps.git
    
## Create a branch off community apps
    $ cd resilient-community-apps 
    $ git checkout -b <yourname>/<product>
    
## Develop or copy in your code
With this repo, you can now develop your code using `resilient-circuits codegen` or by copying in code you've developed in a different file location.
There are many Engineering wiki documents on python development and function code guidelines to ensure best practices are followed. These wikis can be found here:
[Development Guidelines](https://w3-connections.ibm.com/wikis/home?lang=en-gb#!/wiki/Wc375b6e38cc2_46a1_be89_68faa5cc5193/page/API%20and%20Developer%20Resources).
    
Review git for the uses of `git add`, `git commit` and `git push` for adding your code to this branch.

## Test your submission
Ensure you test your integrations using
* Python 2.7
* Python 3.6

These two environments can use different references a given imported library and each version of python handles unicode different. 

Ideally, testing should include a RHEL environment (or CentOS) and Windows. 

## Submit a pull request
After your testing is complete, ensure that it contains a full set of rules and workflows to demonstrate your code.
You can create a Pull Request from the git browser window by navigating to your branch and cicking the `New Pull Request` button.
Make `Mark Scherfling` a reviewer and others may be pulled in to participate.

The code will be reviewed against coding best practices.  
A number of guidelines to keep in mind will speed the process.

* run `pylint` reviewing errors and other standards infractions, as necessary. I don't believe all are needed for submissions.
* run `bandit` to ensure there are no security issues
* review hardcoded URLs which may be more useful to contain (the base address) in an app.config file
* modularize code for easy reading and code separation
* document functions and complex code blocks for readability
* complete the readme document for customer use and installation

It can take multiple iterations until code is accepted for merging.

## Testing the submission by Engineering
Depending on the complexity of the code, an additional level of testing can be done by Engineering. 
If access to the end-point solution is still assessible, sharing the credentials and URLs would be helpful.

## Merge the code to the master branch
Once the code is accepted, Engineering will perform a merge to the master branch.
The development branch will then be deleted.

## Package for App Exchange
This step can be done by either Engineering or the submitting individual, 
depending on your permissions available in the X-Force Exchange. Key parts of a submission are:

* Descriptions of the integration. This can be extracted from the readme.md file or setup.py
* Screenshots. These can be made from the example workflow and possibly the resulting data from an action taken.
* Logos. Engineering can complete this if a vendor logo doesn't exist or cannot be used.





