#!/bin/bash
# Script that sends a POST request to the passed url.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be ehre for PLD" "$1"
