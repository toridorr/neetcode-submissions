class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # BRUTE FORCE SOLUTION: 
        # # You are going to create an empty string and use the loop to ONLY add 
        # # letters and numbers. This method then removes all special characters such as 
        # # question marks and blanks 
        # cleaned = ""
        # for char in s:
        #     if char.isalnum(): # this will run if the loop encounters a letter or digit and will skip if it encounters a special character 
        #         cleaned += char.lower() # I can make the character lowercase and add it at the same time. Creates "wasitacaroracatisaw"
        # return cleaned == cleaned[::-1]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # TWO POINTERS SOLUTIONS
        # the length of the string in example 1 is 28 but since python is 0 index then we want the right pointer to start at index 27, and that will point at the question mark
        left, right = 0, len(s)-1
        
        while left < right: # if left crosses over right then we have a palindrome 
            # Before we jump into comparing, we need to write code to skill over anything that is not alphnumerical
            while left < right and not s[left].isalnum(): # here I had left.isalnum() which would evaluate the index, not the value. So needed to change it to s[left].isalnum(). Also has "and is not". 
                left += 1
            while right > left and not s[right].isalnum(): # same as above
                right -= 1
            # Now we can compare 
            while s[left].lower() != s[right].lower(): # Again just needed to evaluate the value, not the index. So instead of left.lower() needed s[left].lower()
                return False

            left += 1 
            right -= 1 

        return True 

# "Was it a car or a cat I saw?"
#              R L

# 1ST LOOP: L -> W, R -> ? 
# left index = 0, right index = 27 => satisfies condition that left < right and can enter in to the 
# while loop. The left.isalnum() would evaluate to TRUE because the left pointer points to W but we only 
# want the loop to run if it is not alphnumeric so we put the "is not" in front of it. So then it would 
# become FASLE. This is like saying "only run this if this character is not alphanumeric". That first if 
# block condition is false so would move onto the second if block. The right > left -> TRUE and 
# is not alphanumeric so the condition is TRUE so it would move over 1 space. So the right pointer becomes 
# R -> w. Now we can go into the while loop and compare letters. 
# Compare W to w but we use the .lower() method so ensures we are comparing lowercase letters. And 
# w == w and this is false so it would not run this while loop and then would start the loop over again. 

# 9TH LOOP: L -> r, R -> r 
# left index = 11, right index = 14  => satisfies condition that left < right and we can enter into the while loop. 
# Both the if conditions are false so we skip those and then the while loop condition is also false so we start the 
# while loop again 

# 10TH LOOP: L -> space, R -> o 
# left index = 12, right index = 13 => satisfies condition that left < right and we can enter into the while loop. 
# In the first if loop, the left < right -> TRUE and the "is not alphanumeric" is TRUE so the if statement runs and 
# increments the left pointer 1 space up. So the left pointer moves to "o". R points to a letter so the second if 
# statement does not run. Then we can compare. left == right so that while loop does not run. The left and right pointers
# are incremented 1 space. 

# 11TH LOOP: L -> r, R -> blank space 
# left index = 13, right index = 12 => does NOT satisfy the while loop condition so breaks out of the while loop 
# and returns TRUE 




