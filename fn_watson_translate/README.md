This function integrates Watson Translator with the Resilient platform to provide translation services.
The Watson Translation service supports multiple languages, uses Neural Networks for processing and allows building custom models.
The Watson Translate function accepts text to be translated, targets language and optionally source language (in its absence Watson will attempt to identify the language) and returns translated text and its confidence percentage.

Find out more at: https://www.ibm.com/watson/services/language-translator/ 

To install in "development mode"

    pip install -e ./fn_watson_translate/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_watson_translate


To package for distribution,

    python ./fn_watson_translate/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
