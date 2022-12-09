#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create an empty list to store the replaced values
    replaced_list = []

    # Iterate through the input list
    for value in my_list:
        # If the value is the search element, append the replace element to the new list
        if value == search:
            replaced_list.append(replace)
        # Otherwise, append the value to the new list
        else:
            replaced_list.append(value)

    return replaced_list
