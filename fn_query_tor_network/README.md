# About TOR  
 
The Query TOR Network API is a RESTful Web service allowing TOR Customers to query IP Addresses and Host names to search against TOR network Exit Nodes. This function utilizes this API to determine if a Resilient artifact is part of the TOR network.

# Using TOR Function
This package contains one rule and one workflow as an example.
Below are details of the input and outputs of the API.

Input : The function takes an IP Address or DNS Name contained as an artifact value
Output : Returns the json query results through the variable 'results', which contains the following:

1. status -- (if object found in TOR Network it will be 'success' or else 'failed')
2. value  -- (a Boolean value '1' for success and '0' for failures)
3. data   -- (a complete json data object from the result)
      
## Resilient Configuration

Follow the steps to add a TOR section to your app.config file by running resilient-circuits config [-u | -c] and updating the fields:

     [fn_query_tor_network]
     base_url = https://onionoo.torproject.org/details
     flag = Exit      --(The Flag can be 'Running','Exit' for more information on flag settings - https://metrics.torproject.org/onionoo.html)
     data_fields = exit_addresses,or_addresses,host_name   -- (The data fields should be comma separated and no space should be given in between each fields)
  
## Installation

To install in "development mode"

    pip install -e ./fn_query_tor_network/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_query_tor_network


To package for distribution,

    python ./fn_query_tor_network/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
