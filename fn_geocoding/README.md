This package is an implementation of Google's Geocoding API set. 
Two function types are implemented: address and latlng. 
For an address, return coordinate information. 
For coordinates, return an address.

See https://developers.google.com/maps/documentation/geocoding/start

This package contains:

Functions:
- geocoding
     
Workflows:
- Example: Geocoding Get Address
- Example: Geocoding Get Coordinates
     
Rules:
- Example: Geocoding Get Address
- Example: Geocoding Get Coordinates
=======
Components

   Message Destinations:
     fn_geocoding
   Functions:
     geocoding
   Workflows:
     example_geocoding_get_address
     example_geocoding_get_coordinates
   Rules:
     Example: Geocode Get Address
     Example: Geocoding Get Coordinates

To install in "development mode"

    pip install fn_geocoding-<version>.tar.gz

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_geocoding


To package for distribution,

    python ./fn_geocoding/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
    
Edit the app.config file to supply the api_key. 
