#!/bin/sh
#
# Following steps are performed by this script:
#
# 1) Adds an artifact value to the remote machine's white list file.
# 2) Executes a snort.cfg test to check if new rules can be applied and returns the result to stdout.
# 3) Executes SIGHUP to reload the snort configuration. This requires the accurate path to the snort.pid file.
#    This requires using the --pid-path argument when starting Snort, in order specify the path for the Snort PID file
#
# Returns: The output of the Snort test run (2).
#
# Only works in Unix-based environments.
#   !!! Requires passwordless authentication such as SSH key authentication between both machines to prevent prompting for password. !!!

# Remote settings
DEST_HOST=
DEST_USER=

DEST_RULES_DIR=/etc/snort/rules/
DEST_LIST_FILE=resilient_whitelist.rules

DEST_SNORT_DIR=/etc/snort/
DEST_SNORT_FILE=snort.conf

DEST_IF=en0

# Absolute path to the snort.pid file
DEST_SNORT_PID_FILE=/etc/snort/snort.pid

# 1) Create remote file if needed and append artifact value
echo $1 | ssh $DEST_USER@$DEST_HOST "cat >> $DEST_RULES_DIR/$DEST_LIST_FILE"

# 2) Remote test snort.config and print response to stdout
ssh $DEST_USER@$DEST_HOST "snort -T -c $DEST_SNORT_DIR/$DEST_SNORT_FILE -i $DEST_IF" 2>&1

# 3) Reload remote Snort instance using new settings
ssh $DEST_USER@$DEST_HOST "kill -SIGHUP \`cat $DEST_SNORT_PID_FILE\`" > /dev/null 2>&1
