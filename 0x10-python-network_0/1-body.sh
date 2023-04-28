#!/bin/bash
# Script that takes in a URL, sends a GET request and displays the body of thw response.
url="$1"
response=$(curl -sSL -w "%{status_code}" $url)
if [ "$response" == "200" ]; then
   echo "$(curl -sSL $url)"
else
   echo "Error: Response code was $response"
fi
