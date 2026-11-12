class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for parentheses in s:
            if parentheses in dict:
                stack.append(parentheses)
            elif stack == [] or dict[stack.pop()] != parentheses:
                return False
        
        return True if stack == [] else False 

        # Example: s = "([{}])"
        # 1st loop: parentheses = '('
        # '(' is a key in dict so add it to the stack
        # stack = ['(']
        # 2nd loop: parentheses = '['
        # '[' is a key in dict so add i to the stack 
        # stack = ['(', '[']
        # 3rd loop: parentheses = '{'
        # '{' is a key in dict so add it to the stack 
        # stack = ['(', '[', '{']
        # 4th loop: parentheses = '}'
        # '}' is closed so check elif condition, pop off the item on top of the stack which is '{'
        # dict['{'] =  '}' then '}' == '}' so this elif statement does not run and move on to 
        # next item in for loop
        # stack = ['(', '['] 
        # 5th loop: parentheses = ']'
        # ']' is closed so check elif condition
        # dict['['] = ']' and ']' == ']' which makes the condition, as written, false and 
        # we move on to the next item in the for loop 
        # stack = ['('] 
        # 6th loop: parentheses = ')'
        # ')' is closed so check elif condition, it is false because dict['('] == ')' and 
        # ')' == ')' 
        # stack = []
        # There are no more items in our input string so we exit the for loop. We return True
        # because the stack is empty. 

        # Complexity  
        # Time - O(n) because we are going through evey character in the input string 
        # Space - O(n) because we are creating new stuff like a stack and dictionary 

        























        
    
    # STACK SOLUTION - 2ND ATTEMPT     
        # dict = {'(':')', '{':'}', '[':']'}
        # stack = [] 

        # for char in s: 
        #     # if char is an "open" parentheses then add it to the stack
        #     if char in dict: 
        #         stack.append(char) 
        #     # if p is closed, the pop from the stack and use the parentheses 
        #     # you popped as a key in the dictionary. Use it to find the corresponding value
        #     # If the corresponding value is the same as 'char' then you are good to continue
        #     # If they are not equivalent, then this is not value and return False. 
        #     elif stack == [] or dict[stack.pop()] != char: # you need stack == [] in the 
        #         # case where your first character in the stack is "closed", then you 
        #         # automatically know to return False because it should be preceeded by 
        #         # an "open" matching parentheses
        #         return False  

        # return True if len(stack) == 0 else False   # could have also used 'stack == []' here    

        # s = "([{}])"
        # 1st loop: p = '('
        # p is a key in the dictionary so it is "open" so add it to the stack 
        # stack = ['(']
        # 2nd loop: p = '['
        # p is a key in the dictionary so it is "open" so add it to the stack
        # stack = ['(', '[']
        # 3rd loop: p = '{'
        # p is a key in the dictionary so it is "open" so add it to the stack
        # stack = ['(', '[', '{']
        # 4th loop: p = '}'
        # p is not a key in the dictionary. So let's pop off the top item of the stack, 
        # stack.pop() returns '{'. Then we use the dictionary to find the corresponding 
        # parentheses to what we popped off. p_dict['{'] returns '}'. And '}' equals 
        # p which is '}'. 
        # stack = ['(', '['] 
        # 5th loop: p = ']'
        # p is not a key in the dictionary. If we pop off the item on top of the stack, 
        # stack.pop() returns '['. Let's use this key to get it's corresponding value, 
        # p_dict['['] returns ']'. Let's compare the value to p. ']' == ']' so we can 
        # continue on. 
        # stack = ['('] 
        # 6th loop: p = ')'
        # p is not a key in the dictionary. If we pop off the item on top of the stack, 
        # stack.pop() return '('. Let's use this key to get it's corresponding value,
        # p_dict['('] returns ')'. Let's compare the value to p. ')' == ')'.  
        # End of loop:
        # we have gone through each character in s so end the for loop. Then the next line
        # states to return True if the stack is empty. This indicates that every open parentheses
        # was closed in the correct order. 



        # p is NOT a key in the dictionary. To ensure things that this "closed" parentheses
        # matches the last "open" parentheses added to the stack, we need to pop off the
        # last item added to the stack and compare to p. if they are the same then we can 
        # continue on. If they are not the same then return False. 



            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # STACK SOLUTION
        # d = {'(': ')', "{": "}", "[": "]"}

        # stack = []

        # for char in s:
        #     if char in d:
        #         stack.append(char)
        #     elif stack == [] or d[stack.pop()] != char:
        #         return False
        
        # return True if stack == [] else False  


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

        # The return statement will return True if the stack is empty. The stack is empty because all 
        # parentheses added to it have been popped off. This means there was a matching closed
        # parentheses to every closed parentheses and they were in the right order. If there were still 
        # parentheses in the stack then that means there were open parentheses that were not closed. 


