#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create an empty list to store the squared values
    squared_matrix = []

    # Iterate through the rows and columns of the input matrix
    for row in matrix:
        squared_row = []
        for value in row:
            # Compute the square of each value and append it to the new row
            squared_value = value * value
            squared_row.append(squared_value)
        # Append the squared row to the new matrix
        squared_matrix.append(squared_row)

    return squared_matrix
