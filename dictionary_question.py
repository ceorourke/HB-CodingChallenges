# # Sample Inputs
# # 1-800-TOYSRUS
# # 415MISSION
# # +44-omgCORGIS
 
# # Sample Outputs
# # +18008697787
# # +4156477466
# # +44664267447

def letters_to_num(astring):

    phone_nums = {"a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3, "g": 4,
                  "h": 4, "i": 4, "j": 5, "k": 5, "l": 5, "m": 6, "n": 6,
                  "o": 6, "p": 7, "r": 7, "s": 7, "t": 8, "u": 8, "v": 8,
                  "w": 9, "x": 9, "y": 9}


    output = "+"

    for char in astring:
        if char.isalpha():
            output += str(phone_nums[char.lower()])
        elif char.isdigit():
            output += str(char)

    return output

test = "1-800-TOYSRUS"
test2 = "415MISSION"
test3 = "+44-omgCORGIS"

output = letters_to_num(test)
output2 = letters_to_num(test2)
output3 = letters_to_num(test3)

print output
print output2
print output3


# loop through string
# check each letter for:
    # not being a number
        # if it's a - or +, skip
        # if it's a letter
            # check in dict for corresponding number
            # and then add that to output str
        # if it's a num, add to output str
# return output str
