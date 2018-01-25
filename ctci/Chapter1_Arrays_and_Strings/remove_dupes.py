"""Given a string, remove duplicate instances of characters without using any 
   additional buffer. NOTE: One or two additional variables are fine. 
   An extra copy of the array is not.

    >>> remove_dupes("noon")
    'no'
    >>> remove_dupes("nononono")
    'no'
    >>> remove_dupes("abcd")
    'abcd'
    >>> remove_dupes("")
    ''

"""


def remove_dupes(string):
    """Remove duplicate characters in a string"""
    
    # Convert string to a list because strings are immutable in Python
    string_list = list(string)
    outer = 0

    while outer < len(string_list):
        inner = outer

        while inner < len(string_list):
            if inner == outer:
                inner += 1
                continue

            if string_list[inner] == string_list[outer]:
                string_list.pop(inner)
            else:
                inner += 1

        outer += 1
    # Convert list back into a string
    return ''.join(string_list)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"