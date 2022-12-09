#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Compute the symmetric difference of the two sets
    diff_set = set_1.symmetric_difference(set_2)

    # Return the symmetric difference as a set
    return set(diff_set)
