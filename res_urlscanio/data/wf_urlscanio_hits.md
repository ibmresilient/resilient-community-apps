<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# URLScan.io Hits

## Function - Scan with urlscan.io

### API Name
`urlscanio`

### Output Name
`urlscanio`

### Message Destination
`urlscanio`

### Pre-Processing Script
```python
# This is an artifact workflow; 
# The URL to scan is the artifact value
inputs.urlscanio_url = artifact.value

# Set the incident id
inputs.incident_id = incident.id
```

### Post-Processing Script
```python
def verify_for_scan_failed_flag(result_content):
      """ Verify if scan failed """

      result_data = result_content.get('data', None)
      if not result_data:
          return True

      result_data_requests_list = result_data.get('requests', None)
      if not result_data_requests_list:
          return True

      # get first element from the list
      requests_first_el = result_data_requests_list[0]
      if not requests_first_el:
          return True

      response = requests_first_el.get('response', None)
      if not response or 'failed' in response:
          return True

      return False

def prepare_city_country(*argv):
        """
        Prepare a list of non None value or blank "Falsy" parameters.
        :param *argv - city, country
        :return: list
        """
        city_country_list = [el for el in argv if el]
        return city_country_list

if results.png_url is not None:
  result_content = results.report

  stats = result_content.get('stats', None)
  if stats:
      verdicts = result_content.get('verdicts', None)
      urlscan = verdicts.get('urlscan', None)
      malicious_flag = urlscan.get('malicious', None)

      if malicious_flag == 1:

          # Some malicious scans show as failed, do not include those
          if not verify_for_scan_failed_flag(result_content):
            task = result_content.get('task', None)
            page = result_content.get('page', None)
  
            png_url = task.get('screenshotURL', None) if task else None
            scan_time = task.get('time', None) if task else None
            report_url = task.get('reportURL', None) if task else None
            uniq_countries_int = stats.get('uniqCountries', None)
            city_country_list = prepare_city_country(page.get('city', None),
                                                          page.get('country', None)) if page else None
            city_country = ",".join(city_country_list) if city_country_list else None
            server = page.get('server', None) if page else None
            asn = page.get('asnname', None) if page else None
            
            hit = [
                {
                  "name": "Time Last Scanner",
                  "type": "string",
                  "value": "{}".format(scan_time)
                }, 
                {
                  "name": "Number of Countries",
                  "type": "number",
                  "value": "{}".format(uniq_countries_int)
                }, 
                {
                  "name": "City and Country",
                  "type": "string",
                  "value": "{}".format(city_country)
                },
                {
                  "name": "Server",
                  "type": "string",
                  "value": "{}".format(server)
                },
                {
                  "name": "ASN Name",
                  "type": "string",
                  "value": "{}".format(asn)
                },
                {
                  "name": "Report Link",
                  "type": "uri",
                  "value": "{}".format(report_url)
                },
                {
                  "name": "Screenshot Link",
                  "type": "uri",
                  "value": "{}".format(png_url)
                }
                ]
            artifact.addHit("URLScan.io Function hits added", hit)
else:
  LOG.info("No Result information found on URL: {0}".format(result_url))


```

---

