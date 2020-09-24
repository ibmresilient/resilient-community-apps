###Google Geocoding Functions for Resilient

This package is an implementation of Google's Geocoding API set. 
Two function types are available: address and latlng. 

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

## Installation

### App Host
All the components for running this integration in a container already exist when using the App Host app.

To install,

* Navigate to Administrative Settings and then the Apps tab.
* Click the Install button and select the downloaded file: app-fn_geocoding-x.x.x.zip.
* Go to the Configuration tab and edit the app.config file, editing the API key for Google Geocoding.

  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **url** | Yes | `https://maps.googleapis.com/maps/api/geocode/json` | *URL for Google geocoding* |
  | **api_key** | Yes | `AIza...b483sj` | *your Google Geocoding API Key* |

### Integration Server
* Download the `app-fn_geocoding-x.x.x.zip` file.
* Copy the `.zip` file to your Integration Server and SSH into it.
* **Unzip** the package:
  ```
  $ unzip app-fn_geocoding-x.x.x.zip
  ```
* **Install** the package:
  ```
  $ pip install fn_geocoding-x.x.x.tar.gz
  ```
* Import the **configurations** into your app.config file:
  ```
  $ resilient-circuits config -u -l fn-geocoding
  ```
* Import the fn_geocoding **customizations** into the Resilient platform:
  ```
  $ resilient-circuits customize -y -l fn-geocoding
  ```
* Open the config file, scroll to the bottom and edit your fn_geocoding configurations:
  ```
  $ vi ~/.resilient/app.config
  ```
  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **url** | Yes | `https://maps.googleapis.com/maps/api/geocode/json` | *URL for Google geocoding* |
  | **api_key** | Yes | `AIza...b483sj` | *your Google geocoding API Key* |

* **Save** and **Close** the app.config file.
* [Optional]: Run selftest to test the Integration you configured:
  ```
  $ resilient-circuits selftest -l fn-geocoding
  ```
* **Run** resilient-circuits or restart the Service on Windows/Linux:
  ```
  $ resilient-circuits run
  ```
---

## Uninstall
* SSH into your Integration Server.
* **Uninstall** the package:
  ```
  $ pip uninstall fn-geocoding
  ```
* Open the config file, scroll to the [fn_geocoding] section and remove the section or prefix `#` to comment out the section.
* **Save** and **Close** the app.config file.

# History
| Version | Date | Notes |
| ------: | ---: | ----: |
| 1.0.2   | Sept. 2020 | App Host support |
| 1.0.1   | Nov. 2018 | Rule and workflow fixes | 
| 1.0.0   | Nov. 2018 | Initial Release |