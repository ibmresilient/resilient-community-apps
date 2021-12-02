

# Validation Report for SentinelOne

| SDK Version       | Generation Time          |
| :---------------- | ------------------------ |
| 43.1.2490 | 2021/12/02 13:22:57 |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | SentinelOne |
| `name` | fn_sentinelone |
| `version` | 1.0.0 |
| `author` | IBM Resilient |
| `install_requires` | ['resilient-circuits>=37.0.0', 'resilient-lib', 'jinja2', 'simplejson'] |
| `description` | IBM Security SOAR app for SentinelOne |
| `long_description` | Escalate SentinelOne Threats into IBM Security SOAR as an incident/case.' |
| `url` | https://github.com/ibmresilient/fn_sentinelone |
| `entry_points` | {'resilient.circuits.configsection': '/Users/annmarienorcross/resilient-community-apps/fn_sentinelone/fn_sentinelone/util/config.py',<br> 'resilient.circuits.customize': '/Users/annmarienorcross/resilient-community-apps/fn_sentinelone/fn_sentinelone/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/annmarienorcross/resilient-community-apps/fn_sentinelone/fn_sentinelone/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 40.0.6554 |
| `Proxy support` | Proxies not fully supported unless running on AppHost>=1.6 and resilient-circuits>=42.0.0 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### `README.md`
<span style="color:red">CRITICAL</span>: `README.md` still has at least one instance of `<!-- ::CHANGE_ME:: -->`

Edit the README and make sure to remove all `<!-- ::CHANGE_ME:: -->` comments


### `README.md`
<span style="color:red">CRITICAL</span>: `README.md` still has at least one `TODO`

Make sure to complete the README for your app


### `README.md`
<span style="color:red">CRITICAL</span>: Cannot find the following screenshot(s) referenced in the README: [`./doc/screenshots/custom_layouts.png`, `./doc/screenshots/fn-sentinelone-shutdown-agent.png`, `./doc/screenshots/fn-sentinelone-get-agents.png`, `./doc/screenshots/fn-sentinelone-abort-disk-scan.png`, `./doc/screenshots/fn-sentinelone-connect-to-network.png`, `./doc/screenshots/fn-sentinelone-update-threat-status.png`, `./doc/screenshots/fn-sentinelone-download-from-cloud.png`, `./doc/screenshots/fn-sentinelone-disconnect-from-network.png`, `./doc/screenshots/fn-sentinelone-send-soar-note-to-sentinelone.png`, `./doc/screenshots/fn-sentinelone-get-agent-details.png`, `./doc/screenshots/fn-sentinelone-get-hash-reputation.png`, `./doc/screenshots/fn-sentinelone-get-threat-details.png`, `./doc/screenshots/fn-sentinelone-initiate-disk-scan.png`, `./doc/screenshots/fn-sentinelone-update-notes-from-sentinelone.png`, `./doc/screenshots/fn-sentinelone-update-threat-analyst-verdict.png`, `./doc/screenshots/dt-sentinelone-agent.png`]

Make sure all screenshots referenced in the README are placed in the /doc/screenshots folder


### `MANIFEST.in`
<span style="color:green">Pass</span>


### `apikey_permissions.txt`
<span style="color:green">Pass</span>


### `Dockerfile`
<span style="color:green">Pass</span>


### `entrypoint.sh`
<span style="color:green">Pass</span>


### ``config.py``
<span style="color:green">Pass</span>


### ``customize.py``
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: `tox` is not installed in your Python environment

(OPTIONAL) If you want to verify any tests you have written, install `tox` by running ```pip install -U tox```



---
 