# Resilient example email message parsing script
** This package consists of a .res Resilient configuration file which contains an example email parsing script, a rule to run it automatically, and an associated incident field.

## Installation instructions
1. Log on to the Resilient user interface using an account with &&&& permissions.
1. Navigate 
1. Click on 
1. Select the .res file
1. Select "OK"

## Result
After installing, the Resilient system now has a new Python script called "" and a new rule called "". The rule triggers when a new email message is received by Resilient and runs the script. The script is intended to 
perform generic email parsing on newly created email message objects. It:
* Creates a new incident whose title is a combination of the email subject and the mailbox it was received on
* It adds the email message's subject as an artifact to the new incident
* It sets the incident's reporter field to be the email address that sent the message
* Parses the email body text looking for URLs, IP addresses and file hashes. After filtering out invalid and whitelisted values, it adds the remaining data to the incident as artifacts.

## Configuration
### The incident owner
New incidents need an owner, either an individual identified by their email address. In the provided script every incident is owned by the user `admin@co3sys.com`. This should be changed to reflect your system. To change the owner to `l1@businessname.com`, editing line 485 of the script:

```python
# The new incident owner
newIncidentOwner = "admin@co3sys.com"
```
should become
```python
# The new incident owner
newIncidentOwner = "l1@businessname.com"
```

### Whitelisting
There are two categories of whitelist - IP address and URL domain - which are configured by altering data in the script.

| Variable Name | Line number | Purpose |
| ------------- | :--: | :-------:| 
| `ipV4WhiteList` | 214 | General IP v4 whitelist |
| `ipV6WhiteList` | 232 | General IP v6 whitelist |
| `customIPv4WhiteList` | 257 | Additional customer-specific IP v4 whitelist |
| `customIPv6WhiteList` | 258 | Additional customer-specific IP v6 whitelist |
| `domainWhiteList` | 261 | General URL domain whitelist |
| `customDomainWhiteList` | 264 | Additional customer-specific URL domain whitelist |

#### IP address whitelists
The IP address whitelists are split into separate IPv4 and IPv6 lists. These lists apply to the IP addresses retrieved by pattern matching in the body of the email message. If an IP address appears on a whitelist then it will not be added as an artifact to the incident. There are "standard" whitelists which are expected to be the same for all customers, and also customer-specific whitelists which are used in addition to the standard lists. The customer-specific lists are kept separate so that there are four whitelist variables in the script.

Additions to the whitelist should be made to `customIPv4WhiteList` and `customIPv6WhiteList`.

There are two categories of IP whitelist entry - CIDR (Classless Inter-Domain Routing) and IPRange. For example, in IP V4, IBM owns the "9" class A network. The customer may want to also whitelist an IP range (e.g. `12.0.0.1` - `12.5.5.5`).  To add this criterion to the whitelist we would add `CIDR("9.0.0.0/8")` and `IPRange("12.0.0.1-12.5.5.5")` to customIPv4WhiteList. We may also want to whitelist an explicit IP address e.g. `13.13.13.13` would be specified by `CIDR("13.13.13.13")`. IP v6 whitelists operate similarly. For example to whitelist a V6 CIDR `aaaa::/16` we would add `CIDR("aaaa::/16")` to customIPv6WhiteList.

```python
  # Customer-specific IP address whitelists
  # Add entries to these lists to whitelist the entries without disrupting the standard set above
  customIPv4WhiteList = []
  customIPv6WhiteList = []
```
should become:
```python
  # Customer-specific IP address whitelists
  # Add entries to these lists to whitelist the entries without disrupting the standard set above
  customIPv4WhiteList = [CIDR("9.0.0.0/8"), IPRange("12.0.0.1-12.5.5.5"), CIDR("13.13.13.13")]
  customIPv6WhiteList = [CIDR("aaaa::/16")]
```

#### URL domain whitelists
The domain whitelist applies to URLs found in the body of the email. If a whitelisted domain is discovered in a potential URL artifact, then it is not added to the incident. Domains can be added explicitly (e.g. mail.businessname.com) or using a wildcard (e.g. *.otherbusinessname.com).

```python
  # Customer-specific domain whitelist
  customDomainWhiteList=[]
```
should become:
```python
  # Customer-specific domain whitelist
  customDomainWhiteList=[Domain("mail.businessname.com"), Domain("*.otherbusinessname.com")]
```