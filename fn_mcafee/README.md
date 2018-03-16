# McAfee TIE Threat Searcher

This function uses the Python OpenDXL TIE Client to communicate with your TIE server, which is located at 
[GitHit: opendxl-tie-client-python](https://github.com/opendxl/opendxl-tie-client-python).

### Prerequisites
* System must have an OpenSSL version used by Python that supports TLSv1.2 (Version 1.0.1 or greater)
* ePO-managed environments must have 4.0 (or newer) version of DXL ePO extension installed

To install in "development mode"

    pip install -e ./fn_mcafee/

To package for distribution,

    python ./fn_mcafee/setup.py sdist
    
The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

To uninstall,

    pip uninstall fn_mcafee

Once installed the client must be provisioned. Click [here](https://opendxl.github.io/opendxl-client-python/pydoc/provisioningoverview.html) for more info on provisioning

Run with: `resilient-circuits run`


