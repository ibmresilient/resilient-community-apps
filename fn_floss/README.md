# Resilient Function Floss

This Resilient Function package provides a function fn_floss that
takes a binary file as input and returns a list of decoded obfuscated
strings from the file.

Also included in the package are two example workflows: 
- Artifact file input
- Attachment file input

Both workflows create a task or incident note containing the list of
decoded string extracted from the file. 


## Package Dependences
- resilient_circuits version 30 or later
- Python version 2.7.10 or later; Python version 3 is not supported
- Python package vivisect>=0.0.20170525
- Python package floss>=1.5.1

## Installation
1) Install Python vivisect package:
    ```
	$ pip install https://github.com/williballenthin/vivisect/zipball/master
    ```
2) Install Python floss package:
    ```
	$ pip install https://github.com/fireeye/flare-floss/zipball/master
    ```
3) Install fn_floss in "development mode":
    ```
	$ pip install -e  ./fn_floss/
    ```
   or the distribution file can be installed using:
   
    ```
	$ pip install fn_floss-<version>.tar.gz
	```

## Setup

To configure the fn_floss parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the [fn_floss] section to define the parameters to floss:

```
[fn_floss]
# Floss Function
# Use the following floss_options variable to specify the commandline options to be used by 
# the floss package to define the behavior for extracting strings. 
# Each commandline parameter should be separated by a comma.
# The defaults here are: -q quiet mode, -s shellcode, -n minimum string length
# See https://github.com/fireeye/flare-floss/blob/master/doc/usage.md for all possible commandline options.
floss_options=-q,-s,-n 5
```
## Customize
To install function definition, message destination, sample workflows, and rules to the Resilient server:

	$ resilient-circuits customize
	
This package includes the followings:

	Functions:
		- fn_floss

	Sample Workflows that demostrate how to use fn_floss:
		- Example Floss: Artifact input
		- Example Floss: Attachment input

	Sample rules that call the sample Workflows

## Start
To start this function: 

	$ resilient-circuits run


## Uninstall
To uninstall this function:

	$ pip uninstall fn_floss
  
