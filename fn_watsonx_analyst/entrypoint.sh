#!/bin/bash

intexit() {
    # Kill all subprocesses (all processes in the current process group)
    kill -HUP -$$
}

hupexit() {
    # HUP'd (probably by intexit)
    echo
    echo "Interrupted"
    exit
}

trap hupexit HUP
trap intexit INT

if [ -e app.config ]
then
  # if local app config
  APP_CONFIG_SHA=$(sha256sum app.config)
else
  APP_CONFIG_SHA=$(sha256sum /etc/rescircuits/app.config)
fi

# shellcheck disable=SC2116
resilient-circuits run & CIRCUITS_PID=$(echo $!)
# shellcheck disable=SC2116
java -jar -Xmx300m /opt/tika/tika-server.jar >/var/log/tika/tika.log 2>&1 & TIKA_PID=$(echo $!)

tika_expected_output="This is Tika Server (Apache Tika 2.9.3). Please PUT"

while true
do
  sleep 60
  tika_response=$(curl -s http://localhost:9998/tika)
  if [ "$tika_response" != "$tika_expected_output" ]; then
    echo "Tika API gave a bad response, killing app."
    echo "Tika API response: $tika_response"
    echo "Expected API response: $tika_expected_output"
    kill -9 "$CIRCUITS_PID"
    kill -9 "$TIKA_PID"
  fi

  echo -n "`date +'%F %T,%N INFO '`"
  if ! echo $APP_CONFIG_SHA | sha256sum --check --quiet
  then
    echo "Killing the app due to app.config changes"
    kill -9 "$CIRCUITS_PID"
    kill -9 "$TIKA_PID"
    break
  fi
  if [ "$CIRCUITS_PID" != "`ps -o pid= -p $CIRCUITS_PID|xargs`" ]; then break; fi
done
