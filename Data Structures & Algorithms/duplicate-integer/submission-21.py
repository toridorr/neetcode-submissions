class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # in this we use nested for loop to run through and compare every 
        # element. 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False 