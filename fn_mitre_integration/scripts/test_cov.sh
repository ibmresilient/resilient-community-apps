#
#   This is a script to run all the tests in the test folder,
#   collect code coverage data and save it into the cov folder
#

# Make a cov folder
mkdir cov
py.test --cov=../fn_mitre_integration/lib --cov-report html:./cov ../tests

#
#   The code coverage data can be viewed using
# firefox cov/index.html
