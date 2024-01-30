#!/bin/bash
# A bash script that takes in a URL, sends a request to it
curl -sI "$1" | awk '/Content-Length/ {print $2}'
