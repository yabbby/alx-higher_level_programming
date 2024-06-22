#!/bin/bash
# Returns the content size of request
curl -si "$1" | grep 'Content-Length' | cut -d' ' -f2
