#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if (a_dictionary is not None):
        new_dic = a_dictionary.copy()
        for n in a_dictionary:
            new_dic[n] = a_dictionary[n] * 2
        return (new_dic)
