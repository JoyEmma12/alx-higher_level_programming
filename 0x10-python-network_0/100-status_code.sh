#!/bin/bash
# Script that send request to a URL passed as an arguement and display the status code of response.
curl -sSL -o /dev/null -w "%{http_code}" "$1"
