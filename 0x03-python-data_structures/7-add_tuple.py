#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if(len(tuple_a) >= 2 and len(tuple_b) >= 2):
        new_t = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif (len(tuple_a) == 1 and len(tuple_b) >= 2):
        new_t = tuple_a[0] + tuple_b[0], tuple_b[1]
    elif (len(tuple_a) == 0 and len(tuple_b) >= 2):
        new_t = tuple_b
    elif (len(tuple_a) >= 2 and len(tuple_b) == 1):
        new_t = tuple_a[0] + tuple_b[0], tuple_a[1]
    elif (len(tuple_a) >= 2 and len(tuple_b) == 0):
        new_t = tuple_a
    else:
        new_t = 0, 0
    return(new_t)
