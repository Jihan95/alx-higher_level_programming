#!/usr/bin/python3
def uniq_add(my_list=[]):
    if (my_list is None):
        return
    my_set = set(my_list)
    sum = 0
    for n in my_set:
        sum += n
    return (sum)
