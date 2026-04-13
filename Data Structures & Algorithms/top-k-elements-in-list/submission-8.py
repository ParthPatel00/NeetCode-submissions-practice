class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        min_heap = []
        for n in freq_map:
            heapq.heappush(min_heap, (freq_map[n], n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [item[1] for item in min_heap]