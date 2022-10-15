#!/usr/bin/python3
"""
Script that receives arguments and add them
to a list
"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

for idx in range(1, len(sys.argv)):
    my_list.append(sys.argv[idx])

save_to_json_file(my_list, "add_item.json")
