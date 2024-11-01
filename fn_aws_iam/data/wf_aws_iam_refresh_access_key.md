<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.1048
-->

# Example: AWS IAM: Refresh Access Key

## Function - AWS IAM: List Users

### API Name
`fn_aws_iam_list_users`

### Output Name
`None`

### Message Destination
`fn_aws_iam`

### Pre-Processing Script
```python
inputs.aws_iam_user_name = row.UserName
```

### Post-Processing Script
```python
##  AWS IAM - fn_aws_iam_list_users script ##
# Example result:
"""
Result: {
            'version': '1.0', 'success': True, 'reason': None,
            'content': [{'Path': '/', 'UserName': 'iam_test_User', 'UserId': 'ABCDEFG',
                         'Arn': 'arn:aws:iam::123456789123:user/iam_test_User', 'CreateDate': '2019-11-05 15:54:43'},
                        {'Path': '/', 'UserName': 'iam_test_User_2', 'UserId': 'ABCDEFG',
                         'Arn': 'arn:aws:iam::123456789123:user/iam_test_User_2',
                         'CreateDate': '2019-10-31 16:23:07', 'PasswordLastUsed': '2019-11-12 10:55:42'}
                       ],
            'raw': '[{"Path": "/", "UserName": "iam_test_User", "UserId": "ABCDEFG", "Arn": "arn:aws:iam::123456789123:user/iam_test_User", "CreateDate": "2019-11-05 15:54:43"}, {"Path": "/", "UserName": "iam_test_User_2", "UserId": "ABCDEFG", "Arn": "arn:aws:iam::123456789123:user/iam_test_User_2", "CreateDate": "2019-10-31 16:23:07"}]',
            'inputs': {},
            'metrics': {'version': '1.0', 'package': 'fn-aws-iam', 'package_version': '1.0.0',
                        'host': 'myhost.ibm.com', 'execution_time_ms': 7951,
                        'timestamp': '2019-11-14 13:48:30'
                       }
}

"""
import re
#  Globals
# List of fields in datatable fn_aws_iam_list_users script
DATA_TBL_FIELDS = ["query_execution_time", "UserName", "UserId", "Arn", "DefaultUser", "CreateDate", "LoginProfileExists",
                   "PasswordLastUsed", "Tags"]
FN_NAME = "fn_aws_iam_list_users"
WF_NAME = "Refresh Access Key"
# Processing
INPUTS = results.inputs
CONTENT = results.content
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]

def main():
    note_text = ''
    if CONTENT:
        if isinstance(CONTENT, dict) and CONTENT.get("Status") == "NoSuchEntity":
            note_text += "AWS IAM Integration: Workflow <b>{0}</b>: The user <b>{1}</b> does not exist " \
                         "for Resilient function <b>{2}</b>."\
                .format(WF_NAME, INPUTS["aws_iam_user_name"], FN_NAME)
            row.Status = "Deleted"
        elif len(CONTENT) == 1:
            workflow.addProperty("user_exists", {})
        else:
            note_text = "AWS IAM Integration: : Workflow <b>{0}</b>: Too many results <b>{1}</b> returned for user " \
                        "<b>{2}</b> for Resilient function <b>{3}</b>."\
                .format(WF_NAME, len(CONTENT), INPUTS["aws_iam_user_name"], FN_NAME)
            row.Status = "Deleted"
    else:
        note_text += "AWS IAM Integration: Workflow <b>{0}</b>: There were <b>no</b> results returned for user " \
                     "<b>{1}</b> for Resilient function <b>{2}</b>.".format(WF_NAME, INPUTS["aws_iam_user_name"], FN_NAME)
    if note_text:
        incident.addNote(helper.createRichText(note_text))
if __name__ == "__main__":
    main()
```

---

## Function - AWS IAM: List User Access Key IDs

### API Name
`fn_aws_iam_list_user_access_key_ids`

### Output Name
`None`

### Message Destination
`fn_aws_iam`

### Pre-Processing Script
```python
inputs.aws_iam_user_name = row.UserName
```

### Post-Processing Script
```python
##  AWS IAM - fn_aws_iam_list_user_access_keys script ##
# Example result:
"""
Result: {
          'version': '1.0', 'success': True, 'reason': None,
          'content': [{'UserName': 'iam_test_User', 'AccessKeyId': 'ABCDEFGH',
                       'Status': 'Active', 'CreateDate': '2019-11-12 11:09:38'
                       }],
          'raw': '[{"UserName": "iam_test_User", "AccessKeyId": "ABCDEFGH",
                  "Status": "Active", "CreateDate": "2019-11-12 11:09:38"}]',
          'inputs': {'aws_iam_user_name': 'iam_test_User'},
          'metrics': {'version': '1.0', 'package': 'fn-aws-iam', 'package_version': '1.0.0',
                      'host': 'myhost.ibm.com', 'execution_time_ms': 5365, 'timestamp': '2019-11-21 10:41:22'}}
"""
#  Globals
DATA_TBL_FIELDS = ["query_execution_time", "UserName", "AccessKeyId", "CreateDate", "Status", "DefaultKey"]
# List of fields in datatable fn_aws_iam_list_users script last used access keys.
DATA_TBL_FIELDS_LUAK = ["LastUsedDate", "ServiceName", "Region"]

FN_NAME = "fn_aws_iam_list_user_access_keys"
WF_NAME = "Refresh Access Key"
# Processing
CONTENT = results.content
INPUTS = results.inputs
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]

def process_access_key(ak_id, user_name):
    row.query_execution_date = QUERY_EXECUTION_DATE
    for f in DATA_TBL_FIELDS[2:]:
        if ak_id[f] is not None:
            row[f] = ak_id[f]
        # Add key last used data if it exists.
        if ak_id["key_last_used"] is not None:
            luak = ak_id["key_last_used"]
            for l in DATA_TBL_FIELDS_LUAK:
                if luak[l] is not None:
                    row[l] = luak[l]

def main():
    note_text = ''
    if CONTENT:
        for ak_id in CONTENT:
            if ak_id["AccessKeyId"] and ak_id["AccessKeyId"] == row.AccessKeyId:
                note_text = "AWS IAM Integration: Workflow <b>{0}</b>: Access key <b>{1}</b> found for user " \
                    "<b>{2}</b> for Resilient function <b>{3}</b>."\
                    .format(WF_NAME, row.AccessKeyId, INPUTS["aws_iam_user_name"], FN_NAME)
                note_text += "<br>Refreshing data table <b>{0}</b> for user <b>{1}</b> and access key " \
                             "id <b>{2}</b>.</br>"\
                    .format("AWS IAM Access Keys", INPUTS["aws_iam_user_name"], row.AccessKeyId)
                user_name = ak_id["UserName"]
                process_access_key(ak_id, user_name)
            else:
                note_text = "AWS IAM Integration: Workflow <b>{0}</b>: Access key <b>{1}</b> not found for user " \
                            "<b>{2}</b> for Resilient function <b>{3}</b>." \
                    .format(WF_NAME, row.AccessKeyId, INPUTS["aws_iam_user_name"], FN_NAME)
                row.Status = "Deleted"
    else:
        note_text = "AWS IAM Integration: Workflow <b>{0}</b>: There was <b>no</b> Access key <b>{1}</b> not found " \
                    "for user <b>{2}</b> for Resilient function <b>{3}</b>."\
            .format(WF_NAME, row.AccessKeyId, INPUTS["aws_iam_user_name"], FN_NAME)
        row.Status = "Deleted"
        
    if note_text:
        incident.addNote(helper.createRichText(note_text))
if __name__ == "__main__":
    main()
```

---

