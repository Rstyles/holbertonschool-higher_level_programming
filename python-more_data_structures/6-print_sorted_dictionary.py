#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_keys = []
    for key in a_dictionary:
        list_of_keys.append(key)
    for i in sorted(list_of_keys):
        print(f"{i}: {a_dictionary[i]}")
