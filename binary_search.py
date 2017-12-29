def binary_search(sorted_list, num):
    """Returns true or false depending on if num is in list"""

    found = False
    beginning = 0
    end = len(sorted_list) - 1

    while (beginning <= end) and not found:
        middle = (beginning + end) / 2
        if sorted_list[middle] == num:
            found = True
        elif sorted_list[middle] < num:
            beginning = middle + 1
        else:
            end = middle - 1

    return found

def binary_search_index(sorted_list, num):
    
    beginning = 0
    end = len(sorted_list) - 1

    while beginning <= end:
        middle = (beginning + end) / 2
        if sorted_list[middle] == num:
            return middle
        elif sorted_list[middle] < num:
            beginning = middle + 1
        else:
            end = middle - 1

sorted_list = [1,3,6,8,9,12,16,20]
print binary_search(sorted_list, 22) # False
print binary_search(sorted_list, 9) # True

print binary_search_index(sorted_list, 9) # 4
print binary_search_index(sorted_list, 2) # None