class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        # because this is a nested loop the time complexity is O(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# there are more efficient solitions but I'm not there yet 