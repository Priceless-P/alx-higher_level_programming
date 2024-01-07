#!/bin/bash
# Displays the response body for a given URL for 200 status code responses.
if [ -z "$1" ]; then
    echo "Usage $0 <URL>";
    exit 1;
fi;

curl -sL "$1"
