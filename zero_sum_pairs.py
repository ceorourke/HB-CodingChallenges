def zero_sum_pairs(numbers):
    """O(n log n) solution""" 

    numbers = sorted(numbers)
    left = 0
    right = len(numbers)-1
    pairs = []
    while left < right:
        result = numbers[left] + numbers[right]
        if result == 0:
            pairs.append([numbers[left], numbers[right]])
            left += 1
        elif result < 0:
            left += 1
        else:
            right -= 1
    return pairs

def zero_sum_pairs2(numbers):
    """A O(n) solution"""

    seen = set()
    result = []
    target = 0
    for num in numbers:
        if (target - num) not in seen:
            seen.add(num)
        else:
            result.append([(target   - num), num])
    return result


numbers = [1,3,-1,1,1,0, 2, -2, -3]
print zero_sum_pairs(numbers)
print zero_sum_pairs2(numbers)
