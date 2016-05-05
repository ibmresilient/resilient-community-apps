# Action handler for elevating (one way) case to another org
This action handler will take incident fields from one org and replicate them in a new incident in another org.  This is a one way replication, from the source to the destination.

## Execution
```
python syncaction.py
```

## Configuration
The configuration is contained within *app.config*, to change which configuration file is loaded specify in the *APP_CONFIG_FILE* environment variable the full path to the filename e.g
```
export APP_CONFIG_FILE=/home/user/configuration.file
```

The configuration file is broken into sections as follows
### resilient
Connection information to the source org (used by the resilient_circuits module to connect to the source)
+ host = the hostname of the resilient server
+ port = 443 (always port 443)
+ email = Resilient user login (be sure that this user is not a SAML or Two Factor user, it also needs to have MasterAdministrator privileges in order to map enumerated field values)
+ password = the password for the resilient user
+ org = the name of the resilient org that will be the source of the record
+ stomp_port = 65001 (always 65001) Port for connecting to the Queue for the action module
+ logdir= fully qualified or relative path to the directory for the log file (app.log)
+ cafile= path to the file for the certificate for verification (used if a self signed certificate is used, or if the CA is not in your systems accepted CA list)

### resdestination
This is the connection information for the destination org.
+ host = hostname of the destination
+ port = 443
+ email = login for the org (must be MasterAdministrator and must not be SAML or Two Factor)
+ password = password for the user
+ org = destination org name
+ cafile = certificate for the resilient system if selfsigned or a CA that is not in the systems accepted CA list.

### syncauto
The destination queue for the action.  
+ queue= queue name configured in resilient

### syncconfig
Configuration information for the action.  
+ mapfile=Full path name to the field mapping configuration file.

## Field mapping configuration
To make this as generic as possbile a mapping of the configuraiton information from the source to the destination is contained in a configuration file located by the config section *syncconfig* -> *mapfile* directive.  The configuration file is shown below.  For each field, a json structure with the specified fields is required in order to map.  In addition a crosslink field needs to be specified such that the source and destination orgs can track between each other.  This can be a hidden field, but must be of type *number* 
```
{
    "fields":[
        {
            "sourceloc":"location of source field incident,action... "
            ,"sourcetype":"type of field enum, bool,string,text it is expected that the destination field type is the same"
            ,"sourcefield":"source field api name."
            ,"sourcecustom":"true if the source field is a custom field  false or missing otherwise"
            ,"destloc":"location in dest incident,task etc"
            ,"destcustom":"true if the destination field is custom"
            ,"destfield":"field in destination"
        }
    ],
    "crosslink":{
        "sourcefield":"source cross link field name - destination incident id"
        ,"destfield":"destination cross link field name -source incident id"
    }
}
```

## Resilient Configuration
By default, the action that is handled is called *stubfunction*.  Create a action queue destination with the queue name specified in the *syncauto* section of the configuration file. Create an action called *stubfunction* as a manual action, and add any action fields which you wish to be presented to the user.  Fields which are mapped from the action to the destination must be required *Always* to ensure that the action executes properly.