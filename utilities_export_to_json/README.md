# Resilient Utility Export to Json

This Resilient Utility provides the console commands "resilient-export-to-json" and "resilient-merge-incident-json". 

The "resilient-export-to-json" command takes in a filename which specifies what file to export to and exports incident data from Resilient into that file in JSON format. The command also features optional arguments allowing to limit what incidents are exported, ranging from specifying a last modified field name (allowing export for only modified incidents) to exporting incidents created after or before a date. When exporting, "resilient-export-to-json" overwrites the specified file.

When using the "last_modified_field_name" argument, which allows for incidents that were modified to be exported, the "resilient-export-to-json" command creates a hidden file called ".resilient_export_to_json_lastrun". When the command is run, the code finds the highest last modified time in all of the incidents, and exports it as a string to this temporary file. The next time the command is run, the "resilient-export-to-json" command reads in the file, and only exports incidents that are after this last modified time, allowing for the exportation of only modified incidents.

The "resilient-merge-incident-json" command allows for two JSON files, containing incident data exported by "resilient-export-to-json" to be merged together. The command takes in the first filename, second filename, and an output filename which is where merged data is exported to.

## Package Dependences
- resilient_circuits version 30 or later
- Python version 2.7.10 or later;
- Python requests

## Installation
1) Install utilities_export_to_json in "development mode":
    ```
	$ pip install -e  ./utilities_export_to_json
    ```
   or the distribution file can be installed using:
   
    ```
	$ pip install utilities_export_to_json-<version>.tar.gz
	```

## Uninstall
To uninstall this utility:

	$ pip uninstall utilities_export_to_json
  
