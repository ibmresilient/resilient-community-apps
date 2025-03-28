<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.0.974
-->

# ZIA: Get Blocklist

## Function - ZIA: Get Blocklist

### API Name
`funct_zia_get_blocklist`

### Output Name
`None`

### Message Destination
`zia`

### Pre-Processing Script
```python
##  ZIA - wf_zia_get_blocklist pre processing script ##
import re

URL_FILTER = rule.properties.zia_url_filter

def is_regex(regex_str):
    """"Test if sting is a correctly formed regular expression.

    :param regex_str: Regular expression string.
    :return: Boolean.
    """
    try:
        re.compile(regex_str)
        return True
    except (re.error, TypeError):
        return False


def main():
    # Test filter to ensure it is a valid regular expressions.
    if URL_FILTER and not is_regex(URL_FILTER):
        raise ValueError("The query filter '{}' is not a valid regular expression.".format(unicode(URL_FILTER)))

    inputs.zia_url_filter = rule.properties.zia_url_filter

if __name__ == "__main__":
    main()
```

### Post-Processing Script
```python
##  ZIA - wf_zia_get_blocklist post processing script ##

#  Globals
FN_NAME = "funct_zia_get_blocklist"
WF_NAME = "ZIA: Get Blocklist"
CONTENT = results.content
INPUTS = results.inputs
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]

# Processing
def main():
    note_text = u''
    url_filter = INPUTS.get("zia_url_filter")
    if CONTENT:
        if "error_code" not in CONTENT:
            blocklist_urls = CONTENT.blacklistUrls
            url_counts = CONTENT.url_counts
            note_text = u"ZIA Integration: Workflow <b>{0}</b>: There were <b>{1}</b> blocklist URLS(s) out of a total of "\
                        u"<b>{2}</b> using URL filter <b>{3}</b> returned for SOAR function <b>{4}</b>."\
            .format(WF_NAME, url_counts["filtered"], url_counts["total"], url_filter, FN_NAME)
            if blocklist_urls:
                if url_counts["filtered"] <= 50:
                    note_text += u"<br>The data table <b>{0}</b> has been updated".format("Zscaler Internet Access - Blocklist")
                    for url in blocklist_urls:
                        newrow = incident.addRow("zia_blocklist")
                        newrow.query_execution_date = QUERY_EXECUTION_DATE
                        newrow.blocklist_url = url
                        newrow.query_filter = url_filter
                else:
                    note_text += "<br>Blocklisted URLS: <b>{0}</b>".format(", ".join(blocklist_urls))
        else:
            note_text += u"ZIA Integration: Workflow <b>{0}</b>: There was an error returned using URL filter <b>{1}</b> "\
                         u"returned for SOAR function <b>{2}</b>."\
                .format(WF_NAME, url_filter, FN_NAME)
            note_text += u"<br>Error code: <b>{0}</b>, Error code: <b>{1}</b>, Details: <b>{2}</b>."\
                .format(CONTENT["error_code"], CONTENT["status"], CONTENT["text"] )

    else:
        note_text += u"ZIA Integration: Workflow <b>{0}</b>: There were <b>no</b> results using URL filter <b>{1}</b> "\
                     u"returned for SOAR function <b>{2}</b>."\
            .format(WF_NAME, url_filter, FN_NAME)

    incident.addNote(helper.createRichText(note_text))

main()

```

---

