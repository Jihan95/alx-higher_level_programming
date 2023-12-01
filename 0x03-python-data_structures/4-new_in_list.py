#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx >= len(my_list)):
        return(my_list)
    list_copy = my_list.copy()
    for i in range(len(my_list)):
        if (i == idx):
            list_copy[i] = element
            return(list_copy)
