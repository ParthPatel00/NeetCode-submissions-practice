class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """


        """
        min_length = float("inf")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                arr = nums[i:j]
                if sum(arr) >= target:
                    min_length = min(min_length, j - i)
                    break
        
        return 0 if min_length == float("inf") else min_length