def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = {}

    for char in str1:
        counter[char] = counter.get(char, 0) + 1

    print "Original Counter"
    print counter
    print

    for char in str2:
        print counter, char
        if counter.get(char) > 0:
            counter[char] -= 1
        else:
            return False
    return True

# print anagrams("hellboy", "llboyeh") #True
print anagrams("hellboy", "lezoboi") #False