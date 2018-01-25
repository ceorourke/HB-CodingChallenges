def one_away(s1, s2):
    """Check if the two strings are one edit away from each other"""

    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s1, s2)
    return False

def one_edit_replace(s1, s2):
    """Check if there is only one difference"""

    found_difference = False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False # this is the 2nd difference!
            found_difference = True # flag that we found a difference
    return True

def one_edit_insert(s1, s2):
    """Check if you can insert a char into s1 to make s2"""

    index1 = 0
    index2 = 0

    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index2 += 1
            index1 += 1

    return True


print one_away('pale', 'bale') #true
print one_away('pae', 'pale') # true
print one_away('pale', 'bae') #false