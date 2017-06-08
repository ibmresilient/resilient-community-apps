#!/usr/bin/env bash

# find hostname
# called by automatic action from IP Address artifact
# produce just the hostname

python <<EOF
try:
    import sys, socket, json
    ip = "$1"
    result = {"type":"System Name", "description":"Added automatically for IP address " + ip}
    result["value"] = (socket.gethostbyaddr(ip))[0].split('.')[0]
    print(json.dumps(result))
except Exception  as e:
    sys.exit(e)
EOF
