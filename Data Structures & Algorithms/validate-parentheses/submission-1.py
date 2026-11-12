class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', "{": "}", "[": "]"}

        stack = []

        for char in s:
            if char in d:
                stack.append(char)
            elif stack == [] or d[stack.pop()] != char:
                return False
        
        return True if stack == [] else False  


# s = "([{}])"

# 1st loop: char = (. This is an "open" bracket so move to the if block. This is a key in the 
# dictionary d so ( is appended to the stack, so the stack becomes = ['('] and the loop starts
# again 
# 2nd loop: char = [. This is an "open" bracket so move to the if block. This ia a key in 
# the dictionary d so [ is appended to the stack and the stack becomes = ['(', '['] and the loop
# starts again 
# 3rd loop: char = {. This is an "open" bracket so move to the if block. This is a key in the
# dictionary d so { is appended to the stack and it becomes = ['(', '[', '{']
# 4th loop: char = }. This is a "closed" bracket so fails the if block and move to the else 
# block. The stack is not empty. We want to pop off the last char we added to the stack which
# is {. We find the value of { from the dictionary which is }. Then } == } and this else block
# condition fails and we move on to the next character in the loop.
# 5th loop: char = ]. This is "closed" bracket so fails the if block because it is not a key
# in the dictionary d. Move on to the else block and the stack is not empty so that fails.
# 6th loop: char = ). This is not a key in the dictionary so move to the else block. The stack 
# is not empty so that is false. If we pop off the top paretheses in the stack we get (. If we 
# use this as a key in dictonary d then the corresponding value is ). Compare the value to the 
# char so ) == ) and the else block condition is false. So we move on to the next loop. 
# 7th loop: We have reached the end of the for loop so we break out of the for loop and move on 
# to the return statement 

# The return statement will return True is the stack is empty. The stack is empty because all 
# parentheses added to it have been popped off. This means there was a matching closed
# parentheses to every closed parentheses and they were in the right order. If there were still 
# parentheses in the stack then that means there were open parentheses that were not closed. 


