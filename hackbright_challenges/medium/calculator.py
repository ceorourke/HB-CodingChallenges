"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    result = 0
    stack = s.split()
    first = int(stack.pop())
    second = int(stack.pop())

    while stack:
        operator = stack.pop()
        if operator == "+":
            result = second + first
        elif operator == "*":
            result = second * first
        elif operator == "-":
            result = second - first
        else:
            result = second / first
        if stack:
            first = result
            second = int(stack.pop())

    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
