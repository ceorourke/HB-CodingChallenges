"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    results = []

    if (not a) and (not b):
        return results
    elif not a:
        return b
    elif not b:
        return a
    else:
        a_index = 0
        b_index = 0

        while (a_index < len(a)) and (b_index < len(b)):
            if a[a_index] < b[b_index]:
                results.append(a[a_index])
                a_index += 1
            else:
                results.append(b[b_index])
                b_index += 1

        if a_index == len(a):
            leftover = b[b_index:]
            results.extend(leftover)
        elif b_index == len(b):
            leftover = a[a_index]
            results.extend(leftover)
        else:
            return results
        return results



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
