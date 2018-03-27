
This is the ioc parser,a Resilient Function created to run with resilient as part of a workflow.
It uses the ioc_parser found here:
https://github.com/armbues/ioc_parser

Which extract iocs from documents such as those found here:
https://github.com/kbandla/APTnotes

Dependencies:
resilient-circuits
ioc_parser
    pdfminer


Example of preprocess script:
inputs.artifactId=artifact.id
inputs.incidentId=incident.id

To install in "development mode"

    pip install -e ./fn_ioc_parser/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_ioc_parser


To package for distribution,

    python ./fn_ioc_parser/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
