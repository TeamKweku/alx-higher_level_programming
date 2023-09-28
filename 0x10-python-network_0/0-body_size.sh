#!/bin/bash
# script that takes a URL, sends a GET request to the URL and displays the size of the body of the response
curl -s -I "$1" | awk -F ': ' '/Content-Length/ {print $2}'
