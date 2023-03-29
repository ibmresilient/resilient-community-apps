#!/bin/sh
#
# Following steps are performed by this script:
#
# 1) Creates a rule by using the artifact value and adds it to the remote rule file.
# 2) Executes a snort.cfg test to check if new rules can be applied and returns the result to stdout.
# 3) Executes SIGHUP to reload the snort configuration. This requires the accurate path to the snort.pid file.
#    This requires using the --pid-path argument when starting Snort, in order specify the path for the Snort PID file
#
# Returns: The output of the Snort test run (2).
#
# Only works in Unix-based environments. Note that the example rule will need to be customized depending on the objective.
#   !!! Requires passwordless authentication such as SSH key authentication between both machines to prevent prompting for password. !!!

# Settings for the remote snort server
DEST_HOST=172.20.1.3
DEST_USER=root

DEST_RULES_DIR=/etc/snort/rules/
DEST_LIST_FILE=resilient.rules

DEST_SNORT_DIR=/etc/snort/
DEST_SNORT_FILE=snort.conf

DEST_IF=eno16777984

DEST_SNORT_PID_FILE=/etc/snort/snort_virbro0.pid

# 1) Create remote file if needed and append text
rule="alert tcp any any -> any 25 (msg:\"Target Email Detected\"; content:\"$1\";)"
echo $rule | ssh $DEST_USER@$DEST_HOST "cat >> $DEST_RULES_DIR/$DEST_LIST_FILE"

# 2) Remote test Snort and print response to stdout
ssh $DEST_USER@$DEST_HOST "snort -T -c $DEST_SNORT_DIR/$DEST_SNORT_FILE -i $DEST_IF" 2>&1

# 3) Reload remote Snort instance using new settings
ssh $DEST_USER@$DEST_HOST "kill -SIGHUP \`cat $DEST_SNORT_PID_FILE\`" > /dev/null 2>&1
