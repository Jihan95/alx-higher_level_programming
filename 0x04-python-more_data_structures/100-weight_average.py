#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list is None or len(my_list) == 0):
        return 0
    total_sum = 0
    total_mul = 0
    for i in range(len(my_list)):
        total_sum += my_list[i][1]
        total_mul += my_list[i][0] * my_list[i][1]
    return total_mul / total_sum
