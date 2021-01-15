#!/bin/bash
# Sends a comment to GitHub PR
# Requires $GITHUB_AUTH

# Parameters that can be passed
# 1 - optional - additional text
# 2 - optional - success/failure or slack emoji without ::

# We're using different usernames for different outcomes so their green/red logo
# gets displayed
# Professor Farnsworth says - good news everyone
# Paul Revere brings bad news
if [[ $TRAVIS_EVENT_TYPE != "pull_request" ]]; then
	exit 0
fi

message=""
if [[ -n "${PUBLISHED_PACKAGES[*]}" ]]; then
	for package_url in ${PUBLISHED_PACKAGES[@]};
	do
		package=$(echo $package_url | tr "/" "\n" | tail -n 1)
		message="${message}\n[$package]($package_url)"
	done
	curl -s -H "Authorization: token $GITHUB_AUTH_TOKEN" \
 		-X POST -d "{\"body\": \"Bot: ${message}\"}" \
		$GITHUB_PR_COMMENT_URL
else
	echo "No packages to link to PR"
fi
