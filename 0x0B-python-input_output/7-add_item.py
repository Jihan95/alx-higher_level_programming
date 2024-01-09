#!/usr/bin/python3
"""
Module to adds all arguments to a Python list and then save them to a file
"""
from sys import argv
from os.path import isfile
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
if isfile(filename):
    my_obj = load_from_json_file(filename)
else:
    my_obj = []

my_obj.extend(argv[1:])
save_to_json_file(my_obj, filename)
