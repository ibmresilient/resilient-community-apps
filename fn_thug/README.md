# Thug Function

This IBM Resilient Function package can be used to analyze a url for malicious content using thug. It uses a dockerized thug to run analysis in a deatched container then cleans up the output files and container after execution completes.

## To install in *development mode*:

    pip install -e ./fn_thug/

After installation, the package will be loaded by `resilient-circuits run`.

## To uninstall:

    pip uninstall fn_thug

## To package for distribution:

    python ./fn_thug/setup.py sdist

## The resulting .tar.gz file can be installed using:

    pip install <filename>.tar.gz

## Add Thug configuration details to the config file:
    
    resilient-circuits config -u
    
Set the following values in the config file (`app.config`) under the `[fn_thug]` section:

```
thug_dir=Absolute path to a directory that can be mounted into a docker container. Go to Docker -> Preferences -> File Sharing to configure.
```

## How to use the function

1. Import the necessary customization data into the Resilient platform:
                
        resilient-circuits customize
                
    This creates the following customization components:
    * Function inputs: 
        *   `thug_args`
        *   `thug_url`
    * Message Destination: `fn_thug`
    * Function: `thug_analysis`
    * Workflow: `Example of Thug Analysis`
    * Rule: `Thug Analysis`
          
2. Update and edit `app.config`:
                
        resilient-circuits config -u
                
3. Start Resilient Circuits:

        resilient-circuits run

4. Trigger the rule

## Aditional Notes

To use this function, docker must be installed on the machine that is running resilient-circuits.
