class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_ll(self):
        current = self
        while current:
            print current.data,
            current = current.next

    def remove_dupes(self):
        current = self
        seen = set([current.data])
        while current.next:
            if current.next.data in seen: # if we've already seen it
                current.next = current.next.next # skip over the next node
            else:
                seen.add(current.next.data) # otherwise add it to the set
                current = current.next # and keep going


one = Node(1)
two = Node(1)
three = Node(2)
four = Node(2)
five = Node(1)

one.next = two
two.next = three
three.next = four
four.next = five


print "Before (with dupes):"
one.print_ll()
one.remove_dupes()
print "\nAfter (without dupes):"
one.print_ll()