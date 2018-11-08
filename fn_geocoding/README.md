###Google Geocoding Functions for Resilient

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

###Components

 Message Destinations:
   - fn_geocoding
   
 Functions:
   - geocoding
   
 Workflows:
   - example_geocoding_get_address
   - example_geocoding_get_coordinates
   
 Rules:
   - Example: Geocode Get Address
   - Example: Geocoding Get Coordinates

To install in "development mode"

    pip install fn_geocoding-<version>.tar.gz

To uninstall,

    pip uninstall fn_geocoding

To package for distribution,

    python ./fn_geocoding/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install fn_geocoding-<version>.tar.gz
    
###Requirements:
* resilient-circuits 

###Installation:
Run the following command to import this function into IBM Resilient

    resilient-circuits customize

To configure this function run and following command

    resilient-circuits config -u

Then edit the app.config file, providing the api_token for the 
[fn_geocoding] section necessary to communicate with the Google Geocoding API.

