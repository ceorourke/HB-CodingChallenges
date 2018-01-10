def check_permutation(string1, string2):
    """Decide if one string is a permutation of the other.
    This solution simply sorts the characters and compares"""

    if sorted([s for s in string1]) == sorted(s for s in string2):
        return True
    return False


print check_permutation("pop", "aaa")
print check_permutation("cupper", "pucper") 


def check_permutation2(string1, string2):
    """Decide if one string is a permutation of the other.
        This solution counts characters of string1 and compares 
        against the counts in string2"""

    if len(string1) != len(string2):
        return False

    counts = {}

    for char in string1:
        counts[char] = counts.get(char, 0) + 1

    for char in string2:
        if counts.get(char, 0) <= 0:
            return False
    return True

print check_permutation2("pop", "aaa")
print check_permutation2("cupper", "pucper")