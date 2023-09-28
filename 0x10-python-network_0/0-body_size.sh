#!/bin/bash
# script that takes a URL, sends a GET request to the URL
# and displays the size of the body of the response (bytes)

# Check if URL is provided
if [  -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send request to URL and get the size of the body in bytes
SIZE=$(curl -s -w '%{size_download}' -o /dev/null "$1")

echo "$SIZE"
