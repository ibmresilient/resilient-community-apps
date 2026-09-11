These files are intended to be run with the SOARScriptSimulator. The output of a run can be reviewed for correctness. 
Not all the results represent correct execution but the SOARScriptSimulator tool is intended to ensure correct python execution.

Ex. 
```
% SOARScriptingSimulator -f test31CharMD5.json ../EmailParser.py

INFO:Simulator:--Setting emailMessage attribute: attachments=[]
INFO:Simulator:--Creating new incident: title='Incident generated from email "this is subject" via mailbox somemail', owner=''
INFO:Simulator:--Setting incident attribute: reporter=A Example <a@example.com>
INFO:Simulator:--Artifact (Email Subject): 'this is subject'
Description: 'Suspicious email subject'
INFO:Simulator:--Artifact (Malware MD5 Hash): '02e5f98d4835a2bd280b124f55120a51'
Description: 'MD5 hash of potential malware file'
INFO:Simulator:--Artifact (Malware MD5 Hash): 'a49c17ebd60638f1e82e6d41ed51f15e'
Description: 'MD5 hash of potential malware file'
```