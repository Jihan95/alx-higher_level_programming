#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return(None)
    mkey = next(iter(a_dictionary), None)
    n = a_dictionary[mkey]
    for key in a_dictionary:
        if (a_dictionary[key] > n):
            mkey = key
    return(mkey)
