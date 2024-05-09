#!/usr/bin/python3
""" Function to find the peak at list of numbers """


def find_peak(list_of_integers):
    """ Function to find the peak at list of numbers """
    if not list_of_integers or not type(list_of_integers, list):
        return None
    return max(list_of_integers)
