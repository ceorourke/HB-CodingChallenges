def palindrome_permutation(string):
    """Check if string is a permutation of a palindrome"""

    counts = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1

    char_counts = 0

    for char in counts:
        if counts[char] % 2 == 1:
            char_counts += 1
        if char_counts > 1:
            return False
    return True

print palindrome_permutation("tactcoa")
print palindrome_permutation('sdgkshgskldhfj')