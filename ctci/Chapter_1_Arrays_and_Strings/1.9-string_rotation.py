def rotate_string(s1, s2):
    """Check if s2 is a rotation of s1"""

    if len(s1) == len(s2):  # check if they're the same length first

        s2s2 = s2+s2 # erbottlewaterbottlewat << is 'waterbottle' in there?

        if s2s2.find(s1) != -1: # -1 means not found 
            return True
    return False # not found or not same length

print rotate_string('waterbottle', 'erbottlewat')
print rotate_string('hellboy', 'colleen')