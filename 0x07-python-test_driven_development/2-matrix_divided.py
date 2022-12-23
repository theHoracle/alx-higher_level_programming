def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and return a new matrix.

    Parameters:
        matrix (list of lists of int or float): The matrix to divide.
        div (int or float): The number to divide by.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check if each row of the matrix is of the same size
    sizes = [len(row) for row in matrix]
    if len(set(sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide all elements of the matrix by div, rounded to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
