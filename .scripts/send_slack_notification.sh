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

if [ -z "$1" ]; then
	custom_message="No message."
else
	custom_message=$1
fi

if [ -z "$2" ]; then
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

author="$(git log -1 $TRAVIS_COMMIT --pretty="%aN")"

travis_url=https://travis.ibm.com/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID

message="{
	\"icon_emoji\": \":$status:\",
	\"username\": \"$username\",
	\"text\": \"$TRAVIS_REPO_SLUG <$travis_url|Build #$TRAVIS_BUILD_NUMBER> \n$1\", 
	\"blocks\": [
		{
			\"type\": \"divider\"
		},
		{
			\"type\": \"section\",
			\"fields\": [
				{
					\"type\": \"mrkdwn\",
					\"text\": \"*Build*\"
				},
				{
					\"type\": \"mrkdwn\",
					\"text\": \"<$travis_url|#$TRAVIS_BUILD_NUMBER>\"
				},
                {
					\"type\": \"mrkdwn\",
					\"text\": \"*Repo*\n$TRAVIS_REPO_SLUG\"
				},
				{
					\"type\": \"mrkdwn\",
					\"text\": \"*Success*\n:$status:\"
				},
				{
					\"type\": \"mrkdwn\",
					\"text\": \"*Author*\n$author\"
				},
				{
					\"type\": \"mrkdwn\",
					\"text\": \"*Commit*\n$TRAVIS_COMMIT_MESSAGE\"
				}
			]
		},
		{
			\"type\": \"section\",
			\"text\": {
				\"type\": \"mrkdwn\",
				\"text\": \"$custom_message\"
			}
		},
		{
			\"type\": \"divider\"
		}
	]
}"

curl -X POST --data-urlencode "payload=$message" $NOTIFICATION_HOOK