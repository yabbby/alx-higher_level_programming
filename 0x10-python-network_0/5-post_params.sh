#!/bin/bash
# sends a POST request to the passed URL
curl -X POST -s -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
