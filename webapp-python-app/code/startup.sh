#!/bin/sh
if [ ! -z $1 ]
then
export VMAPP_URL=$1 
fi
python3 app.py