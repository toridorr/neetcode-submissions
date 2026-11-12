class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for num in range(len(nums)): # creates index array [0, 1, 2, 3]
            if target - nums[num] in my_dict:
                return [my_dict[target - nums[num]], num]
            else:
                my_dict[nums[num]] = num 
        
        