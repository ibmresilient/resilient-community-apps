## Threatminer Integrations ##

To install in "development mode"

    pip install -e ./fn_threatminer/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_threatminer


To package for distribution,

    python ./fn_threatminer/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
