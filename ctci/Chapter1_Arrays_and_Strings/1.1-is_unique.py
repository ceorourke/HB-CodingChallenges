def is_unique(string):
    """Determine if a string has all unique characters"""

    seen = set()

    for char in string:
        if char not in seen:
            seen.add(char)
        else:
            return False 
    return True

string = "abcdefghijklmnopqrstuvwxyz"
string2 = "abbbbc"

print is_unique(string) # true
print is_unique(string2) # false