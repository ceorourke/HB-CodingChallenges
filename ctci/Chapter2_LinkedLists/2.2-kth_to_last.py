class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def kth_to_last(self, k):
        """Returns the data of the node that is k from the end,
            assuming the end starts counting at 1""" 
        slow = self
        fast = self

        for i in range(k): # move fast up k spots
            fast = fast.next

        while fast: # go until fast is at the end, then slow will be k away from the end
            slow = slow.next
            fast = fast.next
        return slow.data

head = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

head.next = two
two.next = three
three.next = four
four.next = five

print head.kth_to_last(3)