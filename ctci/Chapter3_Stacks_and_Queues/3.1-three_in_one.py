class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3 # three mini stacks in the overall stack
        self.array = [0] * (stacksize * self.numstacks)
        # ^^ this makes an array that's [0,0,0,0,0,0]
        # if stacksize is 2 and numstacks is 3
        self.sizes = [0] * self.numstacks # [0,0,0] keep track of the size of each stack
        self.stacksize = stacksize

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1 # track size increase
        self.array[self.IndexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1 # decrease size
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        # print stacknum, self.stacksize
        # print offset
        # print "offset ^ "
        # print offset + self.sizes[stacknum] - 1
        # print " ^ index of top return statement"
        return offset + self.sizes[stacknum] - 1 # -1

def ThreeInOne():
    newstack = MultiStack(2) # make a multistack of size 2
    print newstack.array
    # print newstack.isEmpty(1)
    newstack.push(3, 1) # push 3 onto stack #1
    print newstack.array
    # print newstack.peek(1) # peek at stack #1
    # print newstack.isEmpty(1) # is stack #1 empty?
    # newstack.push(2, 1) #push 2 onto stack #1
    # print newstack.peek(1)
    # print newstack.isFull(1)
    # print newstack.pop(1)
    # print newstack.peek(1)
    # newstack.push(3, 0)
    # print newstack.peek(0)

ThreeInOne()