#!/usr/bin/python3
""" Function to find the peak at list of numbers """


def find_peak(list_of_integers):
    """ Function to find the peak at list of numbers """
    if not list_of_integers:
        return None
    return max(list_of_integers)
