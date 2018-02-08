import unittest

class Node(object):
    def __init__(self, value):
        self.value = value

class Stack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value


class SetofStacks(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [] # list to hold all the Stacks

    def get_last_stack(self):
        if not self.stacks: # check if it's empty
            return None
        return self.stacks[-1] # return last element

    def is_empty(self):
        last = self.get_last_stack()
        if last.is_empty():
            return last.is_empty()
        else:
            return not last

    def push(self, v):
        last = self.get_last_stack() # get the top stack
        if last and not last.is_full(): # push if the top stack isn't full
            last.push(v)
        else:
            stack = Stack(self.capacity) # create a new stack
            stack.push(v)
            self.stacks.append(stack) # and add to the stacks list

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None # nothing there to pop
        v = last.pop()
        if last.size == 0:
            del self.stacks[-1] # that was the last thing in the stack
        return v



