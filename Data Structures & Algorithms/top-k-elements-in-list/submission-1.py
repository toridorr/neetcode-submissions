class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] = dict[num] + 1 
            else:
                dict[num] = 1 
        
        return heapq.nlargest(k, dict, key=dict.get)

        