#!/usr/bin/python3
"""1. Response header value #0"""
import urllib.request
import sys
req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    print(response.headers.get("X-Request-Id"))
