#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0 or my_list is None):
        return (None)
    max_n = my_list[0]
    for i in range(1, len(my_list)):
        if (my_list[i] > max_n):
            max_n = my_list[i]
            continue
    return(max_n)
