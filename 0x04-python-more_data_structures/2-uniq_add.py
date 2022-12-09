#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store the unique integers
    unique_set = set()

    # Iterate through the input list
    for value in my_list:
        # If the value is not in the set, add it to the set and the sum
        if value not in unique_set:
            unique_set.add(value)
            sum += value

    return sum
