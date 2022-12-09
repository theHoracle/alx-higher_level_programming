#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Compute the intersection of the two sets
    common_set = set_1.intersection(set_2)

    # Return the intersection as a set
    return set(common_set)
