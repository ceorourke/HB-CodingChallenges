def compress_string(string):
    """Compress string using char counts"""

    result = ''
    count = 0
    for i in range(len(string)):
        count += 1 # increment if string[i] == string[i+1]
        if (i+1 >= len(string)) or (string[i] != string[i+1]):
            result += '' + string[i] + str(count)
            count = 0

    if len(string) > result:
        return string
    return result


print compress_string('aabcccccaaa') # 'a2b1c5a3'