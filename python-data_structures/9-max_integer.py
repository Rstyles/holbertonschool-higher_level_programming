#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = 0
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if i == 0:
            largest = my_list[i]
        else:
            if my_list[i] > largest:
                largest = my_list[i]
    return largest
