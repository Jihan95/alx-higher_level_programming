#!/usr/bin/python3
"""
Module to read a file
"""


def read_file(filename=""):
    """
    Function to read a text file and prints it to STDOUT

    Args:
    filename (str): the name of the file to be read
    """
    with open(filename) as f:
        for line in f:
            print(line, end='')
