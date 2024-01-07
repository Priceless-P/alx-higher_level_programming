#!/bin/bash
# Displys the curl body size
curl -s "$1" | wc -c
