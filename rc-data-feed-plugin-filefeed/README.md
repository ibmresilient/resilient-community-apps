# Introduction
This package contains the FileFeed Plugin to the Data Feed extension.  This Data Feed extension allows one to maintain "replica" data for Resilient incidents, artifacts, tasks, notes, etc.  The updates are performed in near real-time.

This plugin allows this replica data to be maintained in a file system, one file per incident, artifact, note, task, etc.

Refer to the documentation on the Data Feed extension for uses cases support and configuration options. Also refer to the other Data Feed plugins which can be used in combination.

  
# License

Unless otherwise specified, contents of this repository are published under the MIT open-source
[LICENSE](LICENSE).

# Installation
  The integration package contains Python components that are called by the Resilient platform. These components run in the Resilient Circuits integration framework. The package also includes Resilient customizations that will be imported into the platform later.
  You perform these installation procedures at the Resilient integration server.
  
## Install the Python components
  Complete the following steps to install the Python components:
* Ensure that the environment is up-to-date, as follows:
```
  sudo pip install --upgrade pip
  sudo pip install --upgrade setuptools
  sudo pip install --upgrade resilient-circuits
```  
*	Run the following commands to install the package:
```
  unzip rc_data_feed-plugin-filefeed-<version>.zip
  [sudo] pip install --upgrade rc_data_feed-plugin-filefeed-<version>.tar.gz
```  
*	Configure Resilient-circuits

  The Resilient Circuits process runs as an unprivileged user, typically named integration. If you do not already have an integration user configured on your appliance, create it now. 
  Complete the following steps to configure and run the integration:
*	Using sudo, switch to the integration user, as follows:

`  sudo su - integration`
*	Use one of the following commands to create or update the resilient-circuits configuration file. Use –c for new environments or –u for existing environments.
```
  resilient-circuits config -c
  or
  resilient-circuits config –u [-l rc-data-feed-plugin-filefeed]
```
*	Edit the resilient-circuits configuration file, as follows:
    
     - In the [resilient] section, ensure that you provide all the information required to connect to the Resilient platform.
     - In the [feed_feed] section, configure the settings for your file storage environment.
     - In the [feeds] section, define the feed(s) you intend to use and create separate sections for each feed. For example:
```
  [feeds]
  feed_names=feed_feed
  reload=True
  # feed_data is the default queue that will be listened to
  queue=feed_data
  
  [file_feed]
  class=FileFeed
  directory=/path/to/feed_directory
```

# FileFeed
The FileFeed class allows you to write all the incoming data to a directory on your file system (one file per object).  
The structure of the file names is either:

    incident_{inc_id}.json (for incident objects)
or (for all other types of objects):

    incident_{inc_id}_{type}_{obj_id}.json 
    
In this context, "type" can be:

* task
* artifact
* milestone
* note
* data table programmatic name
    
The following configuration items are supported:

| Key | Values | Description |
| :-- | :----- | :---------- |
| class | FileFeed | Indicates that the section is for a FileFeed.
| directory | Path for a directory on local system (required)	| Location where the files are to be written. |
