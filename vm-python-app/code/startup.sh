#!/bin/sh
if [ ! -z $1 ]
then
export VMAPP_CONTENT=$1 
fi
python3 app.py