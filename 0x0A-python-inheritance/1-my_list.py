#!/usr/bin/python3
class MyList(list):
    """
    A subclass of the built-in list class.

    This class has a single public instance method, `print_sorted()`, which takes a list and
    prints it in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Parameters:
            self (list): The list to be printed.
        """
        print(sorted(self))
