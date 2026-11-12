class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
# SET SOLUTION - 2ND ATTEMPT
    # You want to use a set here to track the numbers you have seen. If you encounter 
    # a number you have already seen then return True. If you make it through the entire 
    # array then there were no duplicates and return False. 

    # [1, 2, 3, 3]

    # # In the brute force solution you would just use a nested for loop to set a number as i 
    # and compare it to every number after it, so this has a O(n^2) time complexity. With a set
    # you are only going through the array 1x so it has a 0(1) time complexity but the set 
    # solution does have a higher space complexity because you are creating a new set that 
    # has the possibility of having length = n. 

    # You have an empty set = []
    # 1st loop: Is '1' in the set? the set is empty so no then add it to the set 
    # 2nd loop: is '2' in the set? No so add it to the set 
    # 3rd loop: is '3' in the set? No so add it to the set 
    # 4th loop: is '3' in the set? Yes! so return True 

        seen = []

        for num in nums: # we can use this becasue we don't care about the indices 
            if num in seen:
                return True 
            seen.append(num)
        return False 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # BRUTE FORCE: ITERATION - DONE 2X 
        
        # for i in range(len(nums)): # generates [0,1,2,3]
        #     for j in range(i+1, len(nums)): # range(1, 4) will generate [1,2,3]
        #         if nums[i] == nums[j]:
        #             return True
        # return False 
        
        # do a nested for loop where you compare a number to each number after it. 
        # If no match is found then move to the next number and compare to each number after it
        # Example 1:
        # 1 ?= 1      2 ?= 3      3 ?= 3 
        # 1 ?= 2      2 ?= 3
        # 1 ?= 3
        # 1 ?= 3  

        # Example 1:
        # 1st loop: i = index 0, j = index 1 -> nums[0] = 1, nums[1] = 2 and 1 != 2 -> move to next nested for loop
        # 2nd loop: i = index 0, j = index 2 -> nums[0] = 1, nums[2] = 3 and 2 != 3 -> move to next nested for loop
        # 3rd loop: i = index 0, j = index 3 -> nums[0] = 1, nums[3] = 3 and 1 != 3 -> end of array 
        # Move to next number 
        # 4th loop: i = index 1, j = index 2 -> nums[1] = 2, nums[2] = 3 and 2 != 3 -> move to next nested for loop
        # 5th loop: i = index 1, j = index 3 -> nums[1] = 2, nums[3] = 3 and 2 != 3 -> end of array 
        # Move to next number
        # 6th loop: i = index 2, j = index 3 -> nums[2] = 3, nums[3] = 3 and 3 == 3 -> return True 
        

    # SORTING METHOD - DONE 3X
    
        # sorted_nums = sorted(nums) # it is key throughout the code below that I use this array, not nums
        # for i in range(len(sorted_nums)-1): # range(3) generates [0,1,2], we want to subtract 1 b/c we want i to go to the second to last element in the array, and nums[i+1] may go to the last element in the array
        #     if sorted_nums[i] == sorted_nums[i+1]:
        #         return True
        # return False 
        
        # If we sort the array then we don't need to do a nested for loop and we can just 
        # compare an element to the element next to it 
        # Example 1:
        # 1 vs 2 
        # 2 vs 3 
        # 3 vs 3 


        # Example 2:
        # 1st loop: i = index 0 -> sorted_nums[0] = 1, sorted_nums[1] = 2 and 1 != 2 -> move to next number in the array 
        # 2nd loop: i = index 1 -> sorted_nums[1] = 2, sorted_nums[2] = 3 and 2 != 3 -> move to next number in the array 
        # 3rd loop: i = index 2 -> sorted_nums[2] = 3, sorted_nums[3] = 4 and 3 != 4 -> end of range, 
        # no matches found, so end for loop and move to next line of code that instructs to return False   



    # SET SOLUTION - DONE 1X 
        
        # seen = set()
        # for num in nums: # we don't need the indices so this just generates the nums array 
        #     if num in seen:
        #         return True
        #     else:
        #         seen.add(num)
        # return False
    
        # Due to the characteristics of a set (unordered, unchangeable, and does not contain 
        # duplicates) we can use a set to determine if we encounter a duplicate b/c we can
        # use the set to track the numbers we have seen. If we encounter a new number, we 
        # add it to the set because now it has been seen. If we enounter a number we have 
        # already seen then it is a duplicate and we can return True.  

        # Example 1:
        # 1st loop: num = 1
        # new_set = () so empty so does not contain 1 so will add it to the set
        # new_set = (1)
        # 2nd loop: num = 2
        # new_set = (1) and does not contain 2 so will add it to the set 
        # new_set = (1,2)
        # 3rd loop: num = 3 
        # new_set = (1,2) and does not contain 3 so will add to the set 
        # new_set = (1,2,3)
        # 4th loop: num = 3 
        # new_set = (1,2,3) and already contains 3 so run the if statement and return True 
        

    # 1 LINE SET SOLUTION - DONE 1X 
        # nums_set = set(nums)
        # return False if len(nums) == len(nums_set) else True    

        # Since a set cannot contain duplicates, we can create a new set from the nums array. 
        # This set will remove any duplicates that existed in the nums array. If the nums array
        # did contain duplicates, it will be smaller in length. If we compare the length of the 
        # set to the length of the nums array and it is the same then there are not any duplicates
        # and we return False. If the length of the set is smaller than the nums array then there were duplicates and
        # we return True.     
      
    # Complexities
            # Time
                # Brute Force: Iteration: O(n^2) b/c nested for loop
                # Sorting: O(nlog(n)) b/c that's the time complexity for sorting, O(nlog(n)) <  (n^2) 
                # Set: O(n) b/c using a for loop, O(n) < O(nlog(n)) <  (n^2)
            # Space
                # Brute Force: Iteration: O(1) b/c you aren't creating anything new
                # Sorting: O(n) or O(1) depending on the sorting algorithm b/c you create a sorted array that contains all elements in the nums array
                # Set: O(n) b/c you create a set that may contain all elements in the nums array 

        