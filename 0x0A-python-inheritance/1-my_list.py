#!/usr/bin/python3

"""
    module with modified list class
"""


class MyList(list):
    """
    Modified list class
    """

    def print_sorted(self):
        """
        prints the list but sorted in ascending order.
        """
        print(sorted(self))
