# Cracking the Code Interview question 1.2

def reverse_c_string(string):
    """Reverses a string, including null character"""

    # not sure what null character would mean in Python, but this works if 
    # given an empty space at the end

    # can do list slicing to complete in one line
    # return string[::-1]

    # can do it in a loop as well

    results = ""

    # loop through starting at 1, ending at the length of the string +1
    # add 1 because range goes UNTIL but not including the stop number
    for char in range(1, len(string)+1):
        # grab the item at the end of the string by making it negative
        # i.e. index 1 becomes index -1
        results += string[-char]

    return results

print reverse_c_string("hellboy ")
print reverse_c_string("racecar")