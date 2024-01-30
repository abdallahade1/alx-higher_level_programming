#!/bin/bash
# A bash script that takes in a URL, sends a request to it
curl -s "$1" | wc -c
