#!/bin/bash
# Script that takes in URL and display all HTTPS methods
url="$1"

response=$(curl -sSl -X OPTIONS $url)
	methods=$(echo "$response" | grep -i "allow" | sed -e 's/Allow: //i')
	echo "methods for $url are: $methods" 
