"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'
"""

# For example, using our alternate solution::

#     >>> dec2bin_forwards(0)
#     '0'

#     >>> dec2bin_forwards(1)
#     '1'

#     >>> dec2bin_forwards(2)
#     '10'

#     >>> dec2bin_forwards(4)
#     '100'

#     >>> dec2bin_forwards(15)
#     '1111'




def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""

    binary = []

    if num == 0:
        binary.append('0')
    else:

        while num > 0:
            remainder = num % 2
            num = num / 2
            binary.append(str(remainder))

    return "".join(reversed(binary))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
