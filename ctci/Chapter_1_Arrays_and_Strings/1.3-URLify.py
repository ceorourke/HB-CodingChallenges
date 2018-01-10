def urlify(string):
    """Replace all spaces in a string with '%20'"""

    return string.replace(' ', '%20')

print urlify('Mr John Smith') # 'Mr%20John%20Smith%20'

def urlify2(string):
    """Replace all spaces in a string with '%20' without
       using built in methods"""

    result = ''

    for char in string:
        if char == ' ':
            result += '%20'
        else:
            result += char

    return result

print urlify2('Mr John Smith') # 'Mr%20John%20Smith%20'