def linear_sum(A, n):
    """Returns the sum of n elements in the array A"""
    
    if n == 1:
        return A[0]
    return linear_sum(A, n-1) + A[n-1]

nums = [13,14,15,16,17]
n =  2
print linear_sum(nums, n)