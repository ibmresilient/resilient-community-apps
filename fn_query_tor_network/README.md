##About TOR  
 
==
The Query TOR Network API is RESTful Web service allowing TOR Customers to query the IP Addresses and Host names to search in Exit Node TOR Network.

##Using TOR Function
 We have included one rule and one workflow as an example.
Below is details of Input and outputs of the API

Input : The function takes one input at a time IP Address/DNS Names can be passed from Artifact value
Output : returns the json object by the label 'results', which hold 3 type of the information.
        1. status -- (if object found in TOR Network it will be 'success' or else 'failed')
        2. value  -- (a Boolean value '1' for success and '0' for failures)
        3. data   -- (a complete json data object from the result)
        

    resilient-circuits codegen -p fn_query_tor_network [-f fn_tor] [-w ]




To install in "development mode"

    pip install -e ./fn_query_tor_network/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_query_tor_network


To package for distribution,

    python ./fn_query_tor_network/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
