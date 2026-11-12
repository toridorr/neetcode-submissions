class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)): # [0, 1, 2, 3]
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            else: 
                seen[nums[i]] = i # we make the element the key and the index the value so we can use this 

                

            
    

        
        