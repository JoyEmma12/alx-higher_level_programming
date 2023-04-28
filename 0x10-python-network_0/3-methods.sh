#!/bin/bash
# Script that takes in URL and display all HTTPS methods.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
