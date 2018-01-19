class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_ll(self):
        current = self
        while current:
            print current.data,
            current = current.next

    def delete_middle_node(self):
        # copy next node
        self.data = self.next.data
        # delete next node
        self.next = self.next.next


head = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

head.next = two
two.next = three
three.next = four
four.next = five

print "Before (with middle node):"
head.print_ll()
three.delete_middle_node()
print "\nAfter (without middle node):"
head.print_ll()