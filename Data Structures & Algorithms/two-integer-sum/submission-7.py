class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1): # len(nums) == 4, so this creates [0, 1, 2]
            for j in range(i + 1, len(nums)): # [i + 1, ... , 3]
                if nums[i] + nums[j] == target:
                    return [i, j]
            
    

        
        