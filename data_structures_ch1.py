# Exercise from chapter 1 of Data Structues and Algorithms in Python

#R-1.1

def is_multiple(n, m):
    """Takes 2 integer values and returns True if n is a multiple of m"""

    if n < m:
        return False

    if n == m:
        return True

    return is_multiple(n - m, m)

print is_multiple(24, 4) # True
print is_multiple(25, 5) # True
print is_multiple(11, 4) # False

#R-1.2 ####################################################################

def is_even(k):
    """Determines if an integer is even"""

    return True if k % 2 == 0 else False

print is_even(4) # True
print is_even(5) # False

#R-1.3 ####################################################################

def minmax(data):
    """Returns a tuple of the minimum and maximum values in the array"""

    min_num = float("inf")
    max_num = float("-inf")

    for num in data:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)


print minmax([1,2,3,4,5]) # (1, 5)

#R-1.4 ####################################################################

def sum_squares(n):
    """Returns the sum of the squares of all the positive ints smaller than n"""

    if n == 1:
        return 1

    return n ** 2 + sum_squares(n - 1)

print sum_squares(4)

########################################################################

# R-1.5 
the_sum = sum([num ** 2 for num in range(5)])
print the_sum

# R-1.7
the_sum = sum([num **2 for num in range(5) if num % 2 != 0])
print the_sum

# R-1.9
for i in range(50, 81, 10):
    print i

# R-1.10
for i in range(8, -9, -2):
    print i



