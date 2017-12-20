
magazine = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec maximus iaculis porttitor. Morbi pellentesque dapibus tortor, a gravida velit finibus vitae. Donec placerat scelerisque enim quis aliquam. Vestibulum id nisi mollis, congue ex id, scelerisque erat. Cras in augue ac elit posuere dapibus non congue magna. Nulla eget rutrum turpis. Etiam id mi placerat, posuere metus ut, feugiat eros. Etiam faucibus nisi eu ipsum sollicitudin dapibus.'

# check if ransom note can be made from magazine

def ransom_note(note, magazine):
    # create dict of magazine letters as keys and counts as values
    letter_counts = {}

    # for char in magazine:
    #     letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1

    # # loop through letters in note
    # for char in note:
    # # check if in magazine dict and if count > 0 
    # if letter_counts.get(char, 0) > 0:
    #     # if so, decrement count
    #         letter_counts[char] -= 1
    #     # if not available, return False
    #     else:
    #         return False
    #     # if you get all the way through, return True
    # return True

    for char in note:
        letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1

    print letter_counts

    for char in magazine:
        char = char.lower()
        letter_val = letter_counts.get(char, 0)
        if letter_val > 0:
            letter_counts[char] -= 1
        if letter_counts.get(char) == 0:
            del letter_counts[char]
        if not letter_counts:
            return True
    return False


ransomNote1 = 'foobar' # true
ransomNote2 = 'hello world' # false

output = ransom_note(ransomNote1, magazine)
output2 = ransom_note(ransomNote2, magazine)

print output
print output2


