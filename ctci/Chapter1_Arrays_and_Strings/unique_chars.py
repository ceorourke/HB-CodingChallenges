# Implement an algorithm to determine if a string has all unique characters. 
# What if you can not use additional data structures?

# first let's just use additional data structures, then optimize

def is_unique(string):
    """Determines if a string has all unique characters"""

    # loop through string, adding chars to a set as you go
    # check if the char is in the set, if it is, return False

    existing = set()

    for char in string:
        if char not in existing:
            existing.add(char)
        else:
            return False
    return True

print is_unique("noon")
# should be False
print is_unique("abcdefghijklmnopqrstuvwxyz")
# should be True

def is_unique_2(string):
    """Determines if a string has all unique characters without using additional
       data structures"""

       