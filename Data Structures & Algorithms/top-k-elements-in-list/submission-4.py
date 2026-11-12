class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)

        for num in nums:
            my_dict[num] += 1 

        heap = []

        for elt, freq in my_dict.items():
            heapq.heappush(heap, [freq, elt])
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in heap:
            result.append(i[1])

        return result             


 