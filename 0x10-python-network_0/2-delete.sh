#!/bin/bash
# Script that sends a DELETE request to the URL passed at the first argurment.
curl -sX DELETE "$1"
