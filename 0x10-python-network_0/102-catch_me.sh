#!/bin/bash
# Script that makes a request and respond with a message.
curl -s -X PUT -H "Referer: https://www.google.com" -d "user_id=98" "0.0.0.0:5000/catch_me"
