#!/bin/bash
#bash script that takes in a URL and displays all HTTP methods accepted by server
[ $# -eq 1 ] && curl -sI -X OPTIONS "$1" | grep -i "Allow" | awk '{print $2}' | tr -d '\r\n'
