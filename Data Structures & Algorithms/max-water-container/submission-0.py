class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        left, right = 0, len(heights)-1

        while left < right: # because if left == right then there is no container          
            left_height = heights[left]
            right_height = heights[right]
            width = right - left
            max_potential_height = min(left_height, right_height) 
            potential_area = width * max_potential_height 
            max_area = max(max_area, potential_area)
            if left_height < right_height:
                left += 1 
            elif left_height >= right_height: # if they are the same can incremenet a pointer left or right, does not matter
                right -= 1 
        
        return max_area 



