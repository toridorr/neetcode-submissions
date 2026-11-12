class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right: 
            if numbers[left] + numbers[right] < target:
                left += 1 
            elif numbers[left] + numbers[right] > target:
                right -= 1 
            else: # numbers[left] + numbers[right] == target
                return [left + 1, right + 1]
        

        # Example: numbers = [1, 3, 4, 6, 8, 11, 15], target = 10 
        # 1st loop: left = index 0, right = index 6 
        # numbers[0] + numbers[6] = 1 + 15 = 16 > target -> decrement right pointer  
        # right = index 5 
        # 2nd loop: left = index 0, right = index 5 
        # numbers[0] + numbers[5] = 1 + 11 = 12 > target -> decrement right pointer  
        # right = index 4 
        # 3rd loop: left = index 0, right = index 4 
        # numbers[0] + numbers[4] = 1 + 8 = 9 < target -> incrememnt left pointer  
        # left = index 1 
        # 4th loop: left = index 1, right = index 4 
        # numbers[1] + numbers[4] = 3 + 8 = 11 > target -> decrement right pointer 
        # right = index 3 
        # 5th loop: left = index 1, right = index 3 
        # numbers[1] + numbers[3] = 3 + 6 = 9 < target -> increment left pointer 
        # left = index 2 
        # 6th loop: left = index 2, right = index 3 
        # numbers[2] + numbers[3] = 4 + 6 = 10 == target -> return [3, 4] 

        # Complexities 
        # Time: O(n) because we are traversing the entire array 
        # Space: O(1) because we are just reassiging variables but not creating anything new  
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    # TWO POINTES - REVIEW #1     
        
        # left, right = 0, len(numbers) - 1 

        # while left < right: # they can't equal each other 
        #     left_value = numbers[left]
        #     right_value = numbers[right]
        #     if left_value + right_value < target: 
        #         left += 1 
        #     elif left_value + right_value > target:
        #         right -= 1 
        #     else: # left + right == target 
        #         return [left + 1, right + 1]
    

        # Example: [4, 5, 6, 7, 9, 13], target = 12 
        # 1st loop: left = 0, right = 5
        # left_value = numbers[0] = 4 
        # right_value = numbers[5] = 13 
        # left_value + right_value = 4 + 13 = 17
        # 17 > 12 --> move the RIGHT pointer over, 
        # right = 4 
        # 2nd loop: left = 0, right = 4 
        # left_value = 4
        # right_value = 9 
        # 4 + 9 = 13 
        # 13 > 12 --> move the RIGHT pointer over, 
        # right = 3 
        # 3rd loop: left = 0, right = 3 
        # left_value = 4
        # right_value = 7 
        # 4 + 7 = 11 
        # 11 < 12 --> move the LEFT pointer over, 
        # left = 1 
        # 4th loop: left = 1, right = 3 
        # left_value = 5 
        # right_value = 7  
        # 5 + 7 = 12 --> return [2, 4]





    # TWO POINTERS SOLUTION - 2nd attempt

        # left, right = 0, len(numbers) - 1 

        # while left < right: # typical for two pointers problems
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1 # move the right pointer to the left 
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1 # move the left pointer to the right
        #     elif numbers[left] + numbers[right] == target:
        #         return [left+1, right+1]



        # Example (I made up): [3, 5, 7, 8, 10], target = 17
        # Initialize: left = index 0, right = len(numbers) - 1 = 5 - 1 = 4 = index 4 
        # 1st loop: left = index 0, right = index 4 
        #     0 < 4 -> enter while loop -> numbers[0] = 3, numbers[4] = 10 and 3 + 10 = 13 < target
        #     if statement is false and doesn't run. 
        #     1st elif statement is true so runs and moves the left pointer to the right, left = 1 
        # 2nd loop: left = index 1, right = index 4 
        #     1 < 4 -> while loop can continue -> numbers[1] = 5, numbers[4] = 10 and 5 + 10 = 15 < target 
        #     if statement is false and doesn't run 
        #     1st elif statement is true so runs and moves the left pointer to the right, left = 2 
        # 3rd loop: left = index 2, right = index 4 
        #     2 < 4 -> while loop can continue -> numbers[2] = 7, numbers[4] = 10 and 7 + 10 == target
        #     if statement is false and doesn't run 
        #     1st elif statement is false and doesn't run 
        #     2nd elif statement is true and runs and returns [left+1, right+1] = [2+1, 4+1] = [3, 5]


        # The logic before I started the problem 
        # numbers = [1,2,3,4], target = 3
        #            L.    R
        #            1 + 4 = 5 > 3 -> since you want it to be lower than you move 
        #            your right pointer over 1 

        #            1 2 3 4 
        #            L   R
        #            1 + 3 = 4 > 3 -> still bigger than the target so move the right 
        #            pointer over 1 

        #            1 2 3 4 
        #            L R 
        #            1 + 2 = 3 == target! return [0+1, 1+1]


        # Complexities 
        # Time - O(n) 
        # Space - we aren't creating anything new so constant time O(1)


    # TWO POINTERS SOLUTION - 1st attempt

#         left, right = 0, len(numbers) - 1

#         while left < right: 
#             if numbers[left] + numbers[right] > target:
#                 right -= 1 
#             elif numbers[left] + numbers[right] < target:
#                 left += 1 
#             else:
#                 return [left+1, right+1]

# Example: numbers = [1,2,3,4], target = 3
# 1st loop: left = 0, right = 3
# number[left] = 1, number[right] = 4 --> 1 + 4 = 5 > target --> right -= 1 --> right = 2 
# 2nd loop: left = 0, right = 2 
# number[left] = 1, number[right] = 3 --> 1 + 3 = 4 > target --> right -= 1 --> right = 1 
# 3rd loop: left = 0, right = 1 
# number[left] = 1, number[right] = 2 --> 1 + 2 = 3 == target --> return [left+1, right+1]
# --> return [1, 2]

        