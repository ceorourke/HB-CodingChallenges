#given a linked list, figure out if it's a palindrome

#first, want to find the midpoint of the linked list
#use runners, slow and fast
#slow one moves one step, fast one moves 2 steps
#if fast is at None, slow is at the midpoint and the list is even
#if fast.next is None, slow is at the midpoint and the list is odd

#also need to see if the letters match
#as you step through, keep a list of letters until the midpoint
#then after midpoint, compare last item in list to node.data, if it matches, pop
# this works if it's even
#if the word is odd, pop off the last letter before comparing the last item
#in the list to node.data


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_palindrome(self):
        """given a linked list, determine if the word is a palindrome"""

        letters = []
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            letters.append(slow.data)
            slow = slow.next
            fast = fast.next.next  

        if fast is not None:
            # odd number of characters
            slow = slow.next
            # even number of characters
        while slow is not None:
            if slow.data == letters[-1]:
                slow = slow.next
                letters.pop(-1)
            else:
                return False
        return True

r = Node("r")
a = Node("a")
r2 = Node("r")
palindrome = LinkedList()
r.next = a
a.next = r2
palindrome.head = r

print palindrome.is_palindrome()

# good follow up questions: 
# given a ll, find the node that is k-th from the end of the list
# send out fast one k ahead, one fast reaches the end, slow is k
# keep a counter, every time through the while loop, move runner one more space
# keep track of how many spaces you've moved, stop once it reaches k

# cycle detection: can use a runner to find out if a linked list loops back over itself
# if the slow runner and fast runner are ever equal to the same node, there is a cycle
# in this case, fast would move twice as fast as slow

################################################################################
# solution given 
    # def is_palindrome_2(head):
    #     """Return True if ll is palindrome, False if not"""

    #     # set the slow and fast runners to be the head of the ll
    #     slow = head
    #     fast = head

    #     # create a stack to keep track of the letters in the first half of the ll
    #     stack = []

    #     # move the runners so that slow gets to the middle of the ll
    #     while fast is not None and fast.next is not None:
    #         stack.append(slow.data)
    #         slow = slow.next
    #         fast = fast.next.next

    #     # account for odd number of elements and skip the middle element if so
    #     if fast is not None:
    #         slow = slow.next

    #     # compare each letter in the second half of the list to the letters in the first half
    #     while slow is not None:
    #         if slow.data != stack.pop():
    #             return False
    #         slow = slow.next
    #     return True



