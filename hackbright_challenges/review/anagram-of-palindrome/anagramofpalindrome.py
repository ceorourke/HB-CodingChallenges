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

    letters = {}
    # create a dictionary full of letters and their counts
    for letter in word:
        if letters.get(letter) is None:
            letters[letter] = 1
        else:
            letters[letter] += 1

    count = 0

    if len(word) % 2 == 0:
        # if the word is even, want all letters to have a count that's a multiple of 2
        for letter in word:
            if letters[letter] % 2 != 0:
                return False
    else:
        # the word is uneven, want ONE letter to have a count that's not a multiple of 2
        for letter in word:
            if letters[letter] % 2 != 0:
                count +=1
        if count % 2 != 0:
            return True
    return False

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
