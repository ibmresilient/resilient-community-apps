This function converts HTML data into a base64 encoded PDF documnent. 
Alternatively, converts the contents of a website URL into a base64 encoded document.

This function can be used in sequence with other functions, such as `fn_utilities:json2html` and `fn_utilities:base64 to attachment`. See Resilient workflows functions and the use of output workflow properties.

==

To install in "development mode"

    pip install -e ./fn_html2pdf/

To import into Resilient, run:

	resilient-circuits customize -l fn_html2pdf

After installation, the function will be available by running 

	resilient-circuits run


To uninstall,

    pip uninstall fn_html2pdf


To package for distribution,

    python ./fn_html2pdf/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
