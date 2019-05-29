##Escalating Resilient incident to ICD

=======

*This integration contains one 1 function, workflow, rule and custom field (qradar_severity)*

This community app allows for the escalation of a incident from resilient to the icd desk, via a manual rule on each incident. A word document is attached which explains the mapping of resilient fields to the icd ticket fields. If the qradar severity is not set, a default INTERNAL PRIORITY on icd desk (4) will be set. Users can specify the number of IP Sources or Destination Artifacts to be added via keyboard prompt when running the integration. 


To install in "development mode"

    pip install -e ./fn_res_to_icd/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_res_to_icd


To package for distribution,

    python ./fn_res_to_icd/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
