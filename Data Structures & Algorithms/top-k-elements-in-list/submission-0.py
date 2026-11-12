class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        output = []

        for num in nums:
            if num in dict:
                dict[num] += 1 
            else:
                dict[num] = 1
        
        for i in range(k):
            max_key = max(dict, key = dict.get) # finds key '1'
            output.append(max_key)
            del dict[max_key]
        
        return output 
        
        