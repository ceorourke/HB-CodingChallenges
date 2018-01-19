from LinkedList import LinkedList

def is_palindrome(ll):
    """Check if a linked list is a palindrome"""

    stack = []
    slow = fast = ll.head

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if len(stack) % 2 == 0:
        slow = slow.next

    while slow:
        temp = stack.pop()
        # print slow.value, temp
        if slow.value != temp:
            return False
        slow = slow.next
    return True

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
ll_true = LinkedList([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true)) # making sure it works with even lengths too
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(is_palindrome(ll_false)) # and odd ones