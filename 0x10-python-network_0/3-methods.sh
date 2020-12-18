#!/bin/bash
#  displays all HTTP methods the server will accept.
curl -s $1 -I | grep Allow | awk -F " " '{$1="";print $0}' | tail -c +2
