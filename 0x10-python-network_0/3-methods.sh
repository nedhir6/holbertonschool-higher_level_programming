#!/bin/bash
#  displays all HTTP methods the server will accept.
curl -sX OPTIONS * $1 -i | grep -i Allow | awk -F " " '{$1="";print $0}' | tail -c +2
