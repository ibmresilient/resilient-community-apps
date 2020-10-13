#!/bin/sh
# Script watches for changes in app.config and kills circuits when it changes
# This is useful when using this image to run circuits in a Kubernetes Deployment because Kubernetes will start a new
# container in the Pod and this new container will use the new configuration
# In a plain old docker system the container will exit
APP_CONFIG_SHA=`sha256sum /etc/rescircuits/app.config`
resilient-circuits run & CIRCUITS_PID=`echo $!`
while true
do
  if ! echo $APP_CONFIG_SHA | sha256sum --check
  then
    kill -9 $CIRCUITS_PID
    break
  fi
  sleep 60
done