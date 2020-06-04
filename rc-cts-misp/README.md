# MISP Threat Searcher

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
### v1.1.1
* Fix backward compatibility issues.

## Overview
This implements a custom threat service for the [MISP](http://www.misp-project.org/) Threat Intelligence Platform.

## Installation
Install this package with 'pip', or `python setup.py install`.

Update your `app.config` file with parameters for the MISP connection.
To update the configuration file with default parameters:
```
    resilient-circuits config -u
```
Note: For the `misp_url` parameter in the app.config file, the https protocol should be specified.

To run the service:
```
resilient-circuits run
```

Register the custom threat service onto your Resilient server (assuming that the
`resilient-circuits` application is running on the same server, and that the webserver
is listening on port 9000):

```
    sudo resutil threatserviceedit -name MISP -resturl http://127.0.0.1:9000/cts/misp
```

To test the connection:

```
sudo resutil threatservicetest -name MISP
```
## Uninstall
To delete:

```
sudo resutil threatservicedel -name MISP
```
## Supported artifact types 
Map of supported Threat Service artifact types to Misp types:

  | Resilient artifact types | Misp types |
  | ------ | ----------- |
  | file.content | None |
  | file.name | ["filename", "email-attachment", "filename&#124;md5", "filename&#124;sha1", "filename&#124;sha256", "filename&#124;authentihash", "filename&#124;ssdeep", "filename&#124;imphash", "filename&#124;pehash", "filename&#124;sha224", "filename&#124;sha384", "filename&#124;sha512", "filename&#124;sha512/224", "filename&#124;sha512/256"]|
  | file.path | "other" |
  | email.body | "text" |
  | email.header | ["email-src", "email-dst", "target-email", "whois-registrant-email", "dns-soa-email", "email-reply-to", "email-subject", "email-header", "email-x-mailer", "email-message-id", "email-mime-boundary"] |
  | email.header.sender_address | ["email-src", "email-dst", "target-email", "whois-registrant-email", "dns-soa-email", "email-reply-to"] |
  | email.header.sender_name | None |
  | email.header.to | ["email-src", "email-dst", "target-email", "whois-registrant-email", "dns-soa-email", "email-reply-to"] |
  | hash.md5 | ["md5", "authentihash", "filename&#124;md5"] |
  | hash.sha1 | ["sha1", "x509-fingerprint-sha1", "filename&#124;sha1"] |
  | hash.fuzzy | ["other"] |
  | hash.sha256 | ["sha256", "sha512/256", "filename&#124;sha256"] |
  | cert.x509 | ["other"] |
  | net.cidr | ["ip-src", "ip-dst"] |
  | net.ip | ["ip-src", "ip-dst", "ip-dst&#124;port", "ip-src&#124;port", "domain&#124;ip"] |
  | net.name | ["hostname", "domain", "domain&#124;ip"] |
  | net.mac | ["other"] |
  | net.port | ["port"] |
  | net.uri | ["url", "uri", "link"] |
  | net.uri.path | ["uri"] |
  | net.http.request.header | ["http-method", "user-agent"] |
  | net.http.response.header | None |
  | process.name | ["other"] |
  | system.name | ["target-machine"] |
  | system.mutex | ["mutex"] |
  | system.registry | ["regkey"] |
  | system.service.name | ["windows-service-name", "windows-service-displayname"] |
  | system.user.name | ["text", "target-user", "github-username"] |
  | system.user.password | ["other"] |
  | threat.report.cve | ["vulnerability"] |
  | threat.malware.family | ["malware-type"] |
