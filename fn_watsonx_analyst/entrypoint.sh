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

while true
do
  sleep 60

  echo -n "`date +'%F %T,%N INFO '`"
  if ! echo $APP_CONFIG_SHA | sha256sum --check --quiet
  then
    echo "Killing the app due to app.config changes"
    kill -9 "$CIRCUITS_PID"
    break
  fi

  if [ "$CIRCUITS_PID" != "`ps -o pid= -p $CIRCUITS_PID | xargs`" ]; then break; fi
done
