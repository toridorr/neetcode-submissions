class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right: 
            middle_index = (left + right) // 2
            middle_value = nums[middle_index]
            if middle_value == target: 
                return middle_index
            elif middle_value < target:
                # move our search area to the right, so our right index stays where it is 
                # our left pointer will move to the element to the right of the middle index
                left = middle_index + 1 
            else: # middle_value > target 
                # move our search area to the left
                right = middle_index - 1 
        return -1

# Example: nums = [-1,0,2,4,6,8], target = 4
# 1st loop: left = 0, right = len(nums) - 1 = 6 - 1 = 5, the right pointer is pointing to 
# index 5. Our search area is the entire array. 
# We jump into the while loop and the middle_index = (0 + 5) // 2 = 5 // 2 = 2 
# because you only want the integer part of this division so 5/2 = 2.5 but you only want 
# the 2 part. Remember that % would give you the remainder, so the 0.5. The 
# middle_value = nums[2] = 2. Skip the if block because 2 != 4. In the elif block, 2 < 4 
# so we know that since the nums array is sorted that in ascending order that if 4 exists 
# in the array it exists in the right half. We then will move out search area such that the 
# left index moves, left = middle_index + 1 = 2 + 1 = 3, so to index 3. We jump back to the
# top of our while loop.
# 2nd loop: left = 3 and right has not changed, so 3 < 5. Our search area is [4, 6, 8]. We can 
# continue into the while loop. The middle_index needs to be moved to the middle_index of 
# this new search area so middle_index = (left + right)//2 = (3 + 5)//2 = 8//2 = 4, so 
# index 4. And middle_value = nums[4] = 6. We skip the if block because 6 != 4. We skip the 
# elif block because 6 is not smaller than 4. So we move to the else block which is for when 
# the middle_value > target and 6 > 4. We want to make our search area even smaller and move 
# it to the left of the middle_index. So our right pointer is moved to the element to the 
# left of the middle_index, right = middle_index - 1 = 4 - 1 = 3, so index 3. We jump 
# back to the top of our while loop.
# 3rd loop: left = 3, right = 3. The middle_index = (left + right) // 2 = (3 + 3) // 2 
# = 6 // 2 = 3, so index 3 and our search area becomes [4]. We run the if block because 
# 4 = 4 and we break out of the while loop and return the middle_index which is 3. 
