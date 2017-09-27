"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""

    # first pass, O(n)
    # while lst:
    #     print lst[0]
    #     lst.pop(0)
    #     print_recursively(lst)

    # given solution, O(1)
    if lst:
        print lst[0]
        print_recursively(lst[1:])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. GREAT JOB!\n"
