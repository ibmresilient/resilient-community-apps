

# Validation Report for Symantec DLP

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2730 | 2022/03/08 08:23:41 | `cmd`: validate, `package`: fn_symantec_dlp |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Symantec DLP |
| `name` | fn_symantec_dlp |
| `version` | 2.0.0 |
| `author` | IBM QRadar SOAR |
| `install_requires` | ['resilient_circuits>=43.0.0', 'jinja2'] |
| `description` | IBM QRadar SOAR app for Symantec DLP |
| `long_description` | This app allows bi-directional synchronization between IBM SOAR and Symantec DLP.    Symantec DLP incident are escalated to IBM SOAR as cases with the creation of artifacts and notes in SOAR from the incident. |
| `url` | https://ibm.com/mysupport |
| `entry_points` | {'resilient.circuits.configsection': '/Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp/fn_symantec_dlp/util/config.py',<br> 'resilient.circuits.customize': '/Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp/fn_symantec_dlp/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp/fn_symantec_dlp/util/selftest.py'} |
| `SOAR version` | 42.0.7058 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

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


### `app_logo.png`
<span style="color:teal">INFO</span>: `app_logo.png` is the default icon. Consider using your own logo

Icons appear in SOAR when your app is installed with App Host


### `company_logo.png`
<span style="color:teal">INFO</span>: `company_logo.png` is the default icon. Consider using your own logo

Icons appear in SOAR when your app is installed with App Host


### LICENSE
<span style="color:teal">INFO</span>: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD


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


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/symantec_dlp_upload_binaries`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `symantec_dlp_upload_binaries` empty

Fill in values manually or by using ```resilient-sdk codegen -p /Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp --gather-results```


### `payload_samples/symantec_dlp_get_incident_details`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_send_note_to_dlp_incident`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_update_incident_status`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest
<span style="color:red">CRITICAL</span>: While running selftest.py, `resilient-circuits` failed to connect to server. Details:

	...
	2022-03-08 08:23:17,705 DEBUG [debugger] <Event[*] (`exception`, `Actions`, `User admin@example.com is not authorized to read from queue://actions.201.fn_symantec_dlp`, b`java.lang.SecurityException: User admin@example.com is not authorized to read from queue://actions.201.fn_symantec_dlp\n\tat com.co3.embeddedbroker.activemq.ActiveMQBrokerFilter.newSecurityException(ActiveMQBrokerFilter.java:74)\n\tat com.co3.embeddedbroker.activemq.ActiveMQBrokerFilter.addConsumer(ActiveMQBrokerFilter.java:263)\n\tat org.apache.activemq.broker.BrokerFilter.addConsumer(BrokerFilter.java:104)\n\tat org.apache.activemq.broker.TransportConnection.processAddConsumer(TransportConnection.java:703)\n\tat org.apache.activemq.command.ConsumerInfo.visit(ConsumerInfo.java:352)\n\tat org.apache.activemq.broker.TransportConnection.service(TransportConnection.java:336)\n\tat org.apache.activemq.broker.TransportConnection$1.onCommand(TransportConnection.java:200)\n\tat org.apache.activemq.transport.MutexTransport.onCommand(MutexTransport.java:45)\n\tat org.apache.activemq.transport.AbstractInactivityMonitor.onCommand(AbstractInactivityMonitor.java:301)\n\tat org.apache.activemq.transport.stomp.StompTransportFilter.sendToActiveMQ(StompTransportFilter.java:97)\n\tat org.apache.activemq.transport.stomp.ProtocolConverter.sendToActiveMQ(ProtocolConverter.java:179)\n\tat org.apache.activemq.transport.stomp.ProtocolConverter.onStompSubscribe(ProtocolConverter.java:671)\n\tat org.apache.activemq.transport.stomp.ProtocolConverter.onStompCommand(ProtocolConverter.java:249)\n\tat org.apache.activemq.transport.stomp.StompTransportFilter.onCommand(StompTransportFilter.java:85)\n\tat org.apache.activemq.transport.TransportSupport.doConsume(TransportSupport.java:83)\n\tat org.apache.activemq.transport.tcp.SslTransport.doConsume(SslTransport.java:171)\n\tat org.apache.activemq.transport.stomp.StompSslTransportFactory$1$1.doConsume(StompSslTransportFactory.java:73)\n\tat org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:233)\n\tat org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)\n\tat java.lang.Thread.run(Thread.java:825)\n` )>
	2022-03-08 08:23:17,705 DEBUG [debugger] <OnStompError_success[stomp] (<OnStompError[stomp] ()>, None )>
	2022-03-08 08:23:18,399 DEBUG [debugger] <SelftestTerminateEvent[*] ( )>
	2022-03-08 08:23:18,401 INFO [actions_component] SelftestTerminateEvent, exiting resilient-circuits
	
	ERROR: could not connect to SOAR at `deployed1.fyre.ibm.com`.
	Reason: `admin@example.com` is not authorized to read from the App`s Message Destination
	Error Code: 32




---
 

## tox tests
<span style="color:teal">INFO</span>: 1 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 