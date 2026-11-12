class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]:
                    return True 
        return False 


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


        