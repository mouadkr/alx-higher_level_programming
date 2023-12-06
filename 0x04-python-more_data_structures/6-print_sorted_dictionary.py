#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, b in sorted(zip(a_dictionary.keys(), a_dictionary.values())):
        print(i, b)
