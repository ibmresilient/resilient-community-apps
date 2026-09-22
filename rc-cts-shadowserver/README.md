ShadowServer Threat Service
=============

This CTS queries ShadowServer (http://bin-test.shadowserver.org/) and updates Resilient with information about a hash artifact.

## Installation
1. Unzip rc-cts-shadow-server-x.x.x.tar.gz.zip
2. Install this package with `pip`.
3. Use the following commands to register this custom threat service with Resilient and test it:
```
sudo resutil threatserviceedit -name "Shadow Server" -resturl <resilient_circuits_url>/cts/shadow_server_threat_feed
```

To test the connection:

```
sudo resutil threatservicetest -name "Shadow Server"
```

4. Run `resilient-circuits config -u` to install the app.config settings and then edit the `[shadow_server_cts]` section with your configuration information.
5. Run with: `resilient-circuits run`.
