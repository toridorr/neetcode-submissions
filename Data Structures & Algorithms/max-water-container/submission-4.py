class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0 

        while left < right:
            current_area = (min(heights[left], heights[right]))*(right - left)
            max_area = max(max_area, current_area)
            if heights[left] <= heights[right]:
                left += 1 
            else:
                right -= 1 
        
        return max_area 

    # height = [1,7,2,5,4,7,3,6]
    #                   L.R
    # 1st loop: left = 0, right = 7 
    # h[left] = 1, h[right] = 6 -> min = 1 
    # current_area = 1 * 7 = 7 
    # max_area = max(0, 7) = 7 
    # h[left] < h[right] -> move left -> left = 1 
    # 2nd loop: left = 1, right = 7 
    # h[left] = 7, h[right] = 6 -> min = 6 
    # current_area = 6 * 6 = 36 
    # max_area = max(7, 36) = 36 
    # h[left] > h[right] -> move right -> right = 6 
    # 3rd loop: left = 1, right = 6 
    # h[left] = 7, h[right] = 3 -> min = 3 
    # current_area = 3 * 5 = 15 
    # max_area = max(36, 15) = 36 
    # h[left] > h[right] -> move right -> right = 5 
    # 4th loop: left = 1, right = 5 
    # h[left] = 7, h[right] = 7 -> min = 7 
    # current_area = 7 * 4 = 28 
    # max_area = max(36, 28) = 36 
    # h[left] == h[right] -> move left -> left = 2
    # 5th loop: left = 2, right = 5 
    # h[left] = 2, h[right] = 7 -> min = 2 
    # current_area = 2 * 3 = 5 
    # max_area = max(36, 5) = 36 
    # increment left -> left = 3 
    # 6th loop: left = 3, rigt = 5 
    # h[left] = 5, h[right] = 7 -> min = 5 
    # current_area = 5 * 2 = 10 
    # max_area = max(36, 10) = 36 
    # increment left -> left = 4 
    # 7th loop: left = 4, right = 5 
    # h[left] = 4, h[right] = 7 -> min = 4 
    # current_area = 4 * 1 = 4 
    # max_area = max(36, 4) = 36 
    # increment left -> left = 5 
    # 8th loop: left = 5, right = 5 -> this fails the while loop so breaks out and returns the max_area = 36 




            
        