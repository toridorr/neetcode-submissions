class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        seen = {} # initialize an empty dictionary. We want to use a dictionary because we 
        # want to track the values we have seen as well as their corresponding indices
        # because we want to return their indices when we have found them

        for i in range(len(nums)): # creates [0, 1, 2, 3]
            num = nums[i]
            if target - num in seen: 
                return [seen[target - num], i]
            seen[num] = i 

    
    # Example: [3, 4, 5, 6], target = 11 
    # 1st loop: i = 0
    # num = 3 
    # target - num = 11 - 3 = 8 -> Is 8 in seen? Seen is empty so nope -> add it to seen
    # seen = {3:0}
    # 2nd loop: i = 1 
    # num = 4 
    # target - num = 11 - 4 = 7 -> Is 7 in seen? Nope -> Add it to seen
    # seen = {3:0, 4:1}
    # 3rd loop: i = 2
    # num = 5
    # target - num = 11 - 5 = 6 -> Is 6 in seen? Nope -> Add it to seen
    # seen = {3:0, 4:1, 5:2}
    # 4th looop: i = 3 
    # num = 6 
    # target - num = 11 - 6 = 5 -> Is 5 in seen? Yes -> return [seen[target - num], i] =
    # [seen[5], 3] = [2, 3]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # nums = [3,4,5,6], target = 11
        # We are using a dictionary because we can store each num in it with it's corresponding 
        # index, which we will need at the end since that is what we are supposed to return. 
        # A set wouldn't be helpful here because it doesn't associate it's elements with indices.

        # Since we want to use a dictionary, we want to store values. We have target and num that 
        # have been added to the dictionary. It's like we have two knowns and we can use them to 
        # find the unknown.

        # Let's say you have dict = {3:0} and you are num2 = 4 
        # target = 3 + 4 = 7 != 11 so add 4 to dict = {3:0, 4:1} and move on 
        # num2 = 5, so target - num2 = 11 - 5 = 6, do we have 6 in the dict? No we do not 
        # so add 5 to the dict = {3:0, 4:1, 5:2}
        # num = 6, so target - num2 = 11 - 6 = 5, do we have 5 in the dict? Yes we do, it's at 
        # index 2 and num is at index 3 so we return [2, 3]

        # dict = {}

        # for ind in range(len(nums)):
        #     dict[nums[ind]] = ind
        #     if target - nums[ind] in dict:
        #         return [] # how do I return the index of the num already in the array?
            


    
        





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # BRUTE FORCE: ITERATION - 2nd attempt
       
        # for i in range(len(nums)): #range(4) generates [0, 1, 2, 3]
        #     for j in range(i+1, len(nums)): # range(1, 4) generates [1, 2, 3]
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [] # Although we are guaranteed that there will always be an i and j 
        #that sum to target it is good practice to "always include an explicit 
        #return at the end of a function" it's a good "just in case" so you don't 
        #run into problems if the condition is not satisfied.
        
    
        # How we want this to work: The first number is i, and the second is j 
        # 3 + 4       4 + 5       5 + 6 
        # 3 + 5       4 + 6 
        # 3 + 6 

        # Example 1: [3,4,5,6], target = 11 
        # 1st loop: i = 0 
        # j = i + 1 = 0 + 1 = 1 -> nums[0] = 3, nums[1] = 4 and 3 + 4 = 7 != target -> the nested 
        # for loop moves to the next element in the j array '2'
        # 3rd loop: i = 0 
        # j = 2 -> nums[0] = 3, nums[2] = 5 and 3 + 5 = 8 != target -> the nested for loop has
        # moves to the next element in the j array '3'
        # j = 3 -> nums[0] = 3, nums[3] = 6 and 3 + 6 = 9 != target -> the nested for loop has
        # reached the end of the j array
        
        # 4th loop: i = 1
        # The outer for loop moves on to the next element in i array '1'
        # j = i + 1 = 1 + 1 = 2 -> nums[1] = 4, nums[2] = 5 and 4 + 5 = 9 != target -> the nested 
        # for loop moves on to the next element in the j array '3'
        # j = 3 -> nums[1] = 4, nums[3] = 6 and 4 + 6 = 10 != target -> the nested for loop 
        # has reached the end of the j array 
            
        # 7th loop: i = 2 
        # The outer for loop moves on to the next element in the i array '2'
        # j = i + 1 = 2 + 1 = 3 -> nums[2] = 5, nums[3] = 6 and 5 + 6 == target so return [i, j]
            
        # Time and Space Complexity:
        # Time - Nested for loop has a time complexity of O(n^2)  
        # Space - We are not creating something new that will take up more space so O(1)   
        
        
        
        
    # BRUTE FORCE: ITERATION - 1ST ATTEMPT
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)): # during review forgot to set the starting range, this is why you go through the code with an example to make sure it makes sense (like Deepti).
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
























 
