#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted keys of the dictionary
    sorted_keys = sorted(a_dictionary.keys())

    # Print the dictionary with the keys in order
    for key in sorted_keys:
        print(key + ": " + str(a_dictionary[key]))
