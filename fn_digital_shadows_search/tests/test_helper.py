# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
def get_mocked_config():
  return """[fn_digital_shadows_search]
ds_api_key=DFGHJ7564765476457
ds_api_secret=KHGHJ676575
ds_base_url=https://portal-digitalshadows.com"""

def get_mocked_data():
  return [{
        "type": "WEBROOT_IP",
        "entity": {
          "reputationScore": 87,
          "ipReputationHistory": [{
            "timestamp": "2017-11-17T01:10:02.000Z",
            "reputation": 86
          }, {
            "timestamp": "2017-11-11T18:59:00.000Z",
            "reputation": 80
          }, {
            "timestamp": "2017-11-10T18:59:00.000Z",
            "reputation": 5
          }],
          "currentlyClassifiedAsThreat": False,
          "ipGeoInfo": {
            "city": "sample string",
            "country": "sample string",
            "region": "",
            "longitude": "sample string",
            "sld": "sample string",
            "state": "sample string",
            "carrier": "sample string",
            "tld": "sample string",
            "latitude": "sample string",
            "organization": "sample string",
            "asn": "sample string"
          },
          "threatCategories": [],
          "ipIncidentHistory": [{
            "scanDetails": [],
            "durationSeconds": 0,
            "threatType": "Mobile Threats",
            "numOfConnectedLowRepApps": 2,
            "eventDescription": "IP is associated with a malicious mobile app",
            "eventType": "Malicious Mobile Activity",
            "numberOfAttempts": 0,
            "observed": "2017-11-07T01:15:11.000Z",
            "applications": [{
              "category": "Adware",
              "description": "Downloads more apps and adware",
              "appName": "sample string",
              "requestedPermissions": ["sample string", "sample string"],
              "packageName": "sample string",
              "md5Hash": "sample string",
              "reputationCategory": "Malicious",
              "firstSeen": "2017-06-10T10:37:42.000Z"
            }],
            "attackDetails": [],
            "hostingPhishUrls": [],
            "startDateTime": "2017-11-07T00:44:12.000Z",
            "classifiedAsThreat": True
          }],
          "updatedDateTime": "2017-11-17T01:10:02.000Z",
          "ipThreatHistory": [{
            "timestamp": "2017-11-11T04:52:39.000Z",
            "classifiedAsThreat": False
          }, {
            "threatTypes": ["phishing", "proxy"],
            "timestamp": "2017-11-10T19:00:13.000Z",
            "classifiedAsThreat": True
          }, {
            "threatTypes": ["phishing", "proxy", "mobile threats"],
            "timestamp": "2017-11-03T01:35:11.000Z",
            "classifiedAsThreat": True
          }],
          "ipAddress": "192.168.0.1",
          "asn": 16509
        }
      }]