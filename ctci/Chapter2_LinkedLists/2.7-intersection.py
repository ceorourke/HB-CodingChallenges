class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def find_intersection(ll_1, ll_2):
    """Find the intersection of 2 singly linked lists"""

    # get lengths of both linked lists
    one_ll = ll_1
    two_ll = ll_2
    one_ll_length = two_ll_length = 0
    while one_ll:
        one_ll_length += 1
        one_ll = one_ll.next
    while two_ll:
        two_ll_length += 1
        two_ll = two_ll.next

    # reset pointers to the beginning of each ll
    one_ll, two_ll = ll_1, ll_2
    # find out which list is smaller and bigger
    steps = abs(one_ll_length - two_ll_length)
    bigger = smaller = None
    if one_ll_length > two_ll_length:
        bigger = one_ll
        smaller = two_ll
    else:
        bigger = two_ll
        smaller = one_ll
    # move forward the bigger one to meet the smaller one
    for i in range(steps):
        bigger = bigger.next
    # compare evenly
    while bigger and smaller:
        if bigger is smaller:
            return bigger # we've found the intersection
        bigger = bigger.next
        smaller = smaller.next

one = Node('a')
two = Node('b')
three = Node('c')
four = Node('d')
five = Node('e')
six = Node('f')
seven = Node('g')
eight = Node('h')
nine = Node('i')

one.next = two
two.next = three
three.next = eight # intersection
eight.next = nine

#        'a' -> 'b' -> 'c' \
#                            'h' -> 'i' -> None
# 'd' -> 'e' -> 'f' -> 'g' /

four.next = five
five.next = six
six.next = seven
seven.next = eight


print eight # this is where they intersect
print find_intersection(one, four)