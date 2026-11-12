class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force solution with O(n^2) where n = length of array
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]: 
        #             return True
        # return False

        # Sorting with O(nlog(n)) < O(n^2) but sorting will require more space than brute force 
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)-1): # because below, when you get to the end of the array, you would be comparing a element to nothing
            if nums_sorted[i] == nums_sorted[i+1]:
                return True
        return False


        