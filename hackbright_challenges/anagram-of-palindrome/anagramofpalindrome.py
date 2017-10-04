"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # add letters and their counts to a dictionary
    letters = {}

    for letter in word:
        if letters.get(letter, 0) == 0:
            letters[letter] = 1
        else:
            letters[letter] += 1

    count = 0
    # for an even number of characters, we want no letter counts that are
    # not evenly divisible by 2. for odd number of characters, we want ONLY one
    # letter count that is not divisible by 2. here we count that
    for letter in word:
        if letters[letter] % 2 != 0:
            count += 1

    # check if the word has an even num of chars
    if len(word) % 2 == 0:
        # we don't want ANY chars with a count not evenly divisible by 2
        if count > 0:
            return False

    # otherwise it has an odd number of chars
    else:
        # we explcitly want ONE char with a count not evenly divisible by 2
        if count > 1:
            return False

    return True

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
