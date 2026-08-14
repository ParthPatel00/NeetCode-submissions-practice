import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        for n, count in freq.items():
            heapq.heappush(max_heap, (count, n))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [item[1] for item in max_heap]
        