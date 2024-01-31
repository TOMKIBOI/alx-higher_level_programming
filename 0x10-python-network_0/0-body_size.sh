#!/bin/bash
#script that takes in a URL, sends a request to that URL, and displayscontent length
[ $# -eq 1 ] && curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n' || echo "Usage: $0 <URL>"
