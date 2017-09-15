"""Given list of ints, return True if any two nums in list sum to 0.

    >>> add_to_zero_set([])
    False

    >>> add_to_zero_set([1])
    False

    >>> add_to_zero_set([1, 2, 3])
    False

    >>> add_to_zero_set([1, 2, 3, -2])
    True

Given the wording of our problem, a zero in the list will always
make this true, since "any two numbers" could include that same
zero for both numbers, and they sum to zero:

    >>> add_to_zero([0, 1, 2])
    True
"""


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    if 0 in nums:
        return True

    if nums:
        for num in nums:
            for n in nums:
                if num + n == 0:
                    return True

    return False

def add_to_zero_fancy(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    nums = set(nums)

    return any(-num in nums for num in nums)

def add_to_zero_set(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    set_nums = set(nums)

    for num in nums:
        if -num in set_nums:
            return True
    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"
