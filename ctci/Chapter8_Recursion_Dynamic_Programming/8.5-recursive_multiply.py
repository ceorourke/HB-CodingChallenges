def multiply(num1, num2):
    """A simple, not super efficient way to multiply 2 numbers w/o the * operator"""

    if num2 == 1:
        return num1
    return multiply(num1, num2 - 1) + num1


print multiply(2, 3)

###############################################################################

def multiply_memo(num1, num2):
    """A more complicated yet more efficient way using memoization"""

    if num1 < num2:
        smaller, bigger = num1, num2
    else:
        smaller, bigger = num2, num1

    memo = {}
    # it is more efficient to multiple the bigger number by the smaller number
    # i.e. 5, 3 times rather than 3, 5 times
    return mult_helper(smaller, bigger, memo)

def mult_helper(multiplier, num_to_multiply, memo):
    if multiplier == 0:
        return 0 # any num * 0 equals 0
    if multiplier == 1:
        return num_to_multiply # i.e. 1 * 5 = 5
    if memo.get(multiplier):
        return memo[multiplier] # get the answer from the memo

    first_half = multiplier / 2
    second_half = multiplier - first_half

    # recurse on the first half
    first_mult = mult_helper(first_half, num_to_multiply, memo)

    if first_half != second_half: # recurse on the second half
        second_mult = mult_helper(second_half, num_to_multiply, memo)
    else: # they were the same, so same answer
        second_mult = first_mult

    memo[multiplier] = first_mult + second_mult # update memo 

    return memo[multiplier]

print multiply_memo(3, 3)