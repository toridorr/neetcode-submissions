class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # let's use a dictionary. You can add each element to a dictionary. 
        # Since each key must have a value, I am just using 0 as the value. 
        # You check it the value is in the dictionary. If not, add it. If it
        # is then you know it is a repeat and you return True. If the 
        # loop gets through all elements and does not return True then there 
        # are no duplicates and you can return False. 
    
        nums_dict = {}

        for num in nums: 
            if num in nums_dict: 
                return True 
            else:
                nums_dict[num] = 0
        
        return False


   