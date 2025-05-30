#!/usr/bin/python3
"""0. What's my status? #0"""
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    page = response.read()
    for line in page:
        print(f"    f{line}")
