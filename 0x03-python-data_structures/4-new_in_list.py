#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if (idx < 0 or idx >= len(my_list)):
        return(list_copy)
    for i in range(len(my_list)):
        if (i == idx):
            list_copy[i] = element
            return(list_copy)
