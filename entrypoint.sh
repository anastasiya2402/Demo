#!/bin/bash

# start virtual display server
export DISPLAY=:20
Xvfb :20 -screen 0 1366x768x16 &
# x11vnc -passwd secret -display :20 -N -forever &

# set default values
environment="qa"
filepath=""
tags=""
name=""

# check that filepath is provided in the first positional argument
if [ -z "$1" ] || [ "$1" == *"--"* ];
then echo "Path to test files has not been provided"; exit 1;
else filepath=$1; echo "Test / Tests Set to execute: $filepath"; shift;
fi

# parse all params matching "--param_name value"
# and set param_name=value
while [ $# -gt 0 ]; do
  if [[ $1 == *"--"* ]];
    then
      param="${1/--/}"
      declare $param="$2"
  fi
  shift
done

export ENVIRONMENT=$environment
echo "Environment: $environment"

cmd="behave $filepath --no-capture --format plain"
if [ "$tags" != "" ];
then
	echo "Tags to run (optional): $tags"
	cmd="$cmd --tags=\"$tags\""
fi
if [ "$name" != "" ];
then
	echo "Examples name to run (optional): $name"
	cmd="$cmd --name=\"$name\""
fi
# execute behave command; always return success
eval $cmd || :

# fire status 0 no matter of test results
exit