class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1 
            elif numbers[left] + numbers[right] > target:
                right -= 1 
            else:
                return [left + 1, right + 1]

    # numbers = [1, 2, 3, 4], target = 3  
    # first loop:
    # left = 0, right = 3 
    # numbers[left] = 1, numbers[right] = 4 
    # 1 + 4 = 5  > 3 -> decremement right pointer -> right = 2 
    # second loop:
    # left = 0, right = 2 
    # numbers[left] = 1, numbers[right] = 3 
    # 1 + 3 = 4 > target -> decrement right pointer -> right = 1 
    # 3rd loop:
    # left = 0, right = 1 
    # numbers[left] = 1, numbers[right] = 2 
    # 1 + 2 = 3 -> return [0, 1]
        
        