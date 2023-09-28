#!/bin/bash
# a script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -I -L "$1" | awk '/200 OK/ { system("curl -s -L --get " "'"$1"'"); found=1; exit } END { if (!found) exit 1 }'
