class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [2, -1, 1, 2]
        [2, 1, 2, 4]
        """
        result = 0
        curr_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            result += prefix_sums[diff]

            prefix_sums[curr_sum] += 1
    
        return result
            
