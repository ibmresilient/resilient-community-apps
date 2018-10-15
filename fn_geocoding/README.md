This package is an implementation of Google's Geocoding API set. 
Two function types are implemented: address and latlng. 
For an address, return coordinate information. 
For coordinates, return an address.

See https://developers.google.com/maps/documentation/geocoding/start

To install in "development mode"

    pip install -e ./fn_geocoding/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_geocoding


To package for distribution,

    python ./fn_geocoding/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
    
Edit the app.config file to supply the api_key. 
