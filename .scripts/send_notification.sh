#!/bin/bash
# Sends a Slack notification to a webhook.
# Requires $NOTIFICATION_HOOK

# Parameters that can be passed
# 1 - optional - additional text
# 2 - optional - success/failure or slack emoji without ::

# We're using different usernames for different outcomes so their green/red logo
# gets displayed
# Professor Farnsworth says - good news everyone
# Paul Revere brings bad news

if [ -z $2 ]; then
	status="green_square"
	username="Professor Farnsworth"
elif [ $2 == "success" ]; then
	status="green_square"
	username="Professor Farnsworth"
elif [ $2 == "failure" ]; then
	status="red_square"
	username="Paul Revere"
else
	status=$2
	username="Paul Revere"
fi

travis_url=https://travis.ibm.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID

curl -X POST --data-urlencode "payload={\"username\": \"$username\",
\"text\": \"$TRAVIS_REPO_SLUG <$travis_url|Build #$TRAVIS_BUILD_NUMBER> \n$1\", 
\"icon_emoji\": \":$status:\"}" $NOTIFICATION_HOOK