#!/bin/bash
# Sends a JSON POST request to a URL,
# and displays the body of the response

if [ "$#" -lt 2 ]; then
    echo "Usage $0 <URL> <file>";
    exit 1;
fi;

curl -sH "Content-Type: application/json" -X POST -d "${cat "$2"}" "$1"
