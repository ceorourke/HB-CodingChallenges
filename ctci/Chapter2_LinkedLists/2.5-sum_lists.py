# class Node(object):
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

#     def print_ll(self):
#         current = self
#         while current:
#             print current.data,
#             current = current.next

from LinkedList import LinkedList

# def sum_lists(head1, head2):
#     new_head = LinkedList()
#     carry = 0
#     while head1 or head2:
#         result = carry
#         if head1:
#             result += head1.value
#             head1 = head1.next
#         if head2:
#             result += head2.value
#             head2 = head2.next
#         new_head.add(result % 10)
#         carry = result / 10

#     if carry:
#         new_head.next = Node(carry)
#     return new_head

def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll

ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))

# head1 = Node(7)
# two = Node(1)
# three = Node(6)

# head1.next = two
# two.next = three

# head2 = Node(5)
# four = Node(9)
# five = Node(2)

# head2.next = four
# four.next = five

# head1.print_ll()
# print '\n'
# head2.print_ll()
# print '\n'
# temp = head1.sum_lists(head1, head2)
# temp.print_ll()

# ll1 is 7 >> 1 >> 6 (617)
# ll2 is 5 >> 9 >> 2 (295)
# sum is 2 >> 1 >> 9 (912)