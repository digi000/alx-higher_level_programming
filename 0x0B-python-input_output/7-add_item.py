#!/usr/bin/python3
"""7. Load, add, save"""
import sys
ss = __import__("5-save_to_json_file").save_to_json_file
data = []
i = 1
while (i < len(sys.argv)):
    data.append(sys.argv[i])
    i += 1
ss(data, "add_item.json")
