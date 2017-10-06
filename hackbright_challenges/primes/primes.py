"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

def is_prime(num):
    """Is num a prime number?"""

    assert num >= 0, "Num should be a positive integer!"

    # definition: 0 and 1 are not prime
    if num < 2:
        return False

    # definition: 2 is prime
    if num == 2:
        return True

    # if it's divisible by 2, it's not prime
    # (We do this as a special case, so that after this we can check
    # only odd numbers -- all even numbers are divisible by 2)
    if num % 2 == 0:
        return False

    # see if number is prime -- we'll do this by checking
    # to see if there's any odd number 3 .. sqrt(num)
    # that evenly divides num (why square root? think about it!)

    n = 3

    while n * n <= num:
        if num % n == 0:
            return False
        # Go to next odd number
        n += 2

    return True

def primes(count):
    """Return count number of prime numbers, starting at 2."""

    # START SOLUTION

    results = []
    i = 2

    while count > 0:

        if is_prime(i):
            results.append(i)
            count -= 1

        i += 1

    return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
