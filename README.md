![IBM Security](https://raw.githubusercontent.com/ibmresilient/resilient-python-api/master/resilient-sdk/assets/IBM_Security_lockup_pos_RGB.png)

# IBM SOAR Community Applications 

This repository contains the source-code for packaged IBM SOAR Apps.

Many of these apps are available for download from [IBM Security App Exchange](https://exchange.xforce.ibmcloud.com/hub/?br=Resilient).
This source code repository may include unpublished versions, and additional integrations that are not published to App
Exchange, but you will need to build and install them yourself.


### Developing New Integrations

Developing new integrations is straightforward using the IBM SOAR SDK.  A good introduction can be found on the
[IBM SOAR App Developer Guide](https://ibm.biz/soar-docs).

For questions and discussion, head over to the [IBM SOAR Community](http://ibm.biz/resilientcommunity) where you'll
find blogs, technotes, discussion forums and other useful resources.



### Setup

Refer to each directory for any pre-requisites and specific install instructions.

Each application has a `setup.py` installer.  You can install in two ways:

#### Installing in "developer mode"

To install a package in "developer mode", change to the directory that contains `setup.py` and install with:
```shell
pip install -e .
```

If you make any changes to the source files, they will apply next time the application is run.

#### Creating a Distribution

To create a distribution package,
```shell
resilient-sdk package -p .
```

See the [ibm.biz/soar-python-docs](https://ibm.biz/soar-python-docs) for more information on the `resilient-sdk` CLI.

Then in the `dist` subdirectory you will find a .tar.gz file that you can copy to another environment and
install using 'pip' (specifying the filename of the package that you built):

```shell
pip install app_name.tar.gz
```

If you make any changes to the source files, you'll need to rebuild and reinstall the distribution package.

### License

Unless otherwise specified, contents of this repository are published under the MIT open-source license.
[LICENSE](LICENSE)

Files and subdirectories within this repository may contain specific licenses that apply individually to that item.


### Contributing

Applications published to the [IBM Security App Exchange](https://exchange.xforce.ibmcloud.com/hub/?br=Resilient) have
support contact information displayed there.  If you have questions or issues with a published application,
you should start there.

Otherwise, please report issues using the [Issues](https://github.com/ibmresilient/resilient-community-apps/issues) tab on GitHub.

Contributions are welcome.  Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for more about the process.


# Open Source @ IBM

[Find more open source projects on the IBM Github Page](http://ibm.github.io/)
