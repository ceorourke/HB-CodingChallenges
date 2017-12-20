phone = {
    '2': 'abc', '3': 'def', '4': 'ghi',
    '5': 'jkl', '6': 'mno', '7': 'pqrs',
    '8': 'tuv', '9': 'wxzy'
}

combinations = set()

def letter_combinations(digits):

    def recurse(rest_of_the_word, path_so_far):
        if not rest_of_the_word:
            combinations.add(path_so_far)
            return
        first, rest = rest_of_the_word[0], rest_of_the_word[1:]
        letters = phone[first]
        for letter in letters:
            recurse(rest_of_the_word, path_so_far + letter)

    recurse(digits, "")
    return combinations

print letter_combinations('12')
