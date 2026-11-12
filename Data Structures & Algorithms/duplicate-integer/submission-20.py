class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # in this solution, we sort the array. Then just use a for loop to 
        # iterate through the array and compare one element to the one to 
        # right of it. If it finds a match then it returns True. If it goes
        # through the entire array and doesn't find a match it will return False. 
        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted) - 1):
            if nums_sorted[i] == nums_sorted[i + 1]: 
                    return True 
        return False 