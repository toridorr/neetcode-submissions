class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        left, right = 0, len(heights) - 1
        max_area = 0 

        while left < right:
            area = (right - left) * min(heights[left], heights[right]) 
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1 
            elif heights[left] >= heights[right]: # I forgot to include the "=" here to deal with when heights[left] == heights[right]. Because I was missing this I got a 'time exceeded' error. 
                right -= 1 
        
        return max_area 

        # Example: [3, 8, 4, 6, 2, 5, 9]
        # 1st loop: left = 0, right = 6
        # area = (6 - 0) * min(3, 9) = 6 * 3 = 18 
        # max_area = max(0, 18) = 18 
        # 3 < 9 --> move left pointer, left = 1 
        # 2nd loop: left = 1, right = 6 
        # area = (6 - 1) * min(8, 9) = 5 * 8 = 45
        # max_area = max(18, 45) = 45
        # 8 < 9 --> move left pointer, left = 2 
        # 3rd loop: left = 2, right = 6 
        # area = (6 - 2) * min(4, 9) = 4 * 4 = 16 
        # max_area = max(45, 16) = 45 
        # 4 < 9 --> move left pointer, left = 3 
        # 4th loop: left = 3, right = 6 
        # area = ...

        # Complexity:
        # Time = O(n) because you could go through each height in the array
        # Space = the only new thing you are creating is variable so O(1)


    # 1st Attempt  
        # max_area = 0 
        # left, right = 0, len(heights)-1

        # while left < right: # because if left == right then there is no container          
        #     left_height = heights[left]
        #     right_height = heights[right]
        #     width = right - left
        #     max_potential_height = min(left_height, right_height) 
        #     potential_area = width * max_potential_height 
        #     max_area = max(max_area, potential_area)
        #     if left_height < right_height:
        #         left += 1 
        #     elif left_height >= right_height: # if they are the same can incremenet a pointer left or right, does not matter
        #         right -= 1 
        
        # return max_area 

    # Complexity:
    # Time: O(n) because you are going through every height in the array 
    # Space: O(1) because you aren't creating anything new besides variables



