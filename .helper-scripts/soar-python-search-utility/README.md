## History
9/1/2023 -  Initial Documentation

## About this Package:
This branch contains scripts to look for Python2 scripts, workflows, and playbooks

One script is provided:
* [soar-python2-search.py](#soar-python2-search.py)


### Initialization
* Create a Python 3 virtual environment
* source <path to your Python3 virtual environment>>/bin/activate
* pip3 install resilient

## soar-python2-search.py
This script is used to copy all container images from the IBM official registry, quay.io,
to a customer's private registry. It uses local container tools such as `docker` or `podman` to 
pull containers down from quay.io and then push them to the private registry.

### Usage
python3 soar-python2-search.py https://[host] [org] [API key ID]  


### Examples
python3 soar-python2-search.py https://9.30.199.112 SOAR_Apps 23db6760-0618-484a-9649-38e6b909da46

