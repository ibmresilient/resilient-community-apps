## History
9/1/2023 -  Initial Documentation

## About this Package:
This branch contains scripts to look for Python2 scripts, workflows, and playbooks

One script is provided:
* [soar-python2-search.py](#soar-python2-search.py)


### Initialization
Only perform the first 2 steps if a Python virtual environment fits your need
* (Only as needed) Create a Python 3 virtual environment
* (Only as needed) source <path to your Python3 virtual environment>>/bin/activate
* pip3 install resilient requests getpass

## soar-python2-search.py
This script reports on any use of Python2 within SOAR-based scripts, workflows, and playbooks

### Usage
python3 soar-python2-search.py https://[host] [org] [API key ID]  


### Examples
python3 soar-python2-search.py https://9.30.199.112 SOAR_Apps 23db6760-0618-484a-9649-38e6b909da46

