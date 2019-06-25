#!/bin/bash -e

function getJsonVal() {
   releaseID=`python -c "import json,sys;print json.dumps(json.loads('''$1''')$2); sys.exit(0);"` ; 
   echo $releaseID
}

echo Getting Git Tag...
latestTag=$(git tag --list | tail -n 1)

echo Creating release...
echo '{"tag_name": "'$latestTag'","target_commitish": "master","name": "'$latestTag'","body": "Resilient Python API '$latestTag'","draft": false,"prerelease": false}' > json.json
output=$(curl -X POST -H 'Content-Type:application/json' -H 'Accept:application/json' --data-binary @json.json https://api.github.com/repos/ibmresilient/resilient-community-apps/releases?access_token=$GIT_HUB_AUTH_TOKEN)
rm json.json

id=$(getJsonVal "$output" "['id']")
echo Release Id: $id
for file in ./rc[-_]*.tar.gz; do
  echo Uploading file... ${file##*/}
  fileUpload=$(curl --data-binary @./${file##*/} -H "Authorization: token $GIT_HUB_AUTH_TOKEN" -H "Content-Type: application/octet-stream" https://uploads.github.com/repos/ibmresilient/resilient-community-apps/releases/"$id"/assets?name=${file##*/} )
  echo $fileUpload
done

for file in ./fn_*.tar.gz; do
  echo Uploading file... ${file##*/}
  fileUpload=$(curl --data-binary @./${file##*/} -H "Authorization: token $GIT_HUB_AUTH_TOKEN" -H "Content-Type: application/octet-stream" https://uploads.github.com/repos/ibmresilient/resilient-community-apps/releases/"$id"/assets?name=${file##*/} )
  echo $fileUpload
done






