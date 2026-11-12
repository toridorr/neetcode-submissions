class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right: # L/M/R could all converge onto the same value if it is the target. And we will have the return function to return the index INSIDE this while loop. 
            middle = (left + right) // 2 
            middle_num = nums[middle]
            if middle_num < target: 
                left = middle + 1 
            elif middle_num > target:
                right = middle - 1
            else: # middle_num == target 
                return middle
        
        return -1


        
    #    Example: nums = [-1,0,2,4,6,8], target = 4
    #    1st loop: 
    #    [-1,0,2,4,6,8]
    #      L   M     R 
    #    left = 0, right = 5, middle = 5 // 2 = 2 (index)
    #    middle_num = 2 
    #    middle_num = 2 < target = 4 so move your search area to the right of middle
    #    left = middle + 1 = 2 + 1 = 3 
    #    2nd loop: 
    #    [-1,0,2,4,6,8]
    #            L M R
    #    left = 3, right = 5, middle = 8 // 2 = 4 (index)
    #    middle_num = 6 
    #    middle_num = 6 > target = 4 so move your search area to the left of middle 
    #    right = middle - 1 = 4 - 1 = 3 
    #    3rd loop: 
    #    [-1,0,2,4,6,8]
    #          L/M/R
    #    left = 3, right = 3, middle = 6 // 2 = 3 (index)
    #    middle_num = 4 
    #    middle_num = 4 == target = 4 so return middle = 3 
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # BINARY SEARCH SOLUTION 
        # left, right = 0, len(nums)-1

        # while left <= right: # if I didn't have = then this does not work, why?
        #     middle = int((left+right)/2) # can also do middle = (left + right) // 2 - this is floor division and will return the integer

        #     if nums[middle] == target:
        #         return middle 
        #     elif nums[middle] < target:
        #         left = middle + 1 
        #     else: # middle > target
        #         right = middle -1 

        # return -1 


        # Logic - You want to use the left and right pointers to determine a middle pointer.
        # You compare the value at the middle pointer to the target. If the value < target 
        # then you know your target lies above where your middle pointer is pointing so you 
        # move your search window, by moving the left pointer to the index to the right
        # of where the middle index is pointing. If the value at the middle index > target then
        # you know the target lies below so you need to move your search window to the left and
        # so you need to move you right pointer to the index to the left of the middle pointer. 
        # If the array does contain the target then eventually the middle pointer will point to 
        # the target. If left and right pointers meet or crossover then you know the array does 
        # not contain the target so break out of the while loop and return -1 

        # Example: nums = [-1,0,2,4,6,8], target = 4
        
        # 1st loop: left = 0, right = 5, middle = int(5/2) = 2 
        # -1 0 2 4 6 8 
        # L    M     R 
        # nums[middle] = 2, target = 4 -> 2 < 4 so the elif statement runs and left = 3 
        # 2nd loop: left = 3, right = 5, middle = int(8/2) = 4 
        # -1 0 2 4 6 8 
        #        L M R
        # nums[middle] = 6, target 4 -> 6 > 4 so the else statement runs and right = 4 
        # 3rd loop: left = 3, right = 4, middle = int(7/2) = 3 
        # -1  0  2  4  6  8 
        #          L/M R
        # nums[middle] = 4, target = 4 -> 4 == 4 so return True 
        
        
    
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # BRUTE FORCE SOLUTION
        for e in range(len(nums)):
            if nums[e] == target: 
                return e
        return -1
            
    # BINARY SEARCH SOLUTION
        left, right = 0, len(nums)-1

        while left <= right: 
            middle_index = (left + right) // 2
            middle_value = nums[middle_index]
            if target < middle_value:
                right = middle_index - 1
            elif target > middle_value:
                left = middle_index + 1
            else: # target == middle_value
                return middle_index
        
        return -1
            

# Example: nums = [-1,0,2,4,6,8], target = 4
# 1st loop: left = 0, right = len(nums) - 1 = 6 - 1 = 5, the right pointer is pointing to 
# index 5. Our search area is the entire array. 
# We jump into the while loop and the middle_index = (0 + 5) // 2 = 5 // 2 = 2 
# because you only want the integer part of this division so 5/2 = 2.5 but you only want 
# the 2 part. Remember that % would give you the remainder, so the 0.5. The 
# middle_value = nums[2] = 2. Skip the if block because 2 != 4. In the elif block, 2 < 4 
# so we know that since the nums array is sorted that in ascending order that if 4 exists 
# in the array it exists in the right half. We then will move out search area such that the 
# left index moves, left = middle_index + 1 = 2 + 1 = 3, so to index 3. We jump back to the
# top of our while loop.
# 2nd loop: left = 3 and right has not changed, so 3 < 5. Our search area is [4, 6, 8]. We can 
# continue into the while loop. The middle_index needs to be moved to the middle_index of 
# this new search area so middle_index = (left + right)//2 = (3 + 5)//2 = 8//2 = 4, so 
# index 4. And middle_value = nums[4] = 6. We skip the if block because 6 != 4. We skip the 
# elif block because 6 is not smaller than 4. So we move to the else block which is for when 
# the middle_value > target and 6 > 4. We want to make our search area even smaller and move 
# it to the left of the middle_index. So our right pointer is moved to the element to the 
# left of the middle_index, right = middle_index - 1 = 4 - 1 = 3, so index 3. We jump 
# back to the top of our while loop.
# 3rd loop: left = 3, right = 3. The middle_index = (left + right) // 2 = (3 + 3) // 2 
# = 6 // 2 = 3, so index 3 and our search area becomes [4]. We run the if block because 
# 4 = 4 and we break out of the while loop and return the middle_index which is 3. 
