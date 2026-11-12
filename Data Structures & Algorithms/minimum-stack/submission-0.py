class MinStack:
# STACK SOLUTION - 2ND ATTEMPT 
    def __init__(self):
        # where you initialize stuff 
        # you want a second stack, minStack, where you will track the smallest number that 
        # has been added to the stack. You need the minStack for the getMin function to 
        # have a O(1) time complexity. 
        self.stack = [] 
        self.minStack = []

    def push(self, val: int) -> None:
        # Append the value to the stack and then either append the value or the number 
        # on top of the minStack, whichever is smaller, to the minStack
        # This has a O(1) time complexity
        self.stack.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)

    def pop(self) -> None:
        # To remove the value on top of the stack. You don't need to do more with the minStack
        # because when you pop an element off a stack it only pops off the number on top. 
        # This has a 0(1) time complexity
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        # This has an O(1) time complexity
        return self.stack[-1]

    def getMin(self) -> int:
        # This is not a function of stacks, therefore we needed to create a new data structure 
        # through a class to enable this function. To design this class s.t. getMin had a 
        # time complexity of O(1) we needed to create minStack so that this was a simple function
        return self.minStack[-1]



# STACK SOLUTION - 1ST ATTEMPT 
    # def __init__(self):
    #     # this is where we initialize anything we would need for the methods below 
    #     # here we just need to initialize and two empty stacks
    #     self.stack = [] # the self makes it so we are referring to the instance when we use call this method 
    #     self.minStack = [] # we want to track               
        

    # def push(self, val: int) -> None:
    #     # we can just use the same stack method, 'stack.push(val)' to add an element to the stack
    #     # we need to do this before we can know which value to add to the top of minStack
    #     self.stack.append(val)
    #     # To determine which value we append to the minStack, we either append the value or 
    #     # the last val that was appended to minStack. Whichever is lower. Since we are 
    #     # choosing the minimum of two numbers we can just use the min() function. If this is our 
    #     # first loop then minStack will be empty and we need to just add val, so to avoid an error
    #     # add logic so the min function knows which value to pick in the case that minStack is empty. 
    #     # I originally had an if...else statement with 'if self.minStack[-1] > val:' -> this will produce 
    #     # an error as written if minStack is empty. 

        

    # def pop(self) -> None:
    #     # if we pop the smallest number from the stack then our minStack top value must update.
    #     # Thankfully, we could only pop the top number, so we would need to pop the top number 
    #     # from the minStack as well. 
    #     self.stack.pop()
    #     self.minStack.pop()

    # def top(self) -> int:
    #     return self.stack[-1] # forgot the return 
        

    # def getMin(self) -> int:
    #     return self.minStack[-1] # forgot the return 
 

        # Logic before problem 
        # Recall here we want to have our normal stack that we want to add numbers to and 
        # anther stack that tracks what the lowest number in the stack is, we need this to
        # make the getMin() fuction to work. 

        # stack           minStack
        #   1                 1
        #   2                 1
        #   0                 0 
        #   3                 0   

        # Complexity 
        # Time - A stack supports push (stack.append(val)), pop (stack.pop()), and top (stack[-1]) 
        # and all of those have constanst time complexity O(1) but getMin is not a default stack 
        # method so we need to design it to have O(1) time complexity. That's why we use the 
        # minStack. Because if we just track the smallest val added to the stack then we just 
        # simply can pull the top element from the minStack and that definitely has O(1) time complexity. 
        # We could use iteration to find the smallest number in the stack array but that would take 
        # O(n) time. 
