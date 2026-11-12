class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)

        for num in nums:
            my_dict[num] += 1 

        my_heap = []

        for elt, freq in my_dict.items():
            heapq.heappush(my_heap, [freq, elt])
            if len(my_heap) > k:
                heapq.heappop(my_heap)
            
        return [i[1] for i in my_heap]


 