# Example Resilient Circuits Components

These examples are generally delivered as a single module containing a Resilient Circuits 
component as opposed to an installable package.  You will need to configure your resilient-circuits 
application to load them.  

In the "[resilient]" section of your app.config file, set a value for componentsdir to be the 
absolute path of a directory on your system.  Copy the example python modules you wish to load
into it.  Nothing else should be in this directory.  

```
[resilient]
email=user@example.com
host=myresilient
componentsdir=/full/path/to/components
...
```
When you do `resilient-circuits run`, the components from the modules in that directory will be 
automatically loaded.

