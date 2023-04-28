#!/bin/bash
# Script that sends a JSON POST resquest to aURL passed as the first arguement and displays the body
curl -s -H POST -H "Content-Type: application/json" -d  "$(cat "$2")" "$1"
