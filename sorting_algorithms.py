"""Cementing my knowledge of searching algorithms"""

def bubble_sort(unsorted_list):
    """Simple, O(n^2) sorting algorithm"""

    more_swaps = True

    while more_swaps:
        more_swaps = False
        for i in range(len(unsorted_list) -1):
            if unsorted_list[i] > unsorted_list[i+1]:
                # temp = unsorted_list[i]
                # unsorted_list[i] = unsorted_list[i+1]
                # unsorted_list[i+1] = temp
                # line below does the same as 3 above
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                more_swaps = True
    return unsorted_list

def insertion_sort(unsorted_list):
    """Another O(n^2) sorting algorithm"""
    
    for index in range(1, len(unsorted_list)): # starting at 1, loop over the list
        current_value = unsorted_list[index] # store the current value
        while index > 0 and unsorted_list[index - 1] > current_value:
        # ^^^ while we're still in the confines of the list
        # ^^^ and the value of the list to the left of the index is bigger than
        # ^^^ the current value, loop
            unsorted_list[index] = unsorted_list[index - 1] # swap
            index -= 1 # decrement index, keep going "left"

        unsorted_list[index] = current_value # put current value in correct place
    return unsorted_list


def selection_sort(unsorted_list):
    """Another O(n^2) sorting algorithm"""

    for i in range(len(unsorted_list)):
        least = i
        for k in range(i + 1, len(unsorted_list)):
            if unsorted_list[k] < unsorted_list[least]:
                least = k
 
        unsorted_list[least], unsorted_list[i] = unsorted_list[i], unsorted_list[least]

    return unsorted_list


def merge_sort(unsorted_list):
    """A cool recursive O(n log n) sorting algorithm"""
    
    if len(unsorted_list) < 2:
        return unsorted_list

    mid = int(len(unsorted_list) / 2)
    lst1 = merge_sort(unsorted_list[:mid])
    lst2 = merge_sort(unsorted_list[mid:])

    return make_merge(lst1, lst2)

def make_merge(lst1, lst2):
    result_list = []
    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))
        else:
            result_list.append(lst2.pop(0))

    return result_list

def quick_sort(unsorted_list):
    """Another O(n log n) sorting algorithm"""
    
    if len(unsorted_list) < 2:
        return unsorted_list

    mid = int(len(unsorted_list) / 2)
    pivot = unsorted_list[mid]

    lo, hi, eq = [], [] ,[]
    for elem in unsorted_list:
        if elem < pivot:
            lo.append(elem)
        elif elem == pivot:
            eq.append(elem)
        else:
            hi.append(elem)
    return quick_sort(lo) + eq + quick_sort(hi)


unsorted_list = [4,7,2,3,8,1,5,6]
print "Unsorted List: "
print unsorted_list
print "Bubble Sort: "
print bubble_sort(unsorted_list)
print "Insertion Sort:"
print insertion_sort(unsorted_list)
print "Selection Sort: "
print selection_sort(unsorted_list)
print "Merge Sort: "
print merge_sort(unsorted_list)
print "Quick Sort: "
print quick_sort(unsorted_list)