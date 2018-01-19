class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_ll(self, head):
        current = head
        while current:
            print current.data,
            current = current.next

    def partition(self, x):
        current = tail = head = self

        while current:
            next = current.next
            current.next = None
            if current.data < x:
                # insert node at head
                current.next = head
                head = current
            else:
                # insert node at tail
                tail.next = current
                tail = current
            current = next
        if tail.next:
            tail.next = None

        return head

one = Node(3)
two = Node(5)
three = Node(8)
four = Node(5)
five = Node(10)
six = Node(2)
seven = Node(1)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven

one.print_ll(one)
print '\n'
head = one.partition(four)
one.print_ll(head)