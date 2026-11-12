class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(len(nums)-1, 0, -1): #creates index array [3, 2, 1, 0] -> [6, 4. 2, 1]
            product = output[-1]*nums[i]
            output.append(product)
        output = output[::-1]
        left = 1 
        for i in range(len(nums)):
            output[i] = output[i]*left
            left *= nums[i]
        return output