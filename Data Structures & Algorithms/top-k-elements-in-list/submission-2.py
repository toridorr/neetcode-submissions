class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        for num in nums:
            dict[num] += 1 

        heap = []

        for key, value in dict.items():
            if len(heap) < k or heap[0][0]:
                heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]     


        