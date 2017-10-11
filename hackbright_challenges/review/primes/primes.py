"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    prime_nums = []
    i = 2

    while len(prime_nums) < count:
        if is_prime(i) == True:
            prime_nums.append(i)
        i += 1

    return prime_nums

def is_prime(num):
    """Return whether a number is prime"""

    for i in range(1, num+1):
        if (i == 1) or (i == num):
            continue
        if num % i == 0:
            return False

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
