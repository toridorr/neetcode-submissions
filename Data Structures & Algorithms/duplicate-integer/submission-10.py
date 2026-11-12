class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # SET SOLUTION - #1 
        new_set = set()
        for num in nums: # we don't need the indices so this just generates the nums array 
            if num in new_set:
                return True
            else:
                new_set.add(num)
        return False
    

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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # BRUTE FORCE: ITERATION
        
        # do a nested for loop where you compare a number to each number after it. 
        # If no match is found then move to the next number and compare to each number after it
        # Example 1: 
        # 1 vs 1, 1 vs 2, 1 vs 3, 1 vs 3 
        # 2 vs 3, 2 vs 3 
        # 3 vs 3 
        
        # for i in range(len(nums)): # generates [0,1,2,3]
        #     for j in range(i+1, len(nums)): # range(1, 4) will generate [1,2,3]
        #         if nums[i] == nums[j]:
        #             return True
        # return False 

        # Example 1:
        # 1st loop: i = index 0, j = index 1 -> nums[0] = 1, nums[1] = 2 and 1 != 2 -> move to next nested for loop
        # 2nd loop: i = index 0, j = index 2 -> nums[0] = 1, nums[2] = 3 and 2 != 3 -> move to next nested for loop
        # 3rd loop: i = index 0, j = index 3 -> nums[0] = 1, nums[3] = 3 and 1 != 3 -> end of array 
        # Move to next number 
        # 4th loop: i = index 1, j = index 2 -> nums[1] = 2, nums[2] = 3 and 2 != 3 -> move to next nested for loop
        # 5th loop: i = index 1, j = index 3 -> nums[1] = 2, nums[3] = 3 and 2 != 3 -> end of array 
        # Move to next number
        # 6th loop: i = index 2, j = index 3 -> nums[2] = 3, nums[3] = 3 and 3 == 3 -> return True 

        # # SORTING METHOD
        # sorted_nums = sorted(nums)

        # 1 vs 2 
        # 2 vs 3 
        # 3 vs 3 

        # for i in range(len(sorted_nums)-1): # range(3) generates [0,1,2]
        #     if sorted_nums[i] == sorted_nums[i+1]:
        #         return True
        # return False 

        # Example 2:
        # 1st loop: i = index 0 -> sorted_nums[0] = 1, sorted_nums[1] = 2 and 1 != 2 -> move to next number in the array 
        # 2nd loop: i = index 1 -> sorted_nums[1] = 2, sorted_nums[2] = 3 and 2 != 3 -> move to next number in the array 
        # 3rd loop: i = index 2 -> sorted_nums[2] = 3, sorted_nums[3] = 4 and 3 != 4 -> end of range, 
        # no matches found, so end for loop and move to next line of code that instructs to return False

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] == nums[j]:
        #             return True 
        # return False 


    # Example 1:  nums = [1, 2, 3, 3]
    # 1st loop: i = index 0, j = index 1 
    # nums[i] == nums[j] --> if nums[0] == nums[1] --> if 1 == 2 -> false 
    # 2nd loop: i = index 0, j = index 2 
    # nums[0] == nums[2] --> 1 == 3 -> false 
    # 3rd loop: i = index 0, j = index 3 
    # nums[0] == nums[3] --> 1 == 3 -> false 
    # 4th loop: i = index 1, j = index 2 
    # nums[1] == nums[2] --> 2 == 3 -> false 
    # 5th loop: i = index 1, j = index 3 
    # nums[1] == nums[3] --> 2 == 3 -> fasle 
    # 6th loop: i = index 2, j = index 3 
    # nums[2] == nums[3] --> 3 == 3 -> True --> return True 


        # nums_sorted = sorted(nums)
        # # if you sort the array then just compare an element to the element next to it 
        # # [1, 2, 3, 4, 4]
        # # 1 == 2 
        # # 2 == 3 
        # # 3 == 4 
        # # 4 == 4 
        # for i in range(len(nums_sorted)-1):
        #     if nums_sorted[i] == nums_sorted[i+1]:
        #         return True 
        # return False 

    # 1st loop: i = index 0 
    # nums[0] == nums[0+1] --> nums[0] == nums[1] --> 1 == 2 -> false 
    # 2nd loop: i = index 1 
    # nums[1] == nums[1+1] --> nums[1] == nums[2] --> 2 == 3 -> false 
    # 3rd loop: i = index 2 
    # nums[2] == nums[2 + 1] --> nums[2] == nums[3] --> 3 == 4 -> false 
    # 4th loop: i = index 3 
    # nums[3] == nums[3+1] --> nums[3] == nums[4] --> 4 == 4 -> true - return true 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Brute Force solution with O(n^2) where n = length of array
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]: 
        #             return True
        # return False

        # Sorting with O(nlog(n)) < O(n^2) but sorting will require more space than brute force 
        # nums_sorted = sorted(nums)
        # for i in range(len(nums_sorted)-1): # because below, when you get to the end of the array, you would be comparing a element to nothing
        #     if nums_sorted[i] == nums_sorted[i+1]:
        #         return True
        # return False

        # there is a more efficient solution but I'm not there yet


        