#!/bin/bash

scriptname=`basename $0`
tofind=$1
# read by line
IFS="
"
function show_processes() {
  result=`ps -Ao pid,cmd | grep $tofind | grep -v grep | grep -v $scriptname`
  for cmd in $result; do
    echo "    $cmd"
  done
}

echo ">> Find process(es):"
show_processes

echo -n '>> Kill all?[y/n]: '
read anwser
if [ "$anwser" = "y" ];then
  #echo "Yes"
  #continue
  echo -n ''
else
  # user choose not kill the process
  exit 0
fi

# read by line
IFS=
for cmd in $result; do
  echo 'will kill -->' $cmd
  #echo "pid: `echo $cmd | cut -d ' ' -f1`" 
  kill -9 `echo $cmd | cut -d ' ' -f1`
done

echo ">> Now grep result is: "
show_processes
