#!/bin/bash
# Script that sends a JSON POST resquest to aURL passed as the first arguement and displays the body
curl -s -X POST -H "Contnet-Type: application/json" --data-binary "@$2" "$1"
