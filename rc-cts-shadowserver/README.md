To install the threat service with your Resilient server
    (assuming that resilient-circuits application is running on the same server):
        sudo resutil threatserviceedit -name "Shadow Server" -resturl http://127.0.0.1:9000/cts/shadow_server_threat_feed
        
To test the connection:
        sudo resutil threatservicetest -name "Shadow Server"
        
To delete:
        sudo resutil threatservicedel -name "Shadow Server"
