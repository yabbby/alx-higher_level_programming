#!/bin/bash
# displays only the status code of an http request
curl -s -w '%{http_code}' -o /dev/null "$1"
