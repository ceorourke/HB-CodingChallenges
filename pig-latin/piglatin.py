"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    # my solution

    vowels = ('a', 'e', 'i', 'o', 'u')
    new_phrase = []
    new_word = ""

    for word in phrase.split():
        if word[0] in vowels:
            new_word += word + "yay"
            new_phrase.append(new_word)
        else:
            new_word += word[1:] + word[0] + "ay"
            new_phrase.append(new_word)
        new_word = ""

    return " ".join(new_phrase)


# provided solution

# def pig_latin_word(word):
#     """Turn a word into the pig latin version.

#     For example::

#         >>> pig_latin_word('porcupine')
#         'orcupinepay'

#         >>> pig_latin_word('apple')
#         'appleyay'
#     """

#     if word[0] in 'aeiou':
#         return word + 'yay'

#     else:
#         return word[1:] + word[0] + 'ay'

# def pig_latin(phrase):
#     """Turn a phrase into pig latin.

#     There will be no uppercase letters or punctuation in the phrase.

#         >>> pig_latin('hello awesome programmer')
#         'ellohay awesomeyay rogrammerpay'
#     """

#     # START SOLUTION

#     words = phrase.split(' ')

#     pl_words = [pig_latin_word(w) for w in words]
#     print pl_words

#     return " ".join(pl_words)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
