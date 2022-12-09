#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        # Return None if the dictionary is empty
        return None

    # Set the initial best score to the first value in the dictionary
    best_score = list(a_dictionary.values())[0]
    best_key = None

    # Iterate through the keys and values in the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the best score
        if value > best_score:
            # Update the best score and key
            best_score = value
            best_key = key

    # Return the key with the best score
    return best_key
