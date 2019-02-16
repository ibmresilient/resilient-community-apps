mkdir cov
py.test --cov=../fn_mitre_integration/lib --cov-report html:./cov ../tests

