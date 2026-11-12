class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # You can use a set to tell you if there are any duplicates because a set 
    # cannot contain duplicates. If you turn the nums array into a set
    # it will automatically remove any duplicates. Compare the length of the 
    # set to the length of the nums array. If they are different then you know
    # there are duplicates 
        set_nums = set(nums)
        return True if len(set_nums) != len(nums) else False


   