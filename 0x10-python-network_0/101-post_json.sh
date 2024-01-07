#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response
curl -sH "Content-Type: application/json" -X POST -d "${cat "$2"}" "$1"
