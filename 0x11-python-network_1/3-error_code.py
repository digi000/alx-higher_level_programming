#!/usr/bin/python3
"""3. Error code #0"""
import urllib.request
from urllib.error import HTTPError
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())
    except HTTPError as e:
        print(f"Error code: {e.code}")
