<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Example: CVE Search

## Function - CVE Search

### API Name
`function_cve_search`

### Output Name
``

### Message Destination
`fn_cve`

### Pre-Processing Script
```python
inputs.cve_id = rule.properties.cve_id
inputs.cve_vendor = rule.properties.cve_vendor
inputs.cve_product = rule.properties.cve_product
inputs.cve_published_or_updated_after_date = rule.properties.cve_published_or_updated_after_date
```

### Post-Processing Script
```python
from datetime import datetime

output_data = results.get('content')
api_call_type_text = f"<p><b> {results.get('api_call')} :</b> {rule.properties.cve_id} </p>"

#Adding data to table
ref_link_text = ""
if output_data:
  for cve in output_data.get("fkie_nvd", []):
    table_row_object = incident.addRow("cve_data")
    cve_data = cve[1]
    table_row_object["cve_id"] = cve_data.get("id", None)
    if cve_data.get("published", ""):
      table_row_object["published_date"] = int(datetime.strptime(cve_data.get("published", "")[:19], "%Y-%m-%dT%H:%M:%S").timestamp()*1000)
    desc = cve_data.get("descriptions", [])[0]
    table_row_object["summary"] = desc.get("value", None)
    for ref_url in cve_data.get("references", []):
      ref_link_text += '<p><a href="{0}">{0}</a></p>'.format(ref_url.get("url", None))
    table_row_object["references"] = ref_link_text
else:
  incident.addNote("No data returned from CVE Search\n\nCVE-ID: {}\nVendor: {}\nProduct: {}".format(rule.properties.cve_id, rule.properties.cve_vendor, rule.properties.cve_product))
```

---

