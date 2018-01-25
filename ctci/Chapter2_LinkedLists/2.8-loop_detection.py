class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def find_loop_beginning(head):
    """Find the beginning of a circularly linked list.
        This is what's suggested in the book."""
    
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break;

    if fast is None or fast.next is None:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

def find_beginning_alternate(head):
    """An alternate solution utilizing Python sets and their fast lookup"""

    seen = set()

    current = head

    while current:
        if current not in seen:
            seen.add(current)
        else:
            return current
        current = current.next

one = Node('a')
two = Node('b')
three = Node('c')
four = Node('d') # beginning of loop
five = Node('e')
six = Node('f')
seven = Node('g')
eight = Node('h')
nine = Node('i')
ten = Node('j')
eleven = Node('k')

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten
ten.next = eleven

answer =  find_loop_beginning(one)
print answer # should be None

alt_answer = find_beginning_alternate(one)
print alt_answer # should be None


eleven.next = four # adding a loop
print four, four.data # this is the loop beginning

answer =  find_loop_beginning(one)
print answer, answer.data # should be d

alt_answer = find_beginning_alternate(one)
print alt_answer, alt_answer.data # should be d