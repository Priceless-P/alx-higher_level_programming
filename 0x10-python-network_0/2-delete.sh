#!/bin/bash
# Sends a DELETE request to the URL
# and displays the body of the response

if [ -z "$1" ]; then
    echo "Usage $0 <URL>";
    exit 1;
fi;

curl -sX DELETE "$1"
